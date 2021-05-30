Title: Image Optimisation
Date: 2021-05-30 00:27
Category: Meta
Tags: indieweb, blogging
Slug: image-optimisation
Authors: Kevin Houlihan
Summary: Image optimisation experiments and a helpful Pelican plugin

In the [last instalment]({filename}/energy-usage-update.md) of my epic blogging saga I recounted my discovery that the index page of this site had grown to over 1.7MB of content when loaded fresh, largely due to the images. One of my goals for this site was that it be lean - fast to load and energy efficient - and it was not meeting that goal at all. Clearly avoiding Javascript and CSS frameworks was not enough!

I immediately started thinking about how to improve the situation. Though I had previously ruled out the approach used by [Low-tech magazine's solar-powered website][lowtech] because I didn't think it would fit my aesthetic, I decided to see if dithering coloured, rather than monochrome, PNGs would work better for me, and improve on the size and quality of an appropriately-sized 75% quality JPEG.

## PNG Thunderdome

The one to beat - baseline 75% JPEG, Size: 16.1kb

![melanie-pointing_alpha_baseline.jpg]({static}/images/image-optimisation/melanie-pointing_alpha_baseline.jpg "melanie-pointing_alpha_baseline.jpg: 16.1kb"){: .poi-no-optimise}

Using [Pillow][pillow] and the same [hitherdither][hitherdither] library that Low-tech magazine used for their site, I iterated on a script that output hundreds of compressed variations of a given image using different dithering algorithms and parameters.

The best results I found were with the Bayesian algorithm with a 32 colour palette, a 2x2 matrix, and an image size half the expected display size. This produced a result that was relatively readable, and reminiscent of pixel art. The size savings varied by image - sometimes up to 10kB, but often only 2-3kB as for this example. These savings are modest compared to the loss in detail, and I think this approach could only be considered because of the unique aesthetic it produces.

Palette: 32, Dither: bayer, Threshold: 256/8-256-256/8, Order: 2, Size: 13.9kb

![melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh8-1-8.png]({static}/images/image-optimisation/melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh8-1-8.png "melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh8-1-8.png: 13.9kb"){: .poi-no-optimise}

The three "threshold" parameters expected by hitherdither were a bit of a mystery to me. Through trial and error I found that some produced much smaller images, but unfortunately not at a level of quality that I found acceptable. Lower palette sizes also resulted in savings, but below 32 colours they started to look too abstract and unreadable to me.

Palette: 32, Dither: bayer, Threshold: 256/2-256-256/2, Order: 2, Size: 9.6kb

![melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh2-1-2.png]({static}/images/image-optimisation/melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh2-1-2.png "melanie-pointing_alpha_halved_pal32_dithbayer_order2_thresh2-1-2.png: 9.6kb"){: .poi-no-optimise}

## A Challenger Appears

I was about ready to commit to this approach and start converting all the images when my wife reminded me that WEBP exists! After converting a few of my test images to WEBP it was clear that it had my dithered PNGs beat - half the size of the JPEG without any loss of quality.

80% quality WEBP, Size: 9.9kb

![melanie-pointing_alpha_baseline.webp]({static}/images/image-optimisation/melanie-pointing_alpha_baseline.webp "melanie-pointing_alpha_baseline.webp: 9.9kb"){: .poi-no-optimise}

Apparently [support for WEBP][webp-support] is pretty good these days, but there are a couple of annoying outliers - Safari only supports it on Big Sur, and IE11 still exists, as I'm sure it always will.

As such, I decided I should probably try and fallback gracefully to a JPEG or PNG where WEBP isn't supported. This can be achieved using `<picture>` and `<source>` elements to allow the browser to choose the format it likes best.

```html
<picture>
    <source type="image/webp" srcset="{optimal image url}"/>
    <source type="image/jpeg" srcset="{compatible image url}"/>
    <img src="{compatible image url}"/>
</picture>
```

## Let's Automate

The above HTML snippet presents a problem - my posts are not written in HTML but in Markdown, and processed by [Pelican][pelican] into HTML, and that process just results in an `<img>` tag by default.

I threw together [a quick Pelican plugin][plugin] to post-process the generated HTML and replace any `<img>` tags with `<picture>` tags, if the referenced images could be replaced with WEBPs. It also processes the referenced images to create scaled JPEG/PNG versions as well as the WEBP version, so I don't have to do any of that manually either.

## Results

The index of the blog is now 778kB at the time of writing - so reduced by over half! I did also replace a particularly large and troublesome GIF with a static image as well, and converted some PNGs to JPEGs. This results in greater savings because the plugin converts PNGs to lossless WEBPs and JPEGs to lossy ones.

The plugin is actually not even working fully yet - for some reason it is missing some `<img>` tags on the index pages, leaving them serving their original unprocessed files.

I also haven't done anything about the pixel art images, which if served at their original resolution could be a significant saving.

So in short, [huge progress][website-carbon], but still much scope for improvement!

I am almost sorry I'm not going to end up using these dithered PNGs though...

![Tracer and Chun-Li]({static}/images/image-optimisation/tracer_alpha_halved_pal32_dithbayer_order2_thresh8-1-8.png "Wow looks like videogams"){: .poi-no-optimise}

[pelican]: https://blog.getpelican.com/ "Pelican static site generator"
[plugin]: https://github.com/khoulihan/pelican-optimise-images "pelican-optimise-images plugin"
[webp-support]: https://caniuse.com/?search=webp "WEBP support"
[hitherdither]: https://github.com/hbldh/hitherdither "hitherdither library"
[pillow]: https://python-pillow.org/ "Pillow"
[lowtech]: https://solar.lowtechmagazine.com/about.html "Low-tech magazine solar powered web site"
[website-carbon]: https://www.websitecarbon.com/website/blog-hyperlinkyourheart-com/ "76th percentile for energy efficiency"
