import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, Twist
import math

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        self.subscription = self.create_subscription(
            Point, 'target_position', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.current_x = 0.0
        self.current_y = 0.0

    def listener_callback(self, msg: Point):
        dx = msg.x - self.current_x
        dy = msg.y - self.current_y
        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        cmd = Twist()
        cmd.linear.x = min(distance, 1.0)
        cmd.angular.z = angle
        self.publisher_.publish(cmd)

        self.get_logger().info(
            f'Target: ({msg.x:.2f}, {msg.y:.2f}) | distance={distance:.2f}, angle={math.degrees(angle):.1f}°')


def main(args=None):
    rclpy.init(args=args)
    node = FollowerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()