# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 625)
        self.Button5 = QtWidgets.QPushButton(Form)
        self.Button5.setGeometry(QtCore.QRect(160, 80, 281, 27))
        self.Button5.setObjectName("Button5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 150, 67, 17))
        self.label.setObjectName("label")
        self.Button6 = QtWidgets.QPushButton(Form)
        self.Button6.setGeometry(QtCore.QRect(60, 210, 481, 27))
        self.Button6.setObjectName("Button6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 290, 21, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 281, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button5.setText(_translate("Form", "Do you want to get another prediction"))
        self.label.setText(_translate("Form", "OR"))
        self.Button6.setText(_translate("Form", "Would you like to get suggestions to improve the rank for this article?"))
        self.label_2.setText(_translate("Form", "OR"))
        self.pushButton.setText(_translate("Form", "Do you wish to exit Application?"))

