import unittest
from bandcamp_scraper import get_release_id

class TestBandcampScraper(unittest.TestCase):
    def test_valid_url(self):
        url = 'https://logicmoon.bandcamp.com/album/sun'
        expected_release_id = '4152046122'
        
        self.assertEqual(get_release_id(url), expected_release_id)

    def test_invalid_url(self):
        url = 'https://bandcamp.com'
        self.assertIsNone(get_release_id(url))

if __name__ == '__main__':
    unittest.main()