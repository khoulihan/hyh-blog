#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin Houlihan'
SITENAME = 'Hyperlink Your Heart'
SITEURL = 'http://localhost:8000'
SITE_LOGO = 'http://localhost:8000/images/logo.png'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['css-html-js-minify']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/http_your_heart'),
          ('Mastodon', 'https://mastodon.art/@hyperlinkyourheart'),)

# Custom social list that includes icons
SOCIAL_ICONS = (('Twitter', 'twitter.svg', 'https://twitter.com/http_your_heart'),
                ('Mastodon', 'mastodon.svg', 'https://mastodon.art/@hyperlinkyourheart'),
                ('Instagram', 'instagram.svg', 'https://www.instagram.com/hyperlinkyourheart/'),
                ('YouTube', 'youtube.svg', 'https://www.youtube.com/channel/UCc_O9Hp5UfQ-IHswi1H54Zg'),
                ('Twitch', 'twitch.svg', 'https://www.twitch.tv/hyperlinkyourheart'),
                ('Itch', 'itchio.svg', 'https://hyperlinkyourheart.itch.io/'),
                ('GitHub', 'github.svg', 'https://github.com/khoulihan'),)

# TODO: Populate this instead of explicit categories/tags links in theme
MENUITEMS = (('Home', ''),
            ('Categories', 'categories.html'),
            ('Tags', 'tags.html'),)

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/hyper'

SHOW_FULL_ARTICLE = True

HEADER_COLOR = '#777'

TYPOGRIFY = True

DISPLAY_PAGES_IN_MENU = True