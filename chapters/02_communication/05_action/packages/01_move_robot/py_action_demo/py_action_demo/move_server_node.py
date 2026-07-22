import time

import rclpy
from message_demo_interfaces.action import MoveRobot
from rclpy.action import ActionServer, CancelResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node


class MoveServer(Node):
    def __init__(self):
        super().__init__('move_server', namespace='action_demo')
        self.action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',
            self.execute_callback,
            cancel_callback=self.cancel_callback,
            callback_group=ReentrantCallbackGroup(),
        )
        self.get_logger().info('move action server started')

    def cancel_callback(self, goal_handle):
        self.get_logger().info('cancel request accepted')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        target = max(0.0, goal_handle.request.target_distance)
        feedback = MoveRobot.Feedback()
        result = MoveRobot.Result()
        current = 0.0

        while current < target:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result.success = False
                result.final_distance = current
                result.message = f'move canceled at {current:.1f}m'
                return result

            current = min(current + 1.0, target)
            feedback.current_distance = current
            feedback.remaining_distance = target - current
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(
                f'moving: {current:.1f}m / {target:.1f}m'
            )
            time.sleep(1.0)

        goal_handle.succeed()
        result.success = True
        result.final_distance = current
        result.message = f'move completed: {current:.1f}m'
        return result


def main(args=None):
    rclpy.init(args=args)
    node = MoveServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
