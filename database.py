from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import *
import pandas as pd
from sqlalchemy import create_engine

def toDatabase(parent:QWidget,databaseName:str,userName:str,passWord:str,tableName:str,df:pd.DataFrame):
    try:
        engine = create_engine(f"mysql+pymysql://{userName}:{passWord}@localhost/{databaseName}",encoding='utf8')
        df.to_sql(tableName, engine, index=False,if_exists='append')
        return True
    except:
        throwErrors(parent,4)
        return False
    
def runSQL(parent:QWidget,databaseName:str,userName:str,passWord:str,sql:str):
    try:
        engine=create_engine(f"mysql+pymysql://{userName}:{passWord}@localhost/{databaseName}",encoding='utf8')
        conn=engine.connect()
        conn.execute(sql)
    except:
        throwErrors(parent,4)
        return False
    return True

def searchDataBase(parent:QWidget,databaseName:str,userName:str,passWord:str,sql:str):
    df=pd.DataFrame()
    try:
        engine=create_engine(f"mysql+pymysql://{userName}:{passWord}@localhost/{databaseName}",encoding='utf8')
        df=pd.read_sql(sql,engine)
    except:
        throwErrors(parent,4)
        return df,False
    return df,True

def readDatabase(parent:QWidget,databaseName:str,userName:str,passWord:str,tableName:str):
    df=pd.DataFrame()
    try:
        engine=create_engine(f"mysql+pymysql://{userName}:{passWord}@localhost/{databaseName}",encoding='utf8')
        sql=f"select * from {tableName}"
        df=pd.read_sql(sql,engine)
    except:
        throwErrors(parent,4)
        return df,False
    
    return df,True

def throwErrors(parent:QWidget,flag:int):
    errorDict={0:"数据库连接失败！检查ODBC配置和用户名与密码",
                1:"找不到已有的表！将会在默认数据库下新建...",
                2:"创建新表失败！",
                4:"数据库操作失败，确认engine连接",
                5:"请输入全部信息以插入！"}
    QMessageBox.critical(parent,"Error",errorDict[flag],QMessageBox.Ok)
    # print(errorDict[flag])


