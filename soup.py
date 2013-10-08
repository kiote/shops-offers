# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

url = "http://habrahabr.ru"
soup = bs(urlopen(url))
for link in soup.findAll("a"):
  print link.contents