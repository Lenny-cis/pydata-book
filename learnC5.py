# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:19:33 2018

@author: Lenny
"""
from pandas import Series,DataFrame
import numpy as np
import pandas as pd

obj=Series([4,7,-5,3])
obj
obj.values
obj.index

obj2=Series([4,7,-5,3],index=['d','b','a','c'])
obj2.values
obj2.index

obj2['a']
obj2['d']=6
obj2
obj2[['c','a','d']]

obj2[obj2>0]
obj2*2
np.exp(obj2)
obj2

'b' in obj2
'e' in obj2

sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=Series(sdata)
obj3

states=['California','Ohio','Oregon','Texas']
obj4=Series(sdata,index=states)
obj4

pd.isnull(obj4)
pd.notnull(obj4)

obj4.isnull()

obj3
obj4
obj3+obj4

obj4.name='population'
obj4.index.anme='state'
obj4
obj4.index=['Bob','Steve','Jeff','Ryan']
obj4

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
frame
DataFrame(data,columns=['year','state','pop'])

frame2=DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
frame2
frame.columns

frame2['state']
frame2.year
frame2.ix['three']
frame2['debt']=16.5
frame2
frame2.debt=10
frame2
frame2.debt=np.arange(5.)
frame2
val=Series([-1.2,-1.5,-1.7],index=['two','three','five'])
frame2.debt=val
frame2

frame2['eastern']=frame2.state=='Ohio'
frame2

del frame2['eastern']
frame2.columns
pop={'Nevada':{2001:2.4,2002:2.9},"Ohio":{2000:1.5,2001:1.7,2002:3.6}}
pop
frame3=DataFrame(pop)
frame3
frame3.T
DataFrame(pop,index=[2001,2002,2003])

frame3.index.name='year'
frame3.columns.name='state'
frame3.values
frame2.values