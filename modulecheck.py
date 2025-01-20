"""
Created on Fri Jan 20, 2025

@author: tarandeeps
@project: Kisan Call Centre (data.gov.in)
"""

def status_msg(var,checker=1):
    if checker == 1:
        print(f'{var} requirement fulfilled.')
    elif checker == 0:
        print(f'{var} is not installed in this environment.')

#for dataframing operations
try:
    import pandas as pd #type:ignore
    status_msg("pandas")
except ImportError:
    status_msg("pandas",0)

#for file-related operations
try:
    import os
    status_msg("os")
except:
    status_msg("os",0)

#for scraping data from website
try:
    import requests #type:ignore
    status_msg("requests")
except ImportError:
    status_msg("requests",0)

#for lang detection
try:
    import langdetect #type:ignore
    status_msg("langdetect")
except:
    status_msg("langdetect",0)

#for timestamp related operations
try:
    import datetime
    status_msg("datetime")
except ImportError:
    status_msg("datetime",0)

#visualization
try:
    import matplotlib.pyplot
except:
    pass