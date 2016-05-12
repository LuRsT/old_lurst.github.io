#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gil'
SITENAME = u'Lumbercoder'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'extras/htaccess',
    'extras/CNAME',
]
EXTRA_PATH_METADATA = {
    'extras/htaccess': {'path': '.htaccess'},
    'extras/CNAME': {'path': 'CNAME'},
}

DEFAULT_PAGINATION = False

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
