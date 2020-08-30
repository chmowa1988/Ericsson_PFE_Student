#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog


# # Read data:

# In[2]:


# read data
# ask for file .csv

#decomment#Tk().withdraw()
#decomment#file_path = filedialog.askopenfilename(defaultextension='.csv')

# import data from csv file
#decomment#event = pd.read_csv(file_path, skipinitialspace=True, delimiter=";")
event = pd.read_csv("./data/event.csv", skipinitialspace=True, delimiter=";")

# import teams and host groups
teams = pd.read_csv("./data/teams.csv", delimiter=";", header=None)
teams.drop(teams.columns[0], axis=1, inplace=True)


# In[3]:


# test data
event.head(5)


# In[4]:


# test teams and hosts data
# teams
# test - search for a hostname
#print(teams[[c for c in teams.columns if (teams[c].str.contains("m4csnmt2") == True).any()][0]][0])

# init emails
emails = {
    'Charging System': 'charging.system.ericsson16@gmail.com',
    'Channels Team': 'tchannels.team.ericsson16@gmail.com',
    'Order Management Team': 'order.management.team.ericsson16@gmail.com',
    'Billing Team': 'billing.team.ericsson16@gmail.com',
    'Infra Team': 'infra.team.ericsson16@gmail.com',
    'Security Team': 'helpdeskenp@gmail.com'
}


# # Prepare data:

# In[5]:


# drop the NaN values
event.dropna(how="all", inplace=True)


# In[6]:


# define the Severity sorter
sorter = ["INFORMATION", "WARNING", "AVERAGE", "HIGH", "DISASTER"]

# create the dictionary that defines the order for sorting
sorterIndex = dict(zip(sorter,range(len(sorter))))

# generate a rank column that will be used to sort
# the dataframe numerically
event['Severity_Rank'] = event['Severity'].map(sorterIndex)

event.sort_values('Severity_Rank', ascending = True, inplace=True)
event.drop('Severity_Rank', 1, inplace = True)
event


# In[7]:


# drop duplicate Description and keep the last Serverity
event.drop_duplicates(subset='Description', keep='last', inplace=True)
event


# In[8]:


# drop duplicate HostName and keep the last Serverity
event.drop_duplicates(subset='HostName', keep='last', inplace=True)
event


# In[9]:


# add email here
#print(list(event["HostName"]))
Email = []
for host_name in list(event["HostName"]):
    #print(host_name)
    try:
        Email.append(emails[teams[[c for c in teams.columns if (teams[c].str.contains(host_name) == True).any()][0]][0]])
    except IndexError:
        Email.append("ahmed_chawki.harchouche@g.enp.edu.dz")
    #print(teams[[c for c in teams.columns if (teams[c].str.contains(host_name) == True).any()][0]][0])
#event2 = event.assign(Email = [teams[[c for c in teams.columns if (teams[c].str.contains(host_name) == True).any()][0]][0] for host_name in list(event["HostName"])])
event2 = event.assign(Email = Email)
event2


# In[10]:


# export data
Tk().withdraw()
export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
event2.to_csv(export_file_path, index = False, header=True, sep=";")


# In[ ]:





# In[ ]:





# In[ ]:




