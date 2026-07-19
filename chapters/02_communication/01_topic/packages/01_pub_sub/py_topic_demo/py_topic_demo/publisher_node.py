import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TopicPublisher(Node):
    def __init__(self):
        super().__init__('publisher', namespace='topic_demo')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.publish_message)
        self.get_logger().info('publisher started')

    def publish_message(self):
        message = String()
        message.data = f'Hello ROS2 Topic {self.count}'
        self.publisher.publish(message)
        self.get_logger().info(f'publish: {message.data}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = TopicPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
