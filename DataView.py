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


class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_DataView()
        self.ui.setupUi(self)
        df,bool=database.readDatabase(self,"design","root","123456","ccc")
        self.display_dynamic_form(df,self.ui.databaseWidget)
        self.ui.pushButton.clicked.connect(self.controlPage)

    def controlPage(self):
        pass

    def display_dynamic_form(self, df, target_obj):

        # horizontalHeader().setVisible
        # .verticalHeader().setVisible
        input_table_rows = df.shape[0]
        input_table_colunms = df.shape[1]
        input_table_header = df.columns.values.tolist()
        target_obj.setColumnCount(input_table_colunms)
        target_obj.setRowCount(input_table_rows)
        target_obj.setHorizontalHeaderLabels(input_table_header)
        # print(input_table_header)
        for i in range(input_table_rows):
            for j in range(input_table_colunms):
                new_item = QTableWidgetItem(str(df.iat[i, j]))
                target_obj.setItem(i, j, new_item)


# app=QApplication([])
# form=Display()
# form.show()
# app.exec_()