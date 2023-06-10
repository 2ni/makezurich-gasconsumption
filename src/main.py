#Run in terminal
#pip install -r requirements.txt


#Import libraries
import pandas as pd 
from pyproj import Transformer
import numpy as np
from numpy.core.fromnumeric import sort
from numpy import sqrt

# helper function for reading datasets with proper separator
df = pd.read_csv('data/KTZH_00002022_00004064.csv')

# display a small random sample transposed in order to see all variables
df.sample(3).T

# Only select relevant columns
df_selected = df[['Eidgenoessischer_Gebaeudeidentifikator', 'Gebaeudestatus_Code', 'Baujahr_des_Gebaeudes', 'E-Gebaeudekoordinate', 'N-Gebaeudekoordinate','Energiebezugsflaeche', 'Anzahl_Geschosse', 'Gebaeudeflaeche']]

# Filter Gebäude which are existing, remove the other ones
df_selected = df_selected[df_selected['Gebaeudestatus_Code'] == 1004]

# Define the transform the WGS84 coordinates from the gps sensor to LV95 function

def wgs84_to_lv95(latitude, longitude):
    transformer = Transformer.from_crs('EPSG:4326', 'EPSG:2056')
    lv95_x, lv95_y = transformer.transform(latitude, longitude)
    return lv95_x, lv95_y

# Calculate the euclidian distance between the coordinate from the gps sensor and each building
# The building with the smallest distance is considered to be the closest to the sensor
# return the Baujahr of the closest building

def calculate_closest_building_egid(dataframe, lv95_x, lv95_y):
  df_selected = dataframe
  df_selected.loc[:, 'diff_E'] = df_selected.loc[:, 'E-Gebaeudekoordinate'] - lv95_x
  df_selected.loc[:, 'diff_N'] = df_selected.loc[:,'N-Gebaeudekoordinate'] - lv95_y

  df_selected.loc[:, 'euc_dist'] = sqrt(df_selected.loc[:, 'diff_E'] ** 2 + df_selected.loc[:,'diff_N'] ** 2)
  df_selected = df_selected.sort_values(by='euc_dist', ascending=True)
  return(df_selected.iloc[0,0]).astype('int')

# Define the calculate the KPI function

def calculate_kpi(dataframe, egid, consumption_per_year_m3):
  temp = dataframe[dataframe['Eidgenoessischer_Gebaeudeidentifikator'] == egid]
  
# check if Energiebezugsfläche is there. If not, calculate a fictional area from the building area and the number of stories.
  if temp.iloc[0,5] > 0:
    print(f"Energiebezugsfläche vorhanden")
    area = temp.iloc[0,5]
  else:
    print(f"Energiebezugsfläche nicht vorhanden. Die Gebäudefläche wird mit den Anzahl Stockwerken multipliziert")
    area = temp.iloc[0,6] * temp.iloc[0,7]

  print(f"Fläche: {area} m2")
  print(f"Baujahr = {temp.iloc[0,2]}")

  if temp.iloc[0,2] < 1950:
    demand = 211 * area 
  elif temp.iloc[0,2] < 1970 :
    demand = 221.55 * area 
  elif temp.iloc[0,2] < 1980:
    demand = 232.1 * area 
  elif temp.iloc[0,2] < 1990:
    demand = 179.35 * area 
  elif temp.iloc[0,2] < 2000:
    demand = 137.15 * area 
  elif temp.iloc[0,2] < 2010:
    demand = 105.5 * area 
  else:
    demand = 52.75 * area 

  consump_kwh = consumption_per_year_m3 * 10.55
  print(f"Consumption is: {consump_kwh} kwh")
  print(f"Demand is: {demand} kwh")
  return(demand / consump_kwh)

# Call the functions

# transform the coordinates to lv95 format
latitude_wgs84 = 47.360970311453684
longitude_wgs84 = 8.533319745509766
lv95_x, lv95_y = wgs84_to_lv95(latitude_wgs84, longitude_wgs84)
print(f"LV95 coordinates: X={lv95_x}, Y={lv95_y}")

# Get the closest building egid for a specific coordinate
egid = calculate_closest_building_egid(df_selected, lv95_x, lv95_y)
print(f"Egid = {egid}")

# Calculate the KPI
consumption_per_year_m3 = 4306
kpi = calculate_kpi(df_selected, egid, consumption_per_year_m3)
print(f"KPI = {kpi}")

#write kpi to txt file
with open('kpi.txt', 'w') as f:
    f.write(kpi)
