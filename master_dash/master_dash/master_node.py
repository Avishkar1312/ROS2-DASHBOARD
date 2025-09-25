import rclpy
from rclpy.node import Node

class DataCollector(Node):
    def __init__(self):
        super().__init__("data_collector")
        self.timer=self.create_timer(1.0,self.node_metrics)

    def topic_metrics(self):
        topic_names=self.get_topic_names_and_types()
        self.get_logger().info(f"Active topics:{topic_names}")

    def node_metrics(self):
        node_names=self.get_node_names()
        self.get_logger().info(f"Active nodes:{node_names}")


def main(args=None):
    rclpy.init(args=args)
    data_collector=DataCollector()
    rclpy.spin(data_collector)
    data_collector.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
