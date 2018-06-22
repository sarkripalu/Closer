# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:42:45 2018

@author: Closer
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


data = pd.read_excel('C:\\Users\\Closer\\Desktop\\Closer\\Imp_Doc\\A2Z_Insurance.xlsx', delimiter=',' )

df1 = data[['Customer Identity', 'First Policy´s Year', 'Customer Age',
       'Gross Monthly Salary', 'Geographic Living Area',
       'Has Children (Y=1)', 'Customer Monetary Value', 'Claims Rate',
       'Premiums in LOB: Motor', 'Premiums in LOB: Household',
       'Premiums in LOB: Health', 'Premiums in LOB:  Life',
       'Premiums in LOB: Work Compensations']]


df_rename =df1.rename(columns = {'Customer Identity':'Customer_Identity' , 
                           'First Policy´s Year':'First_Policy_Year',
                           'Customer Age':'Customer_Age',
                           'Gross Monthly Salary': 'Gross_Monthly_Salary',
                           'Geographic Living Area':'Geographic_Living_Area',
                           'Has Children (Y=1)': 'Has_Children', 
                           'Customer Monetary Value':'Customer_Monetary_Value',
                           'Claims Rate':'Claims_Rate',
                           'Premiums in LOB: Motor':'Premiums_Motor', 
                           'Premiums in LOB: Household':'Premiums_Household',
                           'Premiums in LOB: Health':'Premiums_Health',
                           'Premiums in LOB:  Life':'Premiums_Life',
                           'Premiums in LOB: Work Compensations':'Premiums_Work_Compensations'})

df_Id_Index = df_rename.set_index('Customer_Identity')
df2= df_Id_Index.fillna(method= 'ffill') #Interpolate the values
df2.isnull().any()


columns =  df2.iloc[:,[3]]
for col in columns:
    df2[col] = df2[col].apply(int)
df2;


# Two column can be added with '+'
df2['Total_Premium'] =  df2.iloc[:,7]+df2.iloc[:,8] + df2.iloc[:,9] + df2.iloc[:,10]+ df2.iloc[:,11];


Demo_Data = df2[['Total_Premium','Customer_Monetary_Value'] ]


# Separating out the Demographic Data.

x = Demo_Data.values

# Separating out the Target as regions. 
y = df2.loc[:,['Customer_Age']].values

# Standardizing the features
scaler = StandardScaler()
x = scaler.fit_transform(x)

pca = PCA(n_components=2)
Demography_Data = pca.fit_transform(x)
principalDf = pd.DataFrame(data = Demography_Data
             , columns = ['Demography_Data 1', 'Demography_Data 2'])

finalDf = pd.concat([principalDf, df2[['Customer_Age']]], axis = 1)
finalDf.head()