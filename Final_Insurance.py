# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:49:41 2018

@author: Closer
"""
# Packages
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import linear_model
import matplotlib.pyplot as plt


#Load the data

data = pd.read_excel('C:\\Users\\Closer\\Desktop\\Closer\\Imp_Doc\\A2Z_Insurance.xlsx', delimiter=',' )

# New Dataset

data1 = data[['Customer Identity', 'First Policy´s Year', 'Customer Age',
       'Gross Monthly Salary', 'Geographic Living Area',
       'Has Children (Y=1)', 'Customer Monetary Value', 'Claims Rate',
       'Premiums in LOB: Motor', 'Premiums in LOB: Household',
       'Premiums in LOB: Health', 'Premiums in LOB:  Life',
       'Premiums in LOB: Work Compensations']]

df1 = data[['Customer Identity', 'First Policy´s Year', 'Customer Age',
       'Gross Monthly Salary', 'Geographic Living Area',
       'Has Children (Y=1)', 'Customer Monetary Value', 'Claims Rate',
       'Premiums in LOB: Motor', 'Premiums in LOB: Household',
       'Premiums in LOB: Health', 'Premiums in LOB:  Life',
       'Premiums in LOB: Work Compensations']]

# Rename 

data2 = data1.rename(columns = {'Customer Identity':'Customer_Identity' , 
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
df_rename.columns;
df_Id_Index = df_rename.set_index('Customer_Identity')
df_fillna= df_Id_Index.fillna(method= 'ffill') #Interpolate the values
df2 = df_fillna.head(n = 10000)
df2.isnull().any()
columns =  df2.iloc[:,:5]
for col in columns:
    df2[col] = df2[col].fillna(method = 'ffill').apply(int)
    
    
df2.Customer_Age.unique()


customer_age = df2.sort_values('Customer_Age', ascending = False)
customer_age;
Gross_Monthly_Salary = df2.sort_values('Gross_Monthly_Salary', ascending = True)
Gross_Monthly_Salary;

sns.pairplot(df2, hue = 'Geographic_Living_Area',size = 4, kind = 'reg')