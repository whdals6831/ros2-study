import rclpy
from message_demo_interfaces.msg import RobotStatus
from rclpy.node import Node


class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher', namespace='message_demo')
        self.publisher = self.create_publisher(RobotStatus, 'status', 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info('status publisher started')

    def publish_status(self):
        message = RobotStatus()
        message.name = 'rover'
        message.battery_percent = max(0, 100 - self.count)
        message.temperature = 36.5 + (self.count % 5) * 0.2
        message.is_active = True

        self.publisher.publish(message)
        self.get_logger().info(
            'publish: '
            f'name={message.name}, '
            f'battery={message.battery_percent}, '
            f'temperature={message.temperature:.1f}, '
            f'is_active={message.is_active}'
        )
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
