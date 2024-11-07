import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import threading
import sys
import termios
import tty
import os
from datetime import datetime

class ImageSaverNode(Node):
    def __init__(self):
        super().__init__('image_saver_node')
        self.get_logger().info('Initializing ImageSaverNode...')
        self.realsense_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.realsense_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/thermal_image_view', self.optris_callback, 10)
        self.cv_bridge = CvBridge()
        self.save_images = False
        self.base_dir = '/home/yeray/sensors_ws/src/Calibration/Imagenes/CALIBRATION21/'
        self.realsense_index = 1
        self.optris_index = 1
        self.date_str = datetime.now().strftime("%B%d")  # MonthDay format like "June25"
        self.realsense_image = None
        self.optris_image = None
        self.get_logger().info('ImageSaverNode has been started.')

    def realsense_callback(self, msg):
        self.realsense_image = msg

    def optris_callback(self, msg):
        self.optris_image = msg

    def save_images_once(self):
        if self.realsense_image is not None and self.optris_image is not None:
            try:
                cv_image = self.cv_bridge.imgmsg_to_cv2(self.realsense_image, desired_encoding='bgr8')
                file_name = os.path.join(self.base_dir, 'Normal', f'{self.date_str}_{self.realsense_index}.png')
                cv2.imwrite(file_name, cv_image)
                self.get_logger().info(f'Realsense image saved at {file_name}')
                self.realsense_index += 1
            except Exception as e:
                self.get_logger().error(f'Failed to save Realsense image: {e}')

            try:
                cv_image = self.cv_bridge.imgmsg_to_cv2(self.optris_image, desired_encoding='bgr8')
                file_name = os.path.join(self.base_dir, 'Thermal', f'{self.date_str}_{self.optris_index}.png')
                cv2.imwrite(file_name, cv_image)
                self.get_logger().info(f'Optris image saved at {file_name}')
                self.optris_index += 1
            except Exception as e:
                self.get_logger().error(f'Failed to save Optris image: {e}')

            self.realsense_image = None
            self.optris_image = None
        else:
            self.get_logger().warn('One or both images are not available. Ensure both cameras are publishing images.')

    def run(self):
        self.get_logger().info('Press "s" to take a photo.')
        key_thread = threading.Thread(target=self.keypress_listener, daemon=True)
        key_thread.start()

        try:
            rclpy.spin(self)
        except KeyboardInterrupt:
            self.get_logger().info('SIGINT received. Exiting...')
        finally:
            self.cleanup()

    def keypress_listener(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        try:
            while True:
                if sys.stdin.read(1) == 's':
                    self.save_images_once()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def cleanup(self):
        self.get_logger().info('Cleaning up...s')
        if rclpy.ok():
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = ImageSaverNode()
        node.run()
    except Exception as e:
        if node:
            node.get_logger().error(f'Exception in main: {e}')
    finally:
        if node and rclpy.ok():
            node.cleanup()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
