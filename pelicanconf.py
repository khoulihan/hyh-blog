#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin Houlihan'
SITENAME = 'Hyperlink Your Heart'
SITESUBTITLE = "Until there's nothing left."
SITEURL = 'http://localhost:8000'
SITE_LOGO = 'http://localhost:8000/images/logo.png'

DEFAULT_OPENGRAPH_IMAGE = 'images/opengraph/OpenGraph_Studio_Yellow.png'
DEFAULT_TWITTER_CARD_IMAGE = DEFAULT_OPENGRAPH_IMAGE

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', '../pelican-embed-svg', '../pelican-optimise-images', '../pelican-gopher', './plugins']
PLUGINS = [
    'css-html-js-minify',
    'pelican_embed_svg',
    'pelican_optimise_images',
    #'pelican_gopher',
]

#PES_FONT_AWESOME_PATH = 'themes/hyper/static/font-awesome'
PES_EMBED_IMG_TAGS = True
PES_SET_IMG_FILL = True

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category.{slug}.atom.xml'
TAG_FEED_ATOM = 'feeds/tag.{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Mastodon', 'https://mastodon.ie/@hyperlinkyourheart'),)

# Custom social list that includes icons
SOCIAL_ICONS = (('Mastodon', 'fab fa-mastodon', 'https://mastodon.ie/@hyperlinkyourheart'),
                ('YouTube', 'fab fa-youtube', 'https://www.youtube.com/channel/UCc_O9Hp5UfQ-IHswi1H54Zg'),
                ('PeerTube', 'fas fa-play-circle', 'https://makertube.net/c/hyperlinkyourheartart/videos'),
                ('Itch', 'fab fa-itch-io', 'https://hyperlinkyourheart.itch.io/'),
                ('GitHub', 'fab fa-github', 'https://github.com/khoulihan'),
                ('Atom Feed', 'fas fa-rss', '/feeds/all.atom.xml'),)

MENUITEMS = (('Home', ''),
            ('Categories', 'categories.html'),
            ('Tags', 'tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/hyper'

SHOW_FULL_ARTICLE = False

HEADER_COLOR = '#777'

TYPOGRIFY = True

DISPLAY_PAGES_IN_MENU = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.sane_lists': {},
    },
    'output_format': 'html5',
}
