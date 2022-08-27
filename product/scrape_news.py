import pandas as pd
import requests
import json
from pandas import json_normalize 

r = requests.get('https://newsapi.org/v2/everything?q=%E5%8F%B0%E7%A9%8D%E9%9B%BB&from=2022-07-26&sortBy=popularity&apiKey=70f505945a394476b47778f4e18665ef')
data = r.text
info = json.loads(data)
# parsed = r.json()
# df = pd.read_json(data, orient='records')
# print(type(r))
df = json_normalize(info["articles"])
# df = json_normalize(info, "articles")
df =df[["publishedAt","title"]]
print(df)