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
		self.float_topic_name = '/micro_ros_arduino_node_publisher'
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		# ROS2 init
		rclpy.init(args=None)
		self.node = Node('Qt_view_node')
		self.Twist = Twist()
		self.pub = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

	def clickedInterrapt(self):
		self.Twist.linear.x = 1.0 # 1[m/s]で直進
		self.pub.publish(self.Twist)
		self.Twist.linear.x = 0.0

		self.node.get_logger().info('Interraptted')

def main():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
	node.destroy_node()
	rclpy.shutdown()

if __name__=="__main__":
	main()
