from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='target_follower',
            executable='target_node',
            name='target_node',
            output='screen'
        ),
        Node(
            package='target_follower',
            executable='follower_node',
            name='follower_node',
            output='screen'
        ),
    ])