import pandas as pd
import requests
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import time
data = {
        'Blog title':[],
        'Blog date':[],
        'Blog image URL':[],
        'Blog likes count':[]
    }
df = pd.DataFrame(data)
for mn in range(1,46):
    url=f'https://rategain.com/blog/page/{mn}/'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    soup=BeautifulSoup(web_byte,'html.parser')
    table = soup.findAll('div',attrs = {'class':"content"})
    for t in table:
        s = str(t.find('a').text)
        c= t.findAll('span')
        new_row = {
            'Blog title': s.replace("\\xe2\\x80\\x99","'"),
            'Blog date':t.span.text,
            'Blog image URL':t.a['href'],
            'Blog likes count':c[3].text
        }
        df.loc[len(df)] = new_row
    time.sleep(2)
df.to_csv('RateGainHackathon.csv')
print(df)
