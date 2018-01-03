# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:59:15 2017

@author: Lenny
"""
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
print('Largest one we saw: %s' % np.max(som_results))