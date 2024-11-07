import numpy as np
import cv2
import json

# Load calibration parameters
with open('/home/giovannaguaragnella/CameraCalibration/codes/rgb_calibration.json', 'r') as f:
    rgb_calibration = json.load(f)

with open('/home/giovannaguaragnella/CameraCalibration/codes/thermal_calibration.json', 'r') as f:
    thermal_calibration = json.load(f)

with open('/home/giovannaguaragnella/CameraCalibration/codes/rgb_extrinsic.json', 'r') as f:
    rgb_extrinsic = json.load(f)

with open('/home/giovannaguaragnella/CameraCalibration/codes/thermal_extrinsic.json', 'r') as f:
    thermal_extrinsic = json.load(f)

# Extract intrinsic parameters
K_rgb = np.array(rgb_calibration['mtx'])
K_thermal = np.array(thermal_calibration['mtx'])

# Extract extrinsic parameters
rvecs_rgb = np.array(rgb_extrinsic['rvecs'])
tvecs_rgb = np.array(rgb_extrinsic['tvecs'])

rvecs_thermal = np.array(thermal_extrinsic['rvecs'])
tvecs_thermal = np.array(thermal_extrinsic['tvecs'])

# Convert rotation vectors to rotation matrices
R_rgb = [cv2.Rodrigues(rvec)[0] for rvec in rvecs_rgb]
R_thermal = [cv2.Rodrigues(rvec)[0] for rvec in rvecs_thermal]

# Compute homography matrices for each pair of images
homography_matrices = []
for i in range(len(rvecs_rgb)):
    R_relative = np.dot(R_rgb[i].T, R_thermal[i])
    t_relative = np.dot(-R_rgb[i].T, tvecs_thermal[i]) + tvecs_rgb[i]
    H = np.dot(K_rgb, np.dot(R_relative - np.outer(t_relative, [0, 0, 1]), np.linalg.inv(K_thermal)))
    H /= H[2, 2]
    homography_matrices.append(H)

# Save homography matrices to a file
output_file = '/home/giovannaguaragnella/CameraCalibration/homography_matrices.json'
with open(output_file, 'w') as f:
    json.dump([H.tolist() for H in homography_matrices], f)

print("Homography matrices saved to", output_file)

# Compute the average homography matrix
average_homography = np.mean(homography_matrices, axis=0)

# Normalize homography matrix
average_homography /= average_homography[2, 2]

print("Average Homography Matrix:")
print(average_homography)

# Save homography matrix to a file
output_file = '/home/giovannaguaragnella/CameraCalibration/average_homography_matrix.json'
with open(output_file, 'w') as f:
    json.dump(average_homography.tolist(), f)

print("Average Homography matrix saved to", output_file)

## this code is similar to avg_homography_mtx.py with difference that uses directly the calibration files generated!
