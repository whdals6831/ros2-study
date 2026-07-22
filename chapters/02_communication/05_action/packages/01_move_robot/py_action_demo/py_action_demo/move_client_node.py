import sys

import rclpy
from message_demo_interfaces.action import MoveRobot
from rclpy.action import ActionClient
from rclpy.node import Node


class MoveClient(Node):
    def __init__(self):
        super().__init__('move_client', namespace='action_demo')
        self.action_client = ActionClient(self, MoveRobot, 'move_robot')
        self.goal_handle = None
        self.cancel_after_feedback = False

    def send_goal(self, target_distance, cancel_after_feedback=False):
        self.cancel_after_feedback = cancel_after_feedback
        self.action_client.wait_for_server()

        goal = MoveRobot.Goal()
        goal.target_distance = target_distance

        return self.action_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback,
        )

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f'feedback: current={feedback.current_distance:.1f}m, '
            f'remaining={feedback.remaining_distance:.1f}m'
        )

        if self.cancel_after_feedback and self.goal_handle is not None:
            self.cancel_after_feedback = False
            self.goal_handle.cancel_goal_async()


def main(args=None):
    rclpy.init(args=args)
    node = MoveClient()

    target_distance = float(sys.argv[1]) if len(sys.argv) > 1 else 5.0
    cancel = len(sys.argv) > 2 and sys.argv[2] == 'cancel'

    send_goal_future = node.send_goal(target_distance, cancel)
    rclpy.spin_until_future_complete(node, send_goal_future)

    node.goal_handle = send_goal_future.result()
    if not node.goal_handle.accepted:
        node.get_logger().info('goal rejected')
        node.destroy_node()
        rclpy.shutdown()
        return

    result_future = node.goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)

    result = result_future.result().result
    node.get_logger().info(
        f'success={result.success}, '
        f'final_distance={result.final_distance:.1f}m, '
        f'message="{result.message}"'
    )
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
