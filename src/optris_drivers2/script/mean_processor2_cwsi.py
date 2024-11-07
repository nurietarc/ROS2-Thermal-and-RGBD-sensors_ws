import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Float32
import cv2
import numpy as np

class MaskTemperatureCalculator(Node):
    def __init__(self):
        super().__init__('mask_temperature_calculator_node')
        self.get_logger().info("Initializing node...")
        self.bridge = CvBridge()
        try:
            self.H = np.loadtxt('/home/yeray/sensors_ws/src/Calibration/Results/average_homography.txt')
            self.get_logger().info("Loaded homography matrix.")
        except Exception as e:
            self.get_logger().error(f"Failed to load homography matrix: {e}")

        self.rgb_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.rgb_callback, 10)
        self.temperature_sub = self.create_subscription(Image, '/thermal_image', self.temperature_callback, 10)
        self.mask_sub = self.create_subscription(Image, '/yolo_individual_masks', self.mask_callback, 10)
        self.mask_temperature_pub = self.create_publisher(Float32, '/mask_temperature', 10)
        self.mask_image_pub = self.create_publisher(Image, '/masked_images', 10)
        
        self.temperature_image = None
        self.rgb_image = None
        self.warped_thermal = None
        self.masked_images = []

        # Definition of Twet and Tdry
        self.Twet = 22.0  # Change to corresponding/appropriate value (?)
        self.Tdry = 27.0  # Change to corresponding/appropriate value (?)

    def rgb_callback(self, rgb_msg):
        self.rgb_image = self.bridge.imgmsg_to_cv2(rgb_msg, desired_encoding='bgr8')
        #self.get_logger().info("RGB image received")

    def temperature_callback(self, thermal_msg):
        thermal_image = self.bridge.imgmsg_to_cv2(thermal_msg, desired_encoding='32FC1')
        self.temperature_image = (thermal_image - 1000) / 10.0

        if self.rgb_image is not None:
            self.warped_thermal = cv2.warpPerspective(self.temperature_image, self.H, (self.rgb_image.shape[1], self.rgb_image.shape[0]))
            #self.get_logger().info("Warped thermal image created")
        else:
            self.get_logger().warn("RGB image is not available yet.")

    def mask_callback(self, mask_msg):
        mask = self.bridge.imgmsg_to_cv2(mask_msg, desired_encoding='passthrough')
        #self.get_logger().warn("Estoy en mask_callback.")

        if self.warped_thermal is not None:
            valid_pixels = np.argwhere(self.warped_thermal > 0)
            mask_temperature = self.compute_mask_temperature(mask, valid_pixels)

            if mask_temperature != 0.0:
                cwsi = (mask_temperature - self.Twet) / (self.Tdry - self.Twet)
                self.mask_temperature_pub.publish(mask_temperature)
                self.get_logger().warn(f"CWSI for Mask: {cwsi:.2f}")
                masked_image_with_text = self.draw_text_on_mask(mask, mask_temperature, cwsi)
                self.masked_images.append(masked_image_with_text, valid_pixels)

            #self.masked_images.append((mask, valid_pixels))
            #self.get_logger().info("Mask received and processed")
        else:
            self.get_logger().warn("Warped thermal image is not available yet.")

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

    def draw_text_on_mask(self, mask, temperature, cwsi):
        masked_image = cv2.bitwise_and(self.rgb_image, self.rgb_image, mask=mask)
        masked_image_with_text = masked_image.copy()
        cv2.putText(masked_image_with_text, f'Temperature: {temperature:.2f} C, CWSI: {cwsi:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return masked_image_with_text

    def publish_masked_images(self):
        self.get_logger().info("Publishing masked images...")
        while rclpy.ok():
            for masked_image, valid_pixels in self.masked_images:
                mask_temperature = self.compute_mask_temperature(masked_image, valid_pixels)

                # Only publish if the mean temperature is different from 0
                if mask_temperature != 0.0:
                    # Draw the ROI of the mask in red
                    cv_mask_visualization = cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB)
                    cv2.rectangle(cv_mask_visualization, (0, 0), (masked_image.shape[1], masked_image.shape[0]), (0, 0, 255), 2)

                    # Add the text of the mean temperature to the mask visualization
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    text = f"Mean Temp: {mask_temperature:.2f} C"
                    text_position = (10, 30)
                    font_scale = 1.5  # Increase this value to make the text bigger
                    cv2.putText(cv_mask_visualization, text, text_position, font, font_scale, (0, 255, 255), 2, cv2.LINE_AA)
                                                            
                    # Publish the visualization of the mask
                    mask_visualization_msg = self.bridge.cv2_to_imgmsg(cv_mask_visualization, encoding='rgb8')
                    self.mask_image_pub.publish(mask_visualization_msg)
                    self.get_logger().info("Published masked image with temperature")

            # Clear the masked images list after publishing
            self.masked_images = []
            rclpy.spin_once(self)

    def run(self):
        self.get_logger().info("Running node...")
        self.get_logger().info(f"Number of masked images: {len(self.masked_images)}")
        self.publish_masked_images()
        self.get_logger().info("Finished running node.")



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

#CHATGPT LO HA HECHO