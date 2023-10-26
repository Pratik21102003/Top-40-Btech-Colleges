import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage=requests.get('https://collegedunia.com/btech-colleges',headers=headers).text
soup=BeautifulSoup(webpage,'lxml')
#print(soup.find_all('h1')[0].text.strip())
n=[]
loc=[]
for i in soup.find_all('h3',class_="jsx-3175684501 font-weight-medium text-lg mb-0"):
   try:
    n.append(i.text.split(',')[0])
    loc.append(i.text.split(',')[1])
   except:
    n.append(np.nan)
    loc.append(np.nan)
   
state=[]
for i in soup.find_all('span', class_="jsx-3175684501 pr-1 location"):
   try:
      state.append(i.text.split(',')[1])
   except:
      state.append(np.nan)     
price=[]
for i in(soup.find_all("td", class_="jsx-3175684501 col-fees")):
   try:
      price.append(i.text.split('BE')[0])
   except:
      price.append(np.nan)
df=pd.DataFrame()
df['Name']=n
df['location']=loc
df['State']=state
df['Fee per Year']=price
df.set_index('Name',inplace=True)
df.to_csv('Top 40 B-Tech Colleges.csv')

   

               