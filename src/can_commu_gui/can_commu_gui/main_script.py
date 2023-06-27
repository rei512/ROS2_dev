import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QStyle, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from .mainWindow import Ui_mainWindow

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_messages.msg import CanMsg
class MainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.float_topic_name = '/can_gui'
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		# ROS2 init
		rclpy.init(args=None)
		self.node = Node('Qt_view_node')
		self.CanMsg = CanMsg()
		self.pub = self.node.create_publisher(CanMsg, '/can_rx', 10)

	def clickedInterrapt(self):
		self.CanMsg.id += 1 # 1[m/s]で直進
		self.pub.publish(self.CanMsg)

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
