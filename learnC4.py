# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:30:24 2017

@author: Lenny
"""

import numpy as np

data1=[6,7.5,8,0,1]
arr1=np.array(data1)
#arr1

data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
#arr2+arr2
#arr2+arr2
#arr2
data3=data2+data2
arr3=np.array(data3)
arr3.ndim
#arr2.ndim
#arr1.ndim
#arr2.shape

#arr1.dtype
#arr2.dtype

#np.zeros(10)
#np.zeros((3,6))
#np.empty((2,3,2))

np.arange(15)

np.eye(10)

arr1=np.array([1,2,3],dtype=np.float64)
arr2=np.array([1,2,3],dtype=np.int32)
arr1.dtype
arr2.dtype

arr=np.array([1,2,3,4,5])
arr.dtype

float_arr=arr.astype(np.float64)
float_arr.dtype

arr=np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
arr.dtype
arr.astype(np.int32)
arr2=arr.astype(np.int32)
arr2

numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_strings.astype(np.float)
numeric_strings

int_array=np.arange(10)
int_array.dtype
calibers=np.array([.22,.270,.357,.380,.44,.50],dtype=np.float)
int_array.astype(calibers.dtype)

empty_uint32=np.empty(8,dtype='u4')
empty_uint32

arr=np.array([[1,2,3],[4,5,6]])
arr*arr
arr-1
arr/arr
arr**arr

arr=np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8]=12
arr
