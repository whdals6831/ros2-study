from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_share = Path(get_package_share_directory('py_launch_demo'))
    parameter_file = package_share / 'config' / 'launch_parameters.yaml'
    worker_launch = package_share / 'launch' / 'worker.launch.py'

    robot_name = LaunchConfiguration('robot_name')
    namespace = LaunchConfiguration('namespace')
    enable_worker = LaunchConfiguration('enable_worker')

    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='launch_rover'),
        DeclareLaunchArgument('namespace', default_value='demo'),
        DeclareLaunchArgument('enable_worker', default_value='true'),
        Node(
            package='py_launch_demo',
            executable='launch_demo_node',
            name='main',
            namespace=namespace,
            parameters=[str(parameter_file), {'robot_name': robot_name}],
            remappings=[('status', 'main_status')],
            output='screen',
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(worker_launch)),
            launch_arguments={
                'robot_name': robot_name,
                'namespace': namespace,
                'enable_worker': enable_worker,
            }.items(),
        ),
    ])
