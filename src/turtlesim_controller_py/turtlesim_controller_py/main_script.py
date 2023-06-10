import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QStyle, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from .mainWindow import Ui_mainWindow

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.float_topic_name = '/turtle1/cmd_vel'
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		# ROS2 init
		rclpy.init(args=None)
		self.node = Node('Qt_view_node')
		self.Twist = Twist()
		self.pub = self.node.create_publisher(Twist, self.float_topic_name, 10)

	def clickedForward(self):
		self.Twist.linear.x = 1.0 # 1[m/s]で直進
		self.pub.publish(self.Twist)
		self.Twist.linear.x = 0.0

		self.node.get_logger().info('go Forward')

	def clickedBack(self):
		self.Twist.linear.x = -1.0
		self.pub.publish(self.Twist)
		self.Twist.linear.x = 0.0

		self.node.get_logger().info('go Back')

	def clickedLeft(self):
		self.Twist.linear.y = 1.0
		self.pub.publish(self.Twist)
		self.Twist.linear.y = 0.0

		self.node.get_logger().info('go Left')

	def clickedRight(self):
		self.Twist.linear.y = -1.0
		self.pub.publish(self.Twist)
		self.Twist.linear.y = 0.0

		self.node.get_logger().info('go Right')

	def clickedLTurn(self):
		self.Twist.angular.z = 0.261792
		self.pub.publish(self.Twist)
		self.Twist.angular.z = 0.0

		self.node.get_logger().info('Turn Left')

	def clickedRTurn(self):
		self.Twist.angular.z = -0.261792
		self.pub.publish(self.Twist)
		self.Twist.angular.z = 0.0

		self.node.get_logger().info('Turn Right')

	def clickedStop(self):
		self.node.get_logger().info('Stop')
	
def main():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
	node.destroy_node()
	rclpy.shutdown()

if __name__=="__main__":
	main()

