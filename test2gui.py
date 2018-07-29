# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 637)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 20))
        self.label.setObjectName("label")
        self.Keyword = QtWidgets.QLineEdit(Form)
        self.Keyword.setGeometry(QtCore.QRect(20, 40, 113, 27))
        self.Keyword.setObjectName("Keyword")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 411, 17))
        self.label_2.setObjectName("label_2")
        self.Trend = QtWidgets.QLineEdit(Form)
        self.Trend.setGeometry(QtCore.QRect(20, 100, 113, 27))
        self.Trend.setObjectName("Trend")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 411, 17))
        self.label_3.setObjectName("label_3")
        self.Wikipedia = QtWidgets.QLineEdit(Form)
        self.Wikipedia.setGeometry(QtCore.QRect(20, 170, 113, 27))
        self.Wikipedia.setObjectName("Wikipedia")
        self.Button2 = QtWidgets.QPushButton(Form)
        self.Button2.setGeometry(QtCore.QRect(180, 240, 99, 27))
        self.Button2.setObjectName("Button2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "What is main targetted Keyword"))
        self.label_2.setText(_translate("Form", "On a scale of 1 to 10 what is the trend level of that Keyword"))
        self.label_3.setText(_translate("Form", "Is there a wikipedia page for that Keyword?"))
        self.Button2.setText(_translate("Form", "Next"))

