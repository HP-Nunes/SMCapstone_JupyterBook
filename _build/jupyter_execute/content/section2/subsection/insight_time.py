#!/usr/bin/env python
# coding: utf-8

# # Temporal Trends

# In[1]:


# from wrangling4 import *
# poly, lyftSF19_df,docked_df,docked_df100_intersect = lyft19Combined()
from plotly_viz import *


# ## Monthly Trends
# 
# <b> Barplot & Trendline of the total number of trips per Month and Quarter </b>
# 
# Although the decrease in total trips between April and May can be attributed to the recall of all e-bikes following reported malfunctions with the model's brakes; the second recall of e-bikes, which included recalling the rollout of the brand new dockless fleet in July, did not result in a sharp decrease of trips.
# 
# The noticeable decrease of trips during Q4 may be attributed towards seasonal inclement weather conditions (such as heatwaves), or worsened air quality (such as the [Kincade Fire](https://www.sfgate.com/california-wildfires/article/how-bad-is-air-bay-area-kincade-fire-sonoma-sf-14569337.php), which spanned from late October to early November).

# In[2]:


barplot_monthly()


# ## Hourly Trends

# The longest daytime trips occur on the weekend, probably for recreational trips in the city's green and touristic areas. Longer daytime rides over the weekdays are busiest during commuter's hours, between 8 to 9 am, and 5 and 6 pm.
# 
# Nightime usage, especially in the early morning of weekdays between 2 to 4 am, tends to be longer than the average largely due to the smallest proportion of rides compared to daytime hours. However, it can be reasonably theorized that longer trips occur over these unconventional hours for workers starting early shifts (in grocery stores and warehouses, for instance), as a commuting alternative to limited public transportation at those hours.
# 
# <b> Heatmap of the Hourly Median Trip Duration (minutes) by Days of the Week </b>
# 
# > Why take the median instead of the average of trip durations? <br> <br>
# Trips taken during "odd hours" (8pm to 6am) are few in numbers, but tend to be longer than the overall average, thereby skewing disproportionally the duration scale. The median in this case is a more robust indicator than the mean.

# In[3]:


heatmap_hourly()


# <b> Heatmap of the Total Hourly Number of Trips by Days of the Week </b>
# 
# As suspected, although nightime/early morning rides may be longer than the average trip, they are much fewer in numbers compared to daytime trips.
# 
# We can also observe peak hours in ridership correlating with commuter behavior: weekdays between 7 and 10 am, and between 4 and 7 pm see the most ridership activity. Weekends from noon to 3 pm indicate a moderate uptick in ridership compared to their equivalent over the weekday.
# 
# This strongly suggest that while Bay Wheels is primarly used as a first-and-last mile commuter option (most likely serving office workers), it also serves a recreational or casual purpose on weekends.

# In[4]:


heatmap_hourly_count()

