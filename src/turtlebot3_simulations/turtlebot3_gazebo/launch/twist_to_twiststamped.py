# Save as twist_to_twiststamped.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
from builtin_interfaces.msg import Time

class TwistConverter(Node):
    def __init__(self):
        super().__init__('twist_to_twiststamped')
        self.publisher = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel_unstamped',
            self.callback,
            10)
    
    def callback(self, msg):
        stamped_msg = TwistStamped()
        stamped_msg.header.stamp = self.get_clock().now().to_msg()
        stamped_msg.twist = msg
        self.publisher.publish(stamped_msg)

def main():
    rclpy.init()
    node = TwistConverter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()