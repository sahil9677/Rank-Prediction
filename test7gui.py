# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled7.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 623)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 17))
        self.label.setObjectName("label")
        self.Button9 = QtWidgets.QPushButton(Form)
        self.Button9.setGeometry(QtCore.QRect(140, 30, 99, 27))
        self.Button9.setObjectName("Button9")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 591, 211))
        self.textEdit.setObjectName("textEdit")
        self.Button10 = QtWidgets.QPushButton(Form)
        self.Button10.setGeometry(QtCore.QRect(150, 320, 99, 27))
        self.Button10.setObjectName("Button10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "To get Suggestions related to topic selection and gap analysis"))
        self.Button9.setText(_translate("Form", "Click Here"))
        self.Button10.setText(_translate("Form", "Next"))

