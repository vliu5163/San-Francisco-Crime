                                                                     
__version__ = '0.2'
__author__ = 'Vivian Liu'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas imports the CSV as a Data Frame object
sfcrime = pd.read_csv("../data/SF-police-data-2016.csv")


sfc_districts = sfcrime.groupby('PdDistrict').aggregate('count')
#print(sfc_districts['Category'])

crime_daydist = pd.crosstab(index=sfcrime["DayOfWeek"],
                            columns=sfcrime["PdDistrict"])
#print(crime_daydist)

crime_catdist = pd.crosstab(index=sfcrime["Category"],
                            columns=sfcrime["PdDistrict"])
#print(crime_catdist)

crime_distcat = pd.crosstab(index=sfcrime["PdDistrict"],
                            columns=sfcrime["Category"])

print(crime_distcat)

crime_distcat_stats = crime_distcat.describe()
#print(crime_distcat.describe())
#print("Arson max= " + str(crime_distcat_stats['ARSON']['max']))

def findmaxdistrict(row):
    """ Returns the name of the District that has the maximum number 
        for the crime this row represents.
    """
    district = { 0 : "BAYVIEW",
    			 1 : "CENTRAL",
    			 2 : "INGLESIDE",
    			 3 : "MISSION",
    			 4 : "NORTHERN",
    			 5 : "PARK",
    			 6 : "RICHMOND",
    			 7 : "SOUTHERN",
    			 8 : "TARAVAL",
    			 9 : "TENDERLOIN" }
    #print("row=")
    #print(row)
    for index in range(len(row)):
    	#print("index= " + str(index) + " row[index]= " + str(row[index]) + " max(row)= " + str(max(row)))
    	if row[index] == max(row):
    		return district[index]
    return "none"
 
crime_catdist["Favorite"] = crime_catdist.apply(findmaxdistrict, axis=1)
#print(crime_catdist)

sfdistricts = pd.read_csv("../data/SF_Police_Districts.csv", index_col='PdDistrict')

#sfdistricts.info()

#print(sfdistricts)

crime_distcat['Total'] = crime_distcat.apply(sum, axis=1)
#print(crime_distcat)

sfcrime_districts = pd.concat( [crime_distcat, sfdistricts], axis=1)

#sfcrime_districts.info()

#print(sfcrime_districts[0:1])

sfcrime_districts['per_capita']=sfcrime_districts['Total']/sfcrime_districts['Population']
sfcrime_districts['per_area']=sfcrime_districts['Total']/sfcrime_districts['Land Mass']

print(sfcrime_districts['per_capita'])
print(sfcrime_districts['per_area'])

sfcrime_districts.plot(kind='scatter', y='Total', x='Schools')
plt.show()

# What if we want the data for only one district?
# tenderloin = sfcrime[sfcrime["PdDistrict"] == 'TENDERLOIN']
# # print(tenderloin[:5])

# tender_catday = pd.crosstab(index=sfcrime["DayOfWeek"],
#                             columns=sfcrime["Category"])
# print(tender_catday)

sfcrime[ sfcrime['Descript'].str.contains("DEATH") ]['Descript'].value_counts()

crime_catres = pd.crosstab(index=sfcrime["Category"],
                            columns=sfcrime["Resolution"])

#print(crime_catres)

plt.close('all')
