import os
import cv2
import numpy as np
from CameraCalibration import CameraCalibration
from FolderManager import FolderManager
from Homography import Homography

"""
Nuria Rodríguez Calderón

This script tests the calibration process for different cameras and computes the homography transformation between two views.
It uses the CameraCalibration and Homography classes to handle the calibration of different camera types and compute the transformation
needed to align images from different perspectives.

Steps:
1. Deletes all existing calibration-related folders.
2. Performs intersection-based camera calibration (or comented, an exemple for the Normal camera type). 
3. Deletes all existing homography-related folders.
4. Computes the average homography between images from two cameras (Normal and Thermal).
"""

# Initial configuration
base_path = "C:\\Users\\nrodriguez\\Desktop\\Calibracion\\CALIBRATION21del10"  # Change this path as needed
images_base_path = os.path.join(base_path, "Images")  # Base path for images
folders_names = ["CalibrationPlots", "CalibrationFiles"]

# Create FolderManager instance for calibration
folder_manager = FolderManager(base_path, images_base_path, folders_names)
folder_manager.delete_all_folders()  # Clean up previous calibration folders

# Initialize CameraCalibration and perform calibration using intersection
camera_type = "Normal"
calibration = CameraCalibration(base_path, images_base_path, folders_names, chessboard_size=(6, 9))
calibration.calibrate_with_intersection()

#-------------------------------------------------------------------------------

# Set up for homography computation
folders_names2 = ["HomographyPlots", "HomographyFiles"]
folder_manager2 = FolderManager(base_path, images_base_path, folders_names2)
folder_manager2.delete_all_folders()  # Clean up previous homography folders

folder1 = "Normal"
folder2 = "Thermal"

# Create an instance of the Homography class and compute the average homography
homography_calibration = Homography(base_path, images_base_path, folder1, folder2, folders_names2)
average_homography = homography_calibration.compute_average_homography()
