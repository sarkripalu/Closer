# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:56:19 2018

@author: Closer
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

data = pd.read_excel('C:\\Users\\Closer\\Desktop\\Closer\\Imp_Doc\\A2Z_Insurance.xlsx', delimiter=',')
data.head(n = 1000)
data1 = data
#data1 = data1.get_loc[(data1[ 'Has_Children (Y=1)' == 0])]
data2 = data1.loc[:,["Customer Age"]]
#lt.hist(data, bins = 10);
#plt.hist(data2, bins= 10);

sbn.set_style("whitegrid")
ax= sbn.swarmplot(x="Customer Age", y ="Gross Monthly Salary", data = data1)
