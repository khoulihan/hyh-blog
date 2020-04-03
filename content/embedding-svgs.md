Title: Embedding SVGs in Pelican
Date: 2020-04-04 00:10
Modified: 2020-04-04 00:10
Category: Programming
Tags: python, blogging, pelican
Slug: embedding-svgs
Authors: Kevin Houlihan
Summary: A static alternative to Font Awesome's dynamic icon embedding.
Status: published

In my [inaugural post]({filename}/remember-blogs.md) I mentioned that one problem I had encountered while designing this blog was styling the SVG icons. I had grabbed a bunch of the individual icon files from [Font Awesome](https://fontawesome.com/), but because of the way SVGs, CSS and HTML interact, I wasn't able to colour them directly using CSS `color` or `fill` properties, and instead had to use `filter` properties (which I calculated using [this tool](https://codepen.io/sosuke/pen/Pjoqqp), so it wasn't too much of a hardship).

I also didn't particularly like that retrieving the icons involved numerous separate requests, nor the visible "pop-in" in Firefox that resulted from having them referenced as external files. The files are tiny, with the request overhead often as large or larger than the files themselves.

A further advantage that I was missing out on by not using Font Awesome as intended was that I couldn't use their handy `<i>` tag shortcuts for specifying the icons to use.

Now, I have taken steps towards solving all of these many problems!

## Just use Font Awesome normally you weirdo

Let's back up a sec and talk about why I didn't just use Font Awesome as intended in the first place (yes tldr; it is probably because I'm a weirdo).

Font Awesome has two ways that it can work: Web Fonts + CSS, or SVG + JavaScript. The former would involve retrieving an additional CSS file or two, as well as a couple of web fonts. The web font for the solid collection alone is 79.4KB - larger than anything else on this website. The JavaScript that would be required for the other method would likely be approaching 1MB in size - larger than this *entire* website so far! I want a lean, fast-loading, low-power website, and these approaches seem entirely at odds with those goals.

It also struck me as odd to be statically generating a site, yet also having the client browser swapping in SVG images. I've nothing against JavaScript, but clearly this is work that can be done in advance!

## Doesn't caching solve this problem?

Well... maybe? In same cases? But not necessarily.

The average size of an icon in Font Awesome's "solid" collection is 660B. A visitor would have to encounter over 1500 such embedded icons before downloading the JavaScript and caching it would be cheaper. The Web Fonts are much better, with caching the separate files becoming worthwhile after only 214 icons. That's about 5 views of this blog's index page, or 15 individual posts.

As such, if somebody reads 16 posts on this blog, they will have transferred more data than they would have if I'd used the Font Awesome web fonts. However, if 15 people read one post each and never visit again, the embedded approach comes out way ahead. So it very much depends on the traffic profile of the site, and I don't think this site is one that people will be checking in on daily.

Embedding also offers other advantages, such as reducing initial load times.

## Solutions

My solution is a [pelican plugin](https://github.com/khoulihan/pelican-embed-svg) that post-processes the generated HTML files and embeds any SVGs it finds, whether specified as `<img>` tags or `<i>` tags.

It also, crucially, sets the `fill` attribute of any SVG paths to `currentColor`, which causes the fill colour to be taken from the current CSS text colour.

Taking the plugin beyond being merely a static implementation of Font Awesome, it also supports embedding of arbitrary SVG files. This can be achieved either by using `<i>` tags with the class `pi` to search a custom icon set, or through `<img>` tags where the SVG file is referenced by URL.

## Future

The plugin probably has loads of rough edges at the moment. I haven't at all tested if it supports Font Awesome's more advanced behaviour, or even investigated how those features work, so there is a lot to be done there.

I may explore an approach that would combine the advantages of static generation with the advantages of a separate, cacheable SVG file. My initial thoughts on how to approach this plugin were to combine any referenced SVGs into a single file, and then reference them in the HTML using an SVG `<use>` tag. I need to learn a lot more about SVGs to know if that's even feasible.

I also want to try to support other icon frameworks that support a similar `<i>` tag shortcut, such as [Fork Awesome](https://forkaweso.me/Fork-Awesome/) and [Friconix](https://friconix.com).

In the meantime, it's serving my purposes already on this site.

<i class="fas fa-thumbs-up body-icon"></i> <i class="fas fa-bomb body-icon"></i> <i class="fas fa-cat body-icon"></i> <i class="fas fa-leaf body-icon"></i> <i class="fas fa-file body-icon"></i> <i class="fas fa-fist-raised body-icon"></i>