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
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 223)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(0, 10, 401, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(19)
        font.setBold(True)
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
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(80, 120, 241, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setItalic(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Select the Subject")
        self.comboBox.addItem("AI")
        self.comboBox.addItem("Cryptography")
        self.comboBox.addItem("DP")
        self.comboBox.addItem("DIP")
        self.comboBox.addItem("ADBMS")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 170, 151, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color : #123298")
        self.pushButton.clicked.connect(self.buttonClick)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def buttonClick(self) :
        option = self.comboBox.currentText()
        if option != 'Select the Subject' :
            f = open('subject.pckl', 'wb')
            pickle.dump(option, f)
            f.close()
            os.system('python main.py')
            f = 1
        if f == 1 :
        	sys.exit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Subject Selection")
        self.label1.setText("<font color = '#B40606'> Automatic Face Recognized")
        self.label2.setText("<font color = '#B40606'> Attendance System")
        self.comboBox.setItemText(0, _translate("Dialog", "Select the Subject"))
        self.comboBox.setItemText(1, _translate("Dialog", "AI"))
        self.comboBox.setItemText(2, _translate("Dialog", "Cryptography"))
        self.comboBox.setItemText(3, _translate("Dialog", "DP"))
        self.comboBox.setItemText(4, _translate("Dialog", "DIP"))
        self.comboBox.setItemText(5, _translate("Dialog", "ADBMS"))
        self.pushButton.setText(_translate("Dialog", "Start Recognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
