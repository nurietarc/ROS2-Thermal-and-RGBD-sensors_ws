import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import os
import json
from datetime import datetime

#--------------------- SET UP + DIRECTORIES ----------------------------------------------
#Successful_indices = given in the THERMAL calibration code. Copy and paste. 
successful_indices = ['133', '138', '118', '105', '136', '102', '134', '28', '101', '29', '130', '5', '2', '30', '14', '119', '129', '103', '15', '96', '99', '97', '16', '128', '37', '137', '100', '127', '17', '98', '13', '116']
print(f"Total thermal images: {len(successful_indices)}")  # Debugging statement

current_datetime = datetime.now().strftime('%Y-%m-%d___%H-%M')
output_base_path = '/home/gerard/my_workspace_ros/src/Calibration/GraficosCalibracion/' #graphics/images path
results_base_path = '/home/gerard/my_workspace_ros/src/Calibration/Results/' #json and .text calibration files

subfolder_name = f'Visual_{current_datetime}'
output_path = os.path.join(output_base_path, subfolder_name)
results_path = os.path.join(results_base_path, subfolder_name)

# Create directories if they do not exist
os.makedirs(output_path, exist_ok=True)
os.makedirs(results_path, exist_ok=True)

# Path to calibration images for the thermal camera
images_path = '/home/gerard/my_workspace_ros/src/Calibration/Imagenes/Normal/*.png'

#---------------------FUNCTIONS ----------------------------------------------
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
#Take only valid normal images (the one with same index as the thermal)
valid_normal_images = []

normal_images = glob.glob(images_path)
for fname in normal_images:
    index = fname.split('/')[-1].split('_')[1].split('.')[0]  # Extraer el índice de la imagen
    if index in successful_indices:
        valid_normal_images.append(fname)

print(f"Total valid normal images: {len(valid_normal_images)}")  # Debugging statement


# Prepare object points
objp = np.zeros((6*8, 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane
chessboard_images = []  # List to store images with detected chessboard corners
normal_images_with_no_corners_found=[]

# Read thermal images and find chessboard corners
for fname in valid_normal_images:
    img = cv2.imread(fname)
    
    if img is None:
        print(f"Failed to load image file: {fname}")
        continue
    
    index = os.path.basename(fname).split('_')[1].split('.')[0] # Extract index from filename
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find chessboard corners
    flags = cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ACCURACY
    ret, corners = cv2.findChessboardCornersSB(gray, (6, 8), flags=flags)

    if ret: # If found corners, add object points and image points
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw the corners and Save the image with chessboard corners
        img = cv2.drawChessboardCorners(img, (6, 8), corners, ret)
        chessboard_images.append(img)
        cv2.imwrite(os.path.join(output_path, f'ChessboardCorners_{index}.png'), img)
    else:
        normal_images_with_no_corners_found.append(index)
        print(f"Chessboard corners not found in image with index {index}. Please, delete that image in both thermal and visual images folders and re-start calibration.")

if normal_images_with_no_corners_found:
    print(f"Indexes of images to delete {normal_images_with_no_corners_found}")
if not normal_images_with_no_corners_found:
    print("All calibration images found chessboard corners for the normal camera.")

# Perform camera calibration for the thermal camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print intrinsic parameters (focal length, principal point, and distortion coefficients)
print("Intrinsic matrix (camera matrix):")
print(mtx)
print("Distortion coefficients:")
print(dist)

#------------------- POST PROCESS: CHESS IMAGES + (JSON + .TEXT) CALIBRATION FILES -----------------------

# CHESS IMAGES: Combine all chessboard images into one large image with a white background
if chessboard_images:
    rows = len(chessboard_images) // 4 + 1
    cols = 4
    combine_images(chessboard_images, rows, cols, output_path)
    print(f"Images saved in {output_path}")

#------------------ Intrinsic ----------------------------------------%
distortion_threshold = 1e-5  # Adjust this threshold as needed
if ret and np.linalg.norm(dist) > distortion_threshold: # Check if the norm of the distortion coefficients is above a certain threshold 

    #JSON-file
    thermal_calibration_data = {
        "mtx": mtx.tolist(),
        "dist": dist.tolist()
    }

    json_file_path = os.path.join(results_path, "visual_calibration.json")
    with open(json_file_path, "w") as json_file:
        json.dump(thermal_calibration_data, json_file)

    print(f"Visual calibration data saved in {json_file_path}")

    #TEXT-file 
    f_x = mtx[0, 0]  # Focal length in x direction
    f_y = mtx[1, 1]  # Focal length in y direction
    c_x = mtx[0, 2]  # Principal point x coordinate
    c_y = mtx[1, 2]  # Principal point y coordinate

    k1, k2, p1, p2, k3 = dist.flatten() # Extract distortion coefficients

    visual_intrinsic_txt_format = f"visual_intrinsic: [{f_x}, {f_y}, {c_x}, {c_y}]"
    distortion_txt_format = f"distortion: [{k1}, {k2}, {p1}, {p2}, {k3}]"

    txt_file_path = os.path.join(results_path, "visual_calibration.txt")
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(visual_intrinsic_txt_format + '\n')
        txt_file.write(distortion_txt_format)

    print(f"Visual calibration data saved in {txt_file_path}")

#------------------ Extrinsic ----------------------------------------%

# JSON file
extrinsic_data = {
    "rvecs": [rvec.tolist() for rvec in rvecs],
    "tvecs": [tvec.tolist() for tvec in tvecs]
}

json_extrinsic_file_path = os.path.join(results_path, "visual_extrinsic.json")
with open(json_extrinsic_file_path, "w") as json_extrinsic_file:
    json.dump(extrinsic_data, json_extrinsic_file)

print(f"Visual extrinsic parameters saved in {json_extrinsic_file_path}")

# Text file
txt_extrinsic_file_path = os.path.join(results_path, "visual_extrinsic.txt")
with open(txt_extrinsic_file_path, "w") as txt_file:
    for i in range(len(rvecs)):
        txt_file.write(f"Image {i+1}:\n")
        txt_file.write(f"Rotation Vector (rvec): {rvecs[i].flatten().tolist()}\n")
        txt_file.write(f"Translation Vector (tvec): {tvecs[i].flatten().tolist()}\n\n")

print(f"Visual extrinsic parameters saved in {txt_extrinsic_file_path}")
