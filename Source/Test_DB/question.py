# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from util import DataUtil
from PyQt5.QtWidgets import QMessageBox
# from answer import *
from tip import *
from functools import partial


global questionconf
questionconf = {
    'cur_index': 1,
    'questions': [],
    'answers': [],
    'user_id': 1,
    'restaurant_id': 1,
    'page_id': 0,
}


class Ui_MainWindow(object):

    def __init__(self):
        global questionconf
        self.getQuestions()

        self.question_sum = len(questionconf['questions'])
        self.pages = [0 for x in range(0, self.question_sum)]
        self.questionlabels = [0 for x in range(0, self.question_sum)]
        self.radioyes = [0 for x in range(0, self.question_sum)]
        self.radiono = [0 for x in range(0, self.question_sum)]
        self.radioButtons = [0 for x in range(0, self.question_sum)]

    def setupUi(self, MainWindow):
        global questionconf

        self.mainwindow = MainWindow
        MainWindow.setStyleSheet(open('style.qss').read())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 70, 600, 311))
        self.stackedWidget.setObjectName("stackedWidget")


        _index = 0
        for _question in questionconf['questions']:
            self.addNewPage(_question, _index)
            _index += 1

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 321, 20))
        self.label.setObjectName("counter")
        self.update_counter()

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 75, 23))
        self.pushButton.setObjectName("submit")
        self.pushButton.setDisabled(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushNext = QPushButton(self.centralwidget)
        self.pushNext.setGeometry(QtCore.QRect(350, 400, 75, 23))
        self.pushNext.setObjectName("Next")
        MainWindow.setCentralWidget(self.centralwidget)

        # self.pushPrev = QPushButton(self.centralwidget)
        # self.pushPrev.setGeometry(QtCore.QRect(350, 450, 75, 23))
        # self.pushPrev.setObjectName("Prev")
        # self.pushPrev.setHidden(False)
        # MainWindow.setCentralWidget(self.centralwidget)

        # self.pushPrev.clicked.connect(self.on_prev_clicked)
        self.pushNext.clicked.connect(self.on_next_clicked)
        self.pushButton.clicked.connect(self.on_submit)
        self.display_buttons()

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        print(questionconf)

    def retranslateUi(self, MainWindow):
        global questionconf
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Questions"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushNext.setText(_translate("MainWindow", "Next"))
        # self.pushPrev.setText(_translate("MainWindow", "Prev"))

        # set background image
        window_pale = QtGui.QPalette()
        window_pale.setBrush(MainWindow.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("bg.jpg")))
        MainWindow.setPalette(window_pale)

    def getQuestions(self):
        global questionconf
        questionconf['questions'], questionconf['page_id'] = DataUtil.get_all_questions(questionconf['restaurant_id'])

    def addNewPage(self, question, index: int):
        self.pages[index] = QWidget()
        self.pages[index].setObjectName("page" + str(index))

        self.questionlabels[index] = QLabel(self.pages[index])
        self.questionlabels[index].setGeometry(QtCore.QRect(50, 90, 321, 20))
        self.questionlabels[index].setObjectName("label" + str(index))
        self.questionlabels[index].setText(str(index+1) + ". " + str(question.question))

        _option_width = 89
        _start_x = 40
        _start_y = 180
        _counter = 0
        self.radioButtons[index] = {}
        for opt in question.option:
            _x = _start_x + (_option_width + 10) * (_counter % 5)
            _y = _start_y + _counter // 5 * 50
            _counter += 1
            _option_key = 'v' + str(opt['value'])
            self.radioButtons[index][_option_key] = QRadioButton(self.pages[index])
            self.radioButtons[index][_option_key].setStyleSheet("font-size: 16px;")
            self.radioButtons[index][_option_key].setGeometry(QtCore.QRect(_x, _y, _option_width, 16))
            self.radioButtons[index][_option_key].setObjectName("radio_" + str(index) + str(opt['value']))
            self.radioButtons[index][_option_key].setText(opt['option'])

            # self.radioButtons[index][_option_key].clicked.connect(lambda: self.on_radio_clicked(opt['value']))
            self.radioButtons[index][_option_key].clicked.connect(partial(self.on_radio_clicked, opt['value']))

        # self.radioyes[index] = QRadioButton(self.pages[index])
        # self.radioyes[index].setGeometry(QtCore.QRect(90, 180, 89, 16))
        # self.radioyes[index].setObjectName("radioYes" + str(index))
        # self.radioyes[index].setText("Yes")

        # self.radiono[index] = QRadioButton(self.pages[index])
        # self.radiono[index].setGeometry(QtCore.QRect(230, 180, 89, 16))
        # self.radiono[index].setObjectName("radioNo" + str(index))
        # self.radiono[index].setText("No")

        # self.radioyes[index].clicked.connect(self.on_yes_clicked)
        # self.radiono[index].clicked.connect(self.on_no_clicked)

        self.stackedWidget.addWidget(self.pages[index])

    def on_radio_clicked(self, value: int):
        global questionconf
        print('click button value: ' + str(value))
        question_id = questionconf['questions'][questionconf['cur_index'] - 1].id
        self.save_answer(question_id, value)
        self.display_buttons()

    def on_yes_clicked(self):
        global questionconf
        question_id = questionconf['questions'][questionconf['cur_index']-1].id
        self.save_answer(question_id, '1')
        self.display_buttons()

    def on_no_clicked(self):
        global questionconf
        question_id = questionconf['questions'][questionconf['cur_index']-1].id
        self.save_answer(question_id, '0')
        self.display_buttons()

    def on_prev_clicked(self):
        global questionconf
        if questionconf['cur_index'] >= self.question_sum:
            self.show_answers()
        else:
            question_id = questionconf['questions'][questionconf['cur_index']-1].id
            self.save_answer(question_id, '1')
            questionconf['cur_index'] += 1
            self.update_counter()
            self.stackedWidget.setCurrentIndex(questionconf['cur_index'])
            self.display_buttons()

    def on_next_clicked(self):
        global questionconf
        _cur_index = questionconf['cur_index']-1
        if not self.check_has_answered():
            QMessageBox.warning(self.mainwindow,
                                "Tips",
                                'You has not answered yet',
                                QMessageBox.Yes)
        elif questionconf['cur_index'] >= self.question_sum:
            self.show_answers()
        else:
            questionconf['cur_index'] += 1
            self.update_counter()
            self.stackedWidget.setCurrentIndex(_cur_index + 1)
            self.display_buttons()

    def save_answer(self, question_id: int, answer: int):
        global questionconf
        _option_info = {}
        for _q in questionconf['questions']:
            if _q.id == question_id:
                for _opt in _q.option:
                    if _opt['value'] == answer:
                        _option_info = _opt
                        break

        _updated = False
        for _answer in questionconf['answers']:
            if _answer['question_id'] == question_id:
                _answer['answer'] = _option_info['option']
                _answer['value'] = _option_info['value']
                _answer['score'] = _option_info['score']
                _updated = True
        if not _updated:
            questionconf['answers'].append({
                'question_id': question_id,
                'answer': _option_info['option'],
                'value': _option_info['value'],
                'score': _option_info['score'],
            })
        print('save_answer: ', questionconf['answers'], 'question_id:' + str(question_id), 'answer:' + str(answer))

    def show_answers(self):
        global questionconf
        msg = ''
        for answer in questionconf['answers']:
            msg += 'id:' + str(answer['question_id']) + ' ' + str(answer['answer']) + "\n"
        QMessageBox.warning(self.mainwindow,
                            "Answers",
                            msg,
                            QMessageBox.Yes)

    def update_counter(self):
        global questionconf
        self.label.setText(str(questionconf['cur_index']) + "/" + str(self.question_sum))

    def check_has_answered(self):
        global questionconf
        return bool(questionconf['cur_index'] <= len(questionconf['answers']))

    def check_all_answered(self):
        global questionconf
        return len(questionconf['answers']) == self.question_sum

    def on_submit(self):
        global questionconf
        print('submit: ', questionconf)

        if not self.check_all_answered():
            QMessageBox.warning(self.mainwindow,
                                "Waining",
                                'There are still questions unanswered.',
                                QMessageBox.Yes)
            return

        save_record = DataUtil.save_answers(questionconf['user_id'],
                                            questionconf['restaurant_id'],
                                            questionconf['page_id'],
                                            questionconf['answers'])

        if save_record:
            reply = QMessageBox.information(self.mainwindow,
                                            "Congratulation",
                                            'Thank you for your participation',
                                            QMessageBox.Ok)
        else:
            reply = QMessageBox.warning(self.mainwindow,
                                        "Waining",
                                        'Save failed',
                                        QMessageBox.Ok)

        if reply == QMessageBox.Ok:
            self.show_answer_window()

    def display_buttons(self):
        print('display buttons')
        global questionconf
        if self.question_sum == 1:
            # self.pushPrev.setHidden(True)
            self.pushNext.setHidden(True)
        elif questionconf['cur_index'] == 1:
            # self.pushPrev.setHidden(True)
            self.pushNext.setHidden(False)
        elif questionconf['cur_index'] == self.question_sum:
            # self.pushPrev.setHidden(False)
            self.pushNext.setHidden(True)
        else:
            # self.pushPrev.setHidden(False)
            self.pushNext.setHidden(False)

        if len(questionconf['answers']) == self.question_sum:
            self.pushButton.setHidden(False)
            self.pushButton.setDisabled(False)
        else:
            self.pushButton.setHidden(True)
            self.pushButton.setDisabled(True)

    def show_answer_window(self):
        # ui_tip_window.setupUi(MainWindow)
        # self.window = QMainWindow()
        self.ui = Ui_TipWindow()
        self.ui.setupUi(self.mainwindow)
        # MainWindow.hide()
        self.mainwindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    questionMainWindow = QMainWindow()
    the_mainwindow = Ui_MainWindow()
    the_mainwindow.setupUi(questionMainWindow)
    questionMainWindow.show()
    # ui_answer = Ui_AnswerWindow()
    # ui_tip_window = Ui_TipWindow()
    sys.exit(app.exec_())

