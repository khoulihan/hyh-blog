Title: I Accidentally Visual Scripting
Date: 2023-11-30 22:31
Category: Game Development
Tags: godot, godot4, gdscript, cutscenegrapheditor
Slug: accidental-visual-scripting
Authors: Kevin Houlihan
Summary: I seem to be accidentally implementing a visual scripting system as part of my tooling...
Status: published

For some months now I've been trying to make some progress on the game I've been "working on" for probably the better part of a decade, [Just a Robot][jar] (yep, 7 years ago was the first post there, and it was already in progress for a few years before that!). I haven't really been working on it for most of that time, though it has always been in the back of my mind.

![Variations on the character art over the years, including sprites and a portrait]({static}/images/accidental-visual-scripting/art_changes.png "All I actually seem to do is redesign the art...")

While I have re-implemented some basic *gunplay* mechanics, and experimented with auto-tiling and the like, my main task has been improving the editor for cutscene graphs that I designed previously (and which I've [mentioned][mention2] a [few times before][mention4]) based on my experience of using it in a [couple][mention1] of [jam games][mention3], and the anticipated requirements for this game.

I am also hoping that it will be something that other people might find useful, and that I can release in the Godot asset library. As such I try to do things in a generalised and user-friendly way, with nothing that would tie it specifically to my game, or rough edges that I would just ignore myself but be embarrassed if other people had to deal with them.

As a result, it's taking quite a while!

One thing I've noticed is that as I try to maintain flexibility I seem to be implementing tiny haphazard visual scripting systems for calculating values and defining conditions. Of course the graph editing is itself a type of visual scripting, but that that was both what I was expecting to be designing, and has well established UI conventions in the engine. I don't think there are any conventions or controls for defining values and conditions in the way that I am.

## Variable Changes

In the initial incarnation of the graph editor, it was possible to set the value of variables, and branch based on the value of variables, but the way it was implemented was... not good.

- Variable names were entered as strings. This seemed like a problem to me - as the scope of a project grew I anticipated that it would become harder and harder to keep track of what variables were being used, and if they were entered correctly everywhere.
- Values were also always strings - if you wanted a boolean, just enter "true" or "false"!
- There was no scoping, just one global pool of variables for all graphs.
- You could only assign constant values to variables. No incrementing or decrementing, arbitrary calculations, or using the values of other variables.
- You could only compare to constant values for branching.

![Screenshot of early version of the editor, showing string variable name and value fields]({static}/images/accidental-visual-scripting/dialogue_editor_example.png "This Naomi be Wolf")

My initial changes to improve this situation were to introduce scoping and type definitions for variables. Variables could be scoped to the graph, to the area (i.e. "level" or "room" or however the game wanted to define it), or be global. They could also be `boolean`, `int`, `float`, or `string`. The UI would change to reflect the type, so you would get a checkbox for booleans and a numbox for numbers.

This was better, but still kind of awful, because everywhere a variable was used the scope and type would have to be selected again! Unlike in code there was no way to declare a variable once and then use it elsewhere with its type and scope already known.

![Screenshot of one of the graphs from my game "Out of Gas", showing scoped boolean variables with values set by checkboxes]({static}/images/accidental-visual-scripting/teenagers_dialogue.png "Teenagers up to no good as usual")

So next... I implemented variable declarations, more or less! These are defined in the project, and anywhere that a variable is required in a graph it can be selected from a searchable dialog.

![Dialog for defining a variable]({static}/images/accidental-visual-scripting/variable_definition.png "Defining a variable")
![Variable set node with the variable selection control and a boolean value]({static}/images/accidental-visual-scripting/predefined_variable_set.png "Variable Set node")
![Dialog for finding a variable]({static}/images/accidental-visual-scripting/variable_selection.png "Selecting a variable")

Now I felt like I was getting places, though the problem of only being able to set and compare constants remains, and is what I'm currently tackling. But more about that in a minute.

## Choice Conditions

Another feature of the initial version of the graph editor was the ability to make dialogue choices only conditionally available to the player - for example making a choice dependent on having encountered a particular character or completed a particular quest. This was of course based on the comparison of a variable to a string constant, so it had all the same deficiencies as everything else about the variables, as well as a few of its own:

- Only one variable could be used for each choice.
- The only comparison available was equality, no greater or less than or anything like that.
- There was no possibility of negation.

The minimal improvement would be to allow a comparison of a single variable with a selectable operator, and a constant value. But what if the choice depends on the value of multiple variables? What if you want to make different choices available if the player has encountered a character but not completed a quest, than if they have done both? This could maybe be achieved using branching nodes to set a third variable, but that seemed like jumping through a lot of unnecessary hoops. I wanted to be able to define complex conditions directly on the choices.

My solution was to add a dialog where an arbitrarily complex condition can be defined - though currently only with constants on the right side of any operator.

![A screenshot of the condition definition dialog alongside the node that it was invoked from]({static}/images/accidental-visual-scripting/farnsworth.png "The Farnsworth Condition")

As you can see above, the condition is structured as a tree with boolean operators grouping the results of comparison operators. The whole condition is summarised as its (frankly much more understandable) equivalent GDScript.

So mission mostly accomplished - it was now possible to define conditions on choices with an arbitrary number of clauses. However, it was starting to seem like a lot of UI complexity to achieve something that is quite simple to do in code - almost like a type of visual scripting...

## Visualising Values

Now it's time to tackle the other side of the equation - the values to set or compare the chosen variables to.

For setting variables, I wanted it to be possible to increment or decrement values as well as setting static ones... But why not also allow values to be multiplied or divided? What if you want to set a variable to 2x another variable, or the result of a more complex calculation? These don't seem like particularly likely requirements for my game, but why reduce the flexibility by only allowing a handful of fixed operations?

For comparisons, I initially only considered allowing a choice between a constant or another variable. But would these not also benefit from more flexibility? What if you want to check if a variable is greater than half another variable? If setting variables was as flexible as described above, this could be achieved by setting a temporary variable, but that seems unnecessarily round-about and annoying to have to do. Since the task is the same for both situations (obtain a value for the right side of an operator), it seemed like it would be prudent to create one control that would cover both.

Another factor is that most of the above concerns only apply to integer and float variables. Booleans have another set of operators that might be applied to them. Strings have a more restricted set of operators, but there are a variety of functions that you might want to apply, or methods that you might want to call on them - `to_lower`, `rstrip`, `replacen`, etc. In fact, the same might be true of integers and floats...

With all that in mind the requirements have become quite complex - I'm faced with implementing a small but significant subset of GDScript in a GUI!

The design I have so far allows for multiple variables or constants to have operators to be applied between them, grouped by brackets if necessary, and for a selection of appropriate (for the type) functions to be called:

![Screenshot of the design of the proposed value calculation control in the designer]({static}/images/accidental-visual-scripting/value_calculation_mockup.png "That's a really long and weird way to write 1...")

One thing that annoys me about this is that it's much the same structure as is involved in creating the conditions (a tree), but uses completely different controls and looks and works completely differently. It's going to look quite strange when they are side by side in the conditions dialog... However, the tree control used for the conditions probably suits that better because the elements need to be selectable, and the "prefix notation" also suits it better I think, while it would be unfamiliar for most people for mathematical operators.

I can't really tell at this point if this is at all intuitive or if there's an obviously much simpler solution that I've overlooked. But it certainly makes me long to be able to just enter the values as code, regardless of their composition.

## Could I Uuuh... Do That?

I have been thinking about what would be involved in allowing the user to enter conditions and values as the GDScript code they would likely already be familiar with.

Godot includes an `Expression` class which can be used to parse and execute arbitrary expressions, so conceivably that could be used to run whatever the user input, and make the entire GDScript language available to them. It looks like it can even parse the text for errors before running it, which would be all that I would want to do in the editor anyway. One likely difficulty is that the referenced variables would not actually be GDScript variables at runtime, but entries in one of several dictionaries, so I might have to write my own parser anyway to pick those out and replace them. I'm not sure I really want to do that.

If that didn't work out, the alternative would be to parse the input myself (even more parsing!) and convert it into the same resource structures that I'm intending to have the UI create. This would likely be much more limited in which language constructs and operations it could support - and that might cause confusion or frustration for the user.

And, there are reasons why allowing these things to be defined as code might not be a good idea anyway:

- I don't really like the idea of having to switch from a GUI way of doing things to a code way of doing things when the rest of the plugin is very much GUI driven.
- I don't like the fact that the predefined variables would not be selectable, negating some of their utility. Or at least, to make them selectable I would have to implement some sort of auto-completion on top of everything else, which might be beyond me! 
- Some people use C# with Godot, and it's unclear if the `Expression` class can parse C# - I suspect it can't.
- Using the `Expression` class would likely allow arbitrary GDScript to be entered and executed during graph processing. That might be too much flexibility! If I want to allow that it will be its own node type.

One other GUI option I can think of would be to allow value calculations and conditions to be defined using their own type of graphs. This might have the advantage of using well established UI conventions and existing controls. On the other hand, a graph editor is not ideal for defining a tree, and it would probably appear even more unnecessarily complex and confusing for the undoubtedly most common use cases of setting variables to constant values and defining simple conditions based on single variables. It would also not be any less work for me!

## Conclusion

UI is hard <i class="fas fa-sad-cry body-icon" /> 

[jar]: https://gamejolt.com/games/just-a-robot/185852 "Just a Robot on GameJolt" 
[mention1]: {filename}/gophers-post-mortem.md "Gophers Post-mortem"
[mention2]: {filename}/coroutine-callbacks.md "Coroutine Callbacks"
[mention3]: {filename}/out-of-gas-post-mortem.md "Out of Gas Post Mortem"
[mention4]: {filename}/all-my-yields.md  "All My Yields post"
