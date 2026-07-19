import rclpy
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node


class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')
        self.declare_parameter('robot_name', 'turtlebot')
        self.declare_parameter('max_speed', 1.0)
        self.validate_initial_parameters()
        self.add_on_set_parameters_callback(self.validate_parameters)
        self.timer = self.create_timer(1.0, self.log_parameters)
        self.get_logger().info('parameter_node started')

    @property
    def robot_name(self):
        return self.get_parameter('robot_name').value

    @property
    def max_speed(self):
        return self.get_parameter('max_speed').value

    def validate_initial_parameters(self):
        # CLI/YAML로 들어온 초기값은 Node 시작 직후 직접 검증한다.
        reason = self.validate_parameter_values(
            self.robot_name,
            self.max_speed,
        )
        if reason:
            raise ValueError(reason)

    def validate_parameters(self, parameters):
        # 실행 중 ros2 param set으로 바뀌는 값은 callback에서 검증한다.
        robot_name = self.robot_name
        max_speed = self.max_speed

        for parameter in parameters:
            if parameter.name == 'robot_name':
                robot_name = parameter.value
            elif parameter.name == 'max_speed':
                max_speed = parameter.value

        reason = self.validate_parameter_values(robot_name, max_speed)
        if reason:
            return SetParametersResult(
                successful=False,
                reason=reason,
            )

        return SetParametersResult(successful=True)

    def validate_parameter_values(self, robot_name, max_speed):
        if not isinstance(robot_name, str) or not robot_name:
            return 'robot_name must not be empty'

        if (
            isinstance(max_speed, bool) or
            not isinstance(max_speed, (int, float)) or
            max_speed <= 0.0
        ):
            return 'max_speed must be greater than 0'

        return ''

    def log_parameters(self):
        self.get_logger().info(
            f'robot_name={self.robot_name}, max_speed={self.max_speed}',
        )


def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
