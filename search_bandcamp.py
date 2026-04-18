import requests
from bs4 import BeautifulSoup

def search_bandcamp(query: str) -> list:
    search_url = f'https://bandcamp.com/search?q={query}'
    try:
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', {'class': 'heading'})
            return [link['href'] for link in links]
        return []
    except Exception:
        return []
