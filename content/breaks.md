Title: The Power of Breaks
Date: 2025-08-08 14:10
Category: Game Development
Tags: godot, life, self-care
Slug: breaks
Authors: Kevin Houlihan
Summary: Sometimes taking a break makes the solution to a problem obvious when you return to it.
Status: published
og_image: images/breaks/cover-image.jpg

A few months ago I was stuck on a particularly frustrating problem in the development of [Digression][digression], my dialogue graph editor for [Godot][godot].

I had recently switched it to a main screen editor, as discussed in my [post-mortem of my last Ludum Dare entry][postmortem], and added a list of open graphs, and another of anchor points in the currently edited graph, similar to the scripts and methods list in the built-in script editor. Basically I have decided to reproduce the UI conventions of the script editor where they are at all applicable.

[![Screenshot of the graph editor main screen described above.][digression-screenshot]][digression]

This seemed fine initally, but as I got stuck into a big refactor of how the underlying resources are updated by the GUI, and how and when those are saved, I noticed something really weird: sometimes when I pressed ctrl-s to save the scene and current graph, the editor would switch to one of the other open graphs!

I think I must have spent two weeks on and off trying to figure out this problem. The code was absolutely littered with debug log lines trying to trace the sequence of events triggered by the save, but there didn't seem to be any connection between the code doing the saving, or the code handling key input, and the code responsible for switching between graphs. Eventually I gave up in frustration, and decided to [do some art][coming-down] in my spare time instead. Then I played some video games.

![Marketing image for the game "The Alters", showing the main character and his clones in a huddle on the right, with the name of the game on the left.][alters]

Well, when I finally came back to it, I figured out what was going on within five minutes. First I noticed that the graph that was being switched to was always one with a name starting with the letter s, and if there wasn't one starting with an s, then nothing happened. I tried other ctrl key combos and those switched to graphs starting with the corresponding letter, if there was one. It wasn't anything to do with saving, or how I'd implemented it, or anything to do with my code at all, it was just a [bug in the search feature of the ItemList node][bug-report]!

When I was deep into the development I had a very blinkered view of what was going on: I'm working on saving, it happens when I save, it must have something to do with that, and it must be due to changes I've made. A little break from it gave me enough perspective to see that none of that was the case, and there was ample evidence demonstrating that.

This of course isn't the first time in my life, in programming or other endeavours, that taking a break has helped me solve a problem or even develop skills. I often find that taking a break from art results in a seemingly huge improvement in my skills when I return to it. In that case I think it is down to being more relaxed and putting less pressure on myself when starting a new piece after a break than when I have recently finished a piece that I feel I need to improve upon.

In conclusion: breaks good. Take a step back sometimes.

[digression-screenshot]: {static}/images/breaks/digression.png "It's nearly looking like a built-in part of the editor now."
[digression]: https://github.com/khoulihan/digression "Digression repository on GitHub."
[godot]: https://godotengine.org/ "The game engine you waited for."
[postmortem]: {filename}/lovely-dark-and-deep.md  "Post-mortem of my Ludum Dare entry Lovely, Dark and Deep."
[coming-down]: {filename}/coming-down.md  "Coming Down art post."
[alters]: {static}/images/breaks/alters.jpg "It's really good."
[bug-report]: https://github.com/godotengine/godot/issues/109274 "Issue on the Godot issue tracker for the described bug."
