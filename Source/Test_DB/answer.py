# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from util import DataUtil
import sys


class Ui_AnswerWindow(object):
    def setupUi(self, MainWindow):

        self.user = DataUtil.get_user_info(user_id=1)

        self.answers = DataUtil.get_answers(user_id=1, restaurant_id=1)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 441, 31))
        self.label.setObjectName("label")

        self.model = QStandardItemModel(len(self.answers), 2)
        self.model.setHorizontalHeaderLabels(['Question', 'Select', 'Score'])

        for row in range(len(self.answers)):
            print(self.answers[row])
            item_question = QStandardItem(self.answers[row]['question'])
            item_answer = QStandardItem(self.answers[row]['answer'])
            item_score = QStandardItem(str(self.answers[row]['score']))
            self.model.setItem(row, 0, item_question)
            self.model.setItem(row, 1, item_answer)
            self.model.setItem(row, 2, item_score)

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(170, 140, 500, 300))
        self.tableView.setObjectName("tabelView")
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(1, 80)
        self.tableView.setColumnWidth(2, 100)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your answers"))
        self.label.setText(_translate("MainWindow", "Hello, ") + self.user.name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lastWindow = QMainWindow()
    the_mainwindow = Ui_AnswerWindow()
    the_mainwindow.setupUi(lastWindow)
    lastWindow.show()
    sys.exit(app.exec_())
