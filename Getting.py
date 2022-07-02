# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Getting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Getting(object):
    def setupUi(self, Getting):
        Getting.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Getting.setWindowModality(QtCore.Qt.ApplicationModal)
        Getting.setObjectName("Getting")
        Getting.resize(532, 395)
        self.Start = QtWidgets.QPushButton(Getting)
        self.Start.setGeometry(QtCore.QRect(200, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Start.setFont(font)
        self.Start.setObjectName("Start")
        self.label = QtWidgets.QLabel(Getting)
        self.label.setGeometry(QtCore.QRect(50, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.page_Start = QtWidgets.QSpinBox(Getting)
        self.page_Start.setGeometry(QtCore.QRect(360, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.page_Start.setFont(font)
        self.page_Start.setMaximum(9)
        self.page_Start.setMinimum(1)
        self.page_Start.setObjectName("page_Start")
        self.label_2 = QtWidgets.QLabel(Getting)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.page_End = QtWidgets.QSpinBox(Getting)
        self.page_End.setGeometry(QtCore.QRect(360, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.page_End.setFont(font)
        self.page_End.setMaximum(9)
        self.page_End.setMinimum(1)
        self.page_End.setObjectName("page_End")
        self.storeMethod = QtWidgets.QComboBox(Getting)
        self.storeMethod.setGeometry(QtCore.QRect(230, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.storeMethod.setFont(font)
        self.storeMethod.setObjectName("storeMethod")
        self.storeMethod.addItem("")
        self.storeMethod.addItem("")
        self.label_3 = QtWidgets.QLabel(Getting)
        self.label_3.setGeometry(QtCore.QRect(120, 310, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Getting)
        QtCore.QMetaObject.connectSlotsByName(Getting)

    def retranslateUi(self, Getting):
        _translate = QtCore.QCoreApplication.translate
        Getting.setWindowTitle(_translate("Getting", "Form"))
        self.Start.setText(_translate("Getting", "开始"))
        self.label.setText(_translate("Getting", "选择要爬取的起始页数"))
        self.label_2.setText(_translate("Getting", "选择要爬取的终止页数"))
        self.storeMethod.setItemText(0, _translate("Getting", "根目录下csv文件"))
        self.storeMethod.setItemText(1, _translate("Getting", "指定数据库"))
        self.label_3.setText(_translate("Getting", "存储到："))

