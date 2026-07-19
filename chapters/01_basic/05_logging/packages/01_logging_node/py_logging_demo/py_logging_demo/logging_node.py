import rclpy
from rclpy.node import Node


class LoggingNode(Node):
    def __init__(self):
        super().__init__('logging_node')
        self.count = 0
        self.timer = self.create_timer(1.0, self.log_once_per_second)
        self.get_logger().info('logging_node started')

    def log_once_per_second(self):
        self.count += 1
        self.get_logger().debug(f'debug count={self.count}')
        self.get_logger().info(f'info count={self.count}')

        if self.count % 3 == 0:
            self.get_logger().warn('warn every 3 seconds')

        if self.count % 5 == 0:
            self.get_logger().error('error every 5 seconds')


def main(args=None):
    rclpy.init(args=args)
    node = LoggingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
