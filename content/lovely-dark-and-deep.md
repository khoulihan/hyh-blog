Title: Lovely, Dark and Deep
Date: 2025-06-14 18:28
Category: Game Development
Tags: ludum-dare, godot, godot4, pixelart, music
Slug: lovely
Authors: Kevin Houlihan
Summary: Post-mortem and results for my Ludum Dare 57 entry.
Status: published
og_image: images/lovely-dark-and-deep/cover_image.png

[![Pixel art of a forest with a man on a bicycle in the foreground, and the text "Lovely, Dark and Deep"][headerimage]][itch]

Back in April I took part in Ludum Dare 57, which had the theme "Depths". As usual I was eager to take [Digression][digression] for a spin and see how much it had improved since its last outing for [Ludum Dare 48][out-of-gas], and this time I managed to come up with something that allowed me to do that. Coincidentally, the theme for LD48 was almost the same ("Deeper and Deeper"), and I ended up making a somewhat similar game in some respects!

## The Concept

The initial concept was one I've had kicking around for a while, of a post-apocalyptic trading game with two phases to the gameplay - one where you travel between outposts by car, possibly having to engage in combat or other encounters, and another at outposts where you have to trade and maintain your car. I think of it as terrestrial [Escape Velocity][ev], though the travel would undoubtedly be much simplified for a jam game.

Of course none of the elements of that idea are set in stone. I usually think of it as being set in a desert (the ol' Mad Max influence I suppose), but in this case I wasn't sure if deserts *have* depths? So that was out. I considered setting it in deep space instead (some sort of *non-terrestrial* Escape Velocity, I suppose? What a notion), but that seemed too close to the [game I made for Ludum Dare 48][out-of-gas] already. And so it became deep forest, and then the car became a bicycle because that seemed more foresty.

Most of the rest of the originally envisioned gameplay mechanics fell away as I tried to scope it to the 72 hours available. The travelling became just an opportunity for a bit of dialogue, the vehicle maintenance became a simple stat alongside others for the player, and the trading disappeared entirely. In an effort to introduce some gameplay beyond just engaging in dialogue, I added in a hand of randomly drawn cards at each location and a limited number of action points for their use. I think I had in mind the dice rolls in [Citizen Sleeper][citizensleeper] when I came up with this, but I couldn't really remember how they worked in that game.

Considering it has been several months since the jam I don't think I could give you a blow by blow even if I wanted to, so I'm just going to talk a bit about what worked and what didn't.

## What Worked

### Digression

Digression worked really well for the most part. I think I encountered one bug, but I was able to work around it. I was able to churn out dialogue really quickly for the encounters and travel, and it was relatively easy to implement changes to the game state during dialogue as well (giving items and buffs and the like) - though that aspect of it could have been better, as I discuss below.

### Use of Resources

I used `Resource` types for all the items, buffs, curses, character classes etc. Although they were a bit of a mess and included some stuff that didn't end up getting used, it really paid off to work with resources right from the beginning. Often in the past I would implement something like the player's gun, for example, as just a scene or part of a scene, with the intention to rework it later to allow different guns defined by resources. And of course in a jam that never happens as time runs out and I get fatigued - so there ends up being only one gun, one pickup etc.

Probably the most obvious effect this had in this game is the character class selection. It doesn't add all that much, but I think it is a neat thing to have in a jam game and it gives the impression of depth.

So, big thumbs up to doing things the right way from the beginning.

### Audio

I used old reliable [LMMS][lmms] for the music this time around. Last time I tried some new tools and had a really bad time. I'm really proud of what I made for this game, it had the exact spooky, mysterious quality I was going for. I don't think [beepbox][beepbox] would have cut it this time.

The game didn't call for many sound effects, but the ones that are there, aside from the UI, are foley - always fun to do that and I think they work pretty well.

### Art

What can I say, I think I did a good job on the art. That's always been my strength anyway so big woop.

I am still using [Pixelorama][pixelorama] and there are still a few things about it that I find grating, but I have gotten used to it enough that it doesn't get in my way. It was better suited to this game than my last one because most of the art was large background pieces rather than tiles.

Something that's kinda new is that I did lot of animation using tweens. Little things like the the back and forth motion of the bicycle and how it enters and exits the screen, and the distribution and flipping of the cards, were entirely done with tweens. They took only minutes to implement and I think they look great, and add so much to the aesthetic of the game. I only had to actually animate one thing by hand, the pedalling.

### The Humour, apparently

That Sully, what a card.

## What Didn't

### Digression

Though it certainly didn't let me down, I definitely noticed a few pain points in actually using it for a game.

1. It was originally a main-screen editor, and at some point I decided it should be in the bottom dock - probably because Godot didn't provide an official way to add a main screen plugin and you had to sort of hack it in. However it requires a lot of space to use properly, and having it in the bottom dock was an impediment to that. I have moved it back to the main screen since the jam.
2. Having to manually manage the size of dialogue nodes was a hassle. I have since updated them to be resizeable width-wise, but to grow with the text length-wise. Much nicer to use.
3. Similarly, it was kind of a pain scrolling up and down a node when there was a long section of text. I have since partially implemented a mechanism to allow the dialogue node to be "maximised" when you want to focus on editing, and I will be doing the same for the choice node.
4. The lack of an open graphs list made it a bit awkward to move back and forth between graphs, as I had to find them in a scene or the filesystem every time. I have since added an open graphs list, as well as an anchors list for navigating around a graph.
5. The two different signals for dialogue and choice dialogue struck me as a little awkward in retrospect. I will be consolidating them I think.
6. There are a few problems with the variable management system. One is that they lacked defaults - I have added these since. Another is that the variables didn't mesh well with the overall game, i.e. game state and dialogue state felt like two separate things that I had to bridge. I'm not sure how I am going to address that yet.

### Gameplay

The gameplay was pretty awful. I clearly do not really know how card games work. Limiting the player's actions to a random selection of cards just resulted in frustration, especially when it was not obvious that some actions required items, and when their use of the cards was also constrained by action points.

The stats generally degraded too slowly as well and there were unclear interdependencies between them - your health doesn't degrade until you exhaust your food or water stats completely.

The encounters were fun, I thought, but there were too few of them and they were too random - you would see the same ones over and over sometimes. Too many of them had disappointing outcomes, and if you didn't get the right cards there was nothing to do.

I think the random encounters worked a bit better in [Out of Gas][out-of-gas] for two reasons: most encounters involved combat, so that is just inherently more exciting - and the fact that you were fleeing something, and could be killed, was slightly more compelling than a set of depleting stats.

Overall, the randomness just left the player with little sense of agency. I would have been better off dropping the gameplay altogether and just making it a short visual novel, with agency expressed only through dialogue choices. Though I'm not sure I could write a compelling story for a visual novel in such a short timespan either...

### Bugs

I introduced a bug at the last minute that prevented the game from ending when your health or vehicle state reached zero lol, lmao.

## Results

![Results table - 257th overall, 600th in Fun, 256th in Innovation, 446th in Theme, 80th in Graphics, 49th in Audio, 48th in Humour, 70th in Mood][results]

Much better than my last two outings, and some good ratings in several categories, but definitely let down overall by the gameplay. I'm a bit disappointed by the mood rating as I felt I nailed that, but it is a very subjective one of course - and it's still pretty good!

Some notables:

1. My highest ever rating, and placing, in humour (please clap).
2. Highest ever audio rating (by a hair), and placing.
3. First time being in the top 100 in four categories as a solo dev.
4. First time being in the top 50 in two categories. Third time being in the top 50 in any category.
5. *Second lowest* rating in fun - only my Ludum Dare 38 entry, which was only the opening scene of an adventure game and had no gameplay, was lower!

![Graph of audio placings][audiograph]
![Graph of humour ratings][humourratings]

## Post-Jam

Nah.

## Future Developments

I was inspired to work on some sweeping improvements to Digression and have made a lot of progress, but there is also a lot of stuff broken and partially completed now. I will post about the changes in more depth when they are done.

![Screenshot of dialogue and choice nodes in Digression][digressioncurrent]

I also created a set of placeholder graphics to use in future jams. I used the default Godot robot sprite in this game, but it is not ideal in some ways because everything ends up looking the same, and when you put in the actual art you have to undo any scaling that was done to make the placeholder the correct size.

![Screenshot of the game in early development, with the Godot logo everywhere][godotbot]

[headerimage]: {static}/images/lovely-dark-and-deep/cover_image.png "Lovely, Dark and Deep"
[digression]: https://github.com/khoulihan/digression "Digression repository on GitHub"
[pixelorama]: https://github.com/Orama-Interactive/Pixelorama "Pixelorama on GitHub"
[out-of-gas]: https://hyperlinkyourheart.itch.io/out-of-gas "Out of Gas on itch.io"
[itch]: https://hyperlinkyourheart.itch.io/lovely-dark-and-deep "itch.io page for the game"
[lmms]: https://lmms.io/ "Website of the LMMS DAW"
[beepbox]: https://www.beepbox.co "Beepbox - an online chiptune music tool"
[results]: {static}/images/lovely-dark-and-deep/results.png "Not too bad. Could be better."
[audiograph]: {static}/images/lovely-dark-and-deep/audioplacings.png
[ev]: https://en.wikipedia.org/wiki/Escape_Velocity_(video_game) "Wikipedia entry for the game Escape Velocity"
[citizensleeper]: https://citizensleeper.com/ "Website of the Citizen Sleeper series of games"
[humourratings]: {static}/images/lovely-dark-and-deep/humourratings.png
[digressioncurrent]: {static}/images/lovely-dark-and-deep/digressioncurrentstate.png "An example of some of the changes I've made"
[godotbot]: {static}/images/lovely-dark-and-deep/placeholders.png "Looks like Godot is already here"
