# -*- coding: utf-8 -*-
"""movement-pattern-in-covid-19-EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v0z6fViI-yL2r3Q_AlrfleFt1PGInzOl
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive 
drive.mount("/gdrive")
# %cd /gdrive

ls

cd/gdrive/My Drive/Movement-Pattern-COVID

ls

import numpy as np 
import pandas as pd

move_data = pd.read_csv("changes-visitors-covid.csv")

move_data.head()

move_data.describe()

move_data.tail()

move_data.iloc[2,3]

move_data.iloc[-3,3]

move_data.Date.dtype

renamed_data = move_data.rename(columns={'Retail & Recreation (%)':'Retail_and_Recreation','Grocery & Pharmacy Stores (%)':'Grocery_and_Pharmacy Stores'})

renamed_data

renamed_data = move_data.rename(columns={'Retail & Recreation (%)':'Retail_and_Recreation','Grocery & Pharmacy Stores (%)':'Grocery_and_Pharmacy_Stores','Residential (%)':'Residential','Transit Stations (%)':'Transit_Stations','Parks (%)':'Parks','Workplaces (%)':'Workplaces'})

renamed_data

renamed_data.Transit_Stations.dtype

renamed_data.Grocery_and_Pharmacy_Stores.dtype

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(20,20))
plt.title("Changes in the movement pattern of visitors in workplaces from February 2020 in workplaces of various countries")
sns.lineplot(x = renamed_data.Date,y=renamed_data.Workplaces,hue = renamed_data.Code)
plt.xlabel("Date from February 2020")
plt.ylabel("Visitors in workplaces in percentage")

plt.figure(figsize=(20,20))
plt.title("Changes in the movement pattern of visitors in workplaces from February 2020 in Bangladesh")
sns.lineplot(x = renamed_data.Date,y=renamed_data.Workplaces.iloc[1162:1291])
plt.xlabel("Date from February 2020")
plt.ylabel("Visitors in workplaces in percentage")

plt.figure(figsize=(30,50))
plt.title("Changes in the movement pattern of visitors in workplaces from February 2020 in workplaces of various countries")
sns.barplot(x = renamed_data.Date,y=renamed_data.Workplaces,hue = renamed_data.Code)
plt.xlabel("Date from February 2020")
plt.ylabel("Visitors in workplaces in percentage")

plt.figure(figsize=(14,7))
plt.title("Changes in the movement pattern of visitors in their own residence from February 2020 in workplaces of various countries")
sns.barplot(x = renamed_data.Date,y=renamed_data.Residential)
plt.xlabel("Date from February 2020 to June 2020")
plt.ylabel("Visitors in their own residence in percentage")

plt.figure(figsize=(14,7))
plt.title("Changes in the movement pattern of visitors in Parks from February 2020 in workplaces of various countries")
sns.scatterplot(x = renamed_data.Date,y=renamed_data.Parks)
plt.xlabel("Date from February 2020 to June 2020")
plt.ylabel("Visitors in parks in percentage")

plt.figure(figsize=(14,7))
plt.title("Relationship between Number of people in their own residence and workplaces")
sns.regplot(x = renamed_data.Residential,y=renamed_data.Workplaces)
plt.xlabel("Number of people in their residence in percentage")
plt.ylabel("Visitors in Workplaces in percentage")

plt.figure(figsize=(14,7))
plt.title("Relationship between Number of people in their own residence and workplaces")
sns.swarmplot(x = renamed_data.Grocery_and_Pharmacy_Stores,y=renamed_data.Retail_and_Recreation)
plt.xlabel("Number of people in Grocery and Pharmacy stores in percentage")
plt.ylabel("Visitors in Retail and Recreation in percentage")

plt.figure(figsize=(14,7))
plt.title("Relationship between Number of people in Grocery and Pharmacy and in Retail and Recreation")
sns.regplot(x = renamed_data.Grocery_and_Pharmacy_Stores,y=renamed_data.Retail_and_Recreation)
plt.xlabel("Number of people in Grocery and Pharmacy stores in percentage")
plt.ylabel("Visitors in Retail and Recreation in percentage")

plt.figure(figsize=(14,10))
plt.title("Changes in the percentage of visitors in Retail and Recreation")
sns.barplot(x = renamed_data.Date,y=renamed_data.Retail_and_Recreation)
plt.xlabel("Date from February 2020 to June 2020")
plt.ylabel("Visitors in Retail and Recreation in percentage")

plt.figure(figsize=(14,10))
plt.title("Relationship between Number of people in Grocery and Pharmacy Stores")
sns.barplot(x = renamed_data.Date,y=renamed_data.Grocery_and_Pharmacy_Stores)
plt.xlabel("Date from February 2020 to June 2020")
plt.ylabel("Visitors in Grocery and Pharmacy Stores in percentage")

plt.figure(figsize=(14,10))
plt.title("Relationship between Number of people in Grocery and Pharmacy Stores")
sns.lineplot(x = renamed_data.Date,y=renamed_data.Grocery_and_Pharmacy_Stores)
plt.xlabel("Date from February 2020 to June 2020")
plt.ylabel("Visitors in Grocery and Pharmacy Stores in percentage")

