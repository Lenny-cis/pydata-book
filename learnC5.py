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