#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

SITENAME = 'Blog &#8211; Yasser Gonzalez'
AUTHOR = 'Yasser Gonzalez Fernandez'

# Put a static page in / and the blog in /blog

SITEURL = '/'

PATH = 'content'
OUTPUT_PATH = 'output'

DIRECT_TEMPLATES = ('index', )

INDEX_SAVE_AS = 'blog/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Blog', '/blog/'),
    ('Resume', '/resume/'),
]

# Disable everything else

DIRECT_TEMPLATES = ['index']

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

STATIC_PATHS = ['blog']

# Feeds

FEED_ALL_ATOM = 'blog/atom.xml'
FEED_ALL_RSS = 'blog/rss.xml'
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
PLUGINS = ['assets', 'related_posts', 'sitemap', 'render_math']

ASSET_SOURCE_PATHS = ['assets']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly'
    }
}
