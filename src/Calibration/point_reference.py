## Code that allows you to define a point in the rgb image and see the corrisponding point in thermal wrt H

import cv2
import numpy as np

def load_homography_matrix(input_file):
    H = np.loadtxt(input_file)
    return H

# Load homography matrix
input_file = '/home/giovannaguaragnella/CameraCalibration/average_homography.txt'
H = load_homography_matrix(input_file)

# Load RGB image
image_rgb = cv2.imread("/home/giovannaguaragnella/CameraCalibration/acquisitions/March_outside/outside_2_Genis/single_images/rgb_img/img_0.jpg")

# Define window for selecting a point on the RGB image
window_name = "Select a point on the RGB image"
cv2.namedWindow(window_name)
selected_point_rgb = None

def mouse_callback(event, x, y, flags, param):
    global selected_point_rgb
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_point_rgb = (x, y)
        print("Selected point coordinates (x, y) on the RGB image:", selected_point_rgb)

cv2.setMouseCallback(window_name, mouse_callback)

while True:
    image_display = image_rgb.copy()

    # Draw the selected point (if any)
    if selected_point_rgb:
        cv2.circle(image_display, selected_point_rgb, 3, (0, 0, 255), -1)

    cv2.imshow(window_name, image_display)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()

if selected_point_rgb:
    # Convert selected point to homogeneous coordinates
    point_rgb_homogeneous = np.array([[selected_point_rgb[0]], [selected_point_rgb[1]], [1]])

    # Transform the point using the homography matrix
    point_thermal_homogeneous = np.dot(H, point_rgb_homogeneous)

    # Normalize the transformed point
    point_thermal_normalized = (point_thermal_homogeneous[0] / point_thermal_homogeneous[2],
                                point_thermal_homogeneous[1] / point_thermal_homogeneous[2])

    # Load thermal image
    image_thermal = cv2.imread("/home/giovannaguaragnella/CameraCalibration/acquisitions/March_outside/outside_2_Genis/single_images/thermal_img/img_0.jpg")

    if image_thermal is not None:
        # Warp thermal image to align with RGB image
        height_rgb, width_rgb = image_rgb.shape[:2]
        warped_thermal = cv2.warpPerspective(image_thermal, H, (width_rgb, height_rgb))

        # Get the dimensions of the thermal image
        height_thermal, width_thermal = warped_thermal.shape[:2]

        # Scale the selected point coordinates based on the resolution difference
        scale_x = width_thermal / width_rgb
        scale_y = height_thermal / height_rgb
        point_thermal_scaled = (int(selected_point_rgb[0] * scale_x), int(selected_point_rgb[1] * scale_y))

        print("Scaled point coordinates (x, y) on the thermal image:", point_thermal_scaled)

        # Draw the transformed point on the warped thermal image
        cv2.circle(warped_thermal, point_thermal_scaled, 5, (0, 0, 255), -1)

        # Display the warped thermal image with the transformed point
        cv2.imshow("Warped Thermal Image with Corresponding Point", warped_thermal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the overlay image
        cv2.imwrite('/home/giovannaguaragnella/CameraCalibration/point_on_thermal.png', warped_thermal)

    else:
        print("Unable to load the thermal image.")
else:
    print("No point selected on the RGB image.")
