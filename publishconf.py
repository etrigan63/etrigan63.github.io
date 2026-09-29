# Pelican publish config. Use: pelican -s publishconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa

# Staging URL until the www.echenique.com DNS cutover is done.
# At cutover, switch back to SITEURL = "https://www.echenique.com".
SITEURL = "https://etrigan63.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
