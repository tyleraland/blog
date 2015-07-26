#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tyler A Land'
SITENAME = u'Tech and Life'
# SITEURL is also defined in publishconf.py; blank URL is for opening with file://
#SITEURL = 'http://tyleraland.github.io/techandlife'
SITEURL = ''
SITESUBTITLE = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/favicon.ico']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

EXTRA_PATH_METADATA = {
#     'extra/404.html': {'path': '404.html'},
#     'extra/403.html': {'path': '403.html'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/.htaccess': {'path':  '.htaccess'},
#     'extra/crossdomain.xml': {'path':  'crossdomain.xml'},
     'extra/favicon.ico': {'path':  'favicon.ico'},
}

# Don't delete .git history when generating output files
OUTPUT_RETENTION = ['.git']

# Extra Menu items
# MENUITEMS = (('Github', 'http://github.com/tyleraland'),)

## Blogroll
LINKS = (('Privacy Policy', 'pages/privacy-policy.html'),)
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# 
SOCIAL = (('Github Profile', 'http://github.com/tyleraland'),
          ('LinkedIn Resume','http://www.linkedin.com/in/tyleraland'),)

DEFAULT_PAGINATION = 10

# Use document-relative URLs when developing
RELATIVE_URLS = True

#READERS = {'html': None}

Typogrify = True

# Plugin build dir
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']

#THEME = "pelican-themes/blueidea"
#THEME = "pelican-themes/Responsive-Pelican"
#THEME = "pelican-themes/bootstrap2"
#THEME = 'pelican-themes/tuxlite_tbs'
#THEME = 'pelican-themes/foundation-default-colours'
#THEME = 'pelican-themes/gum'
#THEME = 'notmyidea'
#THEME = 'pelican-themes/mg'
THEME = 'pelican-themes/zurb-F5-basic'

# BlueIdea options

#DISPLAY_CATEGORIES_ON_MENU = False

