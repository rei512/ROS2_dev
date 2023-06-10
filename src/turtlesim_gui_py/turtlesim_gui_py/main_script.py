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

	def clickedFoward(self):
		rosNode.moveFoward()

	def clickedBack(self):
		rosNode.moveBack()


class rosNode(Node):
	def __init__(self):
		super().__init__('turtle_gui')
		self.cmd_vel_Twist = Twist()
		self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

	def moveFoward(self):
		self.cmd_vel_Twist.linear.x = 1 # 1[m/s]で直進
		self.pub_cmd_vel.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0


	def moveBack(self):
		self.cmd_vel_Twist.linear.x = -1
		self.pub_cmd_vel.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0

def main(args=None):
	rclpy.init(args=args)
	app = QApplication(sys.argv)
	window = mainWindow()
	window.show()
	rclpy.spin(mainWindow)
	sys.exit(app.exec_())
	#window.destroy_node()
	#rclpy.shutdown()

if __name__ == '__main__':
	main()

