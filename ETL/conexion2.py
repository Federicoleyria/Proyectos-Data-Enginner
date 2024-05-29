import requests
import pandas as pd

url = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
headers = {"Accept-Encoding": "gzip, deflate"}

response = requests.get(url, headers=headers)
data = response.json()

#df = pd.DataFrame.from_dict(data['data']['market_data'], orient='index')
#print(df)
