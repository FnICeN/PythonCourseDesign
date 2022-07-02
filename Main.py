# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 500)
        self.Title = QtWidgets.QLabel(Main)
        self.Title.setGeometry(QtCore.QRect(200, 30, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.search_Botton = QtWidgets.QPushButton(Main)
        self.search_Botton.setGeometry(QtCore.QRect(560, 140, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_Botton.setFont(font)
        self.search_Botton.setObjectName("search_Botton")
        self.inputLine = QtWidgets.QLineEdit(Main)
        self.inputLine.setGeometry(QtCore.QRect(90, 140, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.inputLine.setFont(font)
        self.inputLine.setText("")
        self.inputLine.setObjectName("inputLine")
        self.to_Getting = QtWidgets.QPushButton(Main)
        self.to_Getting.setGeometry(QtCore.QRect(160, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.to_Getting.setFont(font)
        self.to_Getting.setObjectName("to_Getting")
        self.to_dataControl = QtWidgets.QPushButton(Main)
        self.to_dataControl.setGeometry(QtCore.QRect(480, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.to_dataControl.setFont(font)
        self.to_dataControl.setObjectName("to_dataControl")
        self.comboBox = QtWidgets.QComboBox(Main)
        self.comboBox.setGeometry(QtCore.QRect(410, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Main)
        self.to_Getting.clicked.connect(Main.goToGettingPage)
        self.to_dataControl.clicked.connect(Main.goToDataPage)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Frame"))
        self.Title.setText(_translate("Main", "知网数据爬取系统"))
        self.search_Botton.setText(_translate("Main", "预览"))
        self.to_Getting.setText(_translate("Main", "爬取"))
        self.to_dataControl.setText(_translate("Main", "数据管理"))
        self.comboBox.setItemText(0, _translate("Main", "按作者"))
        self.comboBox.setItemText(1, _translate("Main", "按主题"))

