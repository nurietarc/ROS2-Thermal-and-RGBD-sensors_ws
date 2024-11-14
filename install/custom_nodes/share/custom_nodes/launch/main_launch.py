"""Launch all nodes needed to use thermal and rgb cameras"""
import os
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource, AnyLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node

import xml.etree.ElementTree as ET

def generate_launch_description():

    # args that can be set from the command line or a default will be used
    align_depth_launch_arg = DeclareLaunchArgument(
        "align_depth", default_value='false'
    )
    pointcloud_enable_launch_arg = DeclareLaunchArgument(
        "pointcloud_enable", default_value='false'
    )
    debug_launch_arg = DeclareLaunchArgument(
        "debug", default_value='false'                  # argument that opens a display of tracker_node
    )
    focus_launch_arg = DeclareLaunchArgument(
        "focus", default_value='80'                  # argument that enables focus modification
    )
    yolo_model_launch_arg = DeclareLaunchArgument(
        "yolo_model", default_value='yolov8m-seg.pt'                  # argument that enables yolo model choice
    )
    rgbd_resolution_launch_arg = DeclareLaunchArgument(
        "rgbd_resolution", default_value='1280,720,30'                  # argument that enables rgbd camera resolution choice '640,480,30'
    )
    homography_file_launch_arg = DeclareLaunchArgument(
        "homography_file", default_value='1280'                  # argument that enables changing the homography
    )
    name_class_id_launch_arg = DeclareLaunchArgument(
        "name_class", default_value='person'                  # argument that enables changing the detected yolo class
    )
    number_class_id_launch_arg = DeclareLaunchArgument(
        "number_class", default_value='0'                  # argument that enables changing the detected yolo class
    )

    # include launch file: realsense camera
    launch_include_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([                     # command that allows to include python launch file
            PathJoinSubstitution([
                    FindPackageShare('realsense2_camera'),
                    'launch',
                    'rs_launch.py'
                    ])
            ]),
            launch_arguments={                  # these arguments can be modified through the terminal
                'align_depth.enable': LaunchConfiguration('align_depth'),
                'pointcloud.enable': LaunchConfiguration('pointcloud_enable'),
                'rgb_camera.color_profile': LaunchConfiguration('rgbd_resolution')
            }.items()
    )
    delay_before_launches = TimerAction(
        period=0.5,                             # Delay in seconds (global time)
        actions=[launch_include_1]
    )

    # include launch file: ultralytics tracker    
    launch_include_2 = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([                        # command that allows to include ant type of launch file (needed for XML)
            PathJoinSubstitution([
                    FindPackageShare('ultralytics_ros'),
                    'launch',
                    'tracker.launch.xml'                    # to use our own models change to: 'tracker-models.launch.xml'
                    ])
            ]),
            launch_arguments={                  # these arguments can be modified through the terminal
                'debug': LaunchConfiguration('debug'),
                'yolo_model': LaunchConfiguration('yolo_model')
            }.items()
    )
    delay_between_launches = TimerAction(
        period=3.0,                             # Delay in seconds (global time)
        actions=[launch_include_2]
    )    

    # start node: optris imager node                                                        # use os.path.expanduser to expand '~' to the full home directory path
    focus_value = LaunchConfiguration('focus')                                              # Obtener el valor del argumento 'focus'
    config_file_path = os.path.expanduser('~/sensors_ws/src/custom_nodes/Homography/config.xml')    # Ruta al archivo XML de configuración de la cámara
    modify_xml_file_path = os.path.expanduser('~/sensors_ws/src/custom_nodes/scripts/modify_xml.py')    # Ruta al archivo de modificacion del XML
    # Modificar el archivo XML usando el valor de 'focus'
    modify_xml_process = ExecuteProcess(
        cmd = ['python3', modify_xml_file_path, config_file_path, focus_value],
        output='screen'
    )       
    delay_config = TimerAction(
        period=0.5,                             # Delay in seconds (global time)
        actions=[modify_xml_process]
    )               
    optris_imager_node = ExecuteProcess(                                                # running the node as if it were done in the terminal
        cmd=[
            'xterm', '-e', 'ros2', 'run', 'optris_drivers2', 'optris_imager_node',
            config_file_path
        ],
        shell=True
    )
    delay_node_1 = TimerAction(
        period=1.5,                            # Delay in seconds (global time)
        actions=[optris_imager_node]
    )   

    # start node: optris colorconvert node
    optris_colorconvert_node = ExecuteProcess(              # running the node as if it were done in the terminal
        cmd=[
            'xterm', '-e', 'ros2', 'run', 'optris_drivers2', 'optris_colorconvert_node'
        ],
        shell=True
    )
    delay_node_2 = TimerAction(
        period=2.5,                            # Delay in seconds (global time)
        actions=[optris_colorconvert_node]
    )  

    # # start node: mask pubisher node
    # script_path = os.path.expanduser('~/sensors_ws/src/ultralytics_ros/script/mask_publisher_node.py')
    # mask_publisher_node = ExecuteProcess(
    #     cmd=['xterm', '-e', 'python3', script_path],        # running the node as if it were done in the terminal
    # )
    # delay_py_node = TimerAction(
    #     period=17.0,                            # Delay in seconds (global time)
    #     actions=[mask_publisher_node]
    # )  

    # # start node: mean processor
    # script_path = os.path.expanduser('~/sensors_ws/src/optris_drivers2/script/mean_processor_filtered_cwsi.py') # mean_processor_filtered_nuria.py  or  mean_processor2_nuria.py
    # mean_processor2_node = ExecuteProcess(
    #     cmd=['xterm', '-e', 'python3', script_path],        # running the node as if it were done in the terminal
    # )
    # delay_py_node_2 = TimerAction(
    #     period=22.0,                            # Delay in seconds (global time)
    #     actions=[mean_processor2_node]
    # ) 

    # start node: Temperature and CWSI
    homography_file_path = LaunchConfiguration('homography_file') 
    name_class_id = LaunchConfiguration('name_class')
    number_class_id = LaunchConfiguration('number_class')
    script_path = os.path.expanduser('~/sensors_ws/src/custom_nodes/scripts/temperature_cswi_calculation.py') # mean_processor_filtered_nuria.py  or  mean_processor2_nuria.py
    mean_processor2_node = ExecuteProcess(
        cmd=['xterm', '-e', 'python3', script_path,
             '--homography_file', homography_file_path, '--name_class', name_class_id, '--number_class', number_class_id],        # running the node as if it were done in the terminal
        output='screen',
        shell=True
    )
    delay_py_node_2 = TimerAction(
        period=6.0,                            # Delay in seconds (global time)
        actions=[mean_processor2_node]
    ) 

    # Rviz2 launch to check everything works properly
    rviz_config_file = os.path.expanduser('~/sensors_ws/src/custom_nodes/launch/rviz2_config3.rviz') # path to configuration file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],     # Pass the configuration file with '-d' argument
        output='screen'
    )
    delay_rviz = TimerAction(
        period=7.0,                            # Delay in seconds (global time)
        actions=[rviz_node]
    )  

    return LaunchDescription([
        align_depth_launch_arg,
        pointcloud_enable_launch_arg,
        debug_launch_arg,
        focus_launch_arg,
        yolo_model_launch_arg,
        rgbd_resolution_launch_arg,
        homography_file_launch_arg,
        name_class_id_launch_arg,
        number_class_id_launch_arg,
        delay_before_launches,
        delay_between_launches,
        delay_config,
        delay_node_1,
        delay_node_2,
        # delay_py_node,
        delay_py_node_2,
        delay_rviz
    ])