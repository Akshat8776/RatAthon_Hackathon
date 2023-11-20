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
print(1)
df = pd.DataFrame(data)

for mn in range(1,46):
    # To fetch the data
    url=f'https://rategain.com/blog/page/{mn}/'
    # print(2)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(3)
    web_byte = urlopen(req).read()
    print(f'Hi{mn}')
    webpage = web_byte.decode('utf-8')
    soup=BeautifulSoup(web_byte,'html.parser')
    # to save the data
    # with open('readme.txt', 'w') as f:
    #     f.write(str(web_byte))

    
    # file1 = open("readme.txt","r+")

    # soup=BeautifulSoup(file1.read(),'html.parser')

    table = soup.findAll('div',attrs = {'class':"content"})
    for t in table:
        # print(t)//success
        # print("\n")
        s = str(t.find('a').text)
        # print(s.replace("\\xe2\\x80\\x99","'")) # name fetch success
        # print(t.a['href'])#link fetch successful
        # print(t.span.text) # date fetch success
        # like count success
        c= t.findAll('span')
        # print(c)
        # print(c[3].text)
        # print()
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
    # print(web_byte)
