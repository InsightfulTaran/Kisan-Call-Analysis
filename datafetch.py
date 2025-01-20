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

def dfdata(var):
    response = requests.get(var)
    data = response.json()
    records = data.get('records',[])
    df = pd.DataFrame(records)
    return df

#api requirements
api = 'https://api.data.gov.in/resource/cef25fe2-9231-4128-8aec-2c948fedd43f'
api_key = '579b464db66ec23bdd000001498b0e2ca98a4ade4e3cbaf3e14912b2'
limit = 1000000

#filters
state = ['A AND N ISLANDS','ANDHRA PRADESH','ARUNACHAL PRADESH','ASSAM','BIHAR','CHANDIGARH','CHHATTISGARH','DADRA AND NAGAR HAVELI','DAMAN AND DIU','DELHI','GOA','GUJARAT','HARYANA',
         'HIMACHAL PRADESH','JAMMU AND KASHMIR','JHARKHAND','KARNATKA','KERALA','LAKSHADWEEP','MADHYA PRADESH','MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','ODISHA','PUDUCHERRY',
         'PUNJAB','RAJASTHAN','SIKKIM','TAMILNADU','TELANGANA','TRIPURA','UTTAR PRADESH','UTTARAKHAND','WEST BENGAL']
state = ['MADHYA PRADESH']
month = [i for i in range(1,13)]
month_dict = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'Novemvber',12:'December'}
year = [i for i in range(2011,datetime.now().year + 1)]
year = [2017]

#creating/checking logfile directory
if not os.path.exists("logfiles"):
    os.mkdir("logfiles")
    print("DIRECTORY CREATION: logfiles directory is created.....")
directory = 'logfiles'

#shape file
shape = pd.read_csv('shape.csv')

#main code for data fetch
#check server response
if apiresponse(api+"?"+"api-key="+api_key+"&format="+"&limit=10") == 200:
    for i in year:
        for j in state:
            for k in month:
                t1 = datetime.now()
                request_url = f'{api}?api-key={api_key}&format=json&filters[StateName.keyword]={j}&filters[year.keyword]={i}&filters[month.keyword]={k}&limit={limit}'
                data = dfdata(request_url)
                data.drop_duplicates()
                if data.shape[0] ==0 and data.shape[1] ==0:
                    pass
                else:
                    filename = f'{i}{j.replace(" ","")}{k}'
                    data.to_csv(f'{directory}\\{filename}.csv',index=False)
                    t2 = datetime.now()
                    t3 = t2-t1
                    print(f"{i} {j} {month_dict[k]} log file created in {str(t3).split(".")[0]} time.")
                    shape2 = pd.DataFrame({'statename':[j],"year":[i],"month":[k],"records":[data.shape[0]],"columns":[data.shape[1]],"fetching time taken":[str(t3).split(".")[0]]})
                    shape = pd.concat([shape,shape2],ignore_index=True)
    shape.to_csv('shape.csv',index=False)

else:
    print("Api not sending data, check the server is active or not or api-key is valid or expired")