# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CGU\OneDrive - Claremont Graduate University\IST303_Spring2019\teamwork\newWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

score = 0

class Ui_newWindow(object):
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
        newWindow.setWindowTitle(_translate("newWindow", "MainWindow"))
        self.label.setText(_translate("newWindow", "1. Have you been seated?"))
        self.label2.setText(_translate("newWindow", "Answer"))
        self.radioButton.setText(_translate("newWindow", "Yes"))
        self.radioButton_2.setText(_translate("newWindow", "No"))
        self.pushButton.setText(_translate("newWindow", "Submit"))

    def btn_clk(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("2. Did your server greet you?")
        self.pushButton.clicked.connect(lambda: self.btn_clk1(self.radioButton.isChecked()))
        print(score)
    def btn_clk1(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("3. Did you order?")
        self.pushButton.clicked.connect(lambda: self.btn_clk2(self.radioButton.isChecked()))
        print(score)
    def btn_clk2(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("4. Did server bring you drinks?")
        self.pushButton.clicked.connect(lambda: self.btn_clk3(self.radioButton.isChecked()))
        print(score)
    def btn_clk3(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("5. Did server bring you appetizers")
        self.pushButton.clicked.connect(lambda: self.btn_clk4(self.radioButton.isChecked()))
        print(score)
    def btn_clk4(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("6. Did server bring you food?")
        self.pushButton.clicked.connect(lambda: self.btn_clk5(self.radioButton.isChecked()))
        print(score)
    def btn_clk5(self, chk):
        global score
        if chk:
            self.label2.setText("yes")
            score += 10
        else:
            self.label2.setText("No")
        self.label.setText("7. Did server clean the table for you?")
        self.pushButton.clicked.connect(lambda: self.btn_clk6(self.radioButton.isChecked()))
        print(score)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newWindow = QtWidgets.QMainWindow()
    ui = Ui_newWindow()
    ui.setupUi(newWindow)
    newWindow.show()
    sys.exit(app.exec_())
