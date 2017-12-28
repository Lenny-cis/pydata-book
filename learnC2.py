# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:35:54 2017

@author: Lenny
"""

path='datasets\\bitly_usagov\\example.txt'
import json
records=[json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in records if 'tz' in rec]
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts
from collections import defaultdict
def get_counts2(sequence):
    counts=defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts
counts=get_counts(time_zones)
counts
def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
top_counts(counts)
from collections import Counter
counts=Counter(time_zones)
counts.most_common(10)

from pandas import DataFrame,Series
import pandas as pd;import numpy as np
frame=DataFrame(records)
tz_counts=frame['tz'].value_counts()
tz_counts[:10]
clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unknown'
tz_counts=clean_tz.value_counts()
tz_counts[:10]
tz_counts[:10].plot(kind='barh',rot=0)
results=Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
cframe=frame[frame.a.notnull()]
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
operating_system[:5]
by_tz_os=cframe.groupby(['tz',operating_system])
agg_counts=by_tz_os.size().unstack().fillna(0)
indexer=agg_counts.sum(1).argsort()
count_subset=agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh',stacked=True)
normed_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('datasets\\movielens\\users.dat',sep='::',header=None,names=unames)
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('datasets\\movielens\\ratings.dat',sep='::',header=None,names=rnames)
mnames=['movie_id','title','genres']
movies=pd.read_table('datasets\\movielens\\movies.dat',sep='::',header=None,names=mnames)
data=pd.merge(pd.merge(ratings,users),movies)
data.ix[0]
mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
mean_ratings[:5]
