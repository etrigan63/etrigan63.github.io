# Pelican publish config. Use: pelican -s publishconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa

# Custom domain mapped to this repo (see content/extra/CNAME).
SITEURL = "https://www.echenique.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
