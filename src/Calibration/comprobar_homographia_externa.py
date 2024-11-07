import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para leer la matriz de homografía desde un archivo txt
def read_homography_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        H = np.array([[float(num) for num in line.split()] for line in lines])
    return H

# Ruta al archivo de la matriz de homografía
homography_file = '/home/yeray/sensors_ws/src/Calibration/Results/average_homography2.txt'

# Leer la matriz de homografía
H = read_homography_matrix(homography_file)
#a partir de 14_10 cambio de matrices
# Cargar las dos imágenes
img1 = cv2.imread('/home/yeray/sensors_ws/src/Calibration/Imagenes/THESIS/Normal/June25_1.png')
img2 = cv2.imread('/home/yeray/sensors_ws/src/Calibration/Imagenes/THESIS/Thermal/June25_1.png')

#img1 = cv2.imread('/home/gerard/my_workspace_ros/src/Calibration/Imagenes/FinalNormal/June06_29.png')
#img2 = cv2.imread('/home/gerard/my_workspace_ros/src/Calibration/Imagenes/FinalThermal/June06_29.png')

# Asegurarse de que las imágenes se cargaron correctamente
if img1 is None or img2 is None:
    print("Error: Una de las imágenes no se pudo cargar.")
    exit()

# Obtener las dimensiones de la imagen 2
height2, width2, channels2 = img2.shape
print(img1.shape)
# Aplicar la transformación de homografía a img1
img1_transformed = cv2.warpPerspective(img1, H, (width2, height2))

# Mostrar las imágenes original, transformada y la segunda imagen usando Matplotlib
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original (Thermal) image')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Wrapped image')
plt.imshow(cv2.cvtColor(img1_transformed, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title('RGB image')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.show()
