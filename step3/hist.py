# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hist(object):
    def setupUi(self, Hist):
        Hist.setObjectName("Hist")
        Hist.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Hist)
        self.pushButton.setGeometry(QtCore.QRect(230, 70, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Hist)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 140, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Hist)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 220, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Hist)
        QtCore.QMetaObject.connectSlotsByName(Hist)

    def retranslateUi(self, Hist):
        _translate = QtCore.QCoreApplication.translate
        Hist.setWindowTitle(_translate("Hist", "Form"))
        self.pushButton.setText(_translate("Hist", "PushButton"))
        self.pushButton_2.setText(_translate("Hist", "OK"))
        self.pushButton_3.setText(_translate("Hist", "Cancel"))

