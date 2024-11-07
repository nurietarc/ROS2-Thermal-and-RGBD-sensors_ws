# Sensing with RGBD and Thermal Camera

This project allows the use of Intel RealSense RGBD Camera along with the thermal camera Optris Drivers Xi400 in the detection of various crops and the computation of its temperature and the Crop Water Stress Index (CSWI) as health parameters.

## Description
The project uses pre-made packages to control both thermal and RGBD cameras as well as the YOLO object-detection model. The information extracted with these packages is processed to compute health indices.

### Structure overview
This repository consists of 3 packages and 3 other folders, which basic structure is as follows:

1. **realsense_ros:** Package that allows the use of the RGBD camera.
 
2. **optris_drivers2:** Package that allows the use of the thermal camera.
   
3. **ultralytics_ros:** Package that allows the use of the YOLO model.

4. **Calibration:** Folder that contains Python scripts for calibrating RGB and thermal cameras and computing the homography matrix.

5. **Saving:** Folder that contains Python scripts for saving images and videos of the executable processes of the project.

6. **ProvesDeCamp:** Folder to save all the videos and images taken with the codes.

### Package description
1. **realsense_ros**
   - Package documentation at the [official site](https://github.com/IntelRealSense/realsense-ros).
   - Modifications and added codes are inside `realsense2_camera/launch`.
   - `main_launch.py`: Main program of the project. Allows to execute all ROS2 nodes at once, while accepting configuration parameters.
 	   - ROS2 nodes:
    	   - RGBD camera
    	   - Ultralytics tracker (object detection node)
    	   - Thermal camera and colorconvert node
    	   - Temperature and CWSI computation
    	   - RVIZ2
 	   - Parameters:
    	   - `align_depth`
    	   - `pointcloud_enable`: if `True` enables depth images.
    	   - `debug`: if `True` opens a window in which the RGBD camera image is displayed along with the YOLO object detection results.
    	   - `focus`: to change the thermal camera focus. Possible values: [0, 100].
    	   - `yolo_model`: to select which YOLO model to use. Use `-seg` models to be able to detect masks and compute temperatures and CSWI. Exemples: `lettuces-seg.pt, leaves-seg.pt, etc`. 
    	   - `rgbd_resolution`: to indicate the RGBD camera resolution to work with. Usual values: `1280,720,30` or `640,480,30`.
    	   - `homography_file`: to select the appropriate homography matrix to be used. This parameter must match with the `rgbd_resolution` selection to ensure proper behavior. Possible values: `1280` or `640`.
    	   - `name_class`: to select the object to be detected by the yolo model.
    	   - `number_class`: to select the id number of the object to be detected by the yolo model. In order to check and get the list the name_class and its number_class of any model, execute `text.py` in `src` folder `optris_drivers2/scripts/test.py`. 
   - `thermal_launch.py`: Program to calibrate the focus of the thermal camera. Allows to change the focus value of the camera configuration when executed. The focus parameter has the same requirements as explained before.
 
2. **optris_drivers2**
   - Package documentation at the [official site](https://github.com/evocortex/optris_drivers2).
   - Modifications and added codes are inside `script`.
  	   - `temperature_cswi_calculation.py`: Program that computes the temperature and CSWI of the detected objects in the images. It only computes these values of the most recent image acquired, so it reacts faster to changes and new objects in the images.
  	   - `modify_xml.py`: Program to modify the `config.xml` file of the thermal camera. It updates the focus value of the configuration while keeping everything else in the file unchanged (comments included).
  	   - `mean_processor(_xxxx.py)`: Outdated codes to compute the temperature and CSWI of the detected objects in the images. These codes got delayed responses when time passed as all images were trying to be processed, forming large queues.
   
3. **ultralytics_ros**
   - Package documentation at the [official site](https://github.com/Alpaca-zip/ultralytics_ros).
   - `tracker_node.py`: Node to perform object detection and tracking.
   - `mask_publisher_node.py`: Node no longer used, as its functionalities are replaced within the `optris_drivers2` nodes.
   - The models to be used must be saved in the folder `~/sensors_ws/install/ultralytics_ros/share/ultralytics_ros/models`.
   - IMPORTANT: The name of the model file must be `name-seg.pt`. If the `-seg` part is omitted, the masks are not generated correctly by the `tracker_node.py`.

4. **Calibration**
   - Inside this folder there are further instructions on how to use its programs.

5. **Saving**
   - In the programs of this folder, there is a `save_dir` parameter which indicates where all the images and video will be saved. This parameter value (path to a folder) has to be specified.
   - The programs create some folders to save the different results in a well structured manner, but the primary path folder must be indicated. So, please, ALWAYS double-check the path specified.
   - `calibration_node.py`:
   - `image_saver_node_all.py`: Program that saves all the result images of the specified topics at an instant when the user presses the `s` key. All images are of the same instant, therefore, if an image could not be retrieved when the others, no image is saved.
   - `video_saver_node_all.py`: Program that starts recording all the results videos of the specified topics when the user presses the `s` key. To stop the recording, the `s` key has to be pressed again.

6. **ProvesDeCamp**
   - This folder's purpose is just for saving results.
   - It is encouraged that this folder (and others if necessary) are created prior to executing the `Saving` programs. Despite this recommendation, the programs are coded to create the necessary folders in case they are missing.


## Getting Started

### Dependencies and Requirements

* Python 3.10.12
* OpenVC (cv2)
* NumPy
* If the program is executed and errors are raised, check the `import` parts of the codes affected.

### Installing

* The codes provided in the project has been done considering the workspace name is `sensors_ws`. If the workspace name is desired to be any other, the codes have to be modified to reflect this change.
* To download and install the used packages, follow the instructions:
   * **realsense_ros:** Follow the steps described [here](https://github.com/IntelRealSense/realsense-ros?tab=readme-ov-file). Recommended installation process:
      - Install latest Intel® RealSense™ SDK 2.0 following Option 1, but install from Linux Debian Installation Guide. 
      - Further explanation and help for this package can be found in the annex C of [this thesis](https://upcommons.upc.edu/handle/2117/413406).
   * **optris_drivers2:** . Follow the following steps:
      - 1. Clone the [repository](https://github.com/evocortex/optris_drivers2) in Github with `git clone your_repository_url`. 
      - 2. Download the library IR Imager Direct SDK from [this link](https://ftp.evocortex.com/) or [this other one](https://evocortex.org/de/downloads/), selecting the system architecture (e.g., i386, arm64, amd64). You can check your system architecture by doing `dpkg -- print - architecture`. 
      - 3. Install the library IR Imager Direct SDK with  `sudo dpkg -i name.deb ` in the folder where the name.deb was installed. 
      - 4. As stated in [here](https://documentation.evocortex.com/libirimager2/html/Installation.html), execute `sudo ir_download_calibration`. 
      - 5.  Generate the camera configuration file required for running the node using
`ir_generate_configuration > config.xml > `. *Save this file in the optris_drivers src main folder and use the name “config” (main_launch expects this name). In this configuration file there are some parameters that can be changed as desired. Some of them are:
         - the focus (range from -1 to 100, -1 meaning focus is disabled, 0 to 100 the percentage of focus. For AgriPV projects with objects at 80cm of distance, a value between 70 and 80 works fine. This parameter can be changed in the main_launch parameters (focus parameter).
         -  Temperature range of camera (not recommended to change because some nodes are coded bases on the default temperature range)
         - Framerate.
      - You can find further explanations and references in the annex C of [this thesis ](https://upcommons.upc.edu/handle/2117/413406) and in the oficial documentation [here](https://documentation.evocortex.com/libirimager2/html/Installation.html)
   * **ultralytics_ros:** Following the instructions of the [official site](https://github.com/Alpaca-zip/ultralytics_ros) there should be no issues.

### Executing program

1. Make sure the workspace is sourced. If not, in a terminal execute the following command (being inside the `sensors_ws` folder):
```
source install/setup.bash
```
or change the `~/.bashrc` file adding at the end the following line:
```
source ~/sensors_ws/install/setup.bash
```
2. Launch only the thermal camera to calibrate the focus percentage suited for the application:
```
ros2 launch realsense2_camera thermal_launch.py focus:=80
```
3. Launch main program with all functionalities with the default parameter values:
```
ros2 launch realsense2_camera main_launch.py
```
or changing the parameters values:
```
ros2 launch realsense2_camera main_launch.py focus:=80 yolo_model:=yolov8m-seg.pt rgbd_resolution:="1280,720,30" homography_file:=1280 name_class:=person number_class:=0
```
4. To save the results, run in another terminal the following command:

For images:
```
python3 ~/sensors_ws/src/Saving/image_saver_node_all.py
```
For videos:
```
python3 ~/sensors_ws/src/Saving/videos_saver_node_all.py
```
5. In case the homography files used for any of the resolutions wants to be changed, the path to the file has to be changed in `~/sensors_ws/src/optris_drivers2/script/HALLEGADOELDIA.py`


## Help

There have been some problems while using some of the codes in certain computers. The majority of these problems seem to be related to the power supply of the cameras or due to the velocity in which the cable camera-computer is able to transmit the information.
   - For the problems with the power supply, no specific solutions have been found.
   - For the other problems related with the cable, depending on the quality of the cable itself it is possible to be forced to work with a resolution of 640x480x30 instead of the full resolution of 1280x720x30. If the resolution is too high, the program has problems retrieving the images on time.

The thermal camera, when it is connected to the computer for a long time, even though it is not being used eventually stops working and sending data to the computer. The only solution that has been found is to disconnect and reconnect the cable physically.


## Authors

Núria Rodríguez Calderón  
[nuria.rodriguez.calderon@upc.edu](nuria.rodriguez.calderon@upc.edu)

Yeray Navarro Soler
[yeray.navarro@upc.edu](yeray.navarro@upc.edu)

## Version History

* 0.1
	* Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
*



