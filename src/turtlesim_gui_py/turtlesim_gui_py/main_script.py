#! /usr/bin/python3
# -*- coding: utf-8 -*-


# GUI。
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .window import Ui_MainWindow # 自動生成したファイルをインポート
# ROS。
import rclpy
from rclpy.node import Node
from geometry_msgs.Twist import Twist


class mainWindow(QmainWindow, Ui_MainWindow, Node):
	def __init__(self, parent=None):
		# GUI部
		super(mainWindow, self).__init__(parent)
		self.ui.setupUi(self)

		# ROS。pubの設定。
		self.cmd_vel_Twist = Twist()
		self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

	def clickedForward(self):
		"""
		Qtデザイナで指定したスロット名。
		「前進」ボタンで実行したい処理を書く。
		"""
		self.cmd_vel_Twist.linear.x = 1 # 1[m/s]で直進
		self.pub_cmd_vel.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0


	def clickedBack(self):
		self.cmd_vel_Twist.linear.x = -1
		self.pub_cmd_vel.publish(self.cmd_vel_Twist)
		self.cmd_vel_Twist.linear.x = 0

def main(args=None):
	rclpy.init('turtlesim_talker')
	app = QApplication(sys.argv)
	window = mainWindow()
	window.show()
	rclpy.spin(window)
	sys.exit(app.exec_())
	window.destroy_node()
	rclpy.shutdown()




if __name__ == '__main__':
	main()
