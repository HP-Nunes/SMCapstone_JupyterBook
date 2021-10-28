#!/usr/bin/env python
# coding: utf-8

# # ETL Process

# In[1]:


get_ipython().run_line_magic('time', '')

### LOAD PACKAGES ####

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
pd.set_option("display.precision", 8)


### LOAD DATA ###

count_trips_df = pd.DataFrame()
count_pickup_df = pd.DataFrame()
count_drop_df = pd.DataFrame()

df = pd.read_csv(r'inputs/data_lyftSF2019/outputs/2019lyftSF_dataset.csv',float_precision=None)
# df = pd.read_csv(r'data_lyftSF2019/outputs/2019lyftSF_intersected.csv',float_precision=None)


### PREPROCESS ###

main_df = pd.DataFrame(df)

# Parse the timestamp field
df['date_start'] = df.start_time.str.split(' ').str[0]
df['hour_start'] = df.start_time.str.split(' ').str[1]
df['date_end'] = df.end_time.str.split(' ').str[0]
df['hour_end'] = df.end_time.str.split(' ').str[1]

for m in range(6,9):

    # Count most popular trips

    count_series=df.groupby(['start_station_name', 'end_station_name','start_station_latitude','start_station_longitude','end_station_latitude','end_station_longitude']).size()
    count_trips_df_l = count_series.to_frame(name = 'count').reset_index()
    count_trips_df=pd.concat([count_trips_df, count_trips_df_l])

    
    # Count most popular pickup spots

    count_series=df.groupby(['start_station_name', 'start_station_latitude', 'start_station_longitude']).size()
    count_pickup_df_l = count_series.to_frame(name = 'count').reset_index()
    count_pickup_df=pd.concat([count_pickup_df, count_pickup_df_l])


    # Count most popular dropoff spots

    count_series=df.groupby(['end_station_name', 'end_station_latitude', 'end_station_longitude']).size()
    count_drop_df_l = count_series.to_frame(name = 'count').reset_index()
    count_drop_df=pd.concat([count_drop_df, count_drop_df_l])

    #drop original df
#     del df


### Observe the Dataframe's properties ###

print('*****Master DF*****')
print(main_df.shape)
print('---------------------------------------------')
print(main_df.dtypes)    
print('') 
print('*****Grouped by Trips*****')
print(count_trips_df.shape)
print('---------------------------------------------')
print(count_trips_df.dtypes)    
print('')
print('*****Grouped by Pick-up Locations*****')
print(count_pickup_df.shape)
print('---------------------------------------------')
print(count_pickup_df.dtypes)
print('')    
print('*****Grouped by Drop-off Locations*****')
print(count_drop_df.shape)
print('---------------------------------------------')
print(count_drop_df.dtypes)


# ## Wrangling
# 
# ### Get the coordinate for all unique stations
# 
# 1. Identify the number of unique stations; beware of the difference between pick-up and drop-off locations;
# 2. Group-by unique stations with their respective geographic coordinates
# 3. Because it is likely that there are various (small) differences in geographic coordinates for any given station, justs average lat/long by their respective unique stations.
# 
# #### Error Identified!
# > (3) When grouping by unique station names and averaging for the coordinates, I omitted to also groupby the unique count of drop-off locations! This caused strange issues, where I had decimal for my count in subsequent dataframes!
# 
# > Another mistake: using the method "unique_stations = count_drop_df.groupby(["end_station_name","count"]).mean()" will fail to group unique stations with <em>different counts</em>, henceforth unique stations will still be duplicated even if their coordinates are averaged. Using the aggregate function helped to sum and average the appropriate fields by unique station's names.

# In[30]:


# 1. Using the count-trips-by-drop-off trips DF, identify the number of known unique stations.
print('1.')
print(len(count_drop_df.end_station_name.unique())) # 446 unique location's names
print(len(count_drop_df)) # rows = 3042

# 2. Groupby the unique name of end_station_name & 3. averaging coordinates by unique locations/stations
unique_stations_end =count_drop_df.groupby(["end_station_name"]).agg({'count':'sum','end_station_latitude':'mean','end_station_longitude':'mean'})


print('2.')                                                                    
print(len(unique_stations_end)) # 446 rows; much better!


# ### Group Rides by Drop-off Stations
# 
# #### Error Rectified
# > The percentage share of drop-off stations for all ridership activity in 2019 has radically changed: the busiest drop-off station accounts for 2.15% of all activities, as opposed to 12% as previously (and erroneaously) calculated. This can also be observed on the box-and-whisker plot, which shows more datapoints as outliers.

# In[31]:


unique_stations_end = unique_stations_end.reset_index() 
unique_stations_end = unique_stations_end.rename(columns={'count': 'end_count'})

unique_stations_end.sort_values(by='end_count', ascending=False).head(10)


# In[32]:


plt.boxplot(unique_stations_end.end_count)


# ###  Group Rides by Pick-Up Stations

# In[33]:


unique_stations_start =count_pickup_df.groupby(["start_station_name"]).agg({'count':'sum','start_station_latitude':'mean','start_station_longitude':'mean'})
unique_stations_start = unique_stations_start.reset_index() 
unique_stations_start = unique_stations_start.rename(columns={'count': 'start_count'})

unique_stations_start.sort_values(by='start_count', ascending=False).head(10)


# In[34]:


plt.boxplot(unique_stations_start.start_count)


# ### Concat both DF
# 
# #### Error Rectified
# > Dataframe of unique start and end stations with their respective field attributes, with a length of 446 rows.

# In[35]:


counting_stations_df = pd.merge(unique_stations_end, unique_stations_start, left_on='end_station_name',right_on='start_station_name')

print(len(counting_stations_df)) # 446 rows. Sounds about right!


# ### Further cleaning:
# 
# * Some typos in the name of stations is creating duplication (see example below); thus my objective will be to identify stations by matching lat and long coordinates:
# ![error](img/typo.png)
# 
# Yet this caused a great deal of confusion, mainly because when I attempted to identify rows with matching lat/long
# for a station's type (pick-up or drop-off), I was not returning Woolsey St at Sacramento. I couldn't understand why, until I realized that the float values of my coordinates were rounded, and that matches had to be exact. Thus, my lat/long appeared to be matching, but by setting the precisions of the decimal display to a higher number, we can finally observe the source of confusion:
# ![error](img/precision.png)
# 
# Therefore, all of my coordinate fields had to be rounded-up uniformly so that I could match possible duplicates.

# In[36]:


cols = ['start_station_latitude', 'start_station_longitude','end_station_latitude','end_station_longitude']
counting_stations_df[cols] = counting_stations_df[cols].round(6)


# * Furthermore, the lat/long location ought to be unique per station, regardless of their designation as either pick-up or drop-off locations. The objective will be to identify mismatch in coordinates between pick-up and drop-off locations, and average coordinates if they differ.

# #### Identify pick-up stations with duplicates

# In[37]:


counting_stations_df[counting_stations_df[cols[0:1]].duplicated(keep = False) == True]


# #### Identify drop-off stations with duplicates

# In[38]:


counting_stations_df[counting_stations_df[cols[2:4]].duplicated(keep = False) == True]


# #### Merge rows with matching coordinates

# In[39]:


aggregation_functions = {'end_count': 'sum', 'start_count': 'sum', 'end_station_name': 'first','start_station_name':'first'}

i = [443,444]

new_row = counting_stations_df.loc[i].groupby(['end_station_latitude','end_station_longitude','start_station_latitude','start_station_longitude']).aggregate(aggregation_functions).reset_index()

counting_stations_df = counting_stations_df.append(new_row, ignore_index=True).drop(i)

#### Only the start station's latitude matches for this location, hence the groupby query has been modified.
aggregation_functions = {'end_count': 'sum', 'start_count': 'sum', 'end_station_name': 'first','start_station_name':'first','end_station_latitude':'mean','start_station_longitude':'mean','end_station_longitude':'mean'}

i = [4,109]

new_row = counting_stations_df.loc[i].groupby(['start_station_latitude']).aggregate(aggregation_functions).reset_index()

counting_stations_df = counting_stations_df.append(new_row, ignore_index=True).drop(i)


# #### Drop 'Null' locations

# In[40]:


i = [13,349]
counting_stations_df = counting_stations_df.drop(i)


# #### Identify stations with drop-off and pick-up coordinates that do not match
# 
#     Upon reflection, it's not necessary to define a 'unique set' of coordinate for any given station; this was mostly in the interest of consistency when processing the datapoints in QGIS. However we can assume reasonably that slight differences in the coordinates between 'pick-up' and 'drop-off' stations will not affect the "true" location of the station when intersected with city or neighborhood boundaries.

# In[41]:


len(counting_stations_df)

cols = ['start_station_latitude', 'start_station_longitude','end_station_latitude','end_station_longitude']

counting_stations_df['lat_diff'] = np.where(counting_stations_df[cols[0]] == counting_stations_df[cols[2]], 'same', 'different')
counting_stations_df['long_diff'] = np.where(counting_stations_df[cols[1]] == counting_stations_df[cols[3]], 'same', 'different')

counting_stations_df.head()


# ### 4. Save to csv and export to QGIS to intersect the station datapoints w/city/neighorhood boundaries

# In[14]:


# counting_stations_df.to_csv('outputs/to_gis.csv') 


# ## Data Processing in QGIS
# 
# ### Import CSVs which have been intersected with the boundaries of cities and SF neighborhoods in QGIS
# 
# Plotting the stations on QGIS allowed to observe a few outlier/dummy values to remove from the dataset:
# 
# ![QGIS1](img/del1.png)
# 
# > Note that some dummy variables, such as locations with lat/long of 0, where already dropped over the second iteration of wrangling.
# Another suitable method within Python to drop features that are out of proper geographic bounds would be to plot the lat and long of datapoints on a point data plot, and identify the outliers to exclude.
# 
# ![QGIS2](img/del2.png)

# The dataframe was imported into QGIS as a csv, and mapped as points with the end station's lat and long coordinates. Those points were overlaid with the shapefile layer of city boundaries for San Francisco (orange), the East Bay (purple) constituting of Oakland, Berkeley, and Emeryville, & San Jose (green).
# 
# Using the intersect function from the geoprocessing tool menu, each datapoint were intersected with their respective intersecting boundaries, capturing those boundaries' attribute features (namely, city's names and, additionally for San Francisco, the names of neighborhood's boundaries).

# ![QGIS3](img/Q_overlay.png)

# Baywheels' stations from the 2019 annual dataset overlaid on San Francisco's neighborhoods.

# ![QGIS4](img/Q_sf_intersect.png)

# ## Re-importing the intersected dataset

# In[42]:


get_ipython().run_cell_magic('time', '', '\npath = r\'./inputs/modifiedFiles\' # use your path\nfiles = glob.glob(path + "/*.csv")\n\nli = []\n\nfor file in files:\n    df = pd.read_csv(file, index_col=None, header=0)\n    df = pd.DataFrame(df)\n    li.append(df)\n\nframe = pd.concat(li, axis=0, ignore_index=True, sort=False)\nframe = frame.rename(columns={\'name\': \'city\', \'n_name\': \'SF_Neigh\',\'end_statio\':\'end_station\',\n                             \'end_stat_1\':\'end_lat\',\'end_stat_2\':\'end_lon\',\n                             \'start_st_1\':\'start_lat\',\'start_st_2\':\'start_lon\',\n                             \'start_coun\':\'start_C\',\'end_count\':\'end_C\',\'start_stat\':\'start_station\',\n                             })\n\nframe = frame.drop(\'field_1\',axis=1)\n\nprint(frame.dtypes)\nprint(\'---------------\')\nprint(frame.shape)\nprint(\'---------------\')\n\nframe.head()')


# ## Insights

# ### Distribution of stations per city (Bay Wheels dataset)

# #### Using Helper Functions to speed-up the process! 
# 
# Storing the code into a .py file

# In[43]:


from pieMaker import * # (dataframe / attribute feature to groupby / piechart's dimensions)

pieMaker(frame,'city',(6,6))


# Filter the dataframe down to stations in San Francisco only.

# In[44]:


frame_sf = frame.loc[frame['city']=='San Francisco']
pieMaker(frame_sf,'SF_Neigh',(30,30))


# <b>We're only interested in insights for the city of San Francisco, which accounts for half of Bay Wheels' 2019 Dataset</b>

# In[45]:


frame_sf = frame.loc[frame['city']=='San Francisco']

print('There are ' + str(len(frame_sf)) + ' unique stations in San Francisco')


# ## Busiest 10 Pick-Up Station

# In[46]:


frame_sf['start_P'] = (frame_sf['start_C'] / frame_sf['start_C'].sum()).astype(float).map("{:.2%}".format)

frame_sf.sort_values(by = ['start_C'],ascending=False).set_index(['start_station','SF_Neigh','start_P'])['start_C'].head(10)


# In[47]:


frame_sf['start_C'].plot.hist(bins=20, alpha=0.5)


# ## 10 Busiest Neighborhoods by Pick-Ups 

# In[48]:


x = pd.DataFrame((frame_sf.groupby(['SF_Neigh'])['start_C'].sum() / frame_sf['start_C'].sum()).
                 astype(float).map("{:.2%}".format)).reset_index().rename(columns={'start_C':'startN_P'})

frame_sf = pd.merge(frame_sf, x, right_on='SF_Neigh',left_on='SF_Neigh').rename(columns={'startN_P_y':'startN_P'})

frame_sf.groupby(['SF_Neigh','startN_P'])['start_C'].sum().sort_values(ascending=False).head(10)


# ## Busiest 10 Drop-Off Station

# In[49]:


frame_sf['end_P'] = (frame_sf['end_C'] / frame_sf['end_C'].sum()).astype(float).map("{:.2%}".format)

frame_sf.sort_values(by = ['end_C'],ascending=False).set_index(['end_station','SF_Neigh','end_P'])['end_C'].head(10)


# In[50]:


frame_sf['end_C'].plot.hist(bins=20, alpha=0.5)


# ## 10 Busiest Neighborhoods by Drop-offs 

# In[51]:


x = pd.DataFrame((frame_sf.groupby(['SF_Neigh'])['end_C'].sum() / frame_sf['end_C'].sum()).
                 astype(float).map("{:.2%}".format)).reset_index().rename(columns={'end_C':'endN_P'})

frame_sf = pd.merge(frame_sf, x, right_on='SF_Neigh',left_on='SF_Neigh').rename(columns={'endN_P_y':'endN_P'})

frame_sf.groupby(['SF_Neigh','endN_P'])['end_C'].sum().sort_values(ascending=False).head(10)


# ## Busiest Routes

# In[52]:


count_trips_df['route'] = "From " + count_trips_df.start_station_name.map(str) + " to " + count_trips_df.end_station_name

routes_df = count_trips_df.groupby(['route','start_station_name','end_station_name','count']).nunique()
routes_df = routes_df.drop(routes_df[['end_station_name','start_station_name','start_station_latitude','start_station_longitude',
         'end_station_latitude','end_station_longitude','count','route']], axis=1)
routes_df = routes_df.reset_index()


### Merge San Francisco's Neighborhoods to unique start/end stations
Neigh_merge_s = frame_sf.groupby(['SF_Neigh','start_station']).nunique()
Neigh_merge_e = frame_sf.groupby(['SF_Neigh','end_station']).nunique()

Neigh_merge_s = Neigh_merge_s[['SF_Neigh','start_station']].drop(Neigh_merge_s[['SF_Neigh','start_station']],axis=1).reset_index()
Neigh_merge_e = Neigh_merge_e[['SF_Neigh','end_station']].drop(Neigh_merge_e[['SF_Neigh','end_station']],axis=1).reset_index()

routesDF1 = pd.merge(left=Neigh_merge_s, right=routes_df, left_on='start_station', right_on='start_station_name').rename(columns={'SF_Neigh':'SF_Neigh_start','count':'route_C'})
routesDF = pd.merge(left=Neigh_merge_e, right=routesDF1, left_on='end_station', right_on='end_station_name').rename(columns={'SF_Neigh':'SF_Neigh_end'})

routesDF = routesDF.drop(routesDF[['start_station']],axis=1)
###

### Find the Percentage
routesDF['route_P'] = (routesDF['route_C'] / routesDF['route_C'].sum()).astype(float).map("{:.2%}".format)
###

routesDF['route_Districts'] = "From " + routesDF.SF_Neigh_start.map(str) + " to " + routesDF.SF_Neigh_end


print(len(routesDF))
# routesDF.sort_values(['route_C'],ascending=False).head(10)

routesDF.groupby('route_Districts')['route_C'].sum().reset_index().sort_values(['route_C'],ascending=False).head(10)
routesDF


# In[ ]:


# routesDF.to_csv('outputs/routes_dataset.csv') 


# In[53]:


print(routesDF.shape)
# routesDF.groupby(['route_Districts']).size().reset_index(name='counts').sort_values('counts',ascending=False)


new_df=routesDF.groupby(['SF_Neigh_start', 'SF_Neigh_end'])['route_C'].sum().reset_index(name='counts').sort_values(by='counts',ascending=False)
new_df.head(10)


# ## Total number of routes by Neighborhoods

# In[54]:


routes_N = routesDF.groupby('SF_Neigh_end')[['route_C']].sum()

### Find the Percentage
routes_N['routeN_P'] = (routes_N['route_C'] / routes_N['route_C'].sum()).astype(float).map("{:.2%}".format)
###

routes_N.sort_values(['route_C'],ascending=False).head(10)

