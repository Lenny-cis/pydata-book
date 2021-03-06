# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:06:46 2018

@author: Lenny
"""

#learnC6
import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import csv
import json
import pyodbc

!type .\\examples\\ex1.csv
df=pd.read_csv('examples\\ex1.csv')
pd.read_table('examples\\ex1.csv',sep=',')

!type .\\examples\\ex2.csv
pd.read_csv('examples\\ex2.csv',header=None)
pd.read_csv('examples\\ex2.csv',names=['a','b','c','d','message'])
pd.read_csv('examples\\ex2.csv',names=['a','b','c','d','message'],index_col='message')

!type .\\examples\\csv_mindex.csv
parsed=pd.read_csv('examples\\csv_mindex.csv',index_col=['key1','key2'])
parsed

!type .\\examples\\ex3.txt
list(open('examples\\ex3.txt'))
result=pd.read_table('examples\\ex3.txt',sep='\s+')
result

!type .\\examples\\ex4.csv
pd.read_csv('examples\\ex4.csv',skiprows=[0,2,3])

!type .\\examples\\ex5.csv
result=pd.read_csv('examples\\ex5.csv')
result
pd.isnull(result)
result=pd.read_csv('examples\\ex5.csv',na_values=['NULL'])
result

sentinels={'message':['foo','NA'],'something':['two']}
pd.read_csv('examples\\ex5.csv',na_values=sentinels)

result=pd.read_csv('examples\\ex6.csv')
result
pd.read_csv('examples\\ex6.csv',nrows=5)
chunker=pd.read_csv('examples\\ex6.csv',chunksize=1000)
chunker
tot=Series([])
for piece in chunker:
    tot=tot.add(piece['key'].value_counts(),fill_value=0)
tot=tot.sort_values(ascending=False)
tot[:10]

data=pd.read_csv('examples\\ex5.csv')
data
data.to_csv('examples\\out.csv')
!type .\\examples\\out.csv
!del .\\examples\\out.csv
data.to_csv(sys.stdout,sep='|')
data.to_csv(sys.stdout,na_rep='NULL')
data.to_csv(sys.stdout,index=False,header=False)
data.to_csv(sys.stdout,index=False,columns=['a','b','c'])

!type .\\examples\\ex7.csv
f=open('examples\\ex7.csv')
reader=csv.reader(f)
for line in reader:
    print(line)
lines=list(csv.reader(open('examples\\ex7.csv')))
header,values=lines[0],lines[1:]
data_dict={h:v for h,v in zip(header,zip(*values))}
data_dict

class my_dialect(csv.Dialect):
    lineterminator='\n'
    delimiter=';'
    quotechar='"'
    quoting=csv.QUOTE_MINIMAL
f=open('examples\\ex7.csv')
reader=csv.reader(f,dialect=my_dialect)
for line in reader:
    print(line)

obj="""
{"name":"Wes",
 "places_lived":["United States","Spain","Germany"],
 "pet":null,
 "siblings":[{"name":"Scott","age":25,"pet":"Zuko"},
             {"name":"Katie","age":33,"pet":"Cisco"}]
}
"""
result=json.loads(obj)
result
asjson=json.dumps(result)
asjson

siblings=DataFrame(result['siblings'],columns=['name','age'])
siblings

from lxml import objectify
path='datasets\\mta_perf\\Performance_MNR.xml'
parsed=objectify.parse(open(path))
root=parsed.getroot()
data=[]
skip_fields=['PARENT_SEQ','INDICATOR_SEQ','DESIRED_CHANGE','DECIMAL_PLACES']
for elt in root.INDICATOR:
    el_data={}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag]=child.pyval
    data.append(el_data)
perf=DataFrame(data)
perf

frame=pd.read_csv('examples\\ex1.csv')
frame

frame.to_pickle('examples\\frame_pickle')
pd.read_pickle('examples\\frame_pickle')
!del .\\examples\\frame_pickle

conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=137.168.99.113;DATABASE=crm;UID=ljn;PWD=p@ssw0rd')
cursor = conn.cursor()
sql="select * from institution"
df = pd.read_sql(sql,conn,)
aa=pd.DataFrame(df)
aa[:1]
aa.to_csv('examples\\aa.csv')
!del .\\examples\\aa.csv
cursor.close()
conn.close()
