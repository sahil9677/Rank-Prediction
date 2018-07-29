# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 634)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 471, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 451, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 461, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 461, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 471, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 551, 17))
        self.label_6.setObjectName("label_6")
        self.KOpt = QtWidgets.QLineEdit(Form)
        self.KOpt.setGeometry(QtCore.QRect(10, 70, 113, 27))
        self.KOpt.setObjectName("KOpt")
        self.Link = QtWidgets.QLineEdit(Form)
        self.Link.setGeometry(QtCore.QRect(10, 140, 113, 27))
        self.Link.setObjectName("Link")
        self.wordcount = QtWidgets.QLineEdit(Form)
        self.wordcount.setGeometry(QtCore.QRect(10, 200, 113, 27))
        self.wordcount.setObjectName("wordcount")
        self.grammar = QtWidgets.QLineEdit(Form)
        self.grammar.setGeometry(QtCore.QRect(10, 260, 113, 27))
        self.grammar.setObjectName("grammar")
        self.Categ = QtWidgets.QLineEdit(Form)
        self.Categ.setGeometry(QtCore.QRect(10, 320, 113, 27))
        self.Categ.setObjectName("Categ")
        self.Button3 = QtWidgets.QPushButton(Form)
        self.Button3.setGeometry(QtCore.QRect(90, 400, 401, 27))
        self.Button3.setObjectName("Button3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 450, 231, 75))
        self.textEdit.setObjectName("textEdit")
        self.Button4 = QtWidgets.QPushButton(Form)
        self.Button4.setGeometry(QtCore.QRect(150, 540, 231, 27))
        self.Button4.setObjectName("Button4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "We have a few more questions related to on page SEO of your article "))
        self.label_2.setText(_translate("Form", "Rate the Keyword Optimization of your article on a scale of 1 to 10"))
        self.label_3.setText(_translate("Form", "Rate the Internal Linking in your article on a scale of 1 to 10"))
        self.label_4.setText(_translate("Form", "What is the word count of your article"))
        self.label_5.setText(_translate("Form", "Rate the Grammar and Language of your article on a scale of 1 to 10"))
        self.label_6.setText(_translate("Form", "Rate the Categorization and Tag Managementof your article on a scale of 1 to 10"))
        self.Button3.setText(_translate("Form", "Click here to get the Rank Prediction of your Article"))
        self.Button4.setText(_translate("Form", "Click Here to Continue"))

