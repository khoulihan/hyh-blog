Title: Energy Usage Update
Date: 2021-05-27 13:20
Modified: 2025-06-12 15:23
Category: Meta
Tags: indieweb, blogging, pixelart
Slug: energy-usage-update
Authors: Kevin Houlihan
Summary: An update on the energy efficiency of this blog.

When I [started this blog]({filename}/remember-blogs.md), one of my [goals]({filename}/embedding-svgs.md) was for it to be lean and efficient, both to improve the reader's experience and to reduce the power usage involved in serving it.

I've been planning recently to write a post on a related topic - the energy efficiency of the Python language and how using it as the backend or API of a more dynamic website would fit with those same goals. In preparation for that, I thought to check in on this blog and whether it is still as lean as it was back when I was figuring out how to embed the SVG icons in it.

Unfortunately, it seems that it is not. Unlike one of my inspirations, [low-tech magazine's solar powered website](https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html), I never found a solution for reducing the size of image files. For my posts about TV shows and movies I use fairly low quality JPEGs. But for my art and game dev posts I have been unwilling to compromise, and, frankly, a bit lazy, and have just been throwing large PNGs and GIFs into my posts without thinking about their size.

As a result, loading the index of this site now transfers 1.7MB if nothing is already cached. The text content and CSS are in the tens of kilobytes, with the rest being images. This is comparable to the initial load of many corporate news sites and large blogs with all their tracking javascript and ads blocked - an improvement over the norm perhaps, since I'm not doing any of the tracking or advertising that have become such a burden on the web, but not particularly notable. This site is now only in the [57th percentile according to websitecarbon.com](https://www.websitecarbon.com/website/blog-hyperlinkyourheart-com/).

For pixel art, one solution does present itself immediately. For my [portfolio site](https://portfolio.hyperlinkyourheart.com), all of the artwork is sent to the browser at 1x resolution and resized there by an integer factor by a small amount of javascript, and perhaps the same thing could be achieved with css. The index of that site is under 400kB despite including all of my artwork, and does not require specially resized image thumbnails or anything like that. I could do the same thing here instead of throwing manually resized art into posts.

I'm less sure what to do about screenshots and screencaps. The solution used by low-tech magazine doesn't really work for me, I think it compromises the readability of the images too much and doesn't fit this site's aesthetic. I tried a number of different techniques for vectorising, posterising and dithering screencaps from TV shows and movies to reduce the number of colours, but they didn't result in significant savings. On the other hand, they did actually look kind of cool and stylised!

![Vectorised Beth Harmon]({static}/images/energy-usage-update/parkchesscrowd_vector.jpg "Vectorised Beth Harmon")

Something I should probably try is scaling such images down significantly and then back up to the required display size in CSS. Obviously this will degrade the quality, but it might be an acceptable trade-off.

Screenshots of things like a text-editor or IDE are even more problematic - if the quality is degraded there they are probably not useful. I will probably just have to try to keep that kind of thing to a minimum, and use tighter crops where necessary.

It's easy to become complacent about efficiency when computers are so powerful that a few tens or hundreds of kilobytes don't seem to cause them any strain, but when you have that mindset they can quickly add up to quite a significant waste of time and power. I think this is well demonstrated by [USA Today's pissy response to the GDPR](https://daringfireball.net/linked/2018/05/27/usa-today-gdpr), where instead of the usual 5.2MB bloated garbage site, readers from the EU were served a lean, content focused site that loaded almost instantly and didn't track them.

Nothing I do is going to have the kind of impact that a site like USA Today improving their efficiency would have, purely because of the scale of the traffic involved, but I still want to try to do better.
