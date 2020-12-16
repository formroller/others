import os
os.getcwd()
os.chdir('./.spyder-py3/others')

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

chromedriver = ('./chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&publicDataPks=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=40&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=')


element = driver.find_elements_by_css_selector(' dl > dt > a > span.title')


title = []
for e in element:
    title.append(e.text)
