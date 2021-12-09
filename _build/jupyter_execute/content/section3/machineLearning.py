#!/usr/bin/env python
# coding: utf-8

# # Machine Learning, Test 1

# In[1]:


## ML Learning

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# from wrangling4 import *
# poly, lyftSF19_df, docked_df, docked_df100_intersect = lyft19Combined()


# In[2]:


from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score


# In[3]:


df = pd.read_csv(r'inputs/data_lyftSF2019/outputs/lyftSF19.csv',float_precision=None)


# In[7]:


del df['Unnamed: 0']
display(df.columns)
df.head()


# In[8]:


### Estimate the duration of a trip by start-location without knowing the destination
    ### Filter dock-to-dock
        ### Narrow to neighborhoods which are the busiest
            ### Factorize all stations within those neighborhoods
                ### Remove datapoints where end_destination is an outlier

df1 = df

df1.user_type = pd.Series(np.where(df1.user_type == 'Customer', 1, 0)) # Customer = 1, Subscriber = 0
df1.bike_share_for_all_trip = pd.Series(np.where(df1.bike_share_for_all_trip == 'No', 1, 0)) # No = 1, Yes = 0
df1.start_time_day = pd.factorize(df1['start_time_day'])[0] # [0, 1, 2, 3, 4, 5, 6] = ['Tuesday', 'Friday', 'Saturday', 'Wednesday', 'Sunday', 'Monday', 'Thursday']
df1.rental_access_method = pd.factorize(df1['rental_access_method'])[0] # [NaN, 'app', 'clipper'] = [-1,0,1]
df1.start_time_month = pd.factorize(df1['start_time_month'])[0] # [0,1,2,3,4,5,6,7,8,9,10,11] = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
df1.Dockless_Type = pd.factorize(df1['Dockless_Type'])[0] # ['N/A', 'Dockless_Start', 'Dockless_End', 'Dockless_to_Dockless'] = [0,1,2,3]
df1.Quarter = pd.factorize(df1['Quarter'])[0] # ['2019Q1', '2019Q2', '2019Q3', '2019Q4'] = [0,1,2,3]
df1.ebike_trip = pd.factorize(df1['ebike_trip'])[0] # ['No', 'Yes'] = [0,1]

df1 = df1[['start_station_latitude',
       'start_station_longitude', 'user_type',
       'bike_share_for_all_trip', 'rental_access_method',
       'start_time_day', 'start_time_month', 'start_time_hour',
       'Dockless_Type', 'Quarter', 'ebike_trip',
       'est_cost','duration_sec']]

X = df1[['start_station_latitude',
       'start_station_longitude', 'user_type',
       'bike_share_for_all_trip', 'rental_access_method',
       'start_time_day', 'start_time_month', 'start_time_hour',
       'Dockless_Type', 'Quarter', 'ebike_trip',
       'est_cost']]

y = df1[['duration_sec']] # Predicting the duration of a trip


# In[ ]:


### Knowing the pick-up stations with xyz (mostly temporal) attributes, can you predict the route (the end station)?
    ### Logistic problem: where to allocate bikes when you've an outflow of people from station A, to B.
        ### "route modelling"
            ### How many bikes should be available at a given station {and at a given time}?
        ### Encode into time intervals: morning, afternoon, evening.
            ### Days: encode into weekdays and weekends
            ### Months: encode into "4 seasons"

    ### Backtracking the data: extract random observations (as a validation set, 10K) in a separate DF as a validation set.
        ### Test the model with the validation set to create  a forecast analysis of the model.


# In[9]:


from sklearn.model_selection import train_test_split

# Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


# In[10]:


from sklearn.linear_model import LinearRegression

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)


# In[24]:


for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))


# In[25]:


intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))


# In[26]:


regression_model.score(X_test, y_test)


# In[27]:


from sklearn.metrics import mean_squared_error

y_predict = regression_model.predict(X_test)

regression_model_mse = mean_squared_error(y_predict, y_test)

regression_model_mse


# In[28]:


import math

math.sqrt(regression_model_mse)


# In[34]:


corrMatrix = df1.corr()

sns.set(rc={'figure.figsize':(18,10)})
sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[35]:


import statsmodels.formula.api as smf
reg = smf.ols('y ~ X', data=df1).fit()
reg.summary()


# In[ ]:




