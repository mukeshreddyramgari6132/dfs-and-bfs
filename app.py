import pymongo
import requests
from bs4 import BeautifulSoup
import json
database_connect=pymongo.MongoClient('mongodb://localhost:27017')
data_base=database_connect['mukesh_reddy']
collection=data_base['mobiles']
#mongo=pymongo.MongoClient(host="localhost",port=27017)
#db = mongo.companymukeshreddyflipkart
#mongo.server_info()
url='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme'
main_url='https://www.flipkart.com'
page=requests.get(url)
content=page.content
soup=BeautifulSoup(content,'html.parser')
tags=soup.find_all('a')
all_urls={}

links = [(main_url+i.get('href')) for i in tags]
keys=[i for i in range(len(links))]
for i in keys:
    for j in links:
        all_urls[i]=j
        links.remove(j)
        break
#regex=r'page=\d'
#links_keys=[(re.findall(regex, i)) for i in links]
#print(links_keys)
#print(all_urls)
#json1=json.dumps(all_urls)
###rec_id1 = collection.insert_one(data)
#cursor = collection.find()
#for record in cursor:
#print(record)
print(all_urls)