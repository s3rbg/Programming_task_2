# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:14:24 2022

@author: Sergio
"""
import numpy as np
import pandas as pd


df = pd.read_pickle('attrition_available_5.pkl')

# print(df.dtypes)

df_copy = df.copy()



# print(np.where(x==True))
for i in df.keys():
    if df[i].dtype == object:
        l = list(df[i].unique())
        if len(l) == 1:
            df = df.drop(i, axis=1)
        else:
            val = np.linspace(0, len(l)-1, len(l))
            df[i].replace(l, val, inplace=True)
            
x = df.isnull().to_numpy()
a = np.where(x==True)