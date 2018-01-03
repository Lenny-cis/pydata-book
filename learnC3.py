# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:55:18 2017

@author: Lenny
"""

import numpy as np
data={i:np.random.randn() for i in range(7)}
#data
#print(data)
b=[1,2,3]
#b?
def add_numbers(a,b):
    """
    Add two numbers together
    Returns
    -------
    the_sum: type of arguments
    """
    return a+b
#add_numbers?
#add_numbers??
#np.*load*?
#%run learnC2.py
#letter_prop
a=np.random.randn(100,100)
%timeit np.dot(a,a)
#%reset?
#%reset
#%quickref
#%whos
#2+1
#_
foo='bar'
#foo
#_35
#%cd D:\Python_test\pydata-book
#%cmd xcopy D:\Python_test\pydata-book\requirements.txt D:\Python_test
strings=['foo','foobar','baz','qux','python','Guido Van Rossum']*100000
%timeit method1=[x for x in strings if x.startswith('foo')]
%timeit method2=[x for x in strings if x[:3]=='foo']
x='foobar'
y='foo'
%timeit x.startswith(y)
%timeit x[:3]==y
import numpy as np
from numpy.linalg import eigvals
def run_experiment(niter=100):
    K=100
    results=[]
    for _ in range(niter):
        mat=np.random.randn(K,K)
        max_eigenvalue=np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
som_results=run_experiment()
#print('Largest one we saw: %s' % np.max(som_results))
#%prun -l 10 -s cumulative run_experiment()
%load_ext line_profiler
import sys
print(sys.path)