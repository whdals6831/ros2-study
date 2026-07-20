import rclpy
from message_demo_interfaces.msg import RobotStatus
from rclpy.node import Node


class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher', namespace='topic_advanced')
        self.declare_parameter('robot_name', 'rover')
        self.declare_parameter('publish_hz', 1.0)

        self.robot_name = self.get_parameter('robot_name').value
        publish_hz = self.get_parameter('publish_hz').value
        if publish_hz <= 0.0:
            publish_hz = 1.0

        self.publisher = self.create_publisher(RobotStatus, 'status', 10)
        self.count = 0
        self.timer = self.create_timer(1.0 / publish_hz, self.publish_status)
        self.get_logger().info(f'status publisher started: {publish_hz:.1f}Hz')

    def publish_status(self):
        message = RobotStatus()
        message.name = self.robot_name
        message.battery_percent = max(0, 100 - self.count)
        message.temperature = 36.5 + (self.count % 5) * 0.2
        message.is_active = message.battery_percent > 0

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
