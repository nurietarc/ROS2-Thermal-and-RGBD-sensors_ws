# Calibration and Homography Library

### Author: Nuria Rodríguez Calderón

## Overview

This library provides tools for camera calibration and homography computation for multi-camera setups (e.g., RGB and thermal cameras). It offers functionality for calibrating individual cameras, performing calibration using intersections across multiple camera views, saving calibration data, and generating visualization plots. Additionally, it computes homography matrices for aligning different perspectives of two given cameras.

## Key Components

The library consists of the following key components:

### 1. `CameraCalibration` Class

The `CameraCalibration` class is responsible for managing and performing camera calibration tasks. It can handle multiple camera types (e.g., RGB and thermal) and includes functions for:

- **Single Camera Calibration**: Calibrate individual cameras by detecting chessboard patterns in images.
- **Intersection Calibration**: Use only images with successfully detected chessboard corners across multiple camera types for calibration.
- **Saving Calibration Data and Plots**: Save intrinsic and extrinsic camera parameters, and generate visualization plots for calibration.

#### Please, ensure that the chessboard pattern is and odd x even or even x odd chessboard. 

### 2. `Homography` Class

The `Homography` class is used for computing homography matrices that transform images from one camera view to align with another. Computes an average homography matrix based on multiple image pairs to map points between two different camera views. Allows visualization of the transformation effect on images.

## Support classes

### 3. FolderManager Class

The `FolderManager` class is responsible for managing folder creation and deletion during the calibration process. This class helps organize the output directories for storing calibration and homography files.

Key Features:

- **Create and Delete Folders**: Handles the setup of folders for different steps of the calibration and homography process. It allows you to create folders with any name, but it is preferable to use the default names provided by the library.
- **Create Subfolders**: You can create subfolders for the calibration process using `create_subfolders()` and for the homography process using `create_combined_subfolder()`.
- **Retrieve Latest Folder**: Allows you to find the latest subfolder to ensure that the most recent calibration data is used. However, as shown in the test example, a good practice is to delete all previous calibration data using the `delete_all_folders()` or `delete_subfolders()` methods to avoid inconsistencies.

### 4. `CalibrationPlots` Class

The `CalibrationPlots` class is used to visualize calibration data and homography transformations. 

- **Transformation Plots**: Creates subplots showing different stages of image transformation.
- **Mosaics**: Generates mosaics of original images, grayscale images, and images with detected corners for a comprehensive visual check of calibration quality.
- **Homography Plots**: Visualizes the effect of applying homography transformations to align images from two different camera views.

### 5. `CalibrationReadme` Class

The `CalibrationReadme` class generates README files that document the calibration process, including intrinsic and extrinsic parameters and the generated plots. README files are not generated for homography because it is considered self-explanatory: the homography files contain the homography matrix, while the plots provide examples of how the homography works.

## Usage Example

Below is a brief overview of how to use the library for camera calibration and homography computation:

```python
import os
from CameraCalibration import CameraCalibration
from FolderManager import FolderManager
from Homography import Homography

# Initial configuration
base_path = "C:\\Users\\nrodriguez\\Desktop\\Calibracion\\CALIBRATION21del10"  # Update as needed
images_base_path = os.path.join(base_path, "Images")  # Base path for images
folders_names = ["CalibrationPlots", "CalibrationFiles"]

# Create FolderManager instance and delete existing calibration folders
folder_manager = FolderManager(base_path, images_base_path, folders_names)
folder_manager.delete_all_folders()

# Initialize CameraCalibration and perform calibration
camera_type = "Normal"
calibration = CameraCalibration(base_path, images_base_path, folders_names, chessboard_size=(6, 9))
calibration.calibrate_with_intersection()

# Set up for homography computation
folders_names2 = ["HomographyPlots", "HomographyFiles"]
folder_manager2 = FolderManager(base_path, images_base_path, folders_names2)
folder_manager2.delete_all_folders()

# Compute average homography between Normal and Thermal camera images
folder1 = "Normal"
folder2 = "Thermal"
homography_calibration = Homography(base_path, images_base_path, folder1, folder2, folders_names2)
average_homography = homography_calibration.compute_average_homography()

from PersonalizedPlots import HomographyPlots
import cv2
import os

# Load images for verification
img1_path = os.path.join(images_base_path, folder1, "image1.png")  # Update with an appropriate image name
img2_path = os.path.join(images_base_path, folder2, "image2.png")  # Update with an appropriate image name

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Visualize the homography effect
homography_plotter = HomographyPlots(output_path=os.path.join(base_path, "HomographyVerification"))
homography_plotter.visualize_homography_effect(img1, img2, average_homography, img1_path, img2_path, index=1, show_only=True)
```

## Installation and dependences

1. Clone the repository to your local machine.
2. Ensure that Python 3.6+ is installed.
3. Install the necessary Python packages:
   ```sh
   pip install numpy opencv-python colorama matplotlib
   ```

- **OpenCV**: Used for image processing, detecting chessboard corners, and calculating calibration parameters.
- **NumPy**: Handles numerical operations and data representation.
- **Matplotlib**: Creates visual plots of calibration data.
- **Colorama**: Adds color to the console output for better readability.

## Notes

- Ensure that the chessboard  is and odd x even or even x odd chessboard. 
- Carefully review the README files generated by the `CalibrationReadme` and `HomographyReadme` classes for more insights into the calibration data and usage.