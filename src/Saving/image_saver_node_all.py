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
import glob

class ImageSaverNode(Node):
    def __init__(self):
        super().__init__('image_saver_node')
        self.get_logger().info('Initializing ImageSaverNode...')
        self.realsense_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.realsense_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/masked_image_with_temperature', self.masked_image_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_rgb', self.rescaled_rgb_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_yolo_masks', self.rescaled_yolo_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/camera/camera/depth/image_rect_raw', self.depth_image_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/thermal_image', self.optris_bw_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/thermal_image_view', self.optris_callback, 10)
        self.optris_sub = self.create_subscription(Image, '/yolo_image', self.yolo_callback, 10)        

        self.cv_bridge = CvBridge()
        self.save_images = False
        self.base_dir = '/home/yeray/sensors_ws/src/Calibration/Imagenes/CALIBRATION21/'
        self.save_dir = '/home/yeray/sensors_ws/src/ProvesDeCamp/25Octubre2024/Calibration1280'
        self.realsense_index = 1
        self.optris_index = 1
        self.masked_image_index = 1
        self.rescaled_rgb_index = 1
        self.rescaled_yolo_index = 1
        self.depth_image_index = 1
        self.optris_bw_index = 1
        self.yolo_index = 1
        self.date_str = datetime.now().strftime("%B%d")  # MonthDay format like "June25"
        self.realsense_image = None
        self.optris_image = None
        self.masked_image = None
        self.rescaled_rgb = None
        self.rescaled_yolo = None
        self.depth_image = None
        self.optris_bw = None
        self.yolo = None
        self.get_logger().info('ImageSaverNode has been started.')

        # Create directories if they don't exist
        self.create_directories()

        # Initialize indices based on existing files
        self.initialize_indices()

    def create_directories(self):
        directories = [
            os.path.join(self.save_dir, 'Normal'),
            os.path.join(self.save_dir, 'Thermal'),
            os.path.join(self.save_dir, 'MaskedImageCSWITemperature'),
            os.path.join(self.save_dir, 'RescaledRGB'),
            os.path.join(self.save_dir, 'RescaledYOLO'),
            os.path.join(self.save_dir, 'DepthImage'),
            os.path.join(self.save_dir, 'OptrisBW'),
            os.path.join(self.save_dir, 'YOLO')
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            self.get_logger().info(f'Ensured directory exists: {directory}')

    def initialize_indices(self):
        # Check each directory for existing files and set the indices accordingly
        directories = {
            'Normal': 'realsense_index',
            'Thermal': 'optris_index',
            'MaskedImageCSWITemperature': 'masked_image_index',
            'RescaledRGB': 'rescaled_rgb_index',
            'RescaledYOLO': 'rescaled_yolo_index',
            'DepthImage': 'depth_image_index',
            'OptrisBW': 'optris_bw_index',
            'YOLO': 'yolo_index'
        }

        for folder, attribute in directories.items():
            folder_path = os.path.join(self.save_dir, folder)
            # Get all files in the directory that match the naming pattern
            files = glob.glob(os.path.join(folder_path, f'{self.date_str}_*.png'))
            # Find the highest index and set the starting index accordingly
            if files:
                max_index = max(int(os.path.splitext(os.path.basename(f))[0].split('_')[-1]) for f in files)
                setattr(self, attribute, max_index + 1)
            else:
                setattr(self, attribute, 1)

    def realsense_callback(self, msg):
        self.realsense_image = msg

    def optris_callback(self, msg):
        self.optris_image = msg

    def masked_image_callback(self, msg):
        self.masked_image = msg

    def rescaled_rgb_callback(self, msg):
        self.rescaled_rgb = msg

    def rescaled_yolo_callback(self, msg):
        self.rescaled_yolo = msg

    def depth_image_callback(self, msg):
        self.depth_image = msg

    def optris_bw_callback(self, msg):
        self.optris_bw = msg

    def yolo_callback(self, msg):
        self.yolo = msg

    def save_images_once(self):
        missing_topics = []
        
        if self.realsense_image is None:
            missing_topics.append('Realsense image (/camera/camera/color/image_raw)')
        if self.optris_image is None:
            missing_topics.append('Optris image (/thermal_image_view)')
        # if self.masked_image is None:
        #     missing_topics.append('Masked image (/Temperature_and_CSWI/masked_image_with_temperature)')
        if self.rescaled_rgb is None:
            missing_topics.append('Rescaled RGB (/Temperature_and_CSWI/rescaled_rgb)')
        # if self.rescaled_yolo is None:
        #     missing_topics.append('Rescaled YOLO (/Temperature_and_CSWI/rescaled_yolo_masks)')
        if self.depth_image is None:
            missing_topics.append('Depth image (/camera/camera/depth/image_rect_raw)')
        if self.optris_bw is None:
            missing_topics.append('Optris BW image (/thermal_image)')
        if self.yolo is None:
            missing_topics.append('YOLO image (/yolo_image)')
        
        if missing_topics:
            for topic in missing_topics:
                self.get_logger().warn(f'Missing: {topic}')
            return  # Salir del método si falta alguna imagen

        # Continuar con el guardado de imágenes si todas están disponibles
        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(self.realsense_image, desired_encoding='bgr8')
            file_name = os.path.join(self.save_dir, 'Normal', f'{self.date_str}_{self.realsense_index}.png')
            cv2.imwrite(file_name, cv_image)
            self.get_logger().info(f'Realsense image saved at {file_name}')
            self.realsense_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save Realsense image: {e}')

        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(self.optris_image, desired_encoding='bgr8')
            file_name = os.path.join(self.save_dir, 'Thermal', f'{self.date_str}_{self.optris_index}.png')
            cv2.imwrite(file_name, cv_image)
            self.get_logger().info(f'Optris image saved at {file_name}')
            self.optris_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save Optris image: {e}')

        # try:
        #     cv_image = self.cv_bridge.imgmsg_to_cv2(self.masked_image, desired_encoding='bgr8')
        #     file_name = os.path.join(self.save_dir, 'MaskedImageCSWITemperature', f'{self.date_str}_{self.masked_image_index}.png')
        #     cv2.imwrite(file_name, cv_image)
        #     self.get_logger().info(f'Masked image saved at {file_name}')
        #     self.masked_image_index += 1
        # except Exception as e:
        #     self.get_logger().error(f'Failed to save Masked image: {e}')

        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(self.rescaled_rgb, desired_encoding='bgr8')
            file_name = os.path.join(self.save_dir, 'RescaledRGB', f'{self.date_str}_{self.rescaled_rgb_index}.png')
            cv2.imwrite(file_name, cv_image)
            self.get_logger().info(f'Rescaled RGB image saved at {file_name}')
            self.rescaled_rgb_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save rescaled RGB: {e}')

        # try:
        #     cv_image = self.cv_bridge.imgmsg_to_cv2(self.rescaled_yolo, desired_encoding='bgr8')
        #     file_name = os.path.join(self.save_dir, 'RescaledYOLO', f'{self.date_str}_{self.rescaled_yolo_index}.png')
        #     cv2.imwrite(file_name, cv_image)
        #     self.get_logger().info(f'Rescaled YOLO image saved at {file_name}')
        #     self.rescaled_yolo_index += 1
        # except Exception as e:
        #     self.get_logger().error(f'Failed to save rescaled YOLO: {e}')

        try:
            depth_image_cv = self.cv_bridge.imgmsg_to_cv2(self.depth_image, desired_encoding='passthrough') # [16UC1]
            # Normalizar los valores para que sean visualizables como una imagen de 8 bits
            depth_image_normalized = cv2.normalize(depth_image_cv, None, 0, 255, cv2.NORM_MINMAX)
            depth_image_8u = depth_image_normalized.astype('uint8')
            file_name = os.path.join(self.save_dir, 'DepthImage', f'{self.date_str}_{self.depth_image_index}.png')
            cv2.imwrite(file_name, depth_image_8u)
            self.get_logger().info(f'Depth image saved at {file_name}')
            self.depth_image_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save Depth image: {e}')

        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(self.optris_bw, desired_encoding='bgr8')
            file_name = os.path.join(self.save_dir, 'OptrisBW', f'{self.date_str}_{self.optris_bw_index}.png')
            cv2.imwrite(file_name, cv_image)
            self.get_logger().info(f'Optris BW image saved at {file_name}')
            self.optris_bw_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save Optris BW image: {e}')

        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(self.yolo, desired_encoding='bgr8')
            file_name = os.path.join(self.save_dir, 'YOLO', f'{self.date_str}_{self.yolo_index}.png')
            cv2.imwrite(file_name, cv_image)
            self.get_logger().info(f'YOLO image saved at {file_name}')
            self.yolo_index += 1
        except Exception as e:
            self.get_logger().error(f'Failed to save YOLO image: {e}')

        # Reset images after saving
        self.realsense_image = None
        self.optris_image = None
        self.masked_image = None
        self.rescaled_rgb = None
        self.rescaled_yolo = None
        self.depth_image = None
        self.optris_bw = None
        self.yolo = None


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
        else:
            print(f'Error during initialization: {e}')
    finally:
        if node and rclpy.ok():
            node.cleanup()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
