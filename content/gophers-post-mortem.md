Title: Gophers
Date: 2020-04-25 17:24
Modified: 2020-04-25 17:24
Category: Game Development
Tags: ludum-dare, gopher
Slug: gophers-post-mortem
Authors: Kevin Houlihan
Summary: A post-mortem of my Ludum Dare 46 entry, Gophers - a short adventure game about keeping a gopher network alive after some sort of nuclear event has destroyed civilisation.
Status: published

[![Overlooking the city]({static}/images/gophers-post-mortem/Gophers_tower.png)](https://hyperlinkyourheart.itch.io/gophers)

[Gophers][itch] is my entry for [Ludum Dare 46][ldjam], the most recent of the bi-annual Ludum Dare game jams. It is a short adventure game about maintaining a [gopher][gopher] network in a post-apocalyptic world.

The basic concept is one I've been kicking around for a while as a sort of casual RPG/survival game about maintaining computer networks on scavenged technology, so it came to mind immediately when I saw the theme ("Keep it alive").

I've been really interested lately in gopher and other low-overhead technologies, and what the internet would look like if the industries that sustain it collapsed. I'd previously envisioned a relatively cheerful solarpunk game about connecting distant sustainable communities, but I think it took on a much darker tone because of recent events.

## Art ##

I did all the art in [Pyxel Edit][pyxel] as usual. My goal was to keep everything abstract and as high-contrast and readable as possible while still allowing for a nice parallax cityscape. I started with a mock-up of the exterior scene, and then essentially flipped the background and foreground colours from that for the bunker scene. I only used 7 colours in the end.

![Bunker Scene]({static}/images/gophers-post-mortem/BunkerScreenie.png)

I put together a timelapse of the art so you can see the whole process:

[![Gophers](https://img.youtube.com/vi/0jPLMCfSE0w/0.jpg)](https://www.youtube.com/watch?v=0jPLMCfSE0w)

## Code ##

The only reason why I considered this a viable idea was because I had previously developed a [cutscene graph editor plugin][graph] for [Godot][godot]. It was untested in any game but I thought it would give me enough of a leg up that I would have time for the art and writing.

[![Graph editor]({static}/images/gophers-post-mortem/graph.png)][graph]

So in effect, the "gopher network" in the game is actually a dialogue tree!

Actually using the editor in a game did reveal some issues with it, but nothing significant enough to prevent me from finishing - and now I have some ideas on what needs work before I use it for another game!

I also took some code from a [previous game of mine][pp] for doing the menus and dealing with the settings. Every bit helps when you're entering the jam solo.

One thing that really came together for me in this jam was using coroutines to manage sequences of events. I've always struggled to wrap my head around them previously for some reason, and would clumsily hook up signal handlers for every step. Using the `yield` statement in [Godot][godot] made handling interactions much easier and quicker to write.

```python
func _on_Terminal_clicked(walk_target, face_direction):
	_player.set_destination(walk_target)
	yield(_player, "arrived_at_destination")
	_player.face(face_direction)
	GameController.set_spawn_location("bunker", "terminal")
	GameController.set_spawn_direction("bunker", "right")
	FadeMask.fade_in()
	yield(FadeMask, "fade_in_complete")
	# Switch to the browser scene
	self.get_tree().change_scene("res://browser/Browser.tscn")
	FadeMask.fade_out()
	yield(FadeMask, "fade_out_complete")
```

## Sound Effects ##

The most exciting part of working on this game, for me, was doing the sound effects. I bought a fancy mic a while back (a [Røde NT-USB][rode]) to do foley SFX rather than my usual SFXR beeps and boops, but this was the first chance I've had to try it out.

![My foley kit, or part of it at least]({static}/images/gophers-post-mortem/foley-kit.jpg)

For the Geiger counter sounds I ran my finger over the teeth of a comb. For the bunker door, I rubbed a hammer and a spanner together in various ways. For the dripping sound in the bunker, I just used an eyedropper to drip drops into a glass of water. The footsteps are real footsteps that I recorded, and the cloth sounds when you're walking around the exterior are me crinkling a vinyl jacket. It was a lot of fun to record all these and I don't think I was even being all that creative. I couldn't figure out how to do buzzing or flickering sounds for the electric light within the time I had though, unfortunately.

One big problem I encountered was that my apartment is apparently incredibly noisy, as am I. It was a windy day and the shutters on my window were banging constantly, my neighbours were going about their noisy lives, oblivious, and my body stubbornly refused to go without oxygen during the recordings. Noise reduction in [Audacity][audacity] helped a bit (make sure you record periods of "silence" to enable this), but there are definitely some extra environmental sounds in there. Thankfully I think they mostly just appear as mysterious underground reverb or get buried by other things. It's something I'm definitely going to have to think about for next time.

I did a bunch of post-processing in [Audacity][audacity] to pick the best bits out of the recordings, and make things sound better. I had to reduce the pitch on the bunker door sound to make it sound heavier, for example.

## Music ##

I was so proud of the sound effects that I almost wasn't going to do any music, but I'm glad I did. I got to it in the last few hours of the jam, so I had to keep it very simple. It's mostly just the notes of a Dmin7 chord played in a few different arrangements on pad instruments, with some slow bass drums coming in and out. The title screen music layers a couple of different pads as well as a Rhodes doing sus4 arpeggios from each note of the chord.

I put everything together in [LMMS][lmms]. I spent a good chunk of time experimenting with different instruments so even though it's really minimalistic it still took a while!

## Abandoned Ideas ##

I had planned several other game elements, including the protagonist saying things to himself (or the player), and another type of interaction involving connecting cables and swapping out computer components.

A full game would probably have more complex survival elements instead of a simple timer, and would see you having to scavenge in the environment for computer equipment and other supplies.

We'll see if anything like that comes to fruition in the future!

[itch]: https://hyperlinkyourheart.itch.io/gophers "Gophers"
[ldjam]: https://ldjam.com/events/ludum-dare/46 "Ludum Dare 46"
[gopher]: https://en.wikipedia.org/wiki/Gopher_(protocol) "Gopher Protocol"
[pyxel]: https://www.pyxeledit.com/ "Pyxel Edit"
[rode]: https://www.rode.com/microphones/nt-usb "Røde NT-USB"
[audacity]: https://www.audacityteam.org/ "Audacity audio editor"
[lmms]: https://lmms.io/ "LMMS"
[graph]: https://github.com/khoulihan/godot-cutscene-graph "Cutscene Graph Editor"
[pp]: https://hyperlinkyourheart.itch.io/people-poker "People Poker"
[godot]: https://godotengine.org/ "The game engine you waited for."
