# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# import cv2
# from cv_bridge import CvBridge
# import threading
# import sys
# import termios
# import tty
# import os
# from datetime import datetime
# import time
# import glob

# class VideoSaverNode(Node):
#     def __init__(self):
#         super().__init__('video_saver_node')
#         self.get_logger().info('Initializing VideoSaverNode...')

#         self.realsense_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.realsense_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/masked_image_with_temperature', self.masked_image_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_rgb', self.rescaled_rgb_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_yolo_masks', self.rescaled_yolo_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/camera/camera/depth/image_rect_raw', self.depth_image_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/thermal_image', self.optris_bw_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/thermal_image_view', self.optris_callback, 10)
#         self.optris_sub = self.create_subscription(Image, '/yolo_image', self.yolo_callback, 10)        

#         self.cv_bridge = CvBridge()
#         self.save_base_dir = '/home/yeray/sensors_ws/src/ProvesDeCamp/25Octubre2024/Calibration1280'
#         self.date_str = datetime.now().strftime("%B%d")  # Format like "October24"
#         self.video_writers = {}
#         self.frame_counts = {}
#         self.is_recording = False  # Controla si la grabación está activa
#         self.fps = 30  # FPS fijo para evitar problemas de sincronización
#         self.frame_interval = 1.0 / self.fps  # Intervalo entre fotogramas en segundos

#         # Variables para sincronización
#         self.start_time = None  # Tiempo de inicio de la grabación
#         self.last_frame_time = {}  # Últimos *time stamps* para cada tópico

#         self.get_logger().info('VideoSaverNode has been started.')

#         # Create directories if they don't exist
#         self.directories = self.create_directories()

#         # Start the key listener thread
#         self.key_thread = threading.Thread(target=self.keypress_listener, daemon=True)
#         self.key_thread.start()

#     def create_directories(self):
#         directories = {
#             'realsense': os.path.join(self.save_base_dir, 'Normal'),
#             'optris': os.path.join(self.save_base_dir, 'Thermal'),
#             'masked_image': os.path.join(self.save_base_dir, 'MaskedImageCSWITemperature'),
#             'rescaled_rgb': os.path.join(self.save_base_dir, 'RescaledRGB'),
#             'rescaled_yolo': os.path.join(self.save_base_dir, 'RescaledYOLO'),
#             'depth_image': os.path.join(self.save_base_dir, 'DepthImage'),
#             'optris_bw': os.path.join(self.save_base_dir, 'OptrisBW'),
#             'yolo': os.path.join(self.save_base_dir, 'YOLO')
#         }

#         for key, directory in directories.items():
#             os.makedirs(directory, exist_ok=True)
#             self.get_logger().info(f'Ensured directory exists: {directory}')
#         return directories

#     def get_next_index(self, prefix):
#         directory = self.directories[prefix]
#         existing_files = glob.glob(os.path.join(directory, f'{self.date_str}_{prefix}_*.avi'))
#         if not existing_files:
#             return 1
#         max_index = max([int(os.path.splitext(f)[0].split('_')[-1]) for f in existing_files])
#         return max_index + 1

#     def initialize_video_writer(self, prefix, frame_size):
#         index = self.get_next_index(prefix)
#         codecs = cv2.VideoWriter_fourcc(*'MJPG')  # Codec compatible para .avi
#         file_path = os.path.join(self.directories[prefix], f'{self.date_str}_{prefix}_{index}.avi')
#         video_writer = cv2.VideoWriter(file_path, codecs, self.fps, frame_size)

#         if not video_writer.isOpened():
#             self.get_logger().error(f'Failed to initialize VideoWriter for {prefix}. Check codec and file path.')
#             return None

#         self.video_writers[prefix] = video_writer
#         self.frame_counts[prefix] = 0
#         self.get_logger().info(f'Initialized video writer for {prefix} at {file_path} with frame size {frame_size} and FPS {self.fps}')

#     def realsense_callback(self, msg):
#         self.process_frame('realsense', msg, encoding='bgr8')

#     def optris_callback(self, msg):
#         self.process_frame('optris', msg, encoding='bgr8')

#     def masked_image_callback(self, msg):
#         self.process_frame('masked_image', msg, encoding='bgr8')

#     def rescaled_rgb_callback(self, msg):
#         self.process_frame('rescaled_rgb', msg, encoding='bgr8')

#     def rescaled_yolo_callback(self, msg):
#         self.process_frame('rescaled_yolo', msg, encoding='bgr8')

#     def depth_image_callback(self, msg):
#         self.process_frame('depth_image', msg, encoding='passthrough', is_depth=True)

#     def optris_bw_callback(self, msg):
#         self.process_frame('optris_bw', msg, encoding='bgr8')

#     def yolo_callback(self, msg):
#         self.process_frame('yolo', msg, encoding='bgr8')

#     def process_frame(self, prefix, msg, encoding='bgr8', is_depth=False):
#         if not self.is_recording:
#             return

#         # Obtiene el *time stamp* del mensaje en segundos
#         msg_time = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9

#         # Inicializa el tiempo de inicio para sincronización si es el primer fotograma
#         if self.start_time is None:
#             self.start_time = msg_time

#         # Calcula el tiempo desde el inicio
#         elapsed_time = msg_time - self.start_time

#         try:
#             if is_depth:
#                 frame = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding=encoding)
#                 depth_image_normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
#                 frame = cv2.convertScaleAbs(depth_image_normalized)
#                 frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
#             else:
#                 frame = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding=encoding)

#             if prefix not in self.video_writers:
#                 frame_size = (frame.shape[1], frame.shape[0])
#                 self.initialize_video_writer(prefix, frame_size)

#             # Alineación temporal: Rellena con el último fotograma si hay un salto en el *time stamp*
#             last_time = self.last_frame_time.get(prefix, self.start_time)
#             while last_time + self.frame_interval <= msg_time:
#                 # Escribe el último fotograma grabado para sincronización
#                 if prefix in self.video_writers and self.video_writers[prefix] is not None:
#                     self.video_writers[prefix].write(frame)
#                     self.frame_counts[prefix] += 1
#                     last_time += self.frame_interval

#             # Escribe el fotograma actual y actualiza `last_frame_time`
#             if prefix in self.video_writers and self.video_writers[prefix] is not None:
#                 self.video_writers[prefix].write(frame)
#                 self.frame_counts[prefix] += 1
#                 self.last_frame_time[prefix] = msg_time

#         except Exception as e:
#             self.get_logger().error(f'Failed to process frame for {prefix}: {e}')

#     def keypress_listener(self):
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         tty.setcbreak(fd)
#         try:
#             while True:
#                 if sys.stdin.read(1) == 's':
#                     self.is_recording = not self.is_recording
#                     if self.is_recording:
#                         self.start_time = None  # Se establecerá en el primer mensaje recibido
#                         self.last_frame_time = {}
#                         self.get_logger().info('Recording started. Press "s" again to stop.')
#                     else:
#                         self.get_logger().info('Recording stopped. Press "s" again to start.')
#                         self.release_video_writers()
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#     def release_video_writers(self):
#         for writer in self.video_writers.values():
#             writer.release()
#         self.video_writers.clear()
#         self.frame_counts.clear()
#         self.get_logger().info('All video writers released.')

#     def run(self):
#         self.get_logger().info('Press "s" to start/stop recording.')
#         try:
#             rclpy.spin(self)
#         except KeyboardInterrupt:
#             self.get_logger().info('SIGINT received. Exiting...')
#         finally:
#             self.cleanup()

#     def cleanup(self):
#         self.get_logger().info('Cleaning up...')
#         self.release_video_writers()
#         if rclpy.ok():
#             self.destroy_node()

# def main(args=None):
#     rclpy.init(args=args)
#     node = None
#     try:
#         node = VideoSaverNode()
#         node.run()
#     except Exception as e:
#         if node:
#             node.get_logger().error(f'Exception in main: {e}')
#         else:
#             print(f'Error during initialization: {e}')
#     finally:
#         if node:
#             node.cleanup()
#         if rclpy.ok():
#             rclpy.shutdown()

# if __name__ == '__main__':
#     main()








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
import time
import glob

class VideoSaverNode(Node):
    def __init__(self):
        super().__init__('video_saver_node')
        self.get_logger().info('Initializing VideoSaverNode...')

        # Configuración de tópicos a grabar (modificar aquí)
        topics_to_record = [
            'realsense',        # Cámara RGB
            'masked_image',     # Imagen con máscara de temperatura
            'rescaled_rgb',     # Imagen RGB reescalada
            'rescaled_yolo',    # Máscara YOLO reescalada
            'depth_image',      # Imagen de profundidad
            'optris_bw',        # Imagen en blanco y negro de Optris
            'optris',         # Imagen térmica
            'yolo'            # Imagen YOLO
        ]

        # Crear suscripciones solo para los tópicos seleccionados
        self.cv_bridge = CvBridge()
        self.save_base_dir = '/home/yeray/sensors_ws/src/ProvesDeCamp/25Octubre2024/Calibration1280'
        self.date_str = datetime.now().strftime("%B%d")
        self.video_writers = {}
        self.frame_counts = {}
        self.is_recording = False
        self.fps = 30
        self.frame_interval = 1.0 / self.fps

        # Variables para sincronización
        self.start_time = None
        self.last_frame_time = {}

        # Definir suscripciones para los tópicos seleccionados
        if 'realsense' in topics_to_record:
            self.realsense_sub = self.create_subscription(Image, '/camera/camera/color/image_raw', self.realsense_callback, 10)
        if 'masked_image' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/masked_image_with_temperature', self.masked_image_callback, 10)
        if 'rescaled_rgb' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_rgb', self.rescaled_rgb_callback, 10)
        if 'rescaled_yolo' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/Temperature_and_CSWI/rescaled_yolo_masks', self.rescaled_yolo_callback, 10)
        if 'depth_image' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/camera/camera/depth/image_rect_raw', self.depth_image_callback, 10)
        if 'optris_bw' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/thermal_image', self.optris_bw_callback, 10)
        if 'optris' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/thermal_image_view', self.optris_callback, 10)
        if 'yolo' in topics_to_record:
            self.optris_sub = self.create_subscription(Image, '/yolo_image', self.yolo_callback, 10)

        self.get_logger().info('VideoSaverNode has been started.')

        # Crear directorios si no existen
        self.directories = self.create_directories()

        # Iniciar el hilo para escuchar teclas
        self.key_thread = threading.Thread(target=self.keypress_listener, daemon=True)
        self.key_thread.start()

    def create_directories(self):
        directories = {
            'realsense': os.path.join(self.save_base_dir, 'Normal'),
            'optris': os.path.join(self.save_base_dir, 'Thermal'),
            'masked_image': os.path.join(self.save_base_dir, 'MaskedImageCSWITemperature'),
            'rescaled_rgb': os.path.join(self.save_base_dir, 'RescaledRGB'),
            'rescaled_yolo': os.path.join(self.save_base_dir, 'RescaledYOLO'),
            'depth_image': os.path.join(self.save_base_dir, 'DepthImage'),
            'optris_bw': os.path.join(self.save_base_dir, 'OptrisBW'),
            'yolo': os.path.join(self.save_base_dir, 'YOLO')
        }

        for key, directory in directories.items():
            os.makedirs(directory, exist_ok=True)
            self.get_logger().info(f'Ensured directory exists: {directory}')
        return directories

    def get_next_index(self, prefix):
        directory = self.directories[prefix]
        existing_files = glob.glob(os.path.join(directory, f'{self.date_str}_{prefix}_*.avi'))
        if not existing_files:
            return 1
        max_index = max([int(os.path.splitext(f)[0].split('_')[-1]) for f in existing_files])
        return max_index + 1

    def initialize_video_writer(self, prefix, frame_size):
        index = self.get_next_index(prefix)
        codecs = cv2.VideoWriter_fourcc(*'MJPG')  # Codec compatible para .avi
        file_path = os.path.join(self.directories[prefix], f'{self.date_str}_{prefix}_{index}.avi')
        video_writer = cv2.VideoWriter(file_path, codecs, self.fps, frame_size)

        if not video_writer.isOpened():
            self.get_logger().error(f'Failed to initialize VideoWriter for {prefix}. Check codec and file path.')
            return None

        self.video_writers[prefix] = video_writer
        self.frame_counts[prefix] = 0
        self.get_logger().info(f'Initialized video writer for {prefix} at {file_path} with frame size {frame_size} and FPS {self.fps}')

    def realsense_callback(self, msg):
        self.process_frame('realsense', msg, encoding='bgr8')

    def optris_callback(self, msg):
        self.process_frame('optris', msg, encoding='bgr8')

    def masked_image_callback(self, msg):
        self.process_frame('masked_image', msg, encoding='bgr8')

    def rescaled_rgb_callback(self, msg):
        self.process_frame('rescaled_rgb', msg, encoding='bgr8')

    def rescaled_yolo_callback(self, msg):
        self.process_frame('rescaled_yolo', msg, encoding='bgr8')

    def depth_image_callback(self, msg):
        self.process_frame('depth_image', msg, encoding='passthrough', is_depth=True)

    def optris_bw_callback(self, msg):
        self.process_frame('optris_bw', msg, encoding='bgr8')

    def yolo_callback(self, msg):
        self.process_frame('yolo', msg, encoding='bgr8')

    def process_frame(self, prefix, msg, encoding='bgr8', is_depth=False):
        if not self.is_recording:
            return

        # Obtiene el *time stamp* del mensaje en segundos
        msg_time = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9

        # Inicializa el tiempo de inicio para sincronización si es el primer fotograma
        if self.start_time is None:
            self.start_time = msg_time

        # Calcula el tiempo desde el inicio
        elapsed_time = msg_time - self.start_time

        try:
            if is_depth:
                frame = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding=encoding)
                depth_image_normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
                frame = cv2.convertScaleAbs(depth_image_normalized)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            else:
                frame = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding=encoding)

            if prefix not in self.video_writers:
                frame_size = (frame.shape[1], frame.shape[0])
                self.initialize_video_writer(prefix, frame_size)

            # Alineación temporal: Rellena con el último fotograma si hay un salto en el *time stamp*
            last_time = self.last_frame_time.get(prefix, self.start_time)
            while last_time + self.frame_interval <= msg_time:
                # Escribe el último fotograma grabado para sincronización
                if prefix in self.video_writers and self.video_writers[prefix] is not None:
                    self.video_writers[prefix].write(frame)
                    self.frame_counts[prefix] += 1
                    last_time += self.frame_interval

            # Escribe el fotograma actual y actualiza `last_frame_time`
            if prefix in self.video_writers and self.video_writers[prefix] is not None:
                self.video_writers[prefix].write(frame)
                self.frame_counts[prefix] += 1
                self.last_frame_time[prefix] = msg_time

        except Exception as e:
            self.get_logger().error(f'Failed to process frame for {prefix}: {e}')

    def keypress_listener(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        try:
            while True:
                if sys.stdin.read(1) == 's':
                    self.is_recording = not self.is_recording
                    if self.is_recording:
                        self.start_time = None  # Se establecerá en el primer mensaje recibido
                        self.last_frame_time = {}
                        self.get_logger().info('Recording started. Press "s" again to stop.')
                    else:
                        self.get_logger().info('Recording stopped. Press "s" again to start.')
                        self.release_video_writers()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def release_video_writers(self):
        for writer in self.video_writers.values():
            writer.release()
        self.video_writers.clear()
        self.frame_counts.clear()
        self.get_logger().info('All video writers released.')

    def run(self):
        self.get_logger().info('Press "s" to start/stop recording.')
        try:
            rclpy.spin(self)
        except KeyboardInterrupt:
            self.get_logger().info('SIGINT received. Exiting...')
        finally:
            self.cleanup()

    def cleanup(self):
        self.get_logger().info('Cleaning up...')
        self.release_video_writers()
        if rclpy.ok():
            self.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = VideoSaverNode()
        node.run()
    except Exception as e:
        if node:
            node.get_logger().error(f'Exception in main: {e}')
        else:
            print(f'Error during initialization: {e}')
    finally:
        if node:
            node.cleanup()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
