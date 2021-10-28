#!/usr/bin/env python
# coding: utf-8

# # Estimating 2019 Revenue 

# ## A Tumultuous Year: 
# 
# 2019 was a landmark year for Lyft and Bay Wheels, but the company also faced many tribulations along the way.
# 
# * March 29th: Lyft went public on the stock market, with a market valuation of \$22.2 billion
# 
# https://www.cnbc.com/2019/03/29/lyft-ipo-stock-starts-trading-on-public-market.html
# 
# ----
# 
# * April 15th: Lyft grounded its entire e-bike fleet, 1,000 bikes, following reports of issues with the e-bikes' brakes.
# 
# https://www.sfchronicle.com/business/article/Lyft-pulls-electric-Ford-GoBikes-off-the-road-13769670.php
# 
# ----
# 
# * June 11th: Lyft rebranded from Ford GoBike to Bay Wheels. 
# 
# https://www.lyft.com/blog/posts/introducing-bay-wheels-new-bikes-and-a-new-name
# 
# ----
# 
# * July 10th: Lyft won a preliminary ruling for exclusive bike-rental rights in San Francisco, locking-out its biggest competitor, Uber's JUMP bikes.
# 
# https://www.sfchronicle.com/business/article/Lyft-wins-preliminary-ruling-for-exclusive-14086941.php?psid=alGCE
# 
# ----
# 
# * July 19th: Lyft redeployed and redesigned its ebike fleet—1,900 ebikes—with both docked and dockless capabilities. 
# 
# https://www.sfchronicle.com/business/article/Lyft-s-electric-Bay-Wheels-bikes-back-in-San-14108790.php
# 
# ----
# 
# * July 31st: Lyft recalled its dockless e-bike fleet once more, following reported fires suspected to be caused by malfunctions of the bikes' batteries.
# 
# <div class="center">
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Don’t think I’ll be going on a <a href="https://twitter.com/lyft?ref_src=twsrc%5Etfw">@lyft</a> <a href="https://twitter.com/baywheels?ref_src=twsrc%5Etfw">@baywheels</a> any time soon. Yikes. <a href="https://t.co/MOU9wIjgII">pic.twitter.com/MOU9wIjgII</a></p>&mdash; Zach Rutta (@zrutta44) <a href="https://twitter.com/zrutta44/status/1155147459313598465?ref_src=twsrc%5Etfw">July 27, 2019</a></blockquote> 
# <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
# 
# </div>
# 
# https://www.theverge.com/2019/7/31/20749396/lyft-electric-bikes-pulled-san-francisco-battery-fires-motivate-bay-wheels
# 
# ----
# 
# * December 19th: Lyft redeployed its dockeless e-bike fleet, with plans to increase its fleet to 4,000 by April of 2020.
# 
# https://medium.com/@baywheels/bringing-ebikes-back-in-san-francisco-and-upcoming-ebike-pricing-changes-b574f621f2db

# <br>
# Annotated 2019 Timeline of Estimated Revenue from Trips

# In[1]:


from plotly_viz import *
annotated_timeline()


# ## 2019 Pricing Scheme
# 
# Bay Wheels' rates for e-bikes changed on [March 2nd, 2020](https://medium.com/@baywheels/sf-ebike-pricing-details-1b97667f1e5a), from the [2019](https://www.tunneltime.io/san-francisco-usa/bay-wheels) rates:
# 
# ![pricing](img/2019pricing.png)
# 
# Bay Wheels also include an annual [Bike Share for All](https://www.lyft.com/bikes/bay-wheels/bike-share-for-all) (BSFA) membership plan for low-income Bay Area residents.

# Estimated Trip Revenue by Quarters

# In[2]:


barplot_revenue()


# ## Trends by Riders' Characteristics

# <b> Pie-chart: Subscribers V. Customers </b>
# 
# 4 out of 5 Bay Wheels riders are subscribed to a membership tier (Monthly, Annual, Day Pass, or BSFA). Only 1 in 5 riders purchase single rides.

# In[3]:


from pieMaker import *

pieMaker2(lyftSF19_df,'user_type',(6,6)) 


# <b> Pie-chart: "Bike Share for All" (BFSA) Subscribers</b>
# 
# Only 3% of all riders in San Francisco take advantage of the BFSA program.

# In[8]:


pieMaker2(lyftSF19_df,'bike_share_for_all_trip',(6,6))


# <b> Pie-chart: Rental Access Method </b>
# 
# The vast majority of riders use the Lyft's Bay Wheels App to purchase rides, with nearly 8% of all riders using the San Francisco Municipal Transportation Agency's Clipper Card.
# 
# 
# <img src= "img/baywheels.jpg" width="300" height="100" /> <img src= "img/clipper.jpg" width="300" height="200" />

# In[9]:


pieMaker2(lyftSF19_df,'rental_access_method',(6,6))

