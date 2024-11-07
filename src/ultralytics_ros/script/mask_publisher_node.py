import cv2
import cv_bridge
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2D, ObjectHypothesisWithPose
from ultralytics_ros.msg import YoloResult

class MaskPublisherNode(Node):
    def __init__(self):
        super().__init__('mask_publisher_node')
        self.bridge = cv_bridge.CvBridge()
        self.mask_pub = self.create_publisher(Image, '/yolo_combined_masks', 10)
        self.individual_mask_pub = self.create_publisher(Image, '/yolo_individual_masks', 10)  # Pubblica le maschere individuali come immagini
        self.create_subscription(YoloResult, '/yolo_result', self.result_callback, 10)
        self.get_logger().warn('Mask node initialized')
        
    def result_callback(self, msg):
        if msg.masks:
            combined_mask = np.zeros((msg.masks[0].height, msg.masks[0].width), dtype=np.uint8)  # Create a black canvas
            individual_masks = []
            self.get_logger().warn('Message task detected')

            for i, mask_image_msg in enumerate(msg.masks):
                mask_image = self.bridge.imgmsg_to_cv2(mask_image_msg, desired_encoding='passthrough')
                combined_mask = cv2.bitwise_or(combined_mask, mask_image)  # Combine masks by taking bitwise OR

                # Publish individual mask as image
                individual_mask_msg = self.bridge.cv2_to_imgmsg(mask_image, encoding='passthrough')
                self.individual_mask_pub.publish(individual_mask_msg)

                # Create ObjectHypothesisWithPose for individual mask
                #object_hypothesis = ObjectHypothesisWithPose()
                #print(object_hypothesis)
                #object_hypothesis.pose.pose.position.x = 0.0
                #object_hypothesis.pose.pose.position.y = 0.0
                #object_hypothesis.pose.pose.position.z = 0.0
                #object_hypothesis.hypothesis.class_id = str(i)  # Assign a unique ID to each mask

                #detection = Detection2D()
                #print(detection.bbox)
                #detection.results.append(object_hypothesis)
                #print("Tipo de dato de size_x antes de la asignación:", type(detection.bbox.size_x))
                #print("Ancho de la imagen de la máscara:", mask_image_msg.width)
                #print("Altura de la imagen de la máscara:", mask_image_msg.height)
                #print("Valor de mask_image_msg.width:", mask_image_msg.width)
                #detection.bbox.size_x = float(mask_image_msg.width)
                #detection.bbox.size_y = float(mask_image_msg.height)
                #detection.bbox.center.x = float(mask_image_msg.width / 2)
                #detection.bbox.center.position.x = float(mask_image_msg.width / 2)
                #detection.bbox.center.y = float(mask_image_msg.height / 2)
                #detection.bbox.center.position.y = float(mask_image_msg.height / 2)

            # Publish combined mask
            combined_mask_msg = self.bridge.cv2_to_imgmsg(combined_mask, encoding='passthrough')
            self.mask_pub.publish(combined_mask_msg)
            self.get_logger().info("Combined mask published")
        else:
            self.get_logger().warn('Received empty masks list.')

def main(args=None):
    rclpy.init(args=args)
    node = MaskPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


#creado por chatgpt!
