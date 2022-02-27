import unittest

from bs4 import BeautifulSoup

import urllib
import urllib.request
import re


class TestingCase(unittest.TestCase):
    def test_scrapy(self):
        with urllib.request.urlopen('http://192.168.1.223/varsity/') as response: html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        type(soup)
        print(soup.prettify()[0:100])
        text_only = soup.get_text()
        print(text_only)


if __name__ == '__main__':
    unittest.main()
