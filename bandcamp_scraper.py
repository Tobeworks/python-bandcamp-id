import os
import requests
from urllib.parse import urlparse
from extract_release_id import fetch_release_data, slugify

class InvalidURLException(Exception):
    pass

def validate_url(url: str):
    parsed = urlparse(url)
    if 'bandcamp.com' not in parsed.netloc or not any(p in parsed.path for p in ('album', 'track')):
        raise InvalidURLException(f'Invalid Bandcamp URL: {url}')

def get_release_id(url: str) -> str:
    validate_url(url)
    data = fetch_release_data(url)
    if not data['release_id']:
        raise Exception(f'Failed to extract release ID from: {url}')
    return data['release_id']

def process(url: str, download_image: bool = True) -> None:
    validate_url(url)
    data = fetch_release_data(url)

    if not data['release_id']:
        raise Exception(f'Failed to extract release ID from: {url}')
    print(data['release_id'])

    if not download_image or not data.get('image_url'):
        if download_image:
            print('No cover image found.')
        return

    artist = slugify(data.get('artist') or 'unknown')
    title = slugify(data.get('title') or 'unknown')
    ext = os.path.splitext(data['image_url'].split('?')[0])[-1] or '.jpg'
    filename = f'cover_{artist}_{title}{ext}'
    response = requests.get(data['image_url'])
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Cover image saved to {filename}')
    else:
        print(f'Failed to download cover image (HTTP {response.status_code})')
