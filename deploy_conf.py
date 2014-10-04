#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from develop_conf import *

SITEURL = 'http://yglezfdez.com/articles'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True



FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
TAG_FEED_ATOM = '%s/atom.xml'
TAG_FEED_RSS = '%s/rss.xml'
