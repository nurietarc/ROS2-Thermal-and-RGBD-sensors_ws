import numpy as np
import cv2
import glob
import json
import os
from datetime import datetime

# Función para combinar imágenes con fondo blanco
def combine_images(images, rows, cols, output_path):
    thumb_height, thumb_width = images[0].shape[:2]
    combined_image = np.ones((rows * thumb_height, cols * thumb_width, 3), dtype=np.uint8) * 255

    for i, img in enumerate(images):
        y = i // cols * thumb_height
        x = i % cols * thumb_width
        combined_image[y:y+thumb_height, x:x+thumb_width] = img

    cv2.imwrite(output_path, combined_image)

# Obtener la fecha y hora actual
current_datetime = datetime.now()
date_string = current_datetime.strftime("%Y%m%d_%H%M%S")

# Path de las imágenes con el patrón de ajedrez para la cámara normal
normal_images_path = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/Normal/*.png'

# Extraer solo las imágenes con un patrón de ajedrez detectado
successful_indices = ['133', '138', '118', '105', '136', '102', '134', '28', '101', '22', '29', '130', '5', '2', '30', '14', '119', '129', '20', '21', '103', '15', '96', '99', '97', '16', '128', '37', '137', '121', '19', '100', '127', '17', '98', '13', '18', '142', '116']

# Lista para almacenar imágenes válidas
valid_normal_images = []

# Leer imágenes y encontrar las esquinas del tablero de ajedrez
normal_images = glob.glob(normal_images_path)
for fname in normal_images:
    index = fname.split('/')[-1].split('_')[1].split('.')[0]  # Extraer el índice de la imagen
    if index in successful_indices:
        img = cv2.imread(fname)
        valid_normal_images.append(img)

# Path donde se guardarán las imágenes combinadas
output_base_path = '/home/gerard/my_workspace_ros/src/Calibration/GraficosCalibracion/'
output_path = os.path.join(output_base_path, f'PUNTOSAjedrez_{date_string}.png')

# Combinar imágenes y guardar la imagen combinada
if valid_normal_images:
    rows = len(valid_normal_images) // 4 + 1
    cols = 4
    combine_images(valid_normal_images, rows, cols, output_path)
    print(f"Combined chessboard images saved to: {output_path}")
else:
    print("No valid chessboard images found.")

# Path a la carpeta donde se guardarán los resultados
results_path = f'/home/gerard/my_workspace_ros/src/Calibration/Results/RGB_{date_string}/'

# Crea el directorio si no existe
os.makedirs(results_path, exist_ok=True)

# Obtener los índices de las imágenes utilizadas para la calibración de la cámara térmica
thermal_indices = [fname.split('/')[-1].split('_')[1].split('.')[0] for fname in glob.glob('/home/gerard/my_workspace_ros/src/Calibration/Imagenes/Thermal/*.png')]

# Verificar si todas las imágenes de calibración de la cámara normal tienen esquinas de tablero de ajedrez detectadas
missing_normal_indices = [index for index in successful_indices if index not in [fname.split('/')[-1].split('_')[1].split('.')[0] for fname in normal_images]]

if missing_normal_indices:
    print("Calibration images missing chessboard corners for normal camera with the following indices:")
    print(missing_normal_indices)
else:
    print("All calibration images found chessboard corners for the normal camera.")


# Prepare object points
objp = np.zeros((6*8, 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Read thermal images and find chessboard corners
for fname in normal_images:
    index = fname.split('/')[-1].split('_')[1].split('.')[0]  # Extraer el índice de la imagen
    if index in successful_indices:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCornersSB(gray, (6, 8), flags=cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ACCURACY)

        # If found, add object points and image points
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (6, 8), corners, ret)
            #cv2.imshow('img', img)
            #cv2.waitKey(2000)

cv2.destroyAllWindows()

# Get the shape of the first image to obtain image resolution
img_shape = cv2.imread(normal_images[0]).shape[:2]  # Extract width and height

# Perform camera calibration
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_shape, None, None)

# Print intrinsic parameters (focal length, principal point, and distortion coefficients)
print("Intrinsic matrix (camera matrix):")
print(mtx)
print("Distortion coefficients:")
print(dist)

# Define el directorio donde se guardarán los archivos
images_path = results_path

# Crea el directorio si no existe
os.makedirs(images_path, exist_ok=True)

#------------------ CALIBRATION/INTRINSIC DATA ----------------------------------------%

# Convierte los parámetros de calibración a un formato compatible con JSON
calibration_data = {
    "mtx": mtx.tolist(),
    "dist": dist.tolist()
}

# Guarda los datos de calibración en un archivo JSON
json_file_path = images_path + "rgb_calibration.json"
with open(json_file_path, "w") as json_file:
    json.dump(calibration_data, json_file)

print(f"Calibration data saved to {json_file_path}")

# Guarda los datos de calibración en un archivo txt en el formato deseado
txt_file_path = images_path + "rgb_intrinsic.txt"
with open(txt_file_path, "w") as txt_file:
    txt_file.write("rgb_intrinsic: [{:.5f}, {:.5f}, {:.5f}, {:.5f}]\n".format(mtx[0, 0], mtx[1, 1], mtx[0, 2], mtx[1, 2]))

print(f"Calibration data saved to {txt_file_path}")

#------------------ Extrinsic DATA ----------------------------------------%

# Convierte los parámetros extrínsecos a un formato compatible con JSON
extrinsic_data = {
    "rvecs": [rvec.tolist() for rvec in rvecs],
    "tvecs": [tvec.tolist() for tvec in tvecs]
}

# Guarda los parámetros extrínsecos en un archivo JSON
json_extrinsic_file_path = images_path + "rgb_extrinsic.json"
with open(json_extrinsic_file_path, "w") as json_extrinsic_file:
    json.dump(extrinsic_data, json_extrinsic_file)

print(f"Extrinsic parameters saved to {json_extrinsic_file_path}")

# Guarda los parámetros extrínsecos en un archivo txt
txt_extrinsic_file_path = images_path + "rgb_extrinsic.txt"
with open(txt_extrinsic_file_path, "w") as txt_extrinsic_file:
    for i in range(len(rvecs)):
        txt_extrinsic_file.write(f"Image {i+1}:\n")
        txt_extrinsic_file.write(f"Rotation vector (rvec): {rvecs[i].flatten().tolist()}\n")
        txt_extrinsic_file.write(f"Translation vector (tvec): {tvecs[i].flatten().tolist()}\n\n")

print(f"Rgb extrinsic parameters saved to {txt_extrinsic_file_path}")

'''
Parámetros Intrínsecos:

    Matriz Intrínseca (mtx): Define la transformación de coordenadas 3D de la cámara a coordenadas 2D de la imagen. Incluye la longitud focal y el punto principal (centro de la imagen).
    Coeficientes de Distorsión (dist): Describen cómo las lentes de la cámara distorsionan las imágenes capturadas. Corrigen distorsiones radiales y tangenciales.

Parámetros Extrínsecos:

    Vectores de Rotación (rvecs): Describen la rotación de la cámara en el espacio 3D.
    Vectores de Traslación (tvecs): Describen la traslación (desplazamiento) de la cámara en el espacio 3D.
'''
