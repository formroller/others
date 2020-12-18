import os

import pandas as pd
import numpy as np

import seaborn as sns

import re
import csv
os.chdir('./medical')
Public = pd.read_csv('./medical/PublicData.csv', encoding='cp949')

Public.columns = ['data','names','provide','date','form']
Public.head()

## 첫 요소 추출
Public['names'] = [i.replace('_',' ') for i in Public['names']]
Public['loc'] = [i.split(' ')[0] for i in name_one]

print(Public['loc'])

## 도시군구읍면동 추출
Public['loc']
Public['loc'] = Public['loc'].str.replace('[한국].+','')
Public['loc'] = Public['loc'].str.replace('[보훈].+','')
Public['loc'] = Public['loc'].str.replace('[보건].+','')
Public['loc'] = Public['loc'].str.replace('[병].+','')
Public['loc'] = Public['loc'].str.replace('[질병].+','')
Public['loc'] = Public['loc'].str.replace('[근].+','')


Public['loc_sort'] = Public['loc'].value_counts(ascending=False)

Public.to_csv('./Public2.csv', encoding='cp949')
