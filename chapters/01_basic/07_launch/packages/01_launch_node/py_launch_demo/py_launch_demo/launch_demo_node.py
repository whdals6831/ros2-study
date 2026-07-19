import rclpy
from rclpy.node import Node


class LaunchDemoNode(Node):
    def __init__(self):
        super().__init__('launch_demo_node')
        self.declare_parameter('robot_name', 'turtlebot')
        self.declare_parameter('update_period', 1.0)
        self.timer = self.create_timer(
            self.get_parameter('update_period').value,
            self.log_launch_context,
        )
        self.get_logger().info('launch_demo_node started')

    def log_launch_context(self):
        self.get_logger().info(
            'name=%s, namespace=%s, robot_name=%s, status_topic=%s' % (
                self.get_name(),
                self.get_namespace(),
                self.get_parameter('robot_name').value,
                self.resolve_topic_name('status'),
            ),
        )


def main(args=None):
    rclpy.init(args=args)
    node = LaunchDemoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
