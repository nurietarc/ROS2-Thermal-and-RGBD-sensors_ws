import os
import cv2
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
from datetime import datetime
from FolderManager import FolderManager
from PersonalizedPlots import CalibrationPlots
from ReadmeGenerator import CalibrationReadme
from colorama import Fore, Style
import random

"""
Nuria Rodríguez Calderón 
CameraCalibration is a class for managing and performing camera calibration tasks for different camera types (e.g., RGB and thermal cameras).
The class provides functionality to calibrate individual cameras or perform calibration using the intersection of successfully detected chessboard patterns
across multiple cameras. It also generates calibration data, saves it, and creates visualization plots for both single-camera and intersection-based calibrations.

Key Features:
- Calibrate a single camera and save the calibration data and plots.
- Calibrate using intersection of detected patterns across multiple cameras.
- Save intrinsic and extrinsic calibration parameters and create detailed README files for data reference.
- Generate plots for visual inspection of calibration, including mosaics of images in grayscale and with detected chessboard corners.
"""

class CameraCalibration:
    def __init__(self, base_path, images_base_path, folders_names=["CalibrationPlots", "CalibrationFiles"], chessboard_size=(6,9), distortion_threshold=1e-5):
        """
        Initialize CameraCalibration with paths, folder names, chessboard settings, and distortion threshold.

        Parameters:
        - base_path (str): The root directory for storing calibration results.
        - images_base_path (str): Path to the base folder containing image data.
        - folders_names (list): Names of the folders for storing plots and calibration files.
        - chessboard_size (tuple): Size of the chessboard used for calibration (rows, columns).
        - distortion_threshold (float): Threshold for determining whether distortion is significant.
        """
        self.base_path = base_path
        self.images_base_path = images_base_path
        self.folders_names = folders_names
        self.chessboard_size = chessboard_size
        self.distortion_threshold = distortion_threshold

        self.setup_paths()
        self.setup_images()
        self.setup_chessboard_object_points()

    def setup_paths(self):
        """
        Set up necessary folders and retrieve camera types (e.g., "Normal" and "Thermal") from the folder structure.
        This function also initializes the FolderManager to create the required folders.
        """
        self.folder_manager = FolderManager(self.base_path, self.images_base_path, self.folders_names)
        self.folder_manager.create_folders()
        self.folder_manager.obtain_name_of_image_folders()
        self.images_types = self.folder_manager.folders_images_names  # List of camera types
        print("Folder names obtained (camera types):", self.images_types)

    def setup_images(self):
        """
        Load image paths for each camera type, organizing them into a dictionary for easy access.
        """
        self.images = {subfolder: glob.glob(os.path.join(self.images_base_path, subfolder, "*.png")) for subfolder in self.images_types}

    def setup_chessboard_object_points(self):
        """
        Define 3D chessboard pattern points used for calibration.
        These points are assumed to be on a plane z=0, providing a consistent reference frame.
        """
        self.objp = np.zeros((self.chessboard_size[1] * self.chessboard_size[0], 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:self.chessboard_size[0], 0:self.chessboard_size[1]].T.reshape(-1, 2)

    def find_chessboard_corners(self, img, index):
        """
        Detect chessboard corners in an image and apply transformations to enhance corner detection.

        Parameters:
        - img (ndarray): The image in which to detect chessboard corners.
        - index (str): The index or filename of the image being processed.

        Returns:
        - ret (bool): Whether the chessboard corners were successfully detected.
        - corners (ndarray): Coordinates of detected corners.
        - gray (ndarray): The grayscale version of the image used for corner detection.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        gray = cv2.bitwise_not(gray)
        ret, corners = cv2.findChessboardCornersSB(gray, self.chessboard_size, flags=cv2.CALIB_CB_EXHAUSTIVE | cv2.CALIB_CB_ACCURACY | cv2.CALIB_CB_NORMALIZE_IMAGE)
        
        if ret is True:
            # Check horizontal flip: compare x-coordinates of the first row's corners
            row_diff = corners[self.chessboard_size[0] - 1][0][0] - corners[0][0][0]
            if row_diff < 0:
                corners = corners[:, ::-1]  # Flip columns

        return ret, corners, gray

    def calibrate_single_camera(self, folder):
        """
        Calibrate a single camera by detecting chessboard patterns in the specified folder.
        Saves calibration data and plots if successful patterns are found.

        Parameters:
        - folder (str): The folder containing images for calibration.
        """
        folder_manager = FolderManager(self.base_path, self.images_base_path, self.folders_names)
        folder_manager.create_subfolders(specific_folder=folder)
        objpoints, imgpoints = [], []
        calibration_data = []
        image_files = self.images[folder]
        successful_calibrations = 0

        for fname in image_files:
            img = cv2.imread(fname)
            index = os.path.basename(fname)
            ret, corners, transformed_img = self.find_chessboard_corners(img,  index)
            if ret:
                objpoints.append(self.objp)
                imgpoints.append(corners)
                successful_calibrations += 1
                calibration_data.append({
                    'original': img,
                    'transformed': transformed_img,
                    'corners': corners
                })

        if successful_calibrations > 0:
            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[:2][::-1], None, None)
            calibration_results = {'ret': ret, 'mtx': mtx, 'dist': dist, 'rvecs': rvecs, 'tvecs': tvecs}

            output_path = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(self.folders_names[1], folder, suffix='') 
            self.save_calibration_data(folder, calibration_results, calibration_data, output_path)
            output_path = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(self.folders_names[0], folder, suffix='')
            self.save_calibration_plots(folder, calibration_data, output_path)

            print(Fore.GREEN + f"{successful_calibrations}/{len(image_files)} images were successfully calibrated." + Style.RESET_ALL)
            print(Fore.GREEN + f"Calibration completed for folder '{folder}'" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"No chessboard patterns detected in folder '{folder}'. Calibration skipped." + Style.RESET_ALL)

    def calibrate_with_intersection(self, folders=None):
        """
        Calibrate using the intersection of images where chessboard patterns are detected across multiple folders.
        Saves calibration data and plots if successful patterns are found.

        Parameters:
        - folders (list, optional): List of folders to use for intersection calibration. Defaults to all available folders.
        """
        folder_manager = FolderManager(self.base_path, self.images_base_path, self.folders_names)
        folder_manager.create_subfolders(suffix='_intersection')
        if folders is None:
            folders = self.images_types

        imgpoints_by_folder = {folder: [] for folder in folders}
        indices_by_folder = {folder: set() for folder in folders}
        calibration_data_by_folder = {folder: [] for folder in folders}

        for folder in folders:
            image_files = self.images[folder]
            for fname in image_files:
                img = cv2.imread(fname)
                index = os.path.basename(fname)
                ret, corners, transformed_img = self.find_chessboard_corners(img,  index)
                if ret:
                    indices_by_folder[folder].add(index)
                    imgpoints_by_folder[folder].append(corners)
                    calibration_data_by_folder[folder].append({
                        'original': img,
                        'transformed': transformed_img,
                        'corners': corners,
                        'filename': index
                    })

        successful_indices = set.intersection(*indices_by_folder.values())
        if not successful_indices:
            print(Fore.RED + "No common images with successful detections found across folders. Calibration skipped." + Style.RESET_ALL)
            return

        final_objpoints = []
        final_imgpoints = {folder: [] for folder in folders}
        filtered_calibration_data_by_folder = {folder: [] for folder in folders}
        
        for index in successful_indices:
            final_objpoints.append(self.objp)
            for folder in folders:
                img_index = [data['filename'] for data in calibration_data_by_folder[folder]].index(index)
                final_imgpoints[folder].append(imgpoints_by_folder[folder][img_index])
                filtered_calibration_data_by_folder[folder].append(calibration_data_by_folder[folder][img_index])

        for folder in folders:
            if len(final_objpoints) == len(final_imgpoints[folder]):
                ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(final_objpoints, final_imgpoints[folder], img.shape[:2][::-1], None, None)
                calibration_results = {'ret': ret, 'mtx': mtx, 'dist': dist, 'rvecs': rvecs, 'tvecs': tvecs}

                output_path = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(self.folders_names[1], folder) 
                self.save_calibration_data(folder, calibration_results, filtered_calibration_data_by_folder[folder], output_path)

                output_path = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(self.folders_names[0], folder)
                self.save_calibration_plots(folder, filtered_calibration_data_by_folder[folder], output_path)

                print(Fore.GREEN + f"{len(successful_indices)}/{len(image_files)} images were successfully calibrated using intersection for folder '{folder}'." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Mismatch in object points and image points for folder '{folder}'. Calibration skipped for this folder." + Style.RESET_ALL)

    def save_calibration_data(self, folder, calibration_results, calibration_data, output_path):
        """
        Save intrinsic and extrinsic camera parameters to JSON files and generate a README.

        Parameters:
        - folder (str): The folder containing images for calibration.
        - calibration_results (dict): Dictionary containing calibration results (intrinsics, distortion, etc.).
        - calibration_data (list): List of dictionaries containing images and detected corners.
        - output_path (str): Path where the calibration files will be saved.
        """
        print("Saving calibration files...")
