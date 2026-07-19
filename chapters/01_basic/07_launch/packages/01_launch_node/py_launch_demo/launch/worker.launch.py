from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
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
            name='worker',
            namespace=namespace,
            parameters=[{'robot_name': robot_name}],
            remappings=[('status', 'worker_status')],
            condition=IfCondition(enable_worker),
            output='screen',
        ),
    ])
