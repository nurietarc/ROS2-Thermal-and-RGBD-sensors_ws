from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from ultralytics_ros.msg import YoloResult
import os

class MaskTemperatureCalculator(Node):
    def __init__(self):
        super().__init__('mask_temperature_calculator_node')
        self.get_logger().info("Initializing node...")
        self.bridge = CvBridge()
        try:
            self.H = np.loadtxt(os.path.expanduser('~/sensors_ws/src/Calibration/Results/average_homography_termica_rgb2.txt'))
            self.get_logger().info("Loaded homography matrix.")
        except Exception as e:
            self.get_logger().error(f"Failed to load homography matrix: {e}")

        self.rgb_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.rgb_callback, 10)
        self.temperature_sub = self.create_subscription(Image, '/thermal_image', self.temperature_callback, 10)
        self.mask_sub = self.create_subscription(YoloResult, '/yolo_result', self.mask_callback, 10)  # Change the subscription to YoloResult
        self.mask_temperature_pub = self.create_publisher(Float32, '/mask_temperature', 10)
        self.masked_image_pub = self.create_publisher(Image, '/masked_image', 10)
        self.warped_image_pub = self.create_publisher(Image, '/warped_image', 10)

        self.temperature_image = None
        self.rgb_image = None
        self.warped_thermal = None
        self.masked_images = []
        self.desired_class_id = 'person'  # Set the desired class ID (e.g., 0 for "person")

    def rgb_callback(self, rgb_msg):
        self.rgb_image = self.bridge.imgmsg_to_cv2(rgb_msg, desired_encoding='bgr8')
        #self.get_logger().info("RGB image received")

    def temperature_callback(self, thermal_msg):
        thermal_image = self.bridge.imgmsg_to_cv2(thermal_msg, desired_encoding='32FC1')
        self.temperature_image = (thermal_image - 1000) / 10.0

        if self.rgb_image is not None:
            self.warped_thermal = cv2.warpPerspective(self.temperature_image, self.H, (self.rgb_image.shape[1], self.rgb_image.shape[0]))
            # Publish the warped thermal image
            warped_thermal_msg = self.bridge.cv2_to_imgmsg(self.warped_thermal, encoding='32FC1')
            self.warped_image_pub.publish(warped_thermal_msg)  # Publishing the warped thermal image
            self.get_logger().info("Published warped thermal image")
        else:
            self.get_logger().warn("RGB image is not available yet.")

    def mask_callback(self, yolo_result_msg):
        if yolo_result_msg.masks and yolo_result_msg.detections.detections:
            for i, mask_image_msg in enumerate(yolo_result_msg.masks):
                detection = yolo_result_msg.detections.detections[i]
                class_id = detection.results[0].hypothesis.class_id  # Access the class ID from the hypothesis
                self.get_logger().info(f"Class id is {class_id}")

                if class_id != self.desired_class_id:
                    self.get_logger().warn(f"Skipping mask of class {class_id}")
                    continue

                mask = self.bridge.imgmsg_to_cv2(mask_image_msg, desired_encoding='passthrough')

                if self.warped_thermal is not None:
                    valid_pixels = np.argwhere(self.warped_thermal > 0)
                    mask_temperature = self.compute_mask_temperature(mask, valid_pixels)
                    masked_image_with_text = self.draw_text_on_mask(mask, mask_temperature)

                    # Publish the masked image with temperature
                    masked_image_msg = self.bridge.cv2_to_imgmsg(masked_image_with_text, encoding='bgr8')
                    self.masked_image_pub.publish(masked_image_msg)
                    self.get_logger().info("Published masked image with temperature")
                else:
                    self.get_logger().warn("Warped thermal image is not available yet.")
        else:
            self.get_logger().warn('Received empty masks or detections list.')

    def compute_mask_temperature(self, mask, valid_pixels):
        if self.warped_thermal is None:
            self.get_logger().warn("Warped thermal image is not available yet.")
            return 0.0

        mask_temperature_values = []

        for pixel in valid_pixels:
            x, y = pixel[1], pixel[0]
            if 0 <= x < mask.shape[1] and 0 <= y < mask.shape[0]:
                temperature = self.warped_thermal[y, x]
                if temperature > 0 and mask[y, x] > 0:
                    mask_temperature_values.append(temperature)

        if mask_temperature_values:
            mean_temperature = np.mean(mask_temperature_values)
            self.get_logger().info(f"Mean Temperature for Mask: {mean_temperature:.2f} C")
            return mean_temperature
        else:
            return 0.0

    def draw_text_on_mask(self, mask, temperature):
        masked_image = cv2.bitwise_and(self.rgb_image, self.rgb_image, mask=mask)
        masked_image_with_text = masked_image.copy()
        cv2.putText(masked_image_with_text, f'Temperature: {temperature:.2f} C', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return masked_image_with_text

    def run(self):
        self.get_logger().info("Running node...")
        rclpy.spin(self)

def main(args=None):
    rclpy.init(args=args)
    mask_temp_calculator = MaskTemperatureCalculator()
    try:
        mask_temp_calculator.run()
    except KeyboardInterrupt:
        mask_temp_calculator.get_logger().info("Node interrupted by user.")
    finally:
        if rclpy.ok():
            print("Calling rclpy.shutdown()")
            rclpy.shutdown()

if __name__ == '__main__':
    main()
