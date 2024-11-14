# import os
# import cv2
# import rclpy
# import subprocess
# import time
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# from pathlib import Path

# class ImageSaver(Node):
#     def __init__(self, output_folder):
#         super().__init__('image_saver')
#         self.bridge = CvBridge()
#         self.subscription = self.create_subscription(
#             Image,
#             '/thermal_image_view',  # Ajusta el tópico si es necesario
#             self.listener_callback,
#             10)
#         self.output_folder = output_folder
#         os.makedirs(self.output_folder, exist_ok=True)
#         self.frame_count = 0

#     def listener_callback(self, msg):
#         # Convertir mensaje a imagen y guardar
#         img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
#         cv2.imwrite(f"{self.output_folder}/frame{self.frame_count:06d}.png", img)
#         self.frame_count += 1
#         self.get_logger().info(f"Saved frame {self.frame_count} to {self.output_folder}")

# def main(args=None):
#     # Configuración de la ruta del rosbag y del directorio de salida
#     bag_path = 'src/ProvesDeCamp/Rosbags/recording_1__thermal_image_view'
#     output_folder = Path(bag_path)  # Usar el mismo directorio para guardar imágenes

#     # Iniciar ROS 2 y el nodo
#     rclpy.init(args=args)
#     image_saver = ImageSaver(output_folder)

#     # Ejecutar `ros2 bag play` como un proceso separado
#     play_process = subprocess.Popen(['ros2', 'bag', 'play', str(bag_path)])

#     try:
#         # Ejecutar el nodo mientras el rosbag se reproduce
#         rclpy.spin(image_saver)
#     except KeyboardInterrupt:
#         image_saver.get_logger().info("Interrumpido por el usuario, deteniendo...")
#     finally:
#         # Finalizar el proceso de reproducción del rosbag y limpiar
#         play_process.terminate()
#         play_process.wait()
#         image_saver.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()






import os
import cv2
import rclpy
import subprocess
import yaml
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from pathlib import Path

class ImageSaver(Node):
    def __init__(self, output_folder, topic_name):
        super().__init__('image_saver')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            topic_name,  # Se suscribe dinámicamente al topic detectado
            self.listener_callback,
            10)
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.frame_count = 0

    def listener_callback(self, msg):
        try:
            # Ajuste en la conversión según el tipo de codificación de la imagen
            if msg.encoding == 'bgr8':
                img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            elif msg.encoding == 'rgb8':
                img = self.bridge.imgmsg_to_cv2(msg, 'rgb8')
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convertir de RGB a BGR para OpenCV
            elif msg.encoding == 'mono8':
                img = self.bridge.imgmsg_to_cv2(msg, 'mono8')
            elif msg.encoding == 'mono16':
                img = self.bridge.imgmsg_to_cv2(msg, 'mono16')
                img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  # Escala a 8 bits
            elif msg.encoding == '16UC1':
                img = self.bridge.imgmsg_to_cv2(msg, '16UC1')  # Conversión sin color para profundidad
                img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)  # Escala a 8 bits
            else:
                self.get_logger().warn(f"Unsupported encoding: {msg.encoding}")
                return

            # Guardar la imagen
            cv2.imwrite(f"{self.output_folder}/frame{self.frame_count:06d}.png", img)
            self.frame_count += 1
            self.get_logger().info(f"Saved frame {self.frame_count} to {self.output_folder}")

        except CvBridgeError as e:
            self.get_logger().error(f"Failed to convert image: {e}")

def detect_topic(bag_path):
    metadata_path = Path(bag_path) / "metadata.yaml"
    if metadata_path.exists():
        with open(metadata_path, 'r') as file:
            metadata = yaml.safe_load(file)
            topics = metadata.get('rosbag2_bagfile_information', {}).get('topics_with_message_count', [])
            if topics:
                # Extrae el nombre del primer topic en la lista
                return topics[0]['topic_metadata']['name']
    return None

def process_rosbag(bag_path):
    # Detecta el topic en el rosbag
    topic_name = detect_topic(bag_path)
    if not topic_name:
        print(f"No topic found in rosbag at {bag_path}")
        return

    print(f"Detected topic '{topic_name}' in rosbag at {bag_path}")

    # Configuración del directorio de salida para las imágenes
    output_folder = Path(bag_path) / 'images'  # Guardar imágenes en una subcarpeta "images"
    
    # Iniciar ROS 2 y el nodo de guardado de imágenes
    rclpy.init(args=None)
    image_saver = ImageSaver(output_folder, topic_name)

    # Ejecutar `ros2 bag play` como un proceso separado
    play_process = subprocess.Popen(['ros2', 'bag', 'play', str(bag_path)])

    try:
        # Ejecutar el nodo mientras el rosbag se reproduce
        while play_process.poll() is None:
            rclpy.spin_once(image_saver, timeout_sec=1.0)
    except KeyboardInterrupt:
        image_saver.get_logger().info("Interrumpido por el usuario, deteniendo...")
    finally:
        # Finalizar el proceso de reproducción del rosbag y limpiar
        play_process.terminate()
        play_process.wait()
        image_saver.destroy_node()
        rclpy.shutdown()

def main():
    # Directorio base donde se encuentran las carpetas de rosbags
    base_folder = Path('src/ProvesDeCamp/Rosbags')

    # Recorrer todas las carpetas dentro de `base_folder`
    for bag_folder in base_folder.iterdir():
        if bag_folder.is_dir():
            print(f"Processing rosbag in folder: {bag_folder}")
            process_rosbag(bag_folder)

if __name__ == '__main__':
    main()
