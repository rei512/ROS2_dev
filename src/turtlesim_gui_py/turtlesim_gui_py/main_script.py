#! /usr/bin/python3
# -*- coding: utf-8 -*-


# GUI。
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .window import Ui_MainWindow # 自動生成したファイルをインポート
# ROS。
import rospy
from geometry_msgs.msg import Twist


class Test(QDialog):
	def __init__(self,parent=None):
		# GUI。
		super(Test, self).__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		# ROS。pubの設定。
		self.cmd_vel_Twist = Twist()
		self.pub_cmd_vel = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

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


if __name__ == '__main__':
	rospy.init_node('turtlesim_talker')
	app = QApplication(sys.argv)
	window = Test()
	window.show()
	sys.exit(app.exec_())


