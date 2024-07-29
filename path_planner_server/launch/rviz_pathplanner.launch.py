import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    rviz_config_file_path = os.path.join(
        get_package_share_directory('path_planner_server'), 'rviz_config', 'pathplanning.rviz')

    return LaunchDescription([

        Node(
            package='rviz2',
            executable='rviz2',
            output='log',
            name='rviz2_node',
            parameters=[{'use_sim_time': True}],
            arguments=['-d', rviz_config_file_path, '--ros-args', '--log-level', "rviz2:=fatal"])
    ])
