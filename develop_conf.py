#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = 'Yasser Gonzalez Fernandez'
SITENAME = 'Personal Website'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'


DIRECT_TEMPLATES = ('index', 'archives')

MENUITEMS = [
    ('Home', '/'),
    ('Resume', '/resume/'),
]


DISPLAY_PAGES_ON_MENU = False
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = 'articles/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''


# Feed generation disabled when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

