#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# PyQt
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from .window import Ui_MainWindow # 変換したファイルをインポート
# ROS
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(mainWindow, self).__init__(parent)
		self.setupUi(self)

		self.node = Node('Qt_test_node')
		self.publisher_ = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.cmd_vel_Twist = Twist()

	def clickedFoward(self):
		self.cmd_vel_Twist.linear.x = 1.0 # 1[m/s]で直進
		self.publisher_.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0.0

	def clickedBack(self):
		self.cmd_vel_Twist.linear.x = -1.0
		self.publisher_.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0.0



def main(args=None):
	rclpy.init(args=args)
	app = QApplication(sys.argv)
	window = mainWindow()
	window.show()
	sys.exit(app.exec_())
	#window.destroy_node()
	#rclpy.shutdown()

if __name__ == '__main__':
	main()

