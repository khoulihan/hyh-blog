Title: Remember Blogs?
Date: 2020-01-02 20:05
Modified: 2020-01-02 20:05
Category: Meta
Tags: indieweb, blogging, pelican
Slug: remember-blogs
Authors: Kevin Houlihan
Summary: The how and the why of this very blog right here.

I've read a lot of articles recently ([here's one](https://omarabid.com/the-modern-web)) lamenting the state of the web. Once distributed, egalitarian, ungovernable, and fast, now centralised, intentionally manipulative, and bloated both technically and conceptually. Even when you manage to fight your way through the popups demanding your attention or personal information, often what is underneath is not worth the effort - more likely a vehicle for advertising than for insight.

It's also incredibly power-hungry. It's hard to tie down an exact figure for exactly *how* power-hungry, but the internet as a whole [could account for up to 10% of global energy use](https://newrepublic.com/article/155993/can-internet-survive-climate-change). A good chunk of that is streaming video and music, which is a topic for another day, but of the power consumed in serving the web, some of it is related to actual valuable content that people want to see, and some of it is related to the trends described above. The latter is waste. At least bloated JavaScript and CSS frameworks can be cached, but advertising has to be constantly served anew.

So, anyway, all this to say... I've decided to start a blog.

## The Tech

My technical goals for this website are for it to be...

 + **Lightweight & fast to load** - I set up a WordPress site recently, on the best hosting I can afford. It is not lightweight or fast to load.
 + **Content focused** - Read one thing or read them all, but I'm sure you can only read one article at a time.
 + **Nice to look at** - Apparently it [doesn't take much](https://perfectmotherfuckingwebsite.com/). Also going for consistent *branding* between all my sites and profiles.
 + **Responsive** - Readable on phones as well as desktops!
 + **Easy to deploy** - I don't have time to configure and maintain a teetering stack of back-end technology, and if I have to move to different hosting at some point, I want it to be a simple task.
 + **Easy to update** - If writing posts is a chore, I won't ever do it.
 + **Hackable** - Created using technologies that I'm somewhat familiar with, so that it is feasible for me to modify or extend if I want/need to.
 
I decided almost immediately that a statically-generated site was going to be the best way to achieve most of those goals. I'm a big fan of Python, so although *hackability* could be achieved by a JavaScript or C# based generator, I checked out the Python ones first, and found plenty of viable options. I settled on [Pelican](https://blog.getpelican.com/) because it's...

 + **Popular** - It seems to be one of the more popular Python generators.
 + **Blog-oriented** - Some generators are geared towards documentation or are intended as replacements for content management systems, but that's not what I'm doing.
 + **Supports Markdown** - I'm sure reST is fine, but I already have to use Markdown elsewhere so I'd rather stick with that.
 + **Easy to update** - Just create a new Markdown file and run a command to rebuild.
 + **Extensible** - It includes a plugin system to modify the output.
 
I also decided to hand-craft my own theme, and to avoid a CSS framework. I love the look of Bootstrap, and how quick it is to get started with, but it's over 200kb and a lot of that is undoubtedly unnecessary for my needs. The spirit of the exercise is bare-bones and DIY!

### The Theme

The first step in hand-crafting a theme was... to find an existing theme to copy! [Atilla](https://github.com/arulrajnet/attila) was the closest to the style I was after, so I took a copy of that and gutted it of CSS and JavaScript and other elements that didn't meet my needs. Then I started building the CSS back up while trying to keep it as minimal as possible. It may not implement every feature supported by Pelican, but you can find it [on my Github](https://github.com/khoulihan/hyh-blog/tree/master/themes/hyper) if it seems like something you could adapt for your own needs.

One departure that I made from the standard Pelican configuration was to have the social media links be taken from a collection of tuples with three elements, so that I could specify both an icon and a title to use.

```python
# Custom social list that includes icons
SOCIAL_ICONS = (('Twitter', 'twitter.svg', 'https://twitter.com/http_your_heart'),
                ('Mastodon', 'mastodon.svg', 'https://mastodon.art/@hyperlinkyourheart'),
                ('Instagram', 'instagram.svg', 'https://www.instagram.com/hyperlinkyourheart/'),
                ('YouTube', 'youtube.svg', 'https://www.youtube.com/channel/UCc_O9Hp5UfQ-IHswi1H54Zg'),
                ('Twitch', 'twitch.svg', 'https://www.twitch.tv/hyperlinkyourheart'),
                ('Itch', 'itchio.svg', 'https://hyperlinkyourheart.itch.io/'),
                ('GitHub', 'github.svg', 'https://github.com/khoulihan'),
                ('Atom Feed', 'rss.svg', '/feeds/all.atom.xml'),)
```

I like that I can just throw custom configuration into the config file and then make use of it in the templates. However, it probably makes the theme less generally useful.

As it stands currently, loading this post requires less than 30kb to be transferred.

### Plugins

Currently, the only plugin I'm using is the [css-html-js-minify](https://github.com/getpelican/pelican-plugins/tree/master/css-html-js-minify) plugin that is available in the pelican-plugins repository. I haven't found anything I need to write my own plugin to handle yet, but I'm sure I will get to it.

One problem that needs solving is that the SVG icons are a big nuisance, because it doesn't seem to be possible to change their colour without using the CSS `filter` property, which is not nearly as convenient as just setting the colour directly. In order to do that, using the `fill` property, I would have to embed the SVGs, or reference them as symbols in a `<use>` tag within an `<svg>` tag. The individual icon files (from [FontAwesome](https://fontawesome.com/)) aren't set up like that, and I didn't want to use their spritesheet because it is rather large.

What I might do in the future is write a plugin to compile the individual files into a single spritesheet of symbols, then find and replace any references to them with appropriate `<svg>` tags. Essentially this will be doing the job that the FontAwesome toolkit usually does in the browser.

## The Content

Uuuh... I'll get back to you on that. Things I like, things I do, that sort of thing.

## Feedback

There's a couple of different strategies for allowing comments on a static site - I'm not going to attempt them for now, and perhaps never will! If you have any feedback or thoughts there are many ways to reach me, such as [Mastodon](https://mastodon.art/@hyperlinkyourheart) or [Twitter](https://twitter.com/http_your_heart), and I think that's just fine.