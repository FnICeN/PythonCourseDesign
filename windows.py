from DataManager import Manager
from Main import Ui_Main
from Getting import Ui_Getting
from DataControl import Ui_DataControl
from DataView import Ui_DataView

import test
import sele
import database

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


All_basename=0
All_user=0
All_password=0
All_table=0
All_Is_Option=False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Main()
        self.ui.setupUi(self)
        self.ui.search_Botton.clicked.connect(self.sele)
    def goToDataPage(self):
        form4.show()
        form4.reading()
    def goToGettingPage(self):
        if not self.ui.inputLine.text():
            QMessageBox.information(self,"error","请输入要爬取的内容！",QMessageBox.Ok)
        else:
            form2.show()
    def sele(self):
        Option=self.ui.comboBox.currentIndex()
        item=self.ui.inputLine.text()
        sele.browserGet(item,Option)

class GettingWindow(QWidget):
    startPage=0
    endPage=0
    getMethod=-1
    searchItem=''
    def __init__(self):
        super().__init__()
        self.ui=Ui_Getting()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.Start)

    def Start(self):
        GettingWindow.startPage=self.ui.page_Start.value()
        GettingWindow.endPage=self.ui.page_End.value()
        GettingWindow.getMethod=form1.ui.comboBox.currentIndex()
        GettingWindow.searchItem=form1.ui.inputLine.text()
        if GettingWindow.startPage>GettingWindow.endPage:
            QMessageBox.critical(self,"error","请正确设置起始和终止页数！",QMessageBox.Ok)
            return

        df=pd.DataFrame()
        if self.ui.storeMethod.currentIndex()==1:
                df=pd.DataFrame()
                df,bool=GettingWindow.GettingPages(self,self,GettingWindow.startPage,GettingWindow.endPage,GettingWindow.searchItem,GettingWindow.getMethod)
                bool=database.toDatabase(self,All_basename,All_user,All_password,All_table,df)
                if bool:
                    QMessageBox.information(self,"成功","已将爬取的数据保存！",QMessageBox.Ok)
                    return
                else:
                    QMessageBox.critical(self,"失败","保存失败",QMessageBox.Ok)
                    return
        else:
            df,bool=self.GettingPages(self,GettingWindow.startPage,GettingWindow.endPage,GettingWindow.searchItem,GettingWindow.getMethod)
            if bool:
                saveOrNot=QMessageBox.question(self,"爬取成功","已经成功爬取" + str((GettingWindow.endPage-GettingWindow.startPage+1)*20) + "条数据！是否将其存储？",QMessageBox.Save|QMessageBox.Cancel,QMessageBox.Save)
                if saveOrNot==QMessageBox.Save:
                    self.saveToCsv(self,df)
    
    def GettingPages(self,parent:QWidget,start,end,searchItem,getMethod):
        # print(start,end,getMethod,searchItem)
        df=pd.DataFrame()
        try:
            for i in range(start,end+1):
                df=pd.concat([df,test.getOnePage(getMethod,searchItem,i)],ignore_index=True)
        except:
            QMessageBox.critical(parent,"error","失败！请检查爬取选项",QMessageBox.Ok)
            return df,False
        return df,True
            

    def saveToCsv(self,parent:QWidget,df:pd.DataFrame):
        try:
            df.to_csv('result.csv',index=False,encoding='utf_8_sig')
        except:
            QMessageBox.critical(parent,"失败","保存失败",QMessageBox.Ok)
            return
        QMessageBox.information(parent,"成功","保存成功！",QMessageBox.Ok)
        parent.close()


class DataOptionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_DataControl()
        self.ui.setupUi(self)
        self.ui.savingButton.clicked.connect(self.Saving)
    def Saving(self):
        global All_basename,All_user,All_password,All_table,All_Is_Option
        basename=self.ui.DataBaseName.text()
        user=self.ui.UserName.text()
        password=self.ui.PassWord.text()
        table=self.ui.TableName.text()
        pack=(basename,user,password,table)
        if '' in pack:
            QMessageBox.information(self,"Caution","请填写完整数据",QMessageBox.Ok)
            return
        else:
            All_basename,All_user,All_password,All_table=pack
            All_Is_Option=True
            self.close()
            return
            

class DataViewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_DataView()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.controlPage)
    
    def reading(self):
        if All_Is_Option:
            df,bool=database.readDatabase(self,All_basename,All_user,All_password,All_table)
        else:
            return
        if not bool:
            database.throwErrors(self,0)
            self.close()
        self.display_dynamic_form(df,self.ui.databaseWidget)


    def controlPage(self):
        form5.show()

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


class ManagerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Manager()
        self.ui.setupUi(self)
        self.ui.Search.clicked.connect(self.Search)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.Delete.clicked.connect(self.Delete)
        self.ui.revise.clicked.connect(self.revise)
    def Search(self):
        df=pd.DataFrame()
        q=self.buildWhereQuery(self.getContents())
        query=f"select * from {All_table} where {q}"
        df,bool=database.searchDataBase(self,All_basename,All_user,All_password,query)
        if not bool:
            return
        DataViewWindow.display_dynamic_form(self,df,self.ui.searchResult)
    def Add(self):
        contents=self.getContents()
        if '' in contents:
            database.throwErrors(self,5)
            return
        title,author,source,date,use,download=contents
        dic={'标题':[title],'作者':[author],'来源':[source],'日期':[date],'被引数':[use],'下载数':[download]}
        df=pd.DataFrame(dic)
        # query=f"insert into test values('{title}','{author}','{source}','{date}','{use}','{download}')"
        bool=database.toDatabase(self,All_basename,All_user,All_password,All_table,df)
        if not bool:
            return
        else:
            QMessageBox.information(self,"成功","成功添加数据！",QMessageBox.Ok)
    def Delete(self):
        q=self.buildWhereQuery(self.getContents())
        delOrNot=QMessageBox.question(self,"警告","确定要删除吗？" ,QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if delOrNot==QMessageBox.Yes:
            query=f"delete from {All_table} where {q}"
            print(query)
            bool=database.runSQL(self,All_basename,All_user,All_password,query)
            if not bool:
                return
            else:
                QMessageBox.information(self,"成功","成功删除数据！",QMessageBox.Ok)
    def revise(self):
        if All_Is_Option:
            df,bool=database.readDatabase(self,All_basename,All_user,All_password,All_table)
        else:
            return
        if not bool:
            database.throwErrors(self,0)
            self.close()
        DataViewWindow.display_dynamic_form(self,df,self.ui.searchResult)


    def buildWhereQuery(self,contents:tuple):
        title,author,source,date,use,download=contents
        query=f"{self.buildPartQuery('标题',title)}and{self.buildPartQuery('作者',author)}and{self.buildPartQuery('来源',source)}and{self.buildPartQuery('日期',date,False)}and{self.buildPartQuery('被引数',use,False)}and{self.buildPartQuery('下载数',download,False)}"
        query=query.split("and")
        while '' in query:
            query.remove('')
        query=" and ".join(query)
        return query


    def buildPartQuery(self,type:str,content:str,isLike:bool=True):
        if content=='':
            return ''
        if isLike:
            queryStr=f"{type} like '%{content}%'"
        else:
            queryStr=f"{type} = '{content}'"
        return queryStr
    def getContents(self):
        pack=[]
        pack.append(self.ui.Title.text())
        pack.append(self.ui.Author.text())
        pack.append(self.ui.Source.text())
        pack.append(self.ui.Date.text())
        pack.append(self.ui.Use.text())
        pack.append(self.ui.Download.text())
        pack=tuple(pack)
        return pack


app=QApplication([])
form1=MainWindow()
form2=GettingWindow()
form3=DataOptionWindow()
form4=DataViewWindow()
form5=ManagerWindow()

form1.show()
form3.show()

app.exec_()