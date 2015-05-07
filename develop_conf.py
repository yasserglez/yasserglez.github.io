#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

SITENAME = "Yasser Gonzalez"
TAGLINE = "Computer Scientist"
AUTHOR = 'Yasser Gonzalez Fernandez'

# Put a static page in / and the blog in /articles

SITEURL = '/articles'

PATH = 'content'
OUTPUT_PATH = 'output/articles'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Articles', '/articles/'),
    ('Resume', '/resume/'),
]

DIRECT_TEMPLATES = ('index', )

PAGE_URL = '../{slug}/'
PAGE_SAVE_AS = '../{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Disable everything else

TAG_URL = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# Theme

THEME = 'theme'
THEME_STATIC_DIR = 'theme'

# Static files

STATIC_PATHS = ['articles']

# Feeds

FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Other settings

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
SLUGIFY_SOURCE = 'basename'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 25

# Plugins

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'related_posts']

ASSET_SOURCE_PATHS = ['assets']
