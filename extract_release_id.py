import requests
from bs4 import BeautifulSoup
import json
import re

def fetch_release_data(url: str) -> dict:
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')

    props = soup.find('meta', {'name': 'bc-page-properties'})
    release_id = json.loads(props.get('content'))['item_id'] if props else None

    og_image = soup.find('meta', {'property': 'og:image'})
    image_url = og_image.get('content') if og_image else None

    og_site = soup.find('meta', {'property': 'og:site_name'})
    artist = og_site.get('content') if og_site else None

    og_title = soup.find('meta', {'property': 'og:title'})
    title = og_title.get('content') if og_title else None
    if title and ', by ' in title:
        title = title.split(', by ')[0].strip()

    return {'release_id': release_id, 'image_url': image_url, 'artist': artist, 'title': title}

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s]+', '_', text.strip())
