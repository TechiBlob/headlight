import rclpy
from rclpy.node import Node

class DemoNode(Node):

    def __init__(self) -> None:
        super().__init__('demo')
        
        self.get_logger().info('Test')


def main() -> None:
    rclpy.init()
    node = DemoNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()