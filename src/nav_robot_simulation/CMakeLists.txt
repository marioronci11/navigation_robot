cmake_minimum_required(VERSION 3.8)
project(nav_robot_simulation)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Install the launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install the URDF and world files
install(
  DIRECTORY urdf worlds
  DESTINATION share/${PROJECT_NAME}
)

# Ament package
ament_package()
