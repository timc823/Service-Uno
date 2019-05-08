# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from question import *
from tip import *
import sys


class Ui_WelcomeWindow(QMainWindow):

    def __init__(self):
        super(Ui_WelcomeWindow, self).__init__()
        self.setupUi(self)

    def openWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setStyleSheet(open('style.qss').read())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 460, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openWindow)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 140, 521, 301))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to"))
        self.pushButton.setText(_translate("MainWindow", "Start rating!"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p style='width:100%;text-align:center'><img src=\"uno.png\"/></p></body></html>"))

        # set background image
        window_pale = QtGui.QPalette()
        window_pale.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("bg.jpg")))
        MainWindow.setPalette(window_pale)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui_tip_window = Ui_TipWindow()
    sys.exit(app.exec_())
