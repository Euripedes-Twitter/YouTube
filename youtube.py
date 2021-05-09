#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
import glob
import re

'''
    Import csv files and add extra column for each country/region
'''
path = r'D:\Twitter\test_youtube' 
files = glob.glob(path + "/*.csv")

ls = []

for filename in files:
    df = pd.read_csv(filename, encoding="ISO-8859–1")
    country_region_code = re.search('test_youtube(.+?)videos.csv', filename).group(1)
    df['country_region_code'] = country_region_code[-2:]
    ls.append(df)


mdf= pd.concat(ls, axis=0, ignore_index=True)

'''
    Clean Date fields
'''

mdf['publish_time'] = pd.to_datetime(mdf['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
mdf['trending_date'] = pd.to_datetime(mdf['trending_date'], format='%y.%d.%m')
mdf['publish_date'] = mdf['publish_time'].dt.date

'''
    Extract the Twitter Profile 
'''

### First - check if there is twitter.com in the description - only for validation later
# Converts all characters in lower case
mdf['description'].str.lower()
# verify if the Description column has the word "twitter.com"
mdf['check_twitter'] = mdf['description'].str.contains("twitter.com")
mdf.head()

### Second - use regex to extract the profile - this was a challenged. 

#convert column to string
mdf['description'] = mdf['description'].astype(str)

#extract twitter profile
mdf['twitter_profile'] = mdf['description'].str.extract('(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?!home|share|privacy|tos)(?P<username>[A-z0-9_]+)\/?', expand=False).str.strip()


'''
    To retrieve the relevant fields for the assigment
'''

mdf = mdf[['video_id','trending_date','channel_title','publish_date','category_id','views','likes','dislikes','comment_count','country_region_code','twitter_profile']]


'''
    Export to csv 
'''

export_csv = mdf.to_csv("D:/Twitter/archive/all_countries_data.csv", index=False,header=True)

'''
    IMPORT THE JSON FILES INTO
'''
pathj = r'D:\Twitter\test_youtube' 
files = glob.glob(pathj + "/*.json")
lsj = []
id_category,title,assignable,country_code = [],[],[],[]
for filename in files:
    dfj = pd.read_json(filename)
    #print(dfj)
    for data in dfj['items']:
        id_category.append(data[u'id'])
        title.append(data[u'snippet'][u'title'])
        assignable.append(data[u'snippet'][u'assignable'])       
        c_code = re.search('test_youtube(.+?)_category_id.json', filename).group(1)
        country_code.append(c_code[-2:])
    cat = pd.DataFrame([id_category,title,assignable,country_code]).T
    
    
cat.rename(columns = {
                    0:'category_id',
                    1:'category_title',
                    2:'assignable',
                    3:'country_region_code'
                    },
                     inplace=True)

'''
    Export JSON files to csv file
'''
export_csv = cat.to_csv("D:/Twitter/archive/all_countries_category.csv", index=False,header=True)




# In[ ]:




