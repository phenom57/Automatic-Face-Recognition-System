from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import pickle
import sqlite3
import subprocess
import openpyxl


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 260)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        Dialog.setFont(font)

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 100, 370, 85))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        
        self.rollLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rollLabel.setObjectName("rollLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rollLabel)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMaxLength(3)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 121, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color : #123298")
        self.pushButton.clicked.connect(self.buttonClick)
        
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(0, 10, 400, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(0, 50, 400, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def feed(self, name, roll) :
    	subject = ["AI", "Cryptography", "DP", "DIP", "ADBMS"]
    	wb = openpyxl.load_workbook('attendance.xlsx')
    	print(roll)
    	for i in subject :
    		sheet = wb[i]
    		sheet.cell(row = (int(roll) + 1), column = 1).value = name + '(' + roll + ')'

    	wb.save('attendance.xlsx')
    	wb.close()

    def buttonClick(self) :
        N = self.lineEdit.text()
        R = self.lineEdit_2.text()
        print("R = ", R)
        alert = QMessageBox()
        f = 0
        conn = sqlite3.connect('database.db')
        if not os.path.exists('./dataset'):
            os.makedirs('./dataset')
        c = conn.cursor()
        c.execute('SELECT rollNo FROM Student')
        result = c.fetchall()
        for row in result :
        	if(row[0] == R) :
        		result = R
        		break

        if(len(N) == 0) :
            alert.setWindowTitle("!!!ERROR!!!")
            alert.setIcon(QMessageBox.Warning)
            alert.setText("Please Enter Your Name")
        elif(len(R) == 0) :
            alert.setWindowTitle("!!!ERROR!!!")
            alert.setIcon(QMessageBox.Warning)
            alert.setText("Roll Number not Entered")
        elif(int(R) < 0 or int(R) > 360 or len(R) != 3) :
            alert.setWindowTitle("!!!ERROR!!!")
            alert.setIcon(QMessageBox.Warning)
            alert.setText("Roll Number Entered is Incorrect")
        elif(result == R) :
            alert.setWindowTitle("!!!ERROR!!!")
            alert.setIcon(QMessageBox.Critical)
            alert.setText("Roll Number Exists")
        else :
            f = open('data.pckl', 'wb')
            pickle.dump([N, R], f)
            f.close()
            os.system('python create_face_dataSet.py')
            self.feed(N, R)
            alert.setWindowTitle("Successful!")
            alert.setText("Name : " + N + "\n" + "Roll Number : " + R + "\nAdded in the Dataset")
            f = 1
        alert.exec_()
        if(f == 1) :
            sys.exit()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Registration System")
        self.rollLabel.setText("<font color = '#301616'>Roll Number")
        self.nameLabel.setText("<font color = '#301616'>Name")
        self.pushButton.setText("ADD")
        self.label1.setText("<font color = '#B40606'> Automatic Face Recognized")
        self.label2.setText("<font color = '#B40606'> Attendance System")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
