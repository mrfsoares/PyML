import requests
import pandas as pd

url = 'https://www.waze.com/editor'

payload = {
        'username': '',
        'provider': 'Venues',
        'category': 'gas',
        'format': 'PROTO',
        'brand': '',
        'product': '',
        'address_search': 'false',
        'address_provider': 'Mozi',
        'auto': 'Venues',
        'ads_mode': 'FULL',
        'sponsered': 1,
        'longtitude': None,
        'latitude': None
    }
headers = {
        'host': 'www.waze.com',
        'user-agent': '/3.2.1.0',
        'content-type': 'application/x-www-form-urlencoded',
        'charset': 'utf-8'
    }

response = requests.post(url, headers=headers, data=payload)
print(response.text)

x = pd.DataFrame(response)
x.head()
x.to_csv('Dados.csv')