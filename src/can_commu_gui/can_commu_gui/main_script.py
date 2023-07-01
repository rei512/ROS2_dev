import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QStyle, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from .window import Ui_MainWindow

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_messages.msg import CanMsg
class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.float_topic_name = '/can_gui'
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		# ROS2 init
		rclpy.init(args=None)
		self.node = Node('Qt_view_node')
		self.CanMsg = CanMsg()
		self.input = ""
		self.pub = self.node.create_publisher(CanMsg, '/can_rx', 10)
		for i in range(8):
			self.CanMsg.data.append(0)
		#self.node.get_logger().info('Interraptted')

	def ADD(self, id):
		self.CanMsg.id = id

	def frameType(self, FT):
		self.CanMsg.frametype = bool(FT)

	def chSelect(self, CH):
		self.CanMsg.channel = bool(CH)

	def DLC(self, DLC):
		s = str(DLC)
		b = bytes(s, 'utf-8')
		self.CanMsg.dlc = b

	def DATA(self, input: str):
		self.input = input 
		#tmp = int.from_bytes(self.CanMsg.dlc, byteorder='little')
		#if(tmp > 0):
		#	tmp -= 48
		
		#print(tmp)
		#for i in range(8):
			#s = input[i]
		#	if(i < tmp):
		#		string = input[i]
		#		self.CanMsg.data[i] = string.encode('utf-8')
		#	else:
		#		string = "0"
		#		self.CanMsg.data[i] = string.encode('utf-8')


	def Sent(self):
		#hex_list = input.split()
		#byte_array = bytes(int(hex_str, 16) for hex_str in hex_list)


		#if self.CanMsg.frametype :
		#	self.CanMsg.data = bytes('', 'utf-8')
		#else :
		#	for i in range(int(self.CanMsg.dlc)):
		#		self.CanMsg.data = byte_array[i]
		self.node.get_logger().info(input)
		#self.pub.publish(self.CanMsg)

def main():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
	node.destroy_node()
	rclpy.shutdown()

if __name__=="__main__":
	main()
