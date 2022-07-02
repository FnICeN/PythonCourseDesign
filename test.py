import requests
from urllib import parse
from lxml import html
import pandas as pd

headers={'Host':'kns.cnki.net',
'Connection':'keep-alive',
'Content-Length':'770',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
'Accept':'text/html, */*; q=0.01',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With':'XMLHttpRequest',
'sec-ch-ua-mobile':'?0',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'sec-ch-ua-platform':'"Windows"',
'Origin':'https://kns.cnki.net',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://kns.cnki.net/kns8/defaultresult/index',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'Ecp_ClientId=7211124224501223118; Ecp_loginuserbk=K10349; cnkiUserKey=8afb3c2f-e918-884f-b967-ad9b28a4f36e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d5268713e40-075435a87d4bc8-978183a-1327104-17d5268713f7d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d5268713e40-075435a87d4bc8-978183a-1327104-17d5268713f7d%22%7D; Ecp_loginuserjf=15991277627; knsLeftGroupSelectItem=1%3B2%3B; Ecp_ClientIp=219.144.235.53; Ecp_Userid=1089517534; cnkiUserKey=d60c6fe6-ba08-b0e6-0993-2199710c7a25; dsorder=cite; RsPerPage=20; UM_distinctid=1816fceacd33-033b740c9a121c-26021b51-144000-1816fceacd4bf; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1655474920,1655479057,1655526956; SID_sug=126002; _pk_ref=%5B%22%22%2C%22%22%2C1656385931%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqWZl4gYatn5WAOIF-uSx4Xf96UP9RsPmIgGWR9rF0KG%26wd%3D%26eqid%3De9b4e07d000008220000000662ba7186%22%5D; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqMDh6cEFITnRlU3J2TVNpK3RlYnE0dlJzYXNRTT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"K10349","ShowName":"%E8%A5%BF%E5%AE%89%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6%E5%9B%BE%E4%B9%A6%E9%A6%86","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"krDVMO"}; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMDh6cEFITnRlU3J2TVNpK3RlYnE0dlJzYXNRTT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=06/28/2022 11:32:11; c_m_expire=2022-06-28%2011%3A32%3A11; ASP.NET_SessionId=h4o0zmd40oo0uarhqnptpzgv; SID_kns8=25123164; dblang=ch; _pk_id=04a88e1a-fa4c-49df-b450-f5eea7c25150.1637765109.13.1656385950.1656385931.',
}

url='https://kns.cnki.net/kns8/Brief/GetGridTableHtml'






def getOnePage(getMethod,searchItem,page):
    
    dic1={"Title":"搜索方式","Name":"方式","Value":"搜索内容","Operate":"=","BlurType":""}
    dic1['Value']=searchItem
    if getMethod==0:
        dic1['Title']='作者'
        dic1['Name']='AU'
    else:
        dic1['Title']='主题'
        dic1['Name']='SU'
        dic1['Operate']="%="
    
    dic2={"Key":"Subject","Title":"","Logic":1,"Items":[dic1],"ChildItems":[]}
    dic3={"QGroup":[dic2]}
    dic4={"Platform":"","DBCode":"CFLS","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":dic3}
    dic={'IsSearch':'false',
    'QueryJson':dic4,
    'PageName': 'defaultresult', 
    'DBCode': 'CFLS', 
    'KuaKuCodes': 'CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN', 
    'CurPage': 1, 
    'RecordsCntPerPage': 20, 
    'CurDisplayMode': 'listmode', 
    'CurrSortField': 'CITY', 
    'CurrSortFieldType': 'desc',
    'IsSentenceSearch': False, 
    'Subject': ''}
    dic['CurPage']=str(page)
    dic = parse.urlencode(dic)


    req=requests.post(headers=headers,url=url,data=dic)
    # print(req.text)

    tree=html.etree
    tree = tree.HTML(req.text)

    titles=[]
    writers=[]
    sources=[]
    dates=[]
    uses=[]
    downloads=[]
    urls=[]
    for i in range(1,21):
        detailUrl="https://kns.cnki.net/kcms/detail/detail.aspx?"
        i=str(i)
        #group titles
        temptile=tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[2]/a//descendant::text()')
        tempurl=tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[2]/a/@href')
        tempurl="".join(tempurl)
        tempurl=tempurl.split("&")
        filename_url=tempurl[4][9:]
        dbname_url=tempurl[5][7:]

        titles.append("".join(temptile))

        #group authors
        tempwriter=",".join(tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[3]/a//descendant::text()'))
        if tempwriter=='':
            tempwriter=",".join(tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[3]//descendant::text()'))
            tempwriter=tempwriter.replace("\n","").replace("\r","").replace("\t","").replace(" ","")
        tempwriter=tempwriter.strip(",")
        writers.append(tempwriter)

        #group sources
        tempsource=str(tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[4]/a/text()')[0])
        sources.append(tempsource)

        #group dates
        tempdate=tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[5]/text()')
        tempdate="".join(tempdate)
        dates.append(tempdate.strip())

        #group uses
        tempuse=tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[7]/span/a/text()')
        if not tempuse:
            tempuse=['0']
        tempuse="".join(tempuse)
        uses.append(tempuse)

        #group downloads
        tempdown=tree.xpath('//*[@id="gridTable"]/table/tr['+ i +']/td[8]/a/text()')
        if not tempdown:
            tempdown=['0']
        downloads.append("".join(tempdown))

        #group urls
        detailUrl2=f"dbcode=CJFD&dbname={dbname_url}&filename={filename_url}&uniplatform=NZKPT&v=yVaiR-TqK3zCk5lBU-Dk57HxgTsFdwRkuI4MGemxETkhOnQw1U9mRM2Fv76YzAkR"
        detailUrl+=detailUrl2
        urls.append(detailUrl)

    res={'标题':titles,'作者':writers,'来源':sources,'日期':dates,'被引数':uses,'下载数':downloads,'详情页url':urls}
    df=pd.DataFrame(res)
    # for a,b,c,d,e,f in zip(titles,writers,sources,dates,uses,downloads):
    #     print(a,b,c,d,e,f)
    return df

# getOnePage(0,'航天',1)
