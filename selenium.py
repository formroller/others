import os
os.getcwd()
os.chdir('./.spyder-py3/others')

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import time
import numpy as np

    
# =============================================================================
# next page
# =============================================================================
chromedriver = ('./chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&publicDataPks=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={}&perPage=40&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=')


for n in range(1, 50):
    driver.get(f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&publicDataPks=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={n}&perPage=40&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=')
    time.sleep(1)
    
    title = driver.find_elements_by_css_selector(' dl > dt > a > span.title')
    date = driver.find_elements_by_css_selector(' span.data')
    category = driver.find_elements_by_css_selector('p > span.labelset.red')
    
    # 제목
    titles = []
    for t in title:
        titles.append(t.text)
        
    # 날짜    
    dates=[]
    for d in date:
        dates.append(d.text)     
        p = re.compile(r'\d+[-]\d+[-]\d+')
        dates = p.findall(str(dates))
        
    # 제공기관
    categorise = []
    for c in category:
        categorise.append(c.text)    
        
    print(titles, dates, categorise)
    

    
    



    
