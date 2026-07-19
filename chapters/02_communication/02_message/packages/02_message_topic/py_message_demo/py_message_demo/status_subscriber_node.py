import rclpy
from message_demo_interfaces.msg import RobotStatus
from rclpy.node import Node


class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber', namespace='message_demo')
        self.subscription = self.create_subscription(
            RobotStatus,
            'status',
            self.listener_callback,
            10,
        )
        self.get_logger().info('status subscriber started')

    def listener_callback(self, message):
        self.get_logger().info(
            'receive: '
            f'name={message.name}, '
            f'battery={message.battery_percent}, '
            f'temperature={message.temperature:.1f}, '
            f'is_active={message.is_active}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
