# ~/nav_robot_wsp/src/nav_robot_simulation/launch/nav_robot_simulation.launch.py
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo server
        ExecuteProcess(
            cmd=['gzserver', '--verbose'],
            output='screen'
        ),

        # Start Gazebo client
        ExecuteProcess(
            cmd=['gzclient'],
            output='screen'
        ),
    ])

