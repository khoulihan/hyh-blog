Title: Big Lick
Date: 2025-06-12 15:36
Category: Art
Tags: pixelart, portrait, dogs, nfts, politics, foss, capitalism, genai
Slug: big-lick
Authors: Kevin Houlihan
Summary: A pixel art painting I did of my brother-in-law and one of my parent's dogs. Also some chat about why I haven't done any art in ages.
Status: published
og_image: images/big-lick/BigLick06_x3.png

[![A pixel art painting of a reclining man being licked on the nose by a small dog.][painting]][portfolio]

Oh boy, it's been *a while* since I posted any art! I think I was put off the whole endeavour back when NFTs were the big thing and a lot of artists I respected were showing their ass over them. I had also started a piece that was maybe a bit too complex for me, and I started to dread working on it, and to feel guilty about not working on it, and then I started thinking that art for its own sake was just a distraction from what I had actually set out to do, which was to make a videogame. I started putting a lot more time into developing my dialogue graph editor for [Godot][godot] instead (since given the name ["Digression"][digression]), and a tiny bit into the mechanics of the game, and just didn't think about art for a while.

Since then of course, NFTs seem to have basically disappeared from the zeitgeist, their promises of vast riches and libertarian copyright enforcement for artists unfulfilled, and all the artists have been replaced by machines that can pull, on command, statistically likely representations of anything you can imagine out of the aggregate of all visual media on the Internet. As if it wasn't bad enough that a huge chunk of it was already owned by giant corporations, capital is now grinding up our culture into a meaningless, commodified slurry and feeding it back to us. The pretense of having the interests of artists at heart has been replaced by a naked, shameless grasping. And with governments falling over each other to attract AI investment, it seems unlikely that there is going to be any recourse for individual creators any time soon.

So I'd like to say, then, that the reason I did this piece was that I'm an obstinate luddite who refuses to accept that the age of human creativity is over, and that I had to do my part to help preserve it. But actually I just needed to do something for my sister's birthday, and it occurred to me that I'd never done any pixel art for her even though she is someone who would probably appreciate it. And isn't that a fine, *human* motivation for getting back into art?

She did appreciate it, btw. I'm not sure she would have if I had *engineered her a prompt* instead.

## Tools and Process

I used to use [Pyxel Edit][pyxel] for all my art, but it is proprietary and Windows only and I couldn't get it running in Wine since I switched to Fedora. So I have switched to [Pixelorama][pixelorama] instead, an open source pixel art paint program developed in Godot. There are a few things that Pyxel Edit did better, but Pixelorama is a very decent substitute. I like that you can put different tools on your left and right mouse buttons, though it tripped me up a lot initially. One thing I really miss is the ability to update a colour globally from the palette. It was great to be able to completely change direction with the colours without having to repaint anything. That was something I used to do quite often and at any stage of the process, sometimes even when a piece was otherwise finished. Maybe I will look into contributing to the project, since I am somewhat familiar with Godot...

When I tried adding the reference image it just automatically put it under the canvas, which I wasn't expecting, but since it did I decided to just trace a rough outline of the figures for expediency.

Unusually for me I did a lot of anti-aliasing in this one, and I really liked how that turned out, especially on the face. More of that in the future.

Also unusually I did not pay much attention at all to how many colours I was using. There is relatively little dithering as a result, and what is there is mostly for texture rather than giving the appearance of additional colours. I usually like the challenge of keeping colour counts low, but it was nice to be more relaxed about it for a change - I ended up using 64, and it's not as if the resulting palette is general purpose!

## Timelapse

The timelapse for this one is a bit of a mess. My previous method of capturing them doesn't work in Wayland, and I overlooked a feature in Pixelorama that would have allowed me to evaluate the canvas without having to zoom in and out constantly. I've since discovered that it has a recorder feature that can save a copy of the canvas after every change, so I will likely try that for my next piece and the timelapse should have a *very* different look...

[![Big Lick Timelapse][ytimage]][ytlink]

[painting]: {static}/images/big-lick/BigLick06_x3.png "Big Lick"
[portfolio]: https://portfolio.hyperlinkyourheart.com/big-lick.html
[godot]: https://godotengine.org/ "Godot Engine"
[digression]: https://github.com/khoulihan/digression "Digression Dialogue Graph Editor (Github)"
[pyxel]: https://pyxeledit.com/ "Pyxel Edit"
[pixelorama]: https://github.com/Orama-Interactive/Pixelorama "Pixelorama (Github)"
[ytimage]: https://img.youtube.com/vi/FPiJwkzLr0U/0.jpg
[ytlink]: https://www.youtube.com/watch?v=FPiJwkzLr0U

