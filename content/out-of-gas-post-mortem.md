Title: Out of Gas
Date: 2021-05-04 10:41
Modified: 2021-05-29 22:52
Category: Game Development
Tags: ludum-dare, sci-fi, music, pixelart, godot
Slug: out-of-gas-post-mortem
Authors: Kevin Houlihan
Summary: A post-mortem of my Ludum Dare 48 entry, Out of Gas - a space-road-trip themed narrative/clicker game about a couple of outlaws fleeing their cryptocurrency debts.
Status: published

[![Out of Gas]({static}/images/out-of-gas-post-mortem/OOG_itch_banner.jpg)](https://hyperlinkyourheart.itch.io/out-of-gas)

[Out of Gas][itch] is my entry for the recent [Ludum Dare 48][ldjam] game jam. It was intended to be a blatant [FTL][ftl] rip-off, but in having much simplified clicker-like combat mechanics and an unusual cars-in-space aesthetic, I think it is sufficiently its own thing (I hope anyway!)

## Concept ##

My initial thought was more of a straight sci-fi concept of travelling into deep space, facing combat and resource management challenges similar to those which ended up in the game. The first thing that came to mind as a title for this was "Out of Gas", after the [Modest Mouse song][out-of-gas-mm] of the same name.

Thinking about that song got me thinking in another direction - essentially the same mechanics, but Earth-bound, set in a Modest Mouse world of highways and drifters, fleeing problems and starting over. The problem to flee in this case would obviously be debt - something that you can get deeper and deeper into.

As you can probably tell by now I ended up combining these two ideas! I didn't want to let either of them go, and I quickly fell in love with the idea of a universe where space combat meant winding down your window and firing a handgun at your enemy.

The combined concept suggested that a new, sci-fi twist on the debt problem was required, and that's where the idea of a constantly growing cryptocurrency debt came in. I've been thinking about cryptocurrencies a lot lately since they're going through another hype cycle. One commonly touted feature of them (or some, like Bitcoin, at least), is that they're deflationary, so any debt denominated in them would constantly grow in value instead of decreasing in value like debts denominated in inflationary fiat currencies. This seemed like the perfect notion for the bizarre world of my game. It doesn't really have any impact on the gameplay, but I think it's a nice bit of narrative flavour, and it fits the theme perfectly.

![Late payment]({static}/images/out-of-gas-post-mortem/OOG-Late-Payment.jpg)

The final piece of the conceptual puzzle was the characters. I couldn't very well have two anonymous nobodies riding along with the player on a trip like this! I turned to two characters I had vague notions of making a game about years ago, Haze & Lee, a gun-toting, post-apocalyptic outlaw couple. Unfortunately I don't think their personalities really come across in the game due to time constraints, but at least they have names!

## Art ##

As usual, I did all the art in [Pyxel Edit][pyxel]. I started off very rough with just pink boxes for the ships and a partial circle for the background, and moved immediately onto the gameplay with those placeholders. This is a somewhat unusual approach for me as I usually try to tie down the look of a game early on.

![First mockup]({static}/images/out-of-gas-post-mortem/FirstMockup.png)

The thing about rough mockups is that by the time I came back to the art a bunch of stuff in the game was already tied to the resolution and shape of the outlines. I wasn't even sure I had done the perspective correctly, but I was stuck with it anyway, and I guess it was close enough because nobody has complained!

![First ships]({static}/images/out-of-gas-post-mortem/art_opt.jpg)

I had planned to do some character portraits as well for the narrative side of the game, and express encounters as dialogues between characters, but unfortunately there wasn't time for that.

The map screen also didn't get much love, with the initial placeholder art surviving into the final game.

![Map screen]({static}/images/out-of-gas-post-mortem/OOG_Map_Trail.jpg)

## Code ##

As for my last Ludum Dare entry, [Gophers]({filename}/gophers-post-mortem.md), a [cutscene graph editor plugin][graph] for [Godot][godot] that I had previously developed was essential to getting this game done within the time constraints of the jam.

![Those darn teenagers!]({static}/images/out-of-gas-post-mortem/teenagers_dialogue.jpg)

I had done a lot of work on this plugin in recent months, applying lessons learned from using it for Gophers to improve the workflow, functionality, and stability. This paid huge dividends, and I found almost no issues while churning out encounter cutscenes. The cutscene graphs created by this plugin power every encounter in the game up to and after combat.

My main task on the first day was to get the map screen working - it wouldn't be much of a game if you couldn't travel between systems. I implemented it as a graph defined by custom `MapSystem` and `MapConnection` control nodes.

![Map graph]({static}/images/out-of-gas-post-mortem/map_ui.jpg)

The new fun thing about this for me was declaring the `MapConnection` class to be a "tool" script, allowing the connections between systems to be drawn in the editor. This kind of custom tooling is important for the efficient design of systems in larger games, so it was fun to give it a try. Here, it mostly served to prevent me from getting confused about which `MapSystem` nodes I had already connected to each other and which I hadn't.

```python
func _draw():
	if usable or used or _can_draw_in_editor():
		_load_nodes_for_editor()
		# TODO: Decide on proper colours for this
		var color = Color.gray
		if usable:
			color = Color.hotpink
		# No idea why the offset is required
		var source_center = _source_node.rect_global_position + CENTER_OFFSET
		var target_center = _target_node.rect_global_position + CENTER_OFFSET
		var start = source_center + ((target_center - source_center).normalized() * SPACE)
		var finish = target_center + ((source_center - target_center).normalized() * SPACE)
		draw_line(
			start,
			finish,
			color,
			LINE_THICKNESS,
			false
		)
```

Implementing the combat was a lot tougher. The battle scene is almost entirely UI nodes, which was perhaps a mistake, and for some reason I struggled most of day two to even get player input to register properly. I don't really remember now what the obstacle was to this - maybe I was just tired.

![Battle UI]({static}/images/out-of-gas-post-mortem/encounter_ui.jpg)

## Sound and Music ##

There's nothing special about the sound this time around. Unlike for Gophers I didn't have time to do any foley work, and I figured I would probably have a hard time creating gunshot and explosion sounds anyway. Instead I fell back to SFXR (specifically, [jsfxr][jsfxr]).

The music I put together in [BeepBox][beepbox], my favourite game jam tool for chiptune music these days due to its simplicity. I tend not to get as bogged down with it as I do with [LMMS][lmms]. I initially wanted to try to create something in the style of Modest Mouse, given the game's inspiration, but it was hard to recreate a guitar sound. Instead I ended up with a simple arpeggiated chord progression over a bass drone that I hope feels kind of epic, kind of longing and lonesome, I dunno.

The battle music is a variation of the same tune but just swaps out one of the instruments, doubles up the drone, and compresses and spreads the arpeggios across more octaves for a more urgent and chaotic feeling. The two tracks play in sync throughout the game and just cut between each other as necessary.

## Abandoned Ideas ##

As usual there were many ideas that I had to put aside due to time constraints. I had planned to include a small number of missiles which could be fired during combat with devastating effect, to allow the player to pull themselves back from the brink of defeat. I had also intended to have targetable/damageable systems on the ships, including injury to the characters, so that you could take out the enemy's weapon to gain a reprieve from being fired upon, or their engines and reduce their chance to dodge. You can see the proposed UI of these mechanics in the initial mockup above. Finally, I had planned a system of weapon upgrades which almost made it in, but not quite.

On the art side, I had wanted to include a number of different backgrounds to improve the sense of travelling between systems.

A big regret that I have is that I wasn't able to include the character portraits, and express the encounters primarily as dialogue between characters. I think this would have introduced a lot more personality to the narrative side of the game, as opposed to the third-person narration that I had to go with.

## Post-Jam ##

I like this game a lot, and I feel it is one that could be polished up and rounded out into a complete experience with relative ease, so I am determined to do a post-jam release with some of the missing features described above, and some of the problems with the jam release resolved (such as the RNG sometimes producing the same encounter multiple times in a row). I have already begun work on this, and I hope to have it completed in the next few months. I'll do another post about my progress on it so far, but for now here's a little sneak peek:

[![Haze speaks!]({static}/images/out-of-gas-post-mortem/HazeSpeaks.jpg)](https://hyperlinkyourheart.itch.io/out-of-gas)

[itch]: https://hyperlinkyourheart.itch.io/out-of-gas "Out of Gas"
[ldjam]: https://ldjam.com/events/ludum-dare/48 "Ludum Dare 48"
[ftl]: https://subsetgames.com/ftl.html "FTL game"
[out-of-gas-mm]: https://www.youtube.com/watch?v=-_heR2ekoxI "Out of gas. Out of road. Out of car I don't know how I'm gonna go."
[pyxel]: https://www.pyxeledit.com/ "Pyxel Edit"
[godot]: https://godotengine.org/ "The game engine you waited for."
[graph]: https://github.com/khoulihan/godot-cutscene-graph "Cutscene Graph Editor"
[jsfxr]: https://sfxr.me/ "jsfxr"
[beepbox]: https://beepbox.co "BeepBox"
[lmms]: https://lmms.io/ "LMMS"
