import requests
from bs4 import BeautifulSoup
import json

def extract_release_id(url: str) -> str:
    try:
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')
        #release_id = soup.find('div', {'class': 'trackTitle'}).find('a').get('href').split('/')[-1]
        #release_id = soup.find('a', {'class': 'album-link'}).get('href').split('-')[2][1:]
        release_id = soup.find('meta', {'name': 'bc-page-properties'}).get('content')
        release_id_json = json.loads(release_id)
        return release_id_json['item_id']
    except Exception as e:
        print(f'Error in extracting the release id from {url}.')
        print(f'Error: {str(e)}')
        return None
