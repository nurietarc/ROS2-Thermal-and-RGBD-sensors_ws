#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import sys
import tty
import termios
from select import select

class ImageSaver(Node):
    def __init__(self, topic, folder):
        super().__init__('image_saver_' + topic.replace('/', '_'))
        self.topic = topic
        self.folder = folder
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(Image, topic, self.image_callback, 10)
        self.latest_image = None  # Variable para almacenar la imagen más reciente recibida
        self.counter = 0  # Contador para los nombres de archivo de imagen
        self.tty_settings = termios.tcgetattr(sys.stdin)

    def __del__(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.tty_settings)

    def image_callback(self, data):
        try:
            if data.encoding == "8UC1":  # Manejar imágenes en escala de grises
                cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
                cv_image = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2BGR)  # Convertir escala de grises a BGR
            elif data.encoding == "16UC1":  # Manejar imágenes de profundidad
                cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
                cv_image = cv2.convertScaleAbs(cv_image, alpha=0.03)  # Escalado para visualización
                cv_image = cv2.applyColorMap(cv_image, cv2.COLORMAP_JET)  # Aplicar mapa de color para visualización
            else:
                cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
                
            self.latest_image = cv_image  # Almacenar la imagen más reciente recibida
        except Exception as e:
            self.get_logger().error(str(e))

    def key_pressed(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select([sys.stdin], [], [], 0.1)
        if rlist:
            char = sys.stdin.read(1)
            if char == 's':
                return True
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.tty_settings)
        return False

    def save_image(self):
        try:
            if self.latest_image is not None:
                filename = os.path.join(self.folder, f'img_{self.counter}.jpg')  # Nombre de archivo con ruta de carpeta
                
                # Verificar si la carpeta existe, crear si no
                if not os.path.exists(self.folder):
                    os.makedirs(self.folder)
                
                cv2.imwrite(filename, self.latest_image)
                self.get_logger().info(f"Imagen guardada: {filename}")
                self.counter += 1  # Incrementar el contador para la próxima imagen
        except Exception as e:
            self.get_logger().error(f"Fallo al guardar la imagen: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    
    # Crear nodos para cada instancia de ImageSaver
    image_saver_rgb = ImageSaver('/camera/color/image_raw', '/home/my_workspace_ros/pictures/FirstTry/single_pics/rgb_img')
    image_saver_thermal = ImageSaver('/optris/thermal_image_view', '/home/my_workspace_ros/pictures/FirstTry/single_pics/thermal_img')
    image_saver_depth = ImageSaver('/camera/depth/image_rect_raw', '/home/my_workspace_ros/pictures/FirstTry/single_pics/depth_img')
    image_saver_yolo = ImageSaver('/yolo_image', '/home/my_workspace_ros/pictures/FirstTry/single_pics/yolo_img')
    image_saver_yolo_mask = ImageSaver('/yolo_individual_masks', '/home/my_workspace_ros/pictures/FirstTry/single_pics/yolo_img_mask')
    image_saver_yolo_masks = ImageSaver('/yolo_combined_masks', '/home/my_workspace_ros/pictures/FirstTry/single_pics/yolo_img_combined_masks')
    image_saver_temperature = ImageSaver('/masked_images', '/home/my_workspace_ros/pictures/FirstTry/single_pics/temperature_masks')
    image_saver_overlay = ImageSaver('/overlay_image', '/home/my_workspace_ros/pictures/FirstTry/single_pics/overlay_pics')

    nodes = [
        image_saver_rgb,
        image_saver_thermal,
        image_saver_depth,
        image_saver_yolo,
        image_saver_yolo_mask,
        image_saver_yolo_masks,
        image_saver_temperature,
        image_saver_overlay
    ]

    try:
        while rclpy.ok():
            if any(node.key_pressed() for node in nodes):
                for node in nodes:
                    node.save_image()
            for node in nodes:
                rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        for node in nodes:
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
