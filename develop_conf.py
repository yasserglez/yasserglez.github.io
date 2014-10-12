#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

SITENAME = "Yasser Gonzalez's Blog"
AUTHOR = 'Yasser Gonzalez Fernandez'

# Put a static page in / and the blog in /articles

SITEURL = '/articles'
PATH = 'content'
OUTPUT_PATH = 'output/articles'
THEME = 'themes/pure-single'

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

# Disable everything else

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# Feeds

FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
TAG_FEED_ATOM = '%s/atom.xml'
TAG_FEED_RSS = '%s/rss.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Pagination

DEFAULT_ORPHANS = 8
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Other settings

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

