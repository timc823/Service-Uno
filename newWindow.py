
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\newWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

#from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from thirdWindow import *
from UnoDBex import ServiceUno
import sys
import config

#score = [0] * 10
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
        self.openWindow()
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

if __name__ == "__main__":
    import sys
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    app = QtWidgets.QApplication(sys.argv)
    newWindow = QtWidgets.QMainWindow()
    ui = Ui_newWindow()
    ui.setupUi(newWindow)
    newWindow.show()
    sys.exit(app.exec_())

'''To Kevin: This is the code to generate the tips, in Q7, you are printing the list now, I sum the list and
    create a scale to calculate it. Hence, when you finish the Q10, it should be able to work if you paste it under the
    function. Let me know when you finish the program and I will paste it.'''
