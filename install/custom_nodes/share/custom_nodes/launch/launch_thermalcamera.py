import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Obtener las rutas necesarias
    config_file_path = os.path.expanduser('~/sensors_ws/src/custom_nodes/Homography/config.xml')
    modify_xml_file_path = os.path.expanduser('~/sensors_ws/src/custom_nodes/scripts/modify_xml.py')

    return LaunchDescription([
        DeclareLaunchArgument('focus', default_value='-1', description='Focus value for the camera'),
        TimerAction(
            period=0.2,
            actions=[
                ExecuteProcess(
                    cmd=['python3', modify_xml_file_path, config_file_path, LaunchConfiguration('focus')],
                    output='screen'
                )
            ]
        ),
        TimerAction(
            period=0.5,
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'run', 'optris_drivers2', 'optris_imager_node', config_file_path],
                    output='screen',  # Redirige la salida estándar al stdout
                    shell=False
                )
            ]
        )
    ])
