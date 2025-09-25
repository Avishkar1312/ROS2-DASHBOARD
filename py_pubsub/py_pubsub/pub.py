import rclpy          #importing
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')  #Used to inherit the methods from the Node class( whatever is written in the brackets is the name of the node)
        self.publisher= self.create_publisher(String, 'topic', 10) # 'topic' is the name of the topic to which the msg is getting published
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) # topic name to be set over here
        self.i = 0

    def timer_callback(self):
        msg = String()  #making an object of the string class
        msg.data = 'Hello World: %d' % self.i #sending a string message along with a counter
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
