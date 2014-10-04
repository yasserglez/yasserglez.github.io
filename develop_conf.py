#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

SITENAME = "Yasser Gonzalez's Blog"
AUTHOR = 'Yasser Gonzalez Fernandez'

# Use a static page in /index.html and the blog in articles/

PATH = 'content'
SITEURL = '/articles'
OUTPUT_PATH = 'output/articles'
THEME_STATIC_DIR = '../theme'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Home', '/'),
    ('Articles', '/articles/'),
    ('Resume', '/resume/'),
]

DIRECT_TEMPLATES = ('index', )

PAGE_URL = '../{slug}/'
PAGE_SAVE_AS = '../{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
TAG_URL = '{slug}/'
TAG_SAVE_AS = '{slug}/index.html'

# Disable everything else:

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# These feeds are disabled when developing:

FEED_DOMAIN = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

# These feeds are always disabled:

CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Other settings:

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
SLUGIFY_SOURCE = 'basename'
TYPOGRIFY = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

