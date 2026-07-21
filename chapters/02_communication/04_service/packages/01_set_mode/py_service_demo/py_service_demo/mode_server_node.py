import rclpy
from message_demo_interfaces.srv import SetRobotMode
from rclpy.node import Node


class ModeServer(Node):
    def __init__(self):
        super().__init__('mode_server', namespace='service_demo')
        self.mode = 'idle'
        self.allowed_modes = {'idle', 'manual', 'auto'}
        self.service = self.create_service(
            SetRobotMode,
            'set_mode',
            self.set_mode_callback,
        )
        self.get_logger().info('mode server started')

    def set_mode_callback(self, request, response):
        if request.mode not in self.allowed_modes:
            response.success = False
            response.message = (
                f'unsupported mode: {request.mode} '
                f'(allowed: {", ".join(sorted(self.allowed_modes))})'
            )
            return response

        self.mode = request.mode
        response.success = True
        response.message = f'mode changed to {self.mode}'
        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ModeServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
