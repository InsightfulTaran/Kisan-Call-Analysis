"""
Created on Fri Jan 20, 2025

@author: tarandeeps
@project: Kisan Call Centre (data.gov.in)
"""

#libraries 
import requests #type:ignore
import pandas as pd #type:ignore
import os
from datetime import datetime

#user defined functions
def apiresponse(var):
    response = requests.get(var)
    return response.status_code

#api requirements
api = 'https://api.data.gov.in/resource/cef25fe2-9231-4128-8aec-2c948fedd43f'
api_key = '579b464db66ec23bdd000001498b0e2ca98a4ade4e3cbaf3e14912b2'
format = 'json'
limit = 10000

#filters
state = ['A AND N ISLANDS','ANDHRA PRADESH','ARUNACHAL PRADESH','ASSAM','BIHAR','CHANDIGARH','CHHATTISGARH','DADRA AND NAGAR HAVELI','DAMAN AND DIU','DELHI','GOA','GUJARAT','HARYANA',
         'HIMACHAL PRADESH','JAMMU AND KASHMIR','JHARKHAND','KARNATKA','KERALA','LAKSHADWEEP','MADHYA PRADESH','MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','ODISHA','PUDUCHERRY',
         'PUNJAB','RAJASTHAN','SIKKIM','TAMILNADU','TELANGANA','TRIPURA','UTTAR PRADESH','UTTARAKHAND','WEST BENGAL']
month = [i for i in range(1,13)]
year = [i for i in range(2011,2026)]

#creating/checking logfile directory
if not os.path.exists("logfiles"):
    os.mkdir("logfiles")
    dir = 'logfiles'
    print("DIRECTORY CREATION: logfiles directory is created.....")

#main code for data fetch
#check server response
if apiresponse(api+"?"+"api-key="+api_key+"&format="+"&limit=1000000") == 200:
    print("Hello Taran world")
else:
    print("Api not sending data, check the server is active or not or api-key is valid or expired")