import requests

url='https://api.data.gov.in/resource/cef25fe2-9231-4128-8aec-2c948fedd43f?api-key=579b464db66ec23bdd000001498b0e2ca98a4ade4e3cbaf3e14912b2&format=json&limit=1000'

response = requests.get(url)
print(type(response.status_code))
if(response.status_code==200):
    print("Hello world")