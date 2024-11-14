import json
import os
import numpy as np
import cv2
import glob
from datetime import datetime
from FolderManager import FolderManager
from ReadmeGenerator import HomographyReadme
from colorama import Fore, Style
from PersonalizedPlots import HomographyPlots
from CornerCorrector import CornerOrderCorrector
import random

"""
Nuria Rodríguez Calderón
    This class manages the computation of homographies between images from two different calibrated folders.
    The class is designed to:
    - Load calibration parameters (apart from corners) (future implementation).
    - Compute an average homography based on chessboard calibration images.
    - Save and visualize the computed homography using specified folder paths.
    - Organize paths for storing results and data using the FolderManager class.
"""

class Homography:
    def __init__(self, base_path, images_base_path, folder1, folder2, folders_names_homography=["HomographyPlots", "HomographyFiles"], folders_names_calibration=["CalibrationPlots", "CalibrationFiles"], chessboard_size=(6, 9)):
        """
        Initializes the Homography class with paths, folders, and chessboard size.
        
        Parameters:
        - base_path: The root directory for storing homography results.
        - images_base_path: Path to the base folder containing image data.
        - folder1, folder2: Names of the two folders with images to calculate homographies.
        - folders_names_homography: Names of the base folders for homography plots and files.
        - folders_names_calibration: Names of the folders containing calibration results.
        - chessboard_size: Size of the chessboard used for calibration (rows, columns).
        """
        self.base_path = base_path
        self.images_base_path = images_base_path
        self.folder1 = folder1
        self.folder2 = folder2
        self.folders_names_homography = folders_names_homography
        self.folders_names_calibration = folders_names_calibration
        self.chessboard_size = chessboard_size

        self.setup_paths() 

    def setup_paths(self):
        """
        Sets up the necessary folder paths for homography files and plots.
        Uses FolderManager to create the required folders and subfolders.
        """
        self.folder_manager = FolderManager(self.base_path, self.images_base_path, self.folders_names_homography)
        self.folder_manager.create_folders()
        self.paths = self.folder_manager.create_combined_subfolder(self.folder1, self.folder2)
        
        # Direct access to the specific paths for homography files and plots
        self.homography_files_path = self.paths["files_path"]
        self.homography_plots_path = self.paths["plots_path"]

    def find_calibration_file(self, folder_name, prefix):
        """
        Locate the latest calibration intrinsic and extrinsic files within a subfolder matching a specific prefix and ending with '_intersection'.
        
        Parameters:
        - folder_name: The name of the folder containing calibration data.
        - prefix: Prefix used for identifying the calibration files.
        
        Returns:
        - Tuple containing paths to the intrinsic and extrinsic files, or (None, None) if not found.
        """
        calibration_folder = self.folders_names_calibration[1]  # Base folder for calibration files

        # Get the latest subfolder with the specified prefix and "_intersection" suffix
        latest_subfolder = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(calibration_folder, prefix, suffix="_intersection")
        
        if latest_subfolder:
            intrinsic_file = os.path.join(latest_subfolder, f"{prefix}_intrinsic.json")
            extrinsic_file = os.path.join(latest_subfolder, f"{prefix}_extrinsic.json")

            if os.path.exists(intrinsic_file) and os.path.exists(extrinsic_file):
                return intrinsic_file, extrinsic_file
            else:
                print(Fore.RED + f"No intrinsic or extrinsic file found in '{latest_subfolder}' for prefix '{prefix}'" + Style.RESET_ALL)
                return None, None
        else:
            print(Fore.RED + f"No subfolder found with prefix '{prefix}' and suffix '_intersection' in '{calibration_folder}'" + Style.RESET_ALL)
            return None, None

    def load_calibration_parameters(self, calibration_file_path):
        """
        Load calibration parameters (intrinsic matrix and distortion coefficients) from a JSON calibration file.
        
        Parameters:
        - calibration_file_path: Path to the JSON file containing calibration data.
        
        Returns:
        - Tuple containing the intrinsic matrix (K) and distortion coefficients (D).
        """
        with open(calibration_file_path, 'r') as file:
            calibration_data = json.load(file)
            K = np.array(calibration_data['mtx'])
            D = np.array(calibration_data['dist'])
        return K, D

    def compute_average_homography(self):
        """
        Compute the average homography between images from two calibrated folders.
        This function loads calibration parameters (future use) and calculates the homography for image pairs.
        
        Returns:
        - The average homography matrix, or None if no valid homographies were computed.
        """
        # Load calibration parameters
        #intrinsic_file1, extrinsic_file1 = self.find_calibration_file(self.folder1, self.folder1)
        #intrinsic_file2, extrinsic_file2 = self.find_calibration_file(self.folder2, self.folder2)

        #K1, D1 = self.load_calibration_parameters(intrinsic_file1) # Future use: apply distortion corrections
        #K2, D2 = self.load_calibration_parameters(intrinsic_file2) # Future use: apply distortion corrections

        # Initialize homography accumulation
        H_accumulated = np.zeros((3, 3))
        num_images = 0

        # Process images in both folders
        images_folder1 = glob.glob(os.path.join(self.images_base_path, self.folder1, "*.png"))
        images_folder2 = glob.glob(os.path.join(self.images_base_path, self.folder2, "*.png"))
        
        for img_path1, img_path2 in zip(images_folder1, images_folder2):
            img1 = cv2.imread(img_path1)
            img2 = cv2.imread(img_path2)

            # Retrieve pre-calculated corners from CameraCalibration
            ret1, corners1 = self.get_corners_from_calibration(img_path1, self.folder1)
            ret2, corners2 = self.get_corners_from_calibration(img_path2, self.folder2)

            if ret1 and ret2:
                corners2 = CornerOrderCorrector.correct_corners(corners1, corners2)
                print(f"\nProcessing pair:\n  - Image: {os.path.basename(img_path1)}")
                print(f"  - Detected corners in Image1: {corners1 is not None and corners1.size > 0}")
                print(f"  - Detected corners in Image2: {corners2 is not None and corners2.size > 0}")

                # Compute homography between corresponding corners
                H, _ = cv2.findHomography(corners1, corners2)

                # Accumulate homography matrix
                H_accumulated += H
                num_images += 1
                print(f"  - Homography matrix H computed for pair: {os.path.basename(img_path1)}")
            else:
                print(f"  - Corners not detected in one image, skipping pair: {os.path.basename(img_path1)}.")

        # Calculate and save average homography if successful
        if num_images > 0:
            average_H = H_accumulated / num_images
            print(Fore.GREEN + f"Homography computed successfully from {self.folder1} to {self.folder2} using {num_images} image pairs." + Style.RESET_ALL)
            self.save_homography(average_H)
            self.visualize_random_homographies(average_H)
            return average_H
        else:
            print(Fore.RED + "No valid homographies were computed." + Style.RESET_ALL)
            return None

    def get_corners_from_calibration(self, img_path, folder):
        """
        Retrieve pre-calculated corners from a JSON file for a given image.
        
        Parameters:
        - img_path: Path to the image for which corners are to be retrieved.
        - folder: Folder name to identify the correct calibration data.
        
        Returns:
        - Tuple containing a boolean indicating success, and the corners if available.
        """
        # Use `get_latest_subfolder_with_prefix_and_suffix` to find the latest subfolder
        latest_subfolder = self.folder_manager.get_latest_subfolder_with_prefix_and_suffix(
            self.folders_names_calibration[1], folder, suffix="_intersection"
        )
        
        if latest_subfolder:
            corners_file = os.path.join(latest_subfolder, f"{folder}_corners.json")

            # Check if the corners file exists in the subfolder
            if os.path.exists(corners_file):
                with open(corners_file, 'r') as file:
                    corners_data = json.load(file)
                    
                    # Search for the corners data for the specific image using `filename`
                    filename = os.path.basename(img_path)
                    for entry in corners_data:
                        if entry.get("filename") == filename:  # Check if 'filename' exists
                            corners = np.array(entry["corners"]) if entry["corners"] else None
                            return corners is not None, corners
        else:
            print(Fore.RED + f"No suitable subfolder found for calibration data with prefix '{folder}' and suffix '_intersection'." + Style.RESET_ALL)

        return False, None

    def save_homography(self, H):
        """
        Save the average homography matrix to the HomographyFiles folder.
        
        Parameters:
        - H: The homography matrix to be saved.
        """
        homography_file_path = os.path.join(self.paths["files_path"], "average_homography.txt")
        np.savetxt(homography_file_path, H)
        print(Fore.GREEN + f"Average homography matrix saved to {homography_file_path}" + Style.RESET_ALL)

        # Generate a README file describing the homography
        readme_generator = HomographyReadme(self.homography_files_path)
        readme_generator.create_homography_readme()

    def visualize_random_homographies(self, H):
        """
        Select random images and visualize homography effect.
        
        Parameters:
        - H: The homography matrix to be applied for visualization.
        """
        self.calibration_plots = HomographyPlots(self.homography_plots_path)

        images_folder1 = glob.glob(os.path.join(self.images_base_path, self.folder1, "*.png"))
        images_folder2 = glob.glob(os.path.join(self.images_base_path, self.folder2, "*.png"))

        # Randomly select 10 image pairs
        sample_pairs = random.sample(list(zip(images_folder1, images_folder2)), min(10, len(images_folder1), len(images_folder2)))

        # Apply and visualize homography for each selected pair
        for index, (img_path1, img_path2) in enumerate(sample_pairs):
            img1 = cv2.imread(img_path1)
            img2 = cv2.imread(img_path2)
            self.calibration_plots.visualize_homography_effect(img1, img2, H, img_path1, img_path2, index, show_only=False)
