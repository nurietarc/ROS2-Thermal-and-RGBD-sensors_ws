# Camera Calibration

This folder contains Python scripts for calibrating RGB and thermal cameras, as well as computing the average homography matrix between them. Below are brief descriptions of each script:

## 1. extrinsic_rgb.py

This script calibrates an RGB camera by finding chessboard corners in calibration images, computing intrinsic and extrinsic parameters, and saving the calibration data to JSON and text files.

## 2. extrinsic_thermal.py

This script calibrates a thermal camera using similar steps as the RGB camera calibration script. It finds chessboard corners in thermal images, computes intrinsic and extrinsic parameters, and saves the calibration data to JSON and text files.

## 3. avg_homography_mtx.py

This script computes the average homography matrix between an RGB camera and a thermal camera. It utilizes intrinsic calibration parameters and images of checkerboards to compute the average homography matrix, allowing for the correct overlay of images captured by both cameras. The average homography matrix is saved to a text file.

## Usage

1. **Prepare Calibration Images:**
   - Capture calibration images for both the RGB and thermal cameras. Ensure that the calibration pattern (e.g., chessboard) is visible in the images.

2. **Set Paths:**
   - Update the file paths in each script to point to the correct locations of calibration images and files.

3. **Run Scripts:**
   - Execute the scripts in the following order:
     - `extrinsic_rgb.py`
     - `extrinsic_thermal.py`
     - `avg_homography_mtx.py`

4. **Retrieve Results:**
   - After running the scripts, calibration data and the average homography matrix will be saved to JSON and text files within the same folder.

## Requirements

- Python 3.8.10
- OpenCV (cv2)
- NumPy


