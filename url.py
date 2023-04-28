import requests
from bs4 import BeautifulSoup
import json

url = 'https://logicmoon.bandcamp.com/album/sun'
#url = 'https://desired.bandcamp.com/album/desired'

#url = 'https://bandcamp.com'
result = requests.get(url)
#print(result.content)

soup = BeautifulSoup(result.content, 'html.parser')
#release_id = soup.find('div', {'class': 'trackTitle'}).find('a').get('href').split('/')[-1]
# release_id = soup.find('a', {'class': 'album-link'}).get('href').split('-')[2][1:]

release_id = soup.find('meta', {'name': 'bc-page-properties'}).get('content')
release_id_json = json.loads(release_id)
print(release_id_json['item_id'])

