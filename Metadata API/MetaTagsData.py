import requests
from bs4 import BeautifulSoup
import json

# Function that returns the requested url metadata tags content
def getMetas(url):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    url = "https://enttry.com.br/contato"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    metas = soup.find_all("meta", attrs={'content': True, 'name': True})
    metas2 = soup.find_all("meta", attrs={'content': True, 'name': False})

    for tags in metas:
        out1 = [tags['content'], tags['name']]
        json1 = json.dumps(out1)
        print({json1})
    for tags in metas2:
        out2 = [tags['content']]
        json2 = json.dumps(out2)
        print(json2)

getMetas("https://enttry.com.br/contato")
