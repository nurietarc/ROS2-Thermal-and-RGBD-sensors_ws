import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
import math

"""
Nuria Rodríguez Calderón
    This class handles the visualization of calibration data for camera calibration processes.
    It provides methods to save step-by-step transformation plots for selected images, as well as 
    mosaics for all original, grayscale (transformed), and corner-detected images used in calibration.
    
    Functions:
    - save_image_transformations: Saves step-by-step transformation images for a subset of selected images.
    - save_original_mosaic: Saves a mosaic of all original images used in calibration.
    - save_gray_mosaic: Saves a mosaic of all grayscale (transformed) images used in calibration.
    - save_corners_mosaic: Saves a mosaic of original images with detected corners drawn on them.
"""

class CalibrationPlots:
    def __init__(self, calibration_data, chessboard_size, output_path):
        """
        Initializes the CalibrationPlots class with calibration data, chessboard size, and output path.

        Parameters:
        - calibration_data (list): List of dictionaries containing original images, transformed images, and detected corners.
        - chessboard_size (tuple): Size of the chessboard used for calibration (number of internal corners per chessboard row and column).
        - output_path (str): Directory where the output images will be saved.
        """
        self.calibration_data = calibration_data
        self.chessboard_size = chessboard_size
        self.output_path = output_path

    def save_image_transformations(self, selected_data):
        """
        Save step-by-step transformation plots for a selected subset of images.
        Each transformation is displayed in a subplot: original, grayscale, equalized, and inverted.

        Parameters:
        - selected_data (list): List of dictionaries containing images and detected corners for a subset of images.
        """
        for index, data in enumerate(selected_data):
            img = data['original']  # Original image

            # Create figure with subplots for each transformation step
            fig, axs = plt.subplots(1, 4, figsize=(20, 10))

            # Original image
            axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axs[0].set_title("Original Image")
            axs[0].axis('off')

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            axs[1].imshow(gray, cmap='gray')
            axs[1].set_title("Grayscale Image")
            axs[1].axis('off')

            # Enhance contrast using histogram equalization
            equalized = cv2.equalizeHist(gray)
            axs[2].imshow(equalized, cmap='gray')
            axs[2].set_title("Equalized Image")
            axs[2].axis('off')

            # Inverted image
            inverted = cv2.bitwise_not(equalized)
            axs[3].imshow(inverted, cmap='gray')
            axs[3].set_title("Inverted Image")
            axs[3].axis('off')

            # Save the transformation plot for the current image
            output_file = os.path.join(self.output_path, f"calibration_transformations_{index}.png")
            plt.savefig(output_file)
            plt.close()

    def save_original_mosaic(self):
        """
        Save a mosaic of all original images used in calibration, arranged in 5 columns and as many rows as needed.
        """
        
        num_images = len(self.calibration_data)
        num_columns = 5
        num_rows = math.ceil(num_images / num_columns)

        fig, axs = plt.subplots(num_rows, num_columns, figsize=(20, 4 * num_rows))

        # Flatten axs to iterate easily if there are multiple rows
        axs = axs.flatten()

        for i, data in enumerate(self.calibration_data):
            axs[i].imshow(cv2.cvtColor(data['original'], cv2.COLOR_BGR2RGB))
            axs[i].axis('off')

        # Hide any remaining subplots if there are fewer images than subplots
        for j in range(i + 1, len(axs)):
            axs[j].axis('off')

        # Save the mosaic of original images
        output_file = os.path.join(self.output_path, "calibration_original_mosaic.png")
        plt.savefig(output_file)
        plt.close()

    def save_gray_mosaic(self):
        """
        Save a mosaic of all grayscale (transformed) images used in calibration, arranged in 5 columns and as many rows as needed.
        """
        num_images = len(self.calibration_data)
        num_columns = 5
        num_rows = math.ceil(num_images / num_columns)

        fig, axs = plt.subplots(num_rows, num_columns, figsize=(20, 4 * num_rows))
        axs = axs.flatten()

        for i, data in enumerate(self.calibration_data):
            axs[i].imshow(data['transformed'], cmap='gray')
            axs[i].axis('off')

        # Hide any remaining subplots if there are fewer images than subplots
        for j in range(i + 1, len(axs)):
            axs[j].axis('off')

        # Save the mosaic of grayscale images
        output_file = os.path.join(self.output_path, "calibration_gray_mosaic.png")
        plt.savefig(output_file)
        plt.close()

    def save_corners_mosaic(self):
        """
        Save a mosaic of original images with detected corners drawn, arranged in 5 columns and as many rows as needed.
        """
        num_images = len(self.calibration_data)
        num_columns = 5
        num_rows = math.ceil(num_images / num_columns)

        fig, axs = plt.subplots(num_rows, num_columns, figsize=(20, 4 * num_rows))
        axs = axs.flatten()

        for i, data in enumerate(self.calibration_data):
            if data['corners'] is not None:
                corners_img = cv2.drawChessboardCorners(data['original'].copy(), self.chessboard_size, data['corners'], True)
                axs[i].imshow(cv2.cvtColor(corners_img, cv2.COLOR_BGR2RGB))
            else:
                axs[i].imshow(cv2.cvtColor(data['original'], cv2.COLOR_BGR2RGB))  # Image without detected corners
            axs[i].axis('off')

        # Hide any remaining subplots if there are fewer images than subplots
        for j in range(i + 1, len(axs)):
            axs[j].axis('off')

        # Save the mosaic of images with detected corners
        output_file = os.path.join(self.output_path, "calibration_corners_mosaic.png")
        plt.savefig(output_file)
        plt.close()

"""
Nuria Rodríguez Calderón
    This class handles the visualization of the homography effect applied to images.
    It provides a method to apply a homography transformation to an image and visualize the result.

    Functions:
    - visualize_homography_effect: Applies the homography transformation to an image and visualizes the original, transformed, and target images.
"""

class HomographyPlots:
    def __init__(self, output_path=None):
        """
        Initializes the HomographyPlots class with an optional output path.
        
        Parameters:
        - output_path (str): Directory where the output images will be saved.
        """
        self.output_path = output_path

    def visualize_homography_effect(self, img1, img2, H, img_path1, img_path2, index=None, show_only=False):
        """
        Visualize the effect of applying a homography transformation to img1 to align it with img2.
        
        Parameters:
        - img1, img2: Images for which homography is visualized.
        - H: Homography matrix used to warp img1.
        - img_path1, img_path2: Paths to the images being visualized.
        - index (int): Optional index for saving the output.
        - show_only (bool): Whether to display the plot or save it.
        """
        height2, width2, _ = img2.shape
        img1_transformed = cv2.warpPerspective(img1, H, (width2, height2))

        plt.figure(figsize=(15, 5))
        plt.suptitle(f"Homography Visualization for:\n{os.path.basename(img_path1)}", fontsize=10)

        plt.subplot(1, 3, 1)
        plt.title('Image 1')
        plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

        plt.subplot(1, 3, 2)
        plt.title('Transformed Image 1')
        plt.imshow(cv2.cvtColor(img1_transformed, cv2.COLOR_BGR2RGB))

        plt.subplot(1, 3, 3)
        plt.title('Image 2')
        plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

        if show_only == True:
            plt.show()
        else:
            output_file = os.path.join(self.output_path, f"homography_effect_{index}.jpg")
            plt.savefig(output_file)
            plt.close()
