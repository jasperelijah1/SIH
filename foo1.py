# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rotronix(object):
    def setupUi(self, rotronix):
        rotronix.setObjectName("rotronix")
        rotronix.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(rotronix)
        self.centralwidget.setObjectName("centralwidget")
        self.Day = QtWidgets.QLabel(self.centralwidget)
        self.Day.setGeometry(QtCore.QRect(70, 120, 55, 16))
        self.Day.setObjectName("Day")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(70, 170, 55, 16))
        self.Time.setObjectName("Time")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 170, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 161, 31))
        self.label.setObjectName("label")
        rotronix.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rotronix)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        rotronix.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rotronix)
        self.statusbar.setObjectName("statusbar")
        rotronix.setStatusBar(self.statusbar)

        self.retranslateUi(rotronix)
        QtCore.QMetaObject.connectSlotsByName(rotronix)

    def retranslateUi(self, rotronix):
        _translate = QtCore.QCoreApplication.translate
        rotronix.setWindowTitle(_translate("rotronix", "MainWindow"))
        self.Day.setText(_translate("rotronix", "DAY:"))
        self.Time.setText(_translate("rotronix", "TIME:"))
        self.pushButton.setText(_translate("rotronix", "SHOW DEMAND"))
        self.label.setText(_translate("rotronix", "DEMAND PREDICTION"))


