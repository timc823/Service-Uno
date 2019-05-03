# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\lastWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import config
from UnoDBex import ServiceUno


class Ui_lastWindow(object):
    def setupUi(self, lastWindow):
        lastWindow.setObjectName("lastWindow")
        lastWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(lastWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(560, 450, 93, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.hide()
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 150, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(310, 120, 113, 22))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 150, 90, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 900, 60))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 300, 900, 80))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 120, 90, 16))
        self.label_5.setObjectName("label_5")

        lastWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lastWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        lastWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lastWindow)
        self.statusbar.setObjectName("statusbar")
        lastWindow.setStatusBar(self.statusbar)

        self.retranslateUi(lastWindow)
        QtCore.QMetaObject.connectSlotsByName(lastWindow)

        self.pushButton.clicked.connect(lambda: self.btn_clk())
        self.pushButton2.clicked.connect(lambda: self.btn_clk2())


    def btn_clk(self):
        text = self.lineEdit.text()
        text2 = self.lineEdit2.text()
        print (text)
        if text == "":
            print("empty")
            finalTip = "Wrong input, please try again."
            self.label_4.setText("")
            self.pushButton2.hide()
        elif text.isdigit() == False:
            print("not a digit")
            finalTip = "Wrong input, please try again."
            self.label_4.setText("")
            self.pushButton2.hide()
        elif int(text) <0:
            print("negative")
            finalTip = "Wrong input, please try again."
            self.label_4.setText("")
            self.pushButton2.hide()
        elif text2 == "":
            print("empty name")
            finalTip = "Please fill in server's name."
            self.label_4.setText("")
            self.pushButton2.hide()
        else:
            overall = sum(config.score)
            scale = overall / 100
            bill = int(text)
            while bill <= 0:
               final = print('The bill amount should be greater than zero. Please input again')

            TipPercent = 0
            if scale >= 0.95:
                TipPercent = 0.35
            elif scale >= 0.9 and scale < 0.95:
                TipPercent = 0.3
            elif scale >= 0.75 and scale < 0.89:
                TipPercent = 0.2
            elif scale >= 0.6 and scale < 0.75:
                TipPercent = 0.15
            else:
                TipPercent = 0.1

            Tips = bill * TipPercent
            finalTip = 'Base on your bill amount and the service you have today,\nwe think amount of $' + "%.2f"%(Tips) + ' is the proper amount to tip your server.'
            self.label_2.setText(finalTip)

            config.finaldb = [text2] + config.score + [bill] + [Tips] + [bill+Tips]
            print("FinalDB:",config.score)
            print("FinalDB:",config.finaldb)

            data = pd.read_csv('Data.csv')
            data = data.drop(data.columns[0],axis=1)
            newdata = data.append(pd.Series(config.finaldb, index= data.columns),ignore_index=True)
            newdata.to_csv('Data.csv')

            ''' Old database
            ss = ServiceUno("service.db")
            try:
                ss.CreateDb()
                ss.AddService(config.score[0], config.score[1], config.score[2], config.score[3], config.score[4], config.score[5],
                          config.score[6], )  # Add questions to table Need to get from NewWindow.py
            except sqlite3.OperationalError as e:
                print('sqlite error:', e.args[0])  # table companies already exists
            '''
            totalText = ' Amout: $'+  "%.2f"%(bill) + '\n Tip:      $' + "%.2f"%(Tips) + '\n Total:   $' + "%.2f"%(bill+Tips) + ''
            self.label_4.setText(totalText)
            self.pushButton2.show()
        self.label_2.setText(finalTip)

    def btn_clk2(self):
        sys.exit()

    def retranslateUi(self, lastWindow):
        _translate = QtCore.QCoreApplication.translate
        lastWindow.setWindowTitle(_translate("lastWindow", "lastWindow"))
        self.pushButton.setText(_translate("lastWindow", "Submit"))
        self.pushButton2.setText(_translate("lastWindow", "Exit"))
        self.label.setText(_translate("lastWindow", "Bill amount:"))
        self.label_2.setText(_translate("lastWindow", "Tip:"))
        self.label_3.setText(_translate("lastWindow", "Thank you!"))
        self.label_4.setText(_translate("lastWindow", ""))
        self.label_5.setText(_translate("lastWindow", "Server Name:"))



if __name__ == "__main__":
    import sys
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    app = QtWidgets.QApplication(sys.argv)
    lastWindow = QtWidgets.QMainWindow()
    ui = Ui_lastWindow()
    ui.setupUi(lastWindow)
    lastWindow.show()
    sys.exit(app.exec_())
