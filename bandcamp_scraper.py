from extract_release_id import extract_release_id
from urllib.parse import urlparse

class InvalidURLException(Exception):
    pass

class ReleaseIDExtractionException(Exception):
    pass

def get_release_id(url):
    parsed_url = urlparse(url)
    if 'bandcamp.com' in parsed_url.netloc and ('album' in parsed_url.path or 'track' in parsed_url.path):
        try:
            return extract_release_id(url)
        except:
            raise ReleaseIDExtractionException('Failed to extract release ID from URL: {}'.format(url))
    else:
        raise InvalidURLException('Invalid Bandcamp album URL: {}'.format(url))