Title: Gemini Launch!
Date: 2021-06-26 14:59
Category: Gemini
Tags: python, pelican, blogging, smolnet
Slug: gemini-launch
Authors: Kevin Houlihan
Summary: All about the launch of my Gemini capsule, and how it is generated and hosted.
Status: published

In the olden-times, before the Web became basically synonymous with the Internet itself in many people's minds, there was another, competing hypertext protocol: [Gopher][gopher].

I say "was", but of course Gopher never really went away - it was kept alive by enthusiasts, and in recent years there has been a resurgence of interest in it as a sort of haven from the ubiquitous surveillance and relentless commercialisation of the Web.

I've long been interested in Gopher (I even [made a game about it][gophersgame]), and have intended to start a phlog for a while without ever going ahead with it. Something about it always just seemed a little bit awkward and off-putting. I was torn between using Gophermap (i.e. menu) files for everything, or using plain text for posts and sacrificing any hypertextuality. I was torn between finding the need to wrap text to be cool and retro, or a hassle that results in an inferior experience for both creating and consuming content.

[Gemini][gemini] is a new protocol which takes inspiration from both Gopher and the Web, and from a certain perspective, improves on both.

When I heard about Gemini I didn't really get it at first. I thought it was just Gopher with SSL, which is nice, but I figured I'd get set up on Gopher first and then consider a Gemini mirror. A few days ago I saw a screenshot of the Lagrange browser on Mastodon and started to look into it a bit more. When I realised just how many issues of both Gopher and the web it addresses, I was hooked! I spent several days after that setting up [a capsule][gemlog] (the Gemini equivalent of a "site").

[![My Gemlog in Lagrange]({static}/images/gemini-launch/gemlog.png "My Gemlog in Lagrange")][gemlog]

## Static Generation

After experimenting with a Gemini server for a bit and creating a few static `text/gemini` files, I decided that I wanted to statically generate my gemlog the same way that I do my blog. I expected to have to write something from scratch to do this, but after some experimentation I was able to get the [Pelican static site generator][pelican] (which I also use for my blog) to both read and output `.gmi` files. It does take a bit of configuration however, and I had to monkeypatch a couple of methods in Pelican.

Unfortunately this means that it is only guaranteed to work with the current version of Pelican, 4.6.0, and could break at any time. Nonetheless, the plugin is [available on GitHub][gemican] if you want to try it out.

### Gemini Reader

The first thing required was a custom "Reader" that can handle `.gmi` files instead of the usual Markdown or reStructuredText files. It's simple enough - it just parses the file up to the first blank line as metadata, and the rest of the content is returned unmodified, since we are also going to output the same format.

```python
class GeminiReader(BaseReader):
    enabled = True

    file_extensions = ['gmi', 'gemini']

    def read(self, filename):
        metadata = {}
        content = ""
        with open(filename, mode='r') as f:
            end_of_meta = False
            while not end_of_meta:
                current = f.readline()
                if current == '\n' or current == '':
                    end_of_meta = True
                    continue
                current = current.strip()
                split = current.split(': ')
                metadata[split[0].lower()] = split[1]
            # After the first blank line, the rest is content.
            content = f.read()

        parsed = {}
        for key, value in metadata.items():
            parsed[key] = self.process_metadata(key, value)

        return content, parsed
```

### Handling Internal Links

Pelican has a mechanism for linking to content internal to the site where you start the URL as `{static}` or `{filename}` and it replaces those with the appropriate paths during generation. However, this didn't work with the Gemini link syntax - the replacement is based on a regular expression that assumes the placeholder will be found in an attribute of a HTML element.

I couldn't find any setting or hook in the plugin system to alter this regular expression. There is a setting to customise the part that specifies the braces, so you could change the placeholders to `¿¿static??` or something if you like, as long as it is still found in HTML. It seemed like my only option was to replace the method where the problem regex pattern is defined, and use something that matches Gemini links instead.

```python
def _get_intrasite_link_regex(self):
    intrasite_link_regex = self.settings['INTRASITE_LINK_REGEX']
    regex = r"(?P<markup>=> )(?P<quote>)(?P<path>{}(?P<value>[\S]*))".format(intrasite_link_regex)
    return re.compile(regex)
```

You'll notice this also has to include a "quote" group because that was present in the HTML version and was expected elsewhere - here it will always be an empty string.

Unfortunately, the problems didn't end there. I found that the placeholders were removed, but not replaced with the absolute URL of the capsule. This turned out to be because urllib is used to join the URL components, and it doesn't recognise the gemini protocol. To get around this I had to replace another method, and make a call to a wrapper around `urllib.urljoin`.

```python
def _urljoin(base, url, *args, **kwargs):
    is_gemini = base.startswith('gemini://')
    if is_gemini:
        base = base.replace('gemini://', 'https://')
    result = urljoin(base, url, *args, **kwargs)
    if is_gemini:
        result = result.replace('https://', 'gemini://')
    return result
```

### Gemini Output

Pelican uses Jinja2 for its templating, which is happy to work with any type of text file, so creating `.gmi` templates wasn't an issue. Handily, there is a setting to look for templates with extensions other than `.html`.

```python
THEME = 'themes/hypergem'
TEMPLATE_EXTENSIONS = ['.gmi', '.gemini']
```

To get Pelican to output files with a `.gmi` extension instead of `.html`, there are a bunch of settings for the different parts of the site. A single "extension" setting like for the templates would be nice, but whatchagonnado? I took the opportunity to customise the article location and file names as well.

```python
# These settings are required to output files as .gmi instead of .html
ARTICLE_URL = 'articles/{date:%Y}-{date:%m}-{date:%d}-{slug}.gmi'
ARTICLE_SAVE_AS = ARTICLE_URL

DRAFT_URL = 'drafts/{slug}.gmi'
DRAFT_SAVE_AS = DRAFT_URL

PAGE_URL = 'pages/{slug}.gmi'
PAGE_SAVE_AS = PAGE_URL

DRAFT_PAGE_URL = 'drafts/pages/{slug}.gmi'
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL

AUTHOR_URL = 'author/{slug}.gmi'
AUTHOR_SAVE_AS = AUTHOR_URL

CATEGORY_URL = 'category/{slug}.gmi'
CATEGORY_SAVE_AS = CATEGORY_URL

TAG_URL = 'tag/{slug}.gmi'
TAG_SAVE_AS = TAG_URL

ARCHIVES_SAVE_AS = 'archives.gmi'
AUTHORS_SAVE_AS = 'authors.gmi'
CATEGORIES_SAVE_AS = 'categories.gmi'
TAGS_SAVE_AS = 'tags.gmi'
```

### Theme

I haven't got much to say about this. I wanted the article links to be a bit more descriptive than just the date and title, so I did something similar to what medusae.space does and included the article summary, the category, and the tags.

It's close to general purpose but not quite - I added a custom `SITELOGO` setting that is used on the index page with an ASCII art version of my logo generated using [ascii-generator.site][ascii], and there is also a custom template for the custom landing page. The index is renamed using a setting, and another page is renamed to index.gmi to take its place. This is so if I want to add content that isn't generated by Pelican, I have the scope to do so.

```python
INDEX_SAVE_AS = 'gemlog.gmi'
```

```
Title: Hyperlink Your Heart
Date: 2021-06-23 22:59
Slug: index
Authors: Kevin Houlihan
Summary: Capsule index
URL: index.gmi
save_as: index.gmi
Template: capsule_intro
Status: hidden
```

## Hosting

I'm serving the capsule using [Jetforce][jetforce] from a first generation Raspberry Pi which I had lying around and haven't done anything with in a while. There was nothing really involved in setting it up beyond what is described in the documentation, except that I installed it in a virtualenv.

I also took steps to make sure it is running as a dedicated user with no permissions to anything else on the system.

![Real professional operation]({static}/images/gemini-launch/hosting.jpg "Real professional operation")

## Future

I'm not sure what's next, but I'm excited! I might discuss with the Pelican crew if there are any ways around the issues I encountered that I might have overlooked, or if it could be adapted to be more suited to non-HTML output. If not, maybe a Gemini fork is in order. I have no idea if there are further issues with it beyond the functionality that I've used.

I have quite a few posts to port over from my blog yet, and I need to get some image optimisation happening there like I have here. Besides that, I guess all I have to do is get to know the community!

## Visit My Capsule (and Beyond)

If you're already familiar with Gemini please [check out my capsule][gemlog].

If you're not, well, I still encourage you to visit, but I should probably give you some guidance on getting started.

If you just want to dip your toes you can browse the Gemini network using a HTTP proxy ([here's one][vulpes], and [another][mozz]). For what I would consider the "full experience" you will need a dedicated browser. I've been using [Lagrange][lagrange], and highly recommend it, but there are a [whole bunch of others][gemsoft] if that doesn't suit you. Many of them also support Gopher, which makes browsing both into a seamless experience outside of the modern Web.

When you want to move beyond my capsule, here are some others I recommend:

* Medusae.space, a content directory: [gemini://medusae.space][medusae]
* Station, a social network with user accounts: [gemini://station.martinrue.com/][station]
* Geddit, an anonymous link aggregator: [gemini://geddit.glv.one/][geddit]
* Astrobotany, a community garden game: [gemini://astrobotany.mozz.us/][astro]
* A gemlog post about the "smolnet", which explains the appeal far better than I ever could: [gemini://republic.circumlunar.space/users/maugre/200701-smolnet.gmi][smolnet]

I leave you with my anxious young poppy, Jennifer, on AstroBotany:
```



            O
            |
           \o
            |o
           \/
.  , _ . ., l, _ ., _ .  
^      '        `    '

name  : "Jennifer"
stage : anxious young poppy
age   : 2 days
rate  : 1st generation (x1.0)
score : 326788
water : |██████████| 100%
bonus : |          | 2%
```

[gopher]: https://en.wikipedia.org/wiki/Gopher_(protocol) "Gopher entry on Wikipedia"
[gophersgame]: https://hyperlinkyourheart.itch.io/gophers "Gophers on itch.io"
[gemini]: https://gemini.circumlunar.space/docs/faq.gmi "Gemini FAQ"
[gemlog]: gemini://gemini.hyperlinkyourheart.com/ "My capsule"
[pelican]: https://blog.getpelican.com/ "Pelican static site generator"
[gemican]: https://github.com/khoulihan/pelican-gemini "pelican-gemini plugin"
[ascii]: https://ascii-generator.site/ "ASCII Generator"
[jetforce]: https://github.com/michael-lazar/jetforce "Jetforce github"
[vulpes]: https://proxy.vulpes.one/gemini/gemini.hyperlinkyourheart.com "Vulpes.one proxy"
[mozz]: https://portal.mozz.us/gemini/gemini.hyperlinkyourheart.com "Mozz.us proxy"
[lagrange]: https://github.com/skyjake/lagrange "Lagrange browser GitHub"
[gemsoft]: https://gemini.circumlunar.space/software/ "Gemini software list"
[medusae]: gemini://medusae.space "Medusae.space content directory"
[station]: gemini://station.martinrue.com/ "Station - where capsuleers hang out"
[geddit]: gemini://geddit.glv.one/ "Geddit?"
[astro]: gemini://astrobotany.mozz.us/ "Astrobotany"
[smolnet]: gemini://republic.circumlunar.space/users/maugre/200701-smolnet.gmi "The smolnet of smol things"
