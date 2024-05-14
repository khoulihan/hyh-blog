Title: From Hell's Heart
Date: 2024-05-14 22:46
Category: Game Development
Tags: godot, godot4, gdscript, ludum-dare, music, pixelart
Slug: from-hells-heart
Authors: Kevin Houlihan
Summary: A post-mortem of my Ludum Dare 55 entry, From Hell's Heart, a twin-stick shooter.
Status: published

![Demon character from my game bound in a circle of protection]({static}/images/from-hells-heart/my_boy_scaled.png "What have they done to my boy??")

[From Hell's Heart][itch] is my entry for Ludum Dare 55, the first Ludum Dare I have participated in since I made [Out of Gas][oog] for Ludum Dare 48 in 2021.

I was not thrilled with it overall (and neither was anybody else - but we'll get to that), but it was good to get into working on actual gameplay programming again after several years of only working on tooling, and it has inspired me to do a lot more gamedev work since.

## The Concept

I was quite disappointed by the theme. I had an idea for the theme "It Spreads", which was one of the final round themes, that I was very invested in. I was going to make a zombie shooter where the weapons were all spreadables like jam and nutella and so on, and I had a lot of fun art and gameplay ideas for that.

So when the theme of "Summoning" was announced I was disappointed. But, the theme is rarely the one I would prefer, so I got to brainstorming and came up with the idea of "reverse-Doom", which evolved into something not explicitly Doom related, but where you play as a demon fighting soldiers nonetheless. For a brief moment I was even considering calling it "What if Doom but you're the Demon".

The thing I liked about this concept was that it allowed me to address the theme in two ways - you are a demon who has been summoned, and you can summon other demons to help you. However, the fact that it is perfectly playable and beatable without ever summoning your demon friends diminishes this somewhat!

One of my hopes for this jam was to try out my dialogue graph editor, [Digression][digression], in another game, and unfortunately there was no place for it with this concept. I used it heavily in [Out of Gas][oog] and [Gophers][gophers] in the past, but it has been fleshed out significantly since then and is ready to be put through its paces. Oh well.

## Art

I couldn't get Pyxel Edit to run on my new computer when setting up for the jam (it is Windows only, and I have run it using Wine in the past), so I decided to branch out and try [Pixelorama][pixelorama] - a pixel art editor built in Godot. Although my muscle memory from Pyxel edit tripped me up constantly in minor ways it was a good experience overall and I think I will continue using it going forward, as I always prefer open-source and native applications when they are available. The only thing I really found lacking was the way it handles the grid/tiles. There are no tools for quickly copying and manipulating tiles, and the grid is specified in the global settings instead of being per-file, even though one grid is unlikely to suit different files even in the same project.

I also had to adapt the way I managed spritesheets, as Pyxel edit allows you to define multiple animations in a single file, with the frames being tiles, while Pixelorama will only animate the entire file as a single unit. As such, character sprites are spread across multiple files each. In Godot this means swapping the sprite texture for each animation, but that didn't seem to cause any problems.

I made some big mistakes with the level art early on, initially designing it at twice the appropriate resolution for the characters I had in mind. I was able to take the basic design ideas and downscale them into the final wall and floor tiles easily enough, but it still wasted a lot of time. I designed them for an auto-tiling approach which I developed a while ago, where a tool script populates the floor tiles when you update the walls.

![The initial oversized art I designed. The walls are about 5 times the height of the characters.]({static}/images/from-hells-heart/humongowalls.png "Humongous walls, and some variants of the player character.")

I based the character shapes roughly on the design I came up with for [Guerrilla Gardening][guerrilla-gardening] for Ludum Dare 41, which is very round and fun, and I've found works really well for shooter games. It also features outlines for the characters which means there's less risk of ending up with characters that don't show up well against the background!

I was quite pleased with the art overall, though when I designed the wall and floor variants for the opening "cutscene" I realised that the game is far too red overall, as the characters looked much better against the bluer background!

![Screenshot of part of the opening scene, with blue-grey crates against blue-grey walls and floor]({static}/images/from-hells-heart/crates.png "The crates had much less contrast though.")

I am determined next time I do a jam solo to not do full animations for each character or game element, and instead use the animation features of Godot to bounce, squash and spin things to bring them to life. This will give me much more time to create a variety of characters and objects, which I think would contribute more to a jam game than full run-cycle animations. The only place I used this kind of technique in this game was for the spinning and pulsing of the portal, and I think it was quite effective. People do some great things with this kind of animation and I am missing out.

## Music

Music is an element of jam games that I am always trying to find a new and better approach to, as it is something that I enjoy a lot but am not particularly skilled at. In the past I have used [beepbox][beepbox], [LMMS][lmms] and [Bosca Ceoil][bosca-ceoil] with different degrees of success.

In the week prior to the jam I came across an application called [Helio][helio] which I thought looked incredibly promising. It looked like it might be as easy to use as Bosca Ceoil but with a wider variety of possible instruments, so I was excited to try it out.

Another type of tool that I am always looking to bring into the fold is modular synth emulators. I have tried [VCV rack][vcv] in the past but never managed to use it for a game, and I recently came across a fork of it called [Cardinal][cardinal] and had been practicing with that. I discovered that I could use Cardinal as a plugin for Helio and create instruments in it to control using Helio, so I planned to either do that or create a patch to generate all the music for the game, depending on what idea I was working on. The concept for From Hell's Heart didn't really seem to call for techno or ambient music, so I ended up trying the latter.

Unfortunately, things did not go smoothly at all with creating the music. I found Helio to be lacking in some essential features, and with a confusing menu system. It crashed constantly, forgetting instrument settings each time and sometimes changing the volume of notes or moving them around arbitrarily. I think the interface with Cardinal may have been responsible for some of this, and ultimately abandoned trying to use it for any instruments in favor of a selection of sound fonts. There was no way to preview the sound fonts in Helio, and I ended up previewing them on the command line using `fluidsynth`, but not all of the ones I found that I liked worked when loaded into instruments in Helio. It was just a frustrating mess all around.

Most bafflingly in terms of missing features in Helio, I couldn't find a way of creating more than one pattern for an instrument, so I ended up having to use multiple tracks of the same instrument when I wanted a different pattern.

It also lacks a central mixer where effects can be applied. Instead you can add effects on a per-instrument basis. I tried to do this in Cardinal as well, but again abandoned that as time dragged on and the application kept crashing.

So overall it was a bit of a nightmare, took five precious hours, and the track ended up being overly repetitive, with just one melody repeated over and over with the only variation being different instruments coming in and out. I hated it when I was done, but it grew on me a bit when I put it in the game. It did kind of have the mood I was aiming for.

Every time I try to make music in Linux I feel like I am missing out on some brilliant workflow that ties a variety of different applications together with their different specialities, but I am just failing to grasp how it all works, and this time was no different. Back to LMMS next time I think...

## Sound Effects

Somewhere that I did get to use Cardinal was for the sound effects! I mostly used the Audible Instruments synth modules with a variety of different setting, and used [Audacity][audacity] to record different notes being played for variety. Some of the results I was really pleased with (the demon snarls), others much less so (the enemy voices, which sounded like robots saying random words), but overall it worked pretty well. I would have preferred to do some foley stuff but there wasn't time, and it was a step up from [SFXR][sfxr] at least.

## Code

Since my long-time project, [Just a Robot][jar], is a shooter, I had a fair bit of base code to plunder for this jam. I don't think I did or learned anything particularly interesting this time around, but the base code did include a technique for showing a character silhouette when they are obscured by a wall which is interesting enough, and some automatic configuration of floor and mask tilemaps to allow rooms to be banged out quickly with little possibility of error.

The trick to the silhouettes is to create a mask of the parts of the walls that should obscure game entities using a `BackBufferCopy` node, and then check that mask in a shader on any sprite that should be obscured. Objects in the game do not need to be children of the `TileMap`, and in fact there is a different `TileMap` for walls and floors.

![Screenshot of Godot editor scene tree showing mask TileMap and BackBufferCopy]({static}/images/from-hells-heart/backbuffer.png "Yes I used nodes as &quot;folders&quot; here, bad very bad.")

The mask `TileMap` is populated automatically in the editor using a script like this:

```
@tool
extends TileMap

@export var copy_map: NodePath
@export var copy_from_layer: int = 0
@export var copy_to_layer: int = 0
@export var refresh_frequency: int = 10

@onready var _copy_map_node = get_node(copy_map)

var time = 0

func _process(delta):
	if Engine.is_editor_hint():
		_tool_process()

func _tool_process():
	if copy_map != null and refresh_frequency > 0:
		_copy_map_node = get_node(copy_map)
		var current_ticks = Time.get_ticks_msec()
		if time == 0 or current_ticks - time > refresh_frequency * 1000:
			time = current_ticks
			_copy_map()

func _copy_map():
	var cells = _copy_map_node.get_used_cells(copy_from_layer)
	self.clear_layer(copy_to_layer)
	for cell in cells:
		if not _copy_map_node.get_cell_source_id(copy_from_layer, cell) == 0:
			self.set_cell(
				copy_to_layer,
				cell,
				_copy_map_node.get_cell_source_id(copy_from_layer, cell),
				_copy_map_node.get_cell_atlas_coords(copy_from_layer, cell),
				_copy_map_node.get_cell_alternative_tile(copy_from_layer, cell)
			)
	self.fix_invalid_tiles()
```

The mask tileset just has 100% red everywhere that should be obscured, so the shader just checks for red in the screen texture and displays a grey colour instead of the sprite's texture anywhere it finds it, leaving the alpha intact:

```
shader_type canvas_item;

uniform bool hide_when_occluded = true;
uniform sampler2D SCREEN_TEXTURE : hint_screen_texture, filter_linear_mipmap;

void fragment() {
	vec4 mask = textureLod(SCREEN_TEXTURE, SCREEN_UV, 0.0);
	if (mask.a > 0.0) {
		if (mask.r > 0.9) {
			if (hide_when_occluded) {
				COLOR.a = 0.0;
			} else {
				COLOR.rgb = vec3(0.2, 0.2, 0.2);
			}
		}
	}
}
```

It turned out that people really hated the tight corridors and enemies being obscured though, so I probably won't be using this technique again!

A similar script to the one that populates the mask also populates a `TileMap` with floor tiles based on the wall tiles. The floor tiles have a different size than the wall tiles however, so it is a bit longer and more involved. I think I would prefer to just put floor and wall tiles on different layers of the same `TileMap` in the future, or as `TileMapLayers` or whatever is being introduced in Godot 4.3...

Another neat thing I did in the editor was to have spawn points for portals and enemies draw a line to the thing they are associated with, or an obvious warning if they are not configured correctly. This helped me ensure that everything was set up properly when rushing through the room designs in the last few hours of the jam! I am trying to get into the habit of adding this sort of tooling to everything that might benefit from it.

![Screenshot of Godot editor showing lines from spawn points to associated entities]({static}/images/from-hells-heart/spawnlines.png "Lines, lines, everywhere are lines")
```
@tool
extends Marker2D


@export var destination: GameRoomSpawnPoint


func _process(delta):
	if Engine.is_editor_hint():
		_tool_process()

func _tool_process():
	queue_redraw()


func _draw():
	if Engine.is_editor_hint():
		if destination != null:
			_draw_to_destination()
		else:
			_draw_warning()


func _draw_warning():
	self.draw_circle(Vector2(0, 0), 15.0, Color.RED)


func _draw_to_destination():
	self.draw_circle(Vector2(0, 0), 15.0, Color.GREEN)
	self.draw_line(
        Vector2(0, 0),
        destination.global_position - self.position,
        Color.GREEN,
        1.0
    )
```

I also took from the base code a node-based state machine for enemy AI. This turned out to be a bit confusing and inflexible, and when I tried to introduce some new behaviour on the final day I ended up making the game crash constantly, and had to roll back. I'm still unclear on exactly what went wrong there - I was getting null references due to the summoned allies despawning, even with null checks before referencing them. It was probably really obvious but I was exhausted by then. In any case there were other problems with the state machine I developed and I have started investigating the Godot plugin [Beehave][beehave] as an alternative for the future.

Something that did not work very well was the enemy navigation and avoidance. I completely misunderstood how the avoidance system was supposed to be used, so it was actually not in play at all. In experiments I've done since the jam I got it working to some extent, but it seems like it does not work very well anyway, with agents just grinding to a halt in many circumstances even after avoiding an obstacle! The navigation itself would have worked much better with one small settings change of `path_postprocessing` in the `NavigationAgent2D` to "edgecentered", as I discovered later. As I had it for the jam, navigation agents are always getting stuck on wall corners...

## Results

My game got lots of nice commments, and also a lot of complaints about out-of-bounds glitches, enemies being obscured by the walls, and being too easy.

I was uninspired by the theme this time around and my skills were somewhat rusty in every area, and the game was generic and buggy as a result, so I was unsurprised by the negative comments. I did think it looked good and was reasonably juicy and sounded alright. I wasn't expecting great overall ratings, but I did think it would do ok in the graphics category at least. However, the ratings were quite bad across the board, at least compared to previous jams!

Category | Rating | Placing | Percentile
:--- | ---: | ---: | ---:
Overall | 3.571 | 574 | 65th
Fun | 3.63 | 418 | 75th
Theme | 3.413 | 792 | 52nd
Innovation | 2.739 | 1080 | 35th
Humor | 2.609 | 823 | 50th
Graphics | 3.935 | 428 | 74th
Audio | 3.619 | 343 | 79th
Mood | 3.457 | 686 | 59th

This game did worse in almost every category in percentile terms than my Ludum Dare 38 entry which I didn't even complete - it was just an opening scene with a short dialog and no gameplay. Quite a drop from my "Gophers" peak!

![Ratings Graph]({static}/images/from-hells-heart/ratingsgraph.png)
![Percentile Graph]({static}/images/from-hells-heart/percentilegraph.png)

## Post-jam and Take-away

I won't make my usual promise to work on a post-jam version of this game, both because it's not interesting enough to be worth it, and because I never keep that promise anyway!

Instead I have been inspired to start working on [Just a Robot][jar] again since the jam, trying to get combat and enemy behaviour working the way I have always envisioned them, to see if it would actually be fun. The idea is to make it a cover-based shooter where the enemies abilities are close to the player's, more or less, and combat feels weighty and dangerous in a way that is distinct from bullet-hell shooters.

I successfully implemented a cover system for the player, but when I went to enable the enemies to use it and switch to using Beehave for their AI I quickly discovered that the way I had built them so far was too centralised and inheritance based, so after watching a few tutorials and considering things a bit I decided to start again mostly from scratch with a more composition-based approach. This is working really well for the player so far and I'm nearly back at the same point as I was previously.

I also thought about and experimented with tiling approaches a bit, creating both a very small scale autotiling tileset with multiple terrains, and a mockup of a more organic looking tileset with a wide variety of designs, angled walls and floor sections and the like. I am tired of creating boxy, uninteresting levels. I was initially inspired in my gamedev journey by the art and design of Hyper Light Drifter, and I want to get back to achieving something of that look and sense of verticality - maybe not in jam games, but in Just a Robot.

![Complex tiles mockup]({static}/images/from-hells-heart/HLD-like Room Experiment.png "Too bright for this game, but moving in the right direction I think")

I started on a greybox version of the above to actually use in designing the game, but it's not quite finished yet.

[itch]: https://hyperlinkyourheart.itch.io/from-hells-heart "From Hell's Heart Itch Page"
[oog]: https://hyperlinkyourheart.itch.io/out-of-gas "Out of Gas Itch Page"
[jar]: https://gamejolt.com/games/just-a-robot/185852 "Just a Robot GameJolt Page"
[digression]: https://github.com/khoulihan/digression "Digression GitHub Page"
[gophers]: https://hyperlinkyourheart.itch.io/gophers "Gophers Itch Page"
[pixelorama]: https://github.com/Orama-Interactive/Pixelorama "Pixelorama GitHub Page"
[guerrilla-gardening]: https://hyperlinkyourheart.itch.io/guerrilla-gardening "Guerrilla Gardening Itch Page"
[beehave]: https://github.com/bitbrain/beehave "Beehave GitHub Page"
[beepbox]: https://www.beepbox.co "Beepbox"
[lmms]: https://lmms.io/ "LMMS Website"
[bosca-ceoil]: https://boscaceoil.net/ "Bosca Ceoil Website"
[vcv]: https://vcvrack.com/ "VCV Rack Website"
[helio]: https://helio.fm/ "Helio Website"
[cardinal]: https://cardinal.kx.studio/ "Cardinal Website"
[audacity]: https://www.audacityteam.org/ "Audacity Website"
[sfxr]: http://www.drpetter.se/project_sfxr.html "SFXR Website"
