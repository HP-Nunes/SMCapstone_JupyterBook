#!/usr/bin/env python
# coding: utf-8

# # **1. Extraction**
# 
# 
# 

# #### Boilerplate Code

# In[1]:


get_ipython().system('pip install -r assets/requirements.txt')


# ## Get the Data

# We are pulling Bay Wheels raw dataset from the [Lyft's System Data](https://www.lyft.com/bikes/bay-wheels/system-data) page (under [Download Bay Wheels trip history data](https://s3.amazonaws.com/baywheels-data/index.html)). The data is contained within zipped csv files for each month of a given year; therefore, I clicked and downloaded all the files within my date range of interest: ie, January 2019 - August 2021.
# 
# I unzipped the files and saved each csv into a folder corresponding to the year the data was created (thus, I had three folders for 2019, 2020, and 2021).
# 
# ---
# Improvements:
# 
# *   Write a batch script to pull the csv files directly from Lyft's website;
#   *   Issues: Lyft does not provide an API to call upon their historical dataset. Furthermore, due to the rebranding of Bay Wheels from Ford Go Bike in mid-2019, which is reflected in the filepath convention to the files, that added a layer of difficulty to work around with. Finally, the zip files contain a folder dedicated to csv files formatted towards MacOS requirements, which I did not need to extract.
# 
# 

# ### Step 1: Combine the raw data, split by months, into a single csv for each given year.

# In[2]:


#@title
def combineRawData(year):
  # filepath2csv must be a string, and link to all csv files
  # needs to end like this: '/*.csv'
    filepath2csv = './rawdata/systemdatalyft/' + str(year) + 'lyftraw/*.csv'
  # filepath is like filepath2csv but without '/*.csv'
    filepath = './rawdata/systemdatalyft/' + str(year) + 'lyftraw/'
  # name_csv is the combined dataframe saved into a single csv within the designated filepath
    name_csv = 'lyft' + str(year) + '_raw.csv'

    files = glob.glob(filepath2csv)

    for i, f in enumerate (files):
        if i == 0:
            df = pd.read_csv(f)
            df['fname'] = f
        else:
            tmp = pd.read_csv(f)
            tmp['fname'] = f
            df = df.append(tmp)
            
    df.to_csv(filepath+name_csv,index=False)


# #### 2019

# In[3]:


#@title
combineRawData('2019')


# The output file will be in the folder with all the input files; you can then just remove the latter.

# <!-- ![img](1extract_img.png)
#  -->
# <img align="left" width="60%" height="30%" style="margin-right:25px" src="1extract_img.png">

# Repeat for the 2020 and 2021 datasets:

# #### *2020*

# In[ ]:


#@title
combineRawData('2020')


# #### *2021*

# In[ ]:


#@title
combineRawData('2021')


# You might think *why not just combine all of the yearly dataset into one csv file?* which is not an unreasonable thought. Wrangling data, in my experience, is an iterative process where incongruity in the raw dataset is uncovered through trials and errors. With these particular sets of data, I observed that their schema was not consistent in-between years (2019 was further complicated due to rebranding, so some of the data inputs changed in the meantime).
# 
# 
