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

# Función para modificar el valor de focus en el archivo XML
def modify_focus_in_xml(xml_path, new_focus_value):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Buscar el elemento <focus> y modificar su valor
    for focus in root.iter('focus'):
        focus.text = str(new_focus_value)

    # Guardar los cambios en el mismo archivo
    tree.write(xml_path)

def generate_launch_description():

    # args that can be set from the command line or a default will be used
    focus_launch_arg = DeclareLaunchArgument(
        "focus", default_value='80'                  # argument that enables focus modification
    )

    # start node: optris imager node                                                        # use os.path.expanduser to expand '~' to the full home directory path
    focus_value = LaunchConfiguration('focus')                                              # Obtener el valor del argumento 'focus'
    config_file_path = os.path.expanduser('~/sensors_ws/src/optris_drivers2/config.xml')    # Ruta al archivo XML de configuración de la cámara
    modify_xml_file_path = os.path.expanduser('~/sensors_ws/src/optris_drivers2/script/modify_xml.py')    # Ruta al archivo de modificacion del XML
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
        period=2.5,                            # Delay in seconds (global time)
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
        period=5.0,                            # Delay in seconds (global time)
        actions=[optris_colorconvert_node]
    )  

    # Rviz2 launch to check everything works properly
    rviz_config_file = os.path.expanduser('~/sensors_ws/src/realsense-ros/realsense2_camera/rviz2_config_thermal.rviz') # path to configuration file
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
        focus_launch_arg,
        delay_config,
        delay_node_1,
        delay_node_2,
        delay_rviz
    ])