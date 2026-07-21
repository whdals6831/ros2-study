import sys

import rclpy
from message_demo_interfaces.srv import SetRobotMode
from rclpy.node import Node


class ModeClient(Node):
    def __init__(self):
        super().__init__('mode_client', namespace='service_demo')
        self.client = self.create_client(SetRobotMode, 'set_mode')

    def send_request(self, mode):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting for service...')

        request = SetRobotMode.Request()
        request.mode = mode
        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = ModeClient()
    mode = sys.argv[1] if len(sys.argv) > 1 else 'auto'

    future = node.send_request(mode)
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node.get_logger().info(
        f'success={response.success}, message="{response.message}"'
    )
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
