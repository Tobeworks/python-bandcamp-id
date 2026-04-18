import unittest
from bandcamp_scraper import get_release_id, InvalidURLException

class TestBandcampScraper(unittest.TestCase):
    def test_valid_url(self):
        self.assertEqual(get_release_id('https://logicmoon.bandcamp.com/album/sun'), '4152046122')

    def test_invalid_url(self):
        with self.assertRaises(InvalidURLException):
            get_release_id('https://bandcamp.com')

if __name__ == '__main__':
    unittest.main()
