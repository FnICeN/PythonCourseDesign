# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataControl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataControl(object):
    def setupUi(self, DataControl):
        DataControl.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        DataControl.setWindowModality(QtCore.Qt.ApplicationModal)
        DataControl.setObjectName("DataControl")
        DataControl.resize(653, 554)
        self.formLayoutWidget = QtWidgets.QWidget(DataControl)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 100, 443, 271))
        self.formLayoutWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.formLayoutWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(33)
        self.formLayout.setVerticalSpacing(41)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.DataBaseName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.DataBaseName.setSizeIncrement(QtCore.QSize(0, 0))
        self.DataBaseName.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DataBaseName.setFont(font)
        self.DataBaseName.setObjectName("DataBaseName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DataBaseName)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.UserName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.UserName.setSizeIncrement(QtCore.QSize(0, 0))
        self.UserName.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserName.setFont(font)
        self.UserName.setObjectName("UserName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.UserName)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.PassWord = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.PassWord.setSizeIncrement(QtCore.QSize(0, 0))
        self.PassWord.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PassWord.setFont(font)
        self.PassWord.setObjectName("PassWord")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PassWord)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.TableName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.TableName.setSizeIncrement(QtCore.QSize(0, 0))
        self.TableName.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TableName.setFont(font)
        self.TableName.setObjectName("TableName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.TableName)
        self.titleConnect = QtWidgets.QLabel(DataControl)
        self.titleConnect.setGeometry(QtCore.QRect(210, 20, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleConnect.setFont(font)
        self.titleConnect.setObjectName("titleConnect")
        self.savingButton = QtWidgets.QPushButton(DataControl)
        self.savingButton.setGeometry(QtCore.QRect(190, 440, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.savingButton.setFont(font)
        self.savingButton.setObjectName("savingButton")
        self.label_4 = QtWidgets.QLabel(DataControl)
        self.label_4.setGeometry(QtCore.QRect(270, 380, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(DataControl)
        # self.savingButton.clicked.connect(DataControl.Saving)
        QtCore.QMetaObject.connectSlotsByName(DataControl)

    def retranslateUi(self, DataControl):
        _translate = QtCore.QCoreApplication.translate
        DataControl.setWindowTitle(_translate("DataControl", "Form"))
        self.label.setText(_translate("DataControl", "数据库名称"))
        self.DataBaseName.setText(_translate("DataControl", "design"))
        self.label_2.setText(_translate("DataControl", "用户名"))
        self.UserName.setText(_translate("DataControl", "root"))
        self.label_3.setText(_translate("DataControl", "密码"))
        self.PassWord.setText(_translate("DataControl", "123456"))
        self.label_5.setText(_translate("DataControl", "表名"))
        self.TableName.setText(_translate("DataControl", "result"))
        self.titleConnect.setText(_translate("DataControl", "数据库连接设置"))
        self.savingButton.setText(_translate("DataControl", "存储"))
        self.label_4.setText(_translate("DataControl", "创建或补充"))
