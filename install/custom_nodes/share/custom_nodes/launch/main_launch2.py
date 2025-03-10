# main_launch_realsense.py
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([
        # Declarar argumentos configurables desde la terminal
        DeclareLaunchArgument('enable_color', default_value='true', description='Enable RGBD camera'),
        DeclareLaunchArgument('enable_depth', default_value='true', description='Enable Depth camera'),
        DeclareLaunchArgument('enable_infra1', default_value='false', description='Enable infra1 channel'),
        DeclareLaunchArgument('enable_infra2', default_value='false', description='Enable infra2 channel'),
        DeclareLaunchArgument('align_depth', default_value='true', description='Enable depth alignment'),
        DeclareLaunchArgument('pointcloud', default_value='true', description='Enable pointcloud'),
        DeclareLaunchArgument('rgb_resolution', default_value='1280x720x30', description='Resolution for RGBD camera'),
        DeclareLaunchArgument('depth_resolution', default_value='640x480x30', description='Resolution for RGBD camera'),
        
        # Lanzar el archivo rs_launch.py del paquete realsense2_camera
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    FindPackageShare('realsense2_camera').find('realsense2_camera'),
                    'launch', 'rs_launch.py'
                )
            ),
            launch_arguments={
                'enable_color': LaunchConfiguration('enable_color'),
                'enable_depth': LaunchConfiguration('enable_depth'),
                'enable_infra1': LaunchConfiguration('enable_infra1'),
                'enable_infra2': LaunchConfiguration('enable_infra2'),
                'align_depth': LaunchConfiguration('align_depth'),
                'pointcloud.enable': LaunchConfiguration('pointcloud'),
                'rgb_camera.color_profile': LaunchConfiguration('rgb_resolution'),
                'depth_module.depth_profile': LaunchConfiguration('depth_resolution'),
                'depth_module.infra_profile': LaunchConfiguration('depth_resolution')
            }.items()
        ),
    ])


