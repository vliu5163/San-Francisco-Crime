
__version__ = '0.1'
__author__ = 'Vivian Liu'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas imports the CSV as a Data Frame object
sfcrime = pd.read_csv("../data/SF-police-data-2016.csv")

print(sfcrime['Category'].value_counts())
print(sfcrime['Resolution'].value_counts())
print(sfcrime['PdDistrict'].value_counts())

burglary = sfcrime[ sfcrime['Category'] == 'BURGLARY' ]
narcos = sfcrime[ sfcrime['Category'] == 'DRUG/NARCOTIC' ]

def res_to_color (res):
	res_colors = { 'NONE' : 'red',
					'ARREST, BOOKED' : 'green', 
					'UNFOUNDED' : 'yellow',
					'JUVENILE BOOKED' : 'blue',
					'EXCEPTIONAL CLEARANCE' : 'black',
					'ARREST, CITED' : 'green',
					'JUVENILE CITED' : 'blue',   
					'JUVENILE DIVERTED' : 'blue' }
	if res in res_colors:
		return res_colors[res]
	else:
		return 'grey'

district_markers = { 'SOUTHERN' : "o", # circle
					'NORTHERN' : "s", # square
					'MISSION' : "d",	# triangle_down
					'CENTRAL' : "x",	# x 
					'BAYVIEW' : ">",	# triangle_right
					'INGLESIDE' : "h", #	hexagon1
					'TARAVAL' : "<",	# triangle_left
					'TENDERLOIN' : "+", # point
					'RICHMOND' : "p", # pentagon
					'PARK' : "*", # star
					}
def dist_to_marker (district):
	return district_markers[district]

""" Other Marker Codes:
"^", # triangle_up
"1"	tri_down
"2"	tri_up
"3"	tri_left
"4"	tri_right
"P"	plus (filled)

"H"	hexagon2
"+"	plus
"X"	x (filled)
"D"	diamond
"d", # thin_diamond


"""

for district in district_markers:
	plt.scatter(x=burglary[ burglary['PdDistrict'] == district ]['X'],
	            y=burglary[ burglary['PdDistrict'] == district ]['Y'],
	            c=burglary['Resolution'].apply(res_to_color),
	            marker=district_markers[district])
plt.title("Burglary Incidents by Resolution and Location in SF for 2016")
plt.show()

for district in district_markers:
	plt.scatter(x=narcos[ narcos['PdDistrict'] == district ]['X'],
	            y=narcos[ narcos['PdDistrict'] == district ]['Y'],
	            c=narcos['Resolution'].apply(res_to_color),
	            marker=district_markers[district])
plt.title("Drug and Narcotic Incidents by Resolution and Location in SF for 2016")
plt.show()

for district in ['CENTRAL','NORTHERN','SOUTHERN','TENDERLOIN']:
	plt.scatter(x=narcos[ narcos['PdDistrict'] == district ]['X'],
	            y=narcos[ narcos['PdDistrict'] == district ]['Y'],
	            c=narcos['Resolution'].apply(res_to_color),
	            marker=district_markers[district])
plt.title("Drug and Narcotic Incidents by Resolution and Location in SF for 2016")
plt.show()
 
