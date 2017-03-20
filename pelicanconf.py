#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Xose Ribes'
SITENAME = 'xose security blog'
SITEURL = 'http://x0se.com'
THEME = 'Flex'
PATH = 'content'
SITELOGO = SITEURL + '/images/foto.jpg'
TIMEZONE = 'Europe/Paris'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

DEFAULT_LANG = 'es'
I18N_TEMPLATES_LANG = 'es'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS = 'UA-41818805-2'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/x0s3'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'css']

EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'
