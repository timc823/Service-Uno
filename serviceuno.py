# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from newWindow import *
import sys
import config
import sqlite3
import welcome_rc
import pandas as pd

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



i = [0] * 10
class Ui_thirdWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_lastWindow()
        self.ui.setupUi(self.window)
        #thirdWindow.hide()
        self.window.show()

    def setupUi(self, thirdWindow):
        thirdWindow.setObjectName("thirdWindow")
        thirdWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(thirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 771, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(50, 20, 50, 20))
        self.radioButton_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_1.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 20, 50, 20))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 20, 50, 20))
        self.radioButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 20, 50, 20))
        self.radioButton_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(350, 20, 50, 20))
        self.radioButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(410, 20, 50, 20))
        self.radioButton_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setGeometry(QtCore.QRect(470, 20, 50, 20))
        self.radioButton_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setGeometry(QtCore.QRect(530, 20, 50, 20))
        self.radioButton_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_10.setGeometry(QtCore.QRect(590, 20, 50, 20))
        self.radioButton_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(290, 20, 50, 20))
        self.radioButton_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 381, 16))
        self.label.setObjectName("label")
        thirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(thirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        thirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(thirdWindow)
        self.statusbar.setObjectName("statusbar")
        thirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(thirdWindow)
        QtCore.QMetaObject.connectSlotsByName(thirdWindow)

        #self.pushButton.clicked.connect(lambda: self.btn_clk())
        self.pushButton.clicked.connect(lambda: self.btn_clk(self.centralwidget.findChildren(QtWidgets.QRadioButton)))


    def retranslateUi(self, thirdWindow):
        _translate = QtCore.QCoreApplication.translate
        thirdWindow.setWindowTitle(_translate("thirdWindow", "thirdWindow"))
        self.pushButton.setText(_translate("thirdWindow", "Submit"))
        self.radioButton_1.setText(_translate("thirdWindow", "1"))
        self.radioButton_2.setText(_translate("thirdWindow", "2"))
        self.radioButton_3.setText(_translate("thirdWindow", "3"))
        self.radioButton_4.setText(_translate("thirdWindow", "4"))
        self.radioButton_5.setText(_translate("thirdWindow", "5"))
        self.radioButton_6.setText(_translate("thirdWindow", "6"))
        self.radioButton_7.setText(_translate("thirdWindow", "7"))
        self.radioButton_8.setText(_translate("thirdWindow", "8"))
        self.radioButton_9.setText(_translate("thirdWindow", "9"))
        self.radioButton_10.setText(_translate("thirdWindow", "10"))
        self.label.setText(_translate("thirdWindow", "8. Please provide a score for how satisified were you for the service: "))

    def btn_clk(self,chk):
        for items in chk:
            if items.isChecked():
                checked_radiobutton = items.text()
                self.label.setText("9. Please provide a score for how friendly your server was: ")
                i[0] = i[0]+1
                if i[0] == 1:
                    config.score[7] = int(checked_radiobutton)
                    #print(config.score)
                    print("Q8", config.score[7], i[0],config.score[7])
        self.pushButton.clicked.connect(lambda: self.btn_clk2(self.centralwidget.findChildren(QtWidgets.QRadioButton)))

    def btn_clk2(self,chk):
        for items in chk:
            if items.isChecked():
                checked_radiobutton = items.text()
                self.label.setText("10. Please provide a overall score for your server: ")
                i[1] = i[1]+1
                if i[1] == 1:
                    config.score[8] = int(checked_radiobutton)
                    #print(config.score)
                    print("Q9", config.score[8], i[1],config.score[8])
        self.pushButton.clicked.connect(lambda: self.btn_clk3(self.centralwidget.findChildren(QtWidgets.QRadioButton)))

    def btn_clk3(self,chk):
        for items in chk:
            if items.isChecked():
                checked_radiobutton = items.text()
                i[2] = i[2]+1
                if i[2] == 1:
                    config.score[9] = int(checked_radiobutton)
                    print("Q10", config.score[9], i[2],config.score[9])
                    print(config.score)
                self.label.setText("")
        self.groupBox.hide()
        #self.openWindow()
        Controller.Show_lastWindow()



i = [0] * 10
class Ui_newWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_thirdWindow()
        self.ui.setupUi(self.window)
        #newWindow.hide()
        self.window.show()

    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(newWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 231, 61))
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(230, 300, 231, 61))
        self.label2.setObjectName("label2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(450, 30, 120, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(360, 510, 93, 28))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.hide()
        newWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        newWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(newWindow)
        self.statusbar.setObjectName("statusbar")
        newWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

        self.pushButton.clicked.connect(lambda: self.btn_clk(self.radioButton.isChecked()))

    def retranslateUi(self, newWindow):
        _translate = QtCore.QCoreApplication.translate
        newWindow.setWindowTitle(_translate("newWindow", "newWindow"))
        self.label.setText(_translate("newWindow", "1. Have you been seated?"))
        self.label2.setText(_translate("newWindow", ""))
        self.radioButton.setText(_translate("newWindow", "Yes"))
        self.radioButton_2.setText(_translate("newWindow", "No"))
        self.pushButton.setText(_translate("newWindow", "Submit"))
        self.pushButton2.setText(_translate("newWindow", "Submit2"))

    def btn_clk(self, chk):
        score1 = 0
        #global score
        global i
        i[0] = i[0]+1
        if chk:
            #self.label2.setText("yes")
            score1 += 10
        else:
            #self.label2.setText("No")
            score1 += 5
        self.label.setText("2. Did your server greet you?")
        if i[0] == 1:
            config.score[0] = score1
            print("Q1", score1, i[0],config.score[0])
        self.pushButton.clicked.connect(lambda: self.btn_clk1(self.radioButton.isChecked()))


    def btn_clk1(self, chk):
        score2 = 0
        #global score
        global i
        i[1] = i[1]+1
        if chk:
            #self.label2.setText("yes")
            score2 += 10
        else:
            #self.label2.setText("No")
            score2 += 5
        self.label.setText("3. Did you order?")
        if i[1] == 1:
            config.score[1] = score2
            print("Q2", score2, i[1],config.score[1])
        self.pushButton.clicked.connect(lambda: self.btn_clk2(self.radioButton.isChecked()))
    def btn_clk2(self, chk):
        score3 = 0
        #global score
        global i
        i[2] = i[2]+1
        if chk:
            #self.label2.setText("yes")
            score3 += 10
        else:
            #self.label2.setText("No")
            score3 += 5
        self.label.setText("4. Did server bring you drinks?")
        if i[2] == 1:
            config.score[2] = score3
            print("Q3", score3, i[2],config.score[2])
        self.pushButton.clicked.connect(lambda: self.btn_clk3(self.radioButton.isChecked()))

    def btn_clk3(self, chk):
        score4 = 0
        #global score
        global i
        i[3] = i[3]+1
        if chk:
            #self.label2.setText("yes")
            score4 += 10
        else:
            #self.label2.setText("No")
            score4 += 5
        self.label.setText("5. Did server bring you appetizers")
        if i[3] == 1:
            config.score[3] = score4
            print("Q4", score4, i[3],config.score[3])
        self.pushButton.clicked.connect(lambda: self.btn_clk4(self.radioButton.isChecked()))
    def btn_clk4(self, chk):
        score5 = 0
        #global score
        global i
        i[4] = i[4]+1
        if chk:
            #self.label2.setText("yes")
            score5 += 10
        else:
            #self.label2.setText("No")
            score5 += 5
        self.label.setText("6. Did server bring you food?")
        if i[4] == 1:
            config.score[4] = score5
            print("Q5", score5, i[4],config.score[4])
        self.pushButton.clicked.connect(lambda: self.btn_clk5(self.radioButton.isChecked()))

    def btn_clk5(self, chk):
        score6 = 0
        #global score
        global i
        i[5] = i[5]+1
        if chk:
            #self.label2.setText("yes")
            score6 += 10
        else:
            #self.label2.setText("No")
            score6 += 5
        self.label.setText("7. Did server clean the table for you?")
        if i[5] == 1:
            config.score[5] = score6
            print("Q6", score6, i[5],config.score[5])
        self.pushButton.clicked.connect(lambda: self.btn_clk6(self.radioButton.isChecked()))

    def btn_clk6(self, chk):
        score7 = 0
        #global score
        global i
        i[6] = i[6]+1
        if chk:
            #self.label2.setText("yes")
            score7 += 10
        else:
            #self.label2.setText("No")
            score7 += 5
        #self.label.setText("Thank you!!!")
        if i[6] == 1:
            config.score[6] = score7
            print("Q7", score7, i[6],config.score[6])
        #self.pushButton.setEnabled(False)
        #self.pushButton.setVisible(False)
        #self.label2.setVisible(False)
        #self.groupBox.setVisible(False)
        #print("openNewWindow")
        #self.window.hide()
        Controller.Show_thirdWindow()
        self.label2.setText("")
        '''
        self.pushButton.setEnabled(False)
        self.pushButton.hide()
        self.pushButton2.show()
        self.pushButton2.clicked.connect(self.openWindow)
        print(config.score)
        #self.pushButton.clicked.connect(self.openWindow)
        #self.pushButton.setEnabled(False)

    def btn_clk7(self, score7):
        self.pushButton.setEnabled(False)
        self.pushButton.hide()
        self.pushButton2.show()
        self.pushButton2.clicked.connect(self.openWindow)
        print("OK")
        self.openWindow()
'''
'''
        overall = sum(score)
        scale = overall / 100
        bill = eval(input('Please input the bill amount: '))
        while bill <= 0:
           print('The bill amount should be greater than zero. Please input again')
           bill = eval(input('Please input the bill amount: '))

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
        print('Base on your bill amount and the service you have today, we think amount of ', "%.2f"%(Tips),
              'is the valuable amount to tip your server.')
        ss = ServiceUno("service.db")
        ss.CreateDb()
        ss.AddService(score[0], score[1], score[2], score[3], score[4], score[5],
                      score[6], )  # Add questions to table Need to get from NewWindow.py
        ss.Close()
        sys.exit()

'''

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
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
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "Start rating!"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/Untitled.png\"/></p></body></html>"))

class Controller:

    def __init__(self):
        pass

    def Show_MainWindow(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.pushButton.clicked.connect(self.Show_newWindow)

        self.MainWindow.show()

    def Show_newWindow(self):

        self.newWindow = QtWidgets.QMainWindow()
        self.ui = Ui_newWindow()
        self.ui.setupUi(self.newWindow)
        #self.ui.pushButton.clicked.connect(self.Show_thirdWindow)

        self.newWindow.show()
        self.MainWindow.hide()

    def Show_thirdWindow(self):

        self.thirdWindow = QtWidgets.QMainWindow()
        self.ui = Ui_thirdWindow()
        self.ui.setupUi(self.thirdWindow)
        #self.ui.pushButton.clicked.connect(self.Print)

        self.thirdWindow.show()
        self.newWindow.hide()

    def Show_lastWindow(self):

        self.lastWindow = QtWidgets.QMainWindow()
        self.ui = Ui_lastWindow()
        self.ui.setupUi(self.lastWindow)
        #self.ui.pushButton.clicked.connect(self.Print)

        self.lastWindow.show()
        self.thirdWindow.hide()

    def Print(self):
        print('After 99 hours of trying out everything')

if __name__ == "__main__":
    import sys
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.show()
    Controller = Controller()
    Controller.Show_MainWindow()
    sys.exit(app.exec_())
