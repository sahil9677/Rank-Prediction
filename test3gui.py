# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 640)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 191, 17))
        self.label.setObjectName("label")
        self.DA = QtWidgets.QLineEdit(Form)
        self.DA.setGeometry(QtCore.QRect(0, 30, 113, 27))
        self.DA.setObjectName("DA")
        self.Alexa = QtWidgets.QLineEdit(Form)
        self.Alexa.setGeometry(QtCore.QRect(0, 90, 113, 27))
        self.Alexa.setObjectName("Alexa")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 221, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 311, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 180, 411, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 230, 401, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 280, 401, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 330, 401, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 380, 401, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 430, 441, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(0, 480, 441, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(0, 530, 441, 17))
        self.label_11.setObjectName("label_11")
        self.SSL = QtWidgets.QLineEdit(Form)
        self.SSL.setGeometry(QtCore.QRect(0, 150, 113, 27))
        self.SSL.setObjectName("SSL")
        self.Frequency = QtWidgets.QLineEdit(Form)
        self.Frequency.setGeometry(QtCore.QRect(0, 200, 113, 27))
        self.Frequency.setObjectName("Frequency")
        self.Schema = QtWidgets.QLineEdit(Form)
        self.Schema.setGeometry(QtCore.QRect(0, 250, 113, 27))
        self.Schema.setObjectName("Schema")
        self.AMP = QtWidgets.QLineEdit(Form)
        self.AMP.setGeometry(QtCore.QRect(0, 300, 113, 27))
        self.AMP.setObjectName("AMP")
        self.Static = QtWidgets.QLineEdit(Form)
        self.Static.setGeometry(QtCore.QRect(0, 350, 113, 27))
        self.Static.setObjectName("Static")
        self.Interface = QtWidgets.QLineEdit(Form)
        self.Interface.setGeometry(QtCore.QRect(0, 400, 113, 27))
        self.Interface.setObjectName("Interface")
        self.Exp = QtWidgets.QLineEdit(Form)
        self.Exp.setGeometry(QtCore.QRect(0, 450, 113, 27))
        self.Exp.setObjectName("Exp")
        self.Mobile = QtWidgets.QLineEdit(Form)
        self.Mobile.setGeometry(QtCore.QRect(0, 500, 113, 27))
        self.Mobile.setObjectName("Mobile")
        self.Ad = QtWidgets.QLineEdit(Form)
        self.Ad.setGeometry(QtCore.QRect(0, 550, 113, 27))
        self.Ad.setObjectName("Ad")
        self.Button1 = QtWidgets.QPushButton(Form)
        self.Button1.setGeometry(QtCore.QRect(160, 590, 99, 27))
        self.Button1.setObjectName("Button1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter the Domain Authority"))
        self.label_2.setText(_translate("Form", "Enter the Alexa Rank of Website"))
        self.label_3.setText(_translate("Form", "Have you purchased SSL Certificate (Yes/No)"))
        self.label_4.setText(_translate("Form", "What is the content update Frequency(No. of Articles/week"))
        self.label_5.setText(_translate("Form", "Is Schema Implemented (Yes/No)"))
        self.label_6.setText(_translate("Form", "Is AMP Implemented (Yes/No)"))
        self.label_7.setText(_translate("Form", "Are all static Pages Present (About Us etc.)"))
        self.label_8.setText(_translate("Form", "Rate the Website in terms of Interface on a scale of 1to 10"))
        self.label_9.setText(_translate("Form", "Rate the Website in terms of User Experience on a scale of 1to 10"))
        self.label_10.setText(_translate("Form", "Is the website optimized for Mobile Devices?(Yes/No)"))
        self.label_11.setText(_translate("Form", "Rate the Website in terms of Ad Optimization on a scale of 1to 10"))
        self.Button1.setText(_translate("Form", "Next"))

