from selenium import webdriver
def browserGet(item,Options):
    Select={0:f"dbcode=SCDB&kw={item}&korder=AU",1:f"dbcode=SCDB&kw={item}&korder=SU"}
    
    url1=Select[Options]
    browser=webdriver.Chrome()
    browser.get("https://kns.cnki.net/kns8/defaultresult/index?"+url1)
    


    # f=input()

# browserGet("艾伦",0)