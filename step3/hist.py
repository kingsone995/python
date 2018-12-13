# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histdlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


#from PyQt5 import QtCore, QtGui, QtWidgets
 
#class HistgramUI(object):
#    def setupUi(self, Dialog):              
#        Dialog.setObjectName("HistgramUI")
#        Dialog.resize(600, 400)

from PyQt5 import QtCore, QtGui, QtWidgets

class HistDlg(object):
    def setupUi(self, HistDlg):
        HistDlg.setObjectName("HistDlg")
        HistDlg.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(HistDlg)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(HistDlg)
        self.buttonBox.accepted.connect(HistDlg.accept)
        self.buttonBox.rejected.connect(HistDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(HistDlg)

    def retranslateUi(self, HistDlg):
        _translate = QtCore.QCoreApplication.translate
        HistDlg.setWindowTitle(_translate("HistDlg", "Dialog"))