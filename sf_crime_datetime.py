""" This module shows some useful tricks with the datetime object and the sf crime dataset.
"""
__version__ = '0.1'
__author__ = 'Vivian Liu'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sfcrime = pd.read_csv("../data/SF-police-data-2016.csv", parse_dates=['Date'], index_col='Date')

sfcrime['weekday'] = sfcrime.index.weekday
#print(sfcrime['weekday'][0:5])

sfc_weekdays = sfcrime.groupby('weekday').aggregate('count')
sfc_weekdays.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sfc_weekdays.plot(kind='bar', y='Category')
plt.title("Most popular weekday for Crime in SF - 2016")
plt.show()

sfcrime['month'] = sfcrime.index.month
sfc_months = sfcrime.groupby('month').aggregate('count')
sfc_months.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December']
print(sfc_months['Category'][0:5])
sfc_months.plot(kind='bar', y='Category')
plt.title("Most popular month for Crime in SF - 2016")
plt.show()

arson = sfcrime[ sfcrime['Category'] == 'ARSON' ]
arson_months = arson.groupby('month').aggregate('count')
arson_months.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December']
arson_months.plot(kind='bar', y='Category')
plt.title("Most popular month for Arson in SF - 2016")
plt.show()

