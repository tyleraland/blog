#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from os import path

### basic theme Options
AUTHOR = u'Tyler A Land'
# This doesn't affect the displayed title
SITENAME = u'superuser blog'
# SITEURL is also defined in publishconf.py; blank URL is for opening with file://
#SITEURL = 'http://tyleraland.github.io/techandlife'
SITEURL = 'http://localhost:8000'
SITESUBTITLE = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
FAVICON = path.join(SITEURL, 'favicon.ico')

### Flex theme options
SITETITLE = 'superuser'
#SITELOGO = ''
SITELOGO = 'http://i1045.photobucket.com/albums/b453/tyleraland/2015-08-29_headshot_small_zpsto26xaw5.jpg'
COPYRIGHT_YEAR = datetime.now().strftime("%Y")
MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = True

###
PATH = 'content'

STATIC_PATHS = ['images', 'extra/favicon.ico']

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
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
#MENUITEMS = (
#             ('Github', 'http://github.com/tyleraland'),
#            )

## Blogroll
#LINKS = (('Privacy Policy', 'pages/privacy-policy.html'),)
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# NOTE: Flex theme requires that these have a specific case-sensitive name
SOCIAL = (
          ('envelope-o', 'mailto:tyleraland-at-gmail-dot-com'),
          # Waiting for https://github.com/alexandrevicenzi/Flex/issues/2 to be merged
          #('email', 'mailto:x@y.com'),
          ('github-alt', 'http://github.com/tyleraland'),
          ('linkedin','http://www.linkedin.com/in/tyleraland'),
#          ('facebook','https://www.facebook.com/tyler.a.land'),
#          ('google', 'http://plus.google.com/+TylerLandA/posts'), # Needs polishing
          ('rss', 'feeds/all.atom.xml'),
         )

DEFAULT_PAGINATION = 10

# Use document-relative URLs when developing
#RELATIVE_URLS = True

#READERS = {'html': None}

Typogrify = True

# Plugin build dir
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'sitemap']

SITEMAP = {'format': 'xml',
           'priorities': {
               'articles': 0.6,
               'indexes': 0.6,
               'pages': 0.5,
           },
           'changefreqs': {
               'articles': 'monthly',
               'indexes': 'daily',
               'pages': 'monthly',
           }
}

#THEME = "pelican-themes/blueidea"
#THEME = "notmyidea"
#THEME = 'pelican-themes/tuxlite_tbs'
#THEME = 'pelican-themes/foundation-default-colours'
#THEME = 'pelican-themes/gum'
#THEME = 'pelican-themes/mg'
#THEME = 'pelican-themes/zurb-F5-basic'
THEME = 'pelican-themes/Flex'
