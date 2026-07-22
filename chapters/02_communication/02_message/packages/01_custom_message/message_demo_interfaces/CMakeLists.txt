cmake_minimum_required(VERSION 3.8)
project(message_demo_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotStatus.msg"
  "srv/SetRobotMode.srv"
  "action/MoveRobot.action"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
