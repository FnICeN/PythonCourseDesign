# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dataset.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import database

class Ui_DataView(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 690)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(360, 20, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.databaseWidget = QtWidgets.QTableWidget(Form)
        self.databaseWidget.setGeometry(QtCore.QRect(30, 100, 881, 431))
        self.databaseWidget.setObjectName("databaseWidget")
        self.databaseWidget.setColumnCount(0)
        self.databaseWidget.setRowCount(0)
        self.databaseWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 580, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "数据一览"))
        self.pushButton.setText(_translate("Form", "进行操作"))



# app=QApplication([])
# form=Display()
# form.show()
# app.exec_()