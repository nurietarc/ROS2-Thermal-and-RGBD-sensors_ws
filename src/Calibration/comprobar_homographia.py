import cv2
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del tablero de ajedrez
chessboard_size = (8, 6)  # Número de esquinas interiores en el tablero (filas, columnas)

# Flags para la detección del tablero de ajedrez
flags = cv2.CALIB_CB_EXHAUSTIVE | cv2.CALIB_CB_ACCURACY | cv2.CALIB_CB_NORMALIZE_IMAGE

# Criterios de terminación para el refinamiento de las esquinas
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Función para detectar las esquinas del tablero de ajedrez
def detect_chessboard_corners(image, chessboard_size, flags):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCornersSB(gray, chessboard_size, flags=flags)
    if ret:
        corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return ret, corners

# Cargar las dos imágenes
img1 = cv2.imread('/home/yeray/sensors_ws/src/Calibration/Imagenes/FinalNormal/June06_136.png') #13
img2 = cv2.imread('/home/yeray/sensors_ws/src/Calibration/Imagenes/FinalThermal/June06_136.png')

# Asegurarse de que las imágenes se cargaron correctamente
if img1 is None or img2 is None:
    print("Error: Una de las imágenes no se pudo cargar.")
    exit()

# Detectar las esquinas del tablero de ajedrez en ambas imágenes
ret1, corners1 = detect_chessboard_corners(img1, chessboard_size, flags)
ret2, corners2 = detect_chessboard_corners(img2, chessboard_size, flags)

if not ret1 or not ret2:
    print("Error: No se pudieron detectar las esquinas del tablero de ajedrez en ambas imágenes.")
    exit()

# Calcular la matriz de homografía
print(f"corners rgb {corners1}")
print(f"corners termica {corners2}")
H, status = cv2.findHomography(corners1, corners2)

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

plt.show()

print(H)