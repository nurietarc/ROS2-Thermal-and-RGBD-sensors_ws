import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import os
import json
from datetime import datetime

#---------------------DIRECTORIES (SET UP) ----------------------------------------------

current_datetime = datetime.now().strftime('%Y-%m-%d___%H-%M')
output_base_path = '/home/gerard/my_workspace_ros/src/Calibration/GraficosCalibracion/' #graphics/images path
results_base_path = '/home/gerard/my_workspace_ros/src/Calibration/Results/' #json and .text calibration files

subfolder_name = f'Thermal_{current_datetime}'
output_path = os.path.join(output_base_path, subfolder_name)
results_path = os.path.join(results_base_path, subfolder_name)

# Create directories if they do not exist
os.makedirs(output_path, exist_ok=True)
os.makedirs(results_path, exist_ok=True)

# Path to calibration images for the thermal camera
images_path = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/Thermal/*.png'

#---------------------FUNCTIONS ----------------------------------------------
#Function to transform blurry thermal images and save them
def transform_image_and_save(img, output_path, index):
    plt.figure(figsize=(20, 10))
    # Original image
    plt.subplot(2, 4, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(2, 4, 2)
    plt.title('Grayscale Image')
    plt.imshow(gray, cmap='gray')
    
    # Enhance contrast using histogram equalization
    gray = cv2.equalizeHist(gray)
    plt.subplot(2, 4, 3)
    plt.title('Equalized Grayscale Image')
    plt.imshow(gray, cmap='gray')
    
    # Apply a sharpening filter
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    gray = cv2.filter2D(gray, -1, kernel)
    plt.subplot(2, 4, 5)
    plt.title('Sharpened Image')
    plt.imshow(gray, cmap='gray')

    # Invert black and white colors
    gray = cv2.bitwise_not(gray)
    plt.subplot(2, 4, 6)
    plt.title('Inverted Image')
    plt.imshow(gray, cmap='gray')
    
    # Save the figure
    transformation_output_path = os.path.join(output_path, f'TransformacionesHechas_{index}.png')
    plt.savefig(transformation_output_path)
    plt.close()

    return gray

# Function to combine chessboard images in one. 
def combine_images(images, rows, cols, output_path):
    output_path = os.path.join(output_path, f'CombinedIMAGES.png')
    thumb_height, thumb_width = images[0].shape[:2]
    combined_image = np.ones((rows * thumb_height, cols * thumb_width, 3), dtype=np.uint8) * 255

    for i, img in enumerate(images):
        y = i // cols * thumb_height
        x = i % cols * thumb_width
        combined_image[y:y+thumb_height, x:x+thumb_width] = img

    cv2.imwrite(output_path, combined_image)

#--------------------- START OF THE CODE ----------------------------------------------
# Prepare object points
objp = np.zeros((6*8, 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane
successful_indices = []  # List of successful image indices
chessboard_images = []  # List to store images with detected chessboard corners

# Read thermal images and find chessboard corners
thermal_images = glob.glob(images_path)
for fname in thermal_images:
    img = cv2.imread(fname)
    
    if img is None:
        print(f"Failed to load image file: {fname}")
        continue
    
    index = os.path.basename(fname).split('_')[1].split('.')[0] # Extract index from filename
    
    gray = transform_image_and_save(img, output_path, index) #Transform thermal images and save transformations for future analysis:

    # Find chessboard corners
    flags = cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ACCURACY
    ret, corners = cv2.findChessboardCornersSB(gray, (6, 8), flags=flags)

    if ret: # If found corners, add object points and image points
        objpoints.append(objp)
        imgpoints.append(corners)
        successful_indices.append(index)

        # Draw the corners and Save the image with chessboard corners
        img = cv2.drawChessboardCorners(img, (6, 8), corners, ret)
        chessboard_images.append(img)
        cv2.imwrite(os.path.join(output_path, f'ChessboardCorners_{index}.png'), img)
    else:
        print(f"Chessboard corners not found in image with index {index}")

print(f"Images where a chessboard pattern was found: {successful_indices}") # Print the list of successful images

# Perform camera calibration for the thermal camera
ret, thermal_mtx, thermal_dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


# Print intrinsic parameters (focal length, principal point, and distortion coefficients)
print("Intrinsic matrix (camera matrix):")
print(thermal_mtx)
print("Distortion coefficients:")
print(thermal_dist)


#------------------- POST PROCESS: CHESS IMAGES + (JSON + .TEXT) CALIBRATION FILES -----------------------

# CHESS IMAGES: Combine all chessboard images into one large image with a white background
if chessboard_images:
    rows = len(chessboard_images) // 4 + 1
    cols=4
    combine_images(chessboard_images, rows, cols, output_path)
    print(f"Images saved in {output_path}")

#------------------ Intrinsic ----------------------------------------%
distortion_threshold = 1e-5  # Adjust this threshold as needed
if ret and np.linalg.norm(thermal_dist) > distortion_threshold: # Check if the norm of the distortion coefficients is above a certain threshold 

    #JSON-file
    thermal_calibration_data = {
        "mtx": thermal_mtx.tolist(),
        "dist": thermal_dist.tolist()
    }

    json_file_path = os.path.join(results_path, "thermal_calibration.json")
    with open(json_file_path, "w") as json_file:
        json.dump(thermal_calibration_data, json_file)

    print(f"Thermal calibration data saved in {json_file_path}")

    #TEXT-file 
    f_x = thermal_mtx[0, 0]  # Focal length in x direction
    f_y = thermal_mtx[1, 1]  # Focal length in y direction
    c_x = thermal_mtx[0, 2]  # Principal point x coordinate
    c_y = thermal_mtx[1, 2]  # Principal point y coordinate

    
    k1, k2, p1, p2, k3 = thermal_dist.flatten() # Extract distortion coefficients

    thermal_intrinsic_txt_format = f"thermal_intrinsic: [{f_x}, {f_y}, {c_x}, {c_y}]"
    thermal_distortion_txt_format = f"thermal_distortion: [{k1}, {k2}, {p1}, {p2}, {k3}]"

    txt_file_path = os.path.join(results_path, "thermal_calibration.txt")
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(thermal_intrinsic_txt_format + '\n')
        txt_file.write(thermal_distortion_txt_format)

    print(f"Thermal calibration data saved in {txt_file_path}")

#------------------ Extrinsic ----------------------------------------%

# JSON file
extrinsic_data = {
    "rvecs": [rvec.tolist() for rvec in rvecs],
    "tvecs": [tvec.tolist() for tvec in tvecs]
}

json_extrinsic_file_path = os.path.join(results_path, "thermal_extrinsic.json")
with open(json_extrinsic_file_path, "w") as json_extrinsic_file:
    json.dump(extrinsic_data, json_extrinsic_file)

print(f"Thermal extrinsic parameters saved in {json_extrinsic_file_path}")

# Text file
txt_extrinsic_file_path = os.path.join(results_path, "thermal_extrinsic.txt")
with open(txt_extrinsic_file_path, "w") as txt_file:
    for i in range(len(rvecs)):
        txt_file.write(f"Image {i+1}:\n")
        txt_file.write(f"Rotation Vector (rvec): {rvecs[i].flatten().tolist()}\n")
        txt_file.write(f"Translation Vector (tvec): {tvecs[i].flatten().tolist()}\n\n")

print(f"Thermal extrinsic parameters saved in {txt_extrinsic_file_path}")
