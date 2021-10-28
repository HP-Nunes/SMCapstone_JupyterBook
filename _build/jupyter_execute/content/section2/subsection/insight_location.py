#!/usr/bin/env python
# coding: utf-8

# # Trends By Locations

# ## Summary by Neighborhoods
# 
# Lyft Ridership in San Francisco is concentrated in the city's white-collar centers of economic activity, sprawling from the South of Market (SoMa) to the Financial District.
# 
# SoMa is also host to major transportation nodes serving commuters from across the Bay Area, including the CalTrain station, and the BART stops peppered on Market Street.

# ### Ridership by Neighborhoods
# 
# Choropleth Map of Total Annual Ridership, as a Percentage of the Sum of Pick-ups and Drop-offs, per San Francisco Neighborhoods

# In[1]:


from IPython.display import IFrame
IFrame(src='./inputs/html_assets/choro.html', width=800, height=600)


# The South of Market was the busiest neighborhood by a fair margin, registering over 20% of all ridership activity over 2019. Mission Bay placed second with nearly 13% of all activity, followed by the Financial District at nearly 11%.

# ### Top Ridership by Neighborhoods
# 
# Barplot of the top 10 neighborhoods with the most combined number of pick-ups and drop-offs

# In[2]:


from plotly_viz import *

barplot()


# ### Top Routes by Neighborhoods
# 
# <em> Chord Diagram of the top 200 busiest routes, docked and dockless trips combined </em>

# In[7]:


chord_diagram()


# ## Summary by Stations
# 
# The two stations adjacent to one another at <em> Townsend St & 4th St </em>, at the San Francisco Caltrain station (SoMa), generated the most pick-ups (5.6%) and drop-offs (4.3%) activity.
# 
# ![dock station](img/dock_townsend.png)
# 
# Excluding the Caltrain location, the next busiest station for pick-ups was on <em> Market St & 10th St (SoMa) </em>, accounting for 2.4% of all pick-ups. 
# 
# ![dock station](img/dock_market.png)
# 
# The next busiest drop-off station was at the <em> Ferry Building by Harry Bridges Plaza (Financial District)</em>, accounting for 2.6% of all drop-offs.
# 
# ![dock station](img/dock_ferry.png)

# In[4]:


# from wrangling4 import *

# from jupyter_datatables import init_datatables_mode

# docked_df = lyft19Combined()

# init_datatables_mode() # Does not render in Jupyter Lab

# docked_df['route'] = docked_df['route'].astype(str)

# docked_df


# ## Busiest Routes
# 
# The majority of the busiest routes are concentrated in-and-around SoMa, such as Mission Bay and the Financial District. Although the vast majority of those routes seem to correspond to first-and-last mile commuter trips, a few routes suggest recreational usage. 

# ### Top 100th Routes (docked-bikes only)
# 
# <em> Mapped by Traffic Volume (width of arcs) & Total Estimated Generated Annual Revenue (color-graded) </em>
# 
# You may notice two nodes located respectively at the Marina and Panhandle neighborhoods which do not have an arc. That is because they indicate a "looped route": i.e., these nodes are both the starting and ending point of a route (arcs on those types of routes are not rendered). 
# 
# These two outliers do make practical sense: they are located in areas that are associated with tourism and recreation (Golden Gate Park, the Presidio/Crissy Fields), which also have fewer density of docking station compared to the SoMa/Downtown area of the city.
# 
# Some nodes which do display arcs, such as the ones located on North Beach and the Northern Waterfront, also suggest rides of a recreational nature.

# In[8]:


## Is not showing the basemap in the IPython Kernel; need to test whether the basemap displays once deployed to Jupyter Book
from IPython.display import IFrame
IFrame(src='./inputs/html_assets/kepler.gl.html', width=900, height=600)

