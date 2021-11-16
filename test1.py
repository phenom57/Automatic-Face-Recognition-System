#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import subprocess


class MyWindow(QMainWindow) :
	def __init__(self) :
		super(MyWindow, self).__init__()
		self.setGeometry(200, 340, 404, 360)
		self.setWindowTitle("Face Recognized Attendance System")
		self.initUI()

	def initUI(self) :
		font = QtGui.QFont()
		font.setPointSize(21)
		font.setBold(True)
		font.setWeight(75)
		self.label = QtWidgets.QLabel(self)
		self.label.setText("<font color = '#B40606'>Automatic Face Recognized</font>")
		self.label.setGeometry(2, 10, 400, 30)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(font)
		# self.label.setFont(QFont('Comic Sans MS', 20))

		self.label2 = QtWidgets.QLabel(self)
		self.label2.setText("<font color = '#B40606'>  Attendance System </font>")
		self.label2.setGeometry(2, 40, 400, 30)
		self.label2.setAlignment(Qt.AlignCenter)
		# self.label2.setFont(QFont('Comic Sans MS', 20))
		self.label2.setFont(font)
		
		self.createDataset = QtWidgets.QPushButton(self)
		self.createDataset.setText("CREATE DATASET")
		self.createDataset.setGeometry(2, 80, 400, 30)
		self.createDataset.clicked.connect(self.createData)
		self.createDataset.setStyleSheet("background-color : #123298")

		self.trainDataset = QtWidgets.QPushButton(self)
		self.trainDataset.setText("TRAIN DATASET")
		self.trainDataset.setGeometry(2, 120, 400, 30)
		self.trainDataset.clicked.connect(self.trainData)
		self.trainDataset.setStyleSheet("background-color : #123298")

		self.recognize = QtWidgets.QPushButton(self)
		self.recognize.setText("Recognize + Attendance")
		self.recognize.setGeometry(2, 160, 400, 30)
		self.recognize.clicked.connect(self.recognizeStudent)
		self.recognize.setStyleSheet("background-color : #123298")

		self.attendance = QtWidgets.QPushButton(self)
		self.attendance.setText("Attendance Sheet")
		self.attendance.setGeometry(2, 200, 400, 30)
		self.attendance.clicked.connect(self.attendanceSheet)
		self.attendance.setStyleSheet("background-color : #123298")

		self.report = QtWidgets.QPushButton(self)
		self.report.setText("Project Report")
		self.report.setGeometry(2, 240, 400, 30)
		self.report.clicked.connect(self.reportFile)
		self.report.setStyleSheet("background-color : #123298")

		self.developers = QtWidgets.QPushButton(self)
		self.developers.setText("Developers Profile")
		self.developers.setGeometry(2, 280, 400, 30)
		self.developers.clicked.connect(self.developersProfile)
		self.developers.setStyleSheet("background-color : #123298")

		self.exit = QtWidgets.QPushButton(self)
		self.exit.setText("EXIT")
		self.exit.setGeometry(2, 320, 400, 30)
		self.exit.clicked.connect(self.exitApp)
		self.exit.setStyleSheet("background-color : #123298")

	def createData(self) :
		self.createDataset.setStyleSheet("background-color : #00FF00")
		self.updateTrainDataset()
		self.updateRecognize()
		self.updateAttendance()
		self.updateProjectReport()
		self.updateDevelopersProfile()
		self.exit.setStyleSheet("background-color : #123298")
		os.system("python form.py")

	def trainData(self) :
		self.trainDataset.setStyleSheet("background-color : #00FF00")
		self.updateCreateDataset()
		self.updateRecognize()
		self.updateAttendance()
		self.updateProjectReport()
		self.updateDevelopersProfile()
		self.exit.setStyleSheet("background-color : #123298")
		os.system("python trainner.py")

	def recognizeStudent(self) :
		self.recognize.setStyleSheet("background-color : #00FF00")
		self.updateCreateDataset()
		self.updateTrainDataset()
		self.updateAttendance()
		self.updateProjectReport()
		self.updateDevelopersProfile()
		self.exit.setStyleSheet("background-color : #123298")
		os.system("python subject.py")

	def attendanceSheet(self) :
		self.attendance.setStyleSheet("background-color : #00FF00")
		self.updateCreateDataset()
		self.updateTrainDataset()
		self.updateRecognize()
		self.updateProjectReport()
		self.updateDevelopersProfile()
		self.exit.setStyleSheet("background-color : #123298")
		subprocess.call(('xdg-open', 'attendance.xlsx'))

	def reportFile(self) :
		self.report.setStyleSheet("background-color : #00FF00")
		self.updateCreateDataset()
		self.updateTrainDataset()
		self.updateRecognize()
		self.updateAttendance()
		self.updateDevelopersProfile()
		self.exit.setStyleSheet("background-color : #123298")
		self.report.setText("!!!!! Not Uploaded yet !!!!!")

	def developersProfile(self) : 
		self.developers.setStyleSheet("background-color : #00FF00")
		self.updateCreateDataset()
		self.updateTrainDataset()
		self.updateRecognize()
		self.updateAttendance()
		self.updateProjectReport()
		self.exit.setStyleSheet("background-color : #123298")
		self.developers.setText("Work Under Progress")

	def exitApp(self) :
		sys.exit()

	def updateCreateDataset(self) :
		self.createDataset.setStyleSheet("background-color : #123298")
		self.createDataset.setText("CREATE DATASET")

	def updateTrainDataset(self) : 
		self.trainDataset.setStyleSheet("background-color : #123298")
		self.trainDataset.setText("TRAIN DATASET")

	def updateRecognize(self) :
		self.recognize.setStyleSheet("background-color : #123298")
		self.recognize.setText("Recognize + Attendance")

	def updateAttendance(self) :
		self.attendance.setStyleSheet("background-color : #123298")
		self.attendance.setText("Attendance Sheet")

	def updateProjectReport(self) :
		self.report.setStyleSheet("background-color : #123298")
		self.report.setText("Project Report")

	def updateDevelopersProfile(self) :
		self.developers.setStyleSheet("background-color : #123298")
		self.developers.setText("Developers Profile")	

def window() :
	app = QApplication(sys.argv)
	win = MyWindow()
	# win.showMaximized()
	win.show()
	sys.exit(app.exec_())

window()

