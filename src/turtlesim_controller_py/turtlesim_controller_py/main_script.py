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
		self.create_menubars()

		self.value = 0;
		
		exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton),
							 '&Exit', self)       
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)
		self.statusBar()
		# ROS2 init
		rclpy.init(args=None)
		self.node = Node('Qt_view_node')
		self.Twist = Twist()
		self.pub = self.node.create_publisher(Twist, self.float_topic_name, 10)


	def create_menubars(self):
		menuBar = self.menuBar()
		# Creating menus using a QMenu object
		fileMenu = QMenu("&File", self)
		fileMenu.addAction(self.exit_action())

		menuBar.addMenu(fileMenu)
		# Creating menus using a title
		editMenu = menuBar.addMenu("&Edit")
		editMenu.addMenu("Undo")
		helpMenu = menuBar.addMenu("&Help")
		helpMenu.addMenu("Get Started")


	def exit_action(self):
	   # Exit Action, connect
		exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton),
							 '&Exit', self)       
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)
		self.statusBar()
		return exitAction


	def clickedInterrupt(self):
		self.Twist.linear.x = 1.0 # 1[m/s]で直進
		self.pub.publish(self.Twist)
		self.Twist.linear.x = 0.0

		self.node.get_logger().info('go Forward')


	def vaueChangedInterrupt(self, value):
		self.node.get_logger().info(value)
	
def main():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
	node.destroy_node()
	rclpy.shutdown()

if __name__=="__main__":
	main()

