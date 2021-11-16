from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

class MyWindow(QMainWindow) :
	def __init__(self) :
		super(MyWindow, self).__init__()
		self.setGeometry(200, 340, 404, 360)
		self.setWindowTitle("Face Recognize Attendance System")
		self.initUI()

	def initUI(self) :
		self.label = QtWidgets.QLabel(self)
		self.label.setText("<font color = 'red'>Automatic Face Recognized</font>")
		self.label.setGeometry(2, 10, 400, 30)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(QFont('Comic Sans MS', 20))

		self.label2 = QtWidgets.QLabel(self)
		self.label2.setText("<font color = 'red'>  Attendance System </font>")
		self.label2.setGeometry(2, 40, 400, 30)
		self.label2.setAlignment(Qt.AlignCenter)
		self.label2.setFont(QFont('Comic Sans MS', 20))

		self.nameLabel = QtWidgets.QLabel(self)
		self.nameLabel.setText("<font color = 'black'> NAME")
		self.nameLabel.setGeometry(20, 90, 100, 30)
		self.nameLabel.setAlignment(Qt.AlignLeft)
		self.nameLabel.setFont(QFont('Comic Sans MS', 10))

		self.rollLabel = QtWidgets.QLabel(self)
		self.rollLabel.setText("<font color = 'black'> ROLL No. ")
		self.rollLabel.setGeometry(20, 140, 100, 30)
		self.rollLabel.setAlignment(Qt.AlignLeft)
		self.rollLabel.setFont(QFont('Comic Sans MS', 10))

		self.name = QtWidgets.QLineEdit(self)
		self.name.setGeometry(95, 80, 400, 30)
		self.name.resize(280, 40)

		self.roll = QtWidgets.QLineEdit(self)
		self.roll.setGeometry(95, 130, 400, 30)
		self.roll.resize(280, 40)

		self.enter = QPushButton(self)
		# self.enter.move(20, 80)
		self.enter.setText("Create Dataset")
		self.enter.setGeometry(150, 180, 120, 30)
		self.enter.clicked.connect(self.buttonClick)
		self.enter.show()
		self.enter.setStyleSheet("background-color : #123298")
	
	def buttonClick(self) :
		N = self.name.text()
		alert = QMessageBox()
		alert.setText(N + " data has been added in the Dataset!")
		alert.exec_()
		sys.exit()
		# self.name.setText("")

def window() :
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()
