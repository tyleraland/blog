#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tyler A Land'
SITENAME = u'Tech and Life'
SITEURL = ''
SITESUBTITLE = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_RETENTION = ['.git']

# Extra Menu items
MENUITEMS = (('Github', 'http://github.com/tyleraland'),)

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# 
SOCIAL = (('Github Profile', 'http://github.com/tyleraland'),
          ('LinkedIn Resume','http://www.linkedin.com/in/tyleraland'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#READERS = {'html': None}

Typogrify = True

DISQUS_SITENAME = "tyleraland"
GOOGLE_ANALYTICS = 'UA-64863813-1'

THEME = "pelican-themes/blueidea"
#THEME = "pelican-themes/Responsive-Pelican"
#THEME = "pelican-themes/bootstrap2"
#THEME = 'pelican-themes/tuxlite_tbs'
#THEME = 'pelican-themes/foundation-default-colours'
#THEME = 'pelican-themes/gum'
#THEME = 'notmyidea'
#THEME = 'pelican-themes/mg'

# BlueIdea options

#DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']

MATH_JAX = {}
