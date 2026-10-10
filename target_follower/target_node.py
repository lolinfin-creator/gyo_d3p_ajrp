import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random

class TargetNode(Node):
    def __init__(self):
        super().__init__('target_node')
        self.publisher_ = self.create_publisher(Point, 'target_position', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.x = 0.0
        self.y = 0.0

    def timer_callback(self):
        self.x += random.uniform(-1.0, 1.0)
        self.y += random.uniform(-1.0, 1.0)

        msg = Point()
        msg.x = self.x
        msg.y = self.y
        msg.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Target position: x={msg.x:.2f}, y={msg.y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = TargetNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()