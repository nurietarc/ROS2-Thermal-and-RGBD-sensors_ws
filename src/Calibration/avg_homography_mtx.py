import numpy as np
import cv2
import os
import json
import shutil
import glob
import matplotlib.pyplot as plt
from datetime import datetime


# Función para cargar los parámetros de calibración desde un archivo JSON
def load_calibration_parameters(calibration_file):
    with open(calibration_file, 'r') as file:
        calibration_data = json.load(file)
        K = np.array(calibration_data['mtx'])  # Matriz de la cámara
        D = np.array(calibration_data['dist'])  # Coeficientes de distorsión
    return K, D

# Función para dibujar las correspondencias entre las imágenes
def draw_correspondence(img1, img2, corners1, corners2, indice, ruta_destino):
    height_img1, width_img1 = img1.shape[:2]
    height_img2, width_img2 = img2.shape[:2]

    desired_height = height_img2
    img1_resized = cv2.resize(img1, (int(width_img1 * desired_height / height_img1), desired_height))

    scale_x = img1_resized.shape[1] / width_img1
    scale_y = img1_resized.shape[0] / height_img1

    # Ajustar las coordenadas de las esquinas
    adjusted_corners1 = []
    for corner in corners1:
        x = corner[0][0] * scale_x
        y = corner[0][1] * scale_y
        adjusted_corners1.append([[x, y]])

    # Calcular la matriz de homografía
    H, _ = cv2.findHomography(np.array(adjusted_corners1), np.array(corners2))

    # Dibujar líneas entre los puntos correspondientes
    img_draw_matches = np.hstack((img1_resized, img2))
    for i in range(len(adjusted_corners1)):
        pt1 = np.array([adjusted_corners1[i][0][0], adjusted_corners1[i][0][1], 1], dtype=np.float32).reshape(3, 1)
        pt2 = np.dot(H, pt1)
        pt2 = pt2 / pt2[2]
        end = (int(img1_resized.shape[1] + pt2[0, 0]), int(pt2[1, 0]))
        start_point = (int(adjusted_corners1[i][0][0]), int(adjusted_corners1[i][0][1]))
        end_point = (end[0], end[1])
        img_draw_matches = cv2.line(img_draw_matches, start_point, end_point, (0, 255, 0), 1)

    # Guardar la imagen con las correspondencias dibujadas
    nombre_archivo = f"individual_{indice}.jpg"
    ruta_salida = os.path.join(ruta_destino, nombre_archivo)
    cv2.imwrite(ruta_salida, img_draw_matches)

# Función para calcular la homografía promedio entre las imágenes RGB y térmicas
def compute_average_homography(rgb_folder, thermal_folder, rgb_calibration_file, thermal_calibration_file, ruta_destino):
    # Cargar los parámetros de calibración intrínseca
    K_rgb, D_rgb = load_calibration_parameters(rgb_calibration_file)
    K_thermal, D_thermal = load_calibration_parameters(thermal_calibration_file)
    
    # Acumuladores para las matrices de homografía
    H_accumulated = np.zeros((3, 3))
    num_images = 0
    
    # Iterar sobre las imágenes en las carpetas RGB y térmica
    for filename in os.listdir(rgb_folder):
        if filename.endswith(".png"):
            num_images += 1
            
            # Cargar las imágenes RGB y térmica
            undistorted_rgb = cv2.imread(os.path.join(rgb_folder, filename))
            undistorted_thermal = cv2.imread(os.path.join(thermal_folder, filename))
            
            # Corregir la distorsión de las imágenes
            #undistorted_rgb = cv2.undistort(rgb_image, K_rgb, D_rgb)
            #undistorted_thermal = cv2.undistort(thermal_image, K_thermal, D_thermal)
            
            #cv2.imwrite(os.path.join(ruta_destino, f'undistorted_rgb_{filename}'), undistorted_rgb)
            #cv2.imwrite(os.path.join(ruta_destino, f'undistorted_thermal_{filename}'), undistorted_thermal)

            # Convertir las imágenes corregidas a escala de grises
            gray_rgb = cv2.cvtColor(undistorted_rgb, cv2.COLOR_BGR2GRAY)
            gray_thermal = cv2.cvtColor(undistorted_thermal, cv2.COLOR_BGR2GRAY)
            
            # Equalizar el histograma y aplicar filtro para mejorar la imagen térmica
            gray_thermal = cv2.equalizeHist(gray_thermal)
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            gray_thermal = cv2.filter2D(gray_thermal, -1, kernel)
            gray_thermal = cv2.bitwise_not(gray_thermal)
            
            # Tamaño del tablero de ajedrez (columnas, filas)
            checkerboard_size = (8, 6)
            
            # Flags para la detección del tablero de ajedrez
            flags = cv2.CALIB_CB_EXHAUSTIVE | cv2.CALIB_CB_ACCURACY | cv2.CALIB_CB_NORMALIZE_IMAGE #cambiar los flags cambia potencialmente en qué imagenes se encuentran corners
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            # Encontrar las esquinas del tablero de ajedrez en las imágenes RGB y térmica
            ret_rgb, corners_rgb = cv2.findChessboardCornersSB(gray_rgb, checkerboard_size, flags=flags)
            ret_thermal, corners_thermal = cv2.findChessboardCornersSB(gray_thermal, checkerboard_size, flags=flags)
            
            # Verificar que se encontraron las esquinas en ambas imágenes
            if ret_rgb and ret_thermal:
                print(f"Bien! Se encontraron esquinas en la imagen {filename}.")
                # Refinar las posiciones de las esquinas
                corners_rgb = cv2.cornerSubPix(gray_rgb, corners_rgb, (11, 11), (-1, -1), criteria)
                corners_thermal = cv2.cornerSubPix(gray_thermal, corners_thermal, (11, 11), (-1, -1), criteria)
                
                # Calcular la matriz de homografía entre las imágenes térmica y RGB
                H, _ = cv2.findHomography(corners_rgb, corners_thermal)
                
                # Acumular la matriz de homografía
                H_accumulated += H
                
                # Dibujar las correspondencias entre las imágenes y guardarlas
                index = os.path.basename(filename).split('_')[1].split('.')[0] # Extract index from filename
                #draw_correspondence(undistorted_rgb, undistorted_thermal, corners_rgb, corners_thermal, index, ruta_destino)
                visualize_homography_effect(undistorted_thermal, undistorted_rgb, H, ruta_destino, index)

                # Mostrar la matriz de homografía acumulada y su efecto sobre las imágenes de referencia
                #visualize_homography_effect(undistorted_rgb, undistorted_thermal, H, H_accumulated, ruta_destino)

            else:
                print(f"No se encontraron esquinas en la imagen {filename}. Revisar la detección de esquinas.")

    # Calcular la matriz de homografía promedio
    average_H = H_accumulated / num_images
    
    # Guardar la matriz de homografía promedio en un archivo de texto
    np.savetxt('/home/gerard/my_workspace_ros/src/Calibration/Results/average_homography2.txt', average_H)
    
    return average_H

def visualize_homography_effect(img1, img2, H, ruta_destino, index):

    # Obtener las dimensiones de la imagen 2
    height2, width2, channels2 = img2.shape

    # Aplicar la transformación de homografía a img1
    img1_transformed = cv2.warpPerspective(img1, H, (width2, height2))

    # Mostrar las imágenes original, transformada y la segunda imagen usando Matplotlib
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title('Imagen Original')
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 3, 2)
    plt.title('Imagen Transformada')
    plt.imshow(cv2.cvtColor(img1_transformed, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 3, 3)
    plt.title('Imagen 2')
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

    # Guardar la figura en la ruta de destino
    nombre_archivo = f"homography_effect_{index}.jpg"
    ruta_salida = os.path.join(ruta_destino, nombre_archivo)
    plt.savefig(ruta_salida)
    print(f"Imagen de efecto de homografía guardada en {ruta_salida}")

    # Cerrar la figura para liberar memoria
    plt.close()



# Función para crear la carpeta final de imágenes
def create_final_image_folder(index_list, camera_type):
    base_path = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/'
    final_folder_path = os.path.join(base_path, f'Final{camera_type}')
    
    # Crear la carpeta final si no existe
    os.makedirs(final_folder_path, exist_ok=True)
    
    # Obtener la lista de todas las imágenes
    all_images = glob.glob(os.path.join(base_path, f'{camera_type}/*.png'))
    
    # Copiar las imágenes utilizadas para la calibración a la carpeta final
    for index in index_list:
        for image_path in all_images:
            if f"_{index}." in image_path:
                shutil.copy(image_path, final_folder_path)
                break

# Configuración inicial
successful_indices = ['2', '5', '13', '14', '15', '16', '28', '29', '30', '37', '96', '97', '102', '118', '119', '127', '133', '134', '136', '137', '138']

#successful_indices = ['133', '138', '118', '105', '136', '102', '134', '28', '101', '29', '130', '5', '2', '30', '14', '119', '129', '103', '15', '96', '99', '97', '16', '128', '37', '137', '100', '127', '17', '98', '13', '116']
create_final_image_folder(successful_indices, 'Normal')
create_final_image_folder(successful_indices, 'Thermal')

# Definir las carpetas que contienen las imágenes RGB y térmicas
rgb_folder = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/FinalNormal'
thermal_folder = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/FinalThermal'

# Definir las rutas a los archivos de calibración
rgb_calibration_file = '/home/gerard/my_workspace_ros/src/Calibration/Results/Visual_2024-06-18___16-27/visual_calibration.json'
thermal_calibration_file = '/home/gerard/my_workspace_ros/src/Calibration/Results/Thermal_2024-06-18___16-21/thermal_calibration.json'

ruta_destino = '/home/gerard/my_workspace_ros/src/Calibration/GraficosCalibracion/correspondencia_termica_rgb'

# Ejecutar el cálculo de la homografía promedio
average_homography = compute_average_homography(rgb_folder, thermal_folder, rgb_calibration_file, thermal_calibration_file, ruta_destino)

# Imprimir la matriz de homografía promedio
print("Matriz de homografía promedio:")
print(average_homography)
