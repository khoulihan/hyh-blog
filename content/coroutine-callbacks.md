Title: Coroutine Callbacks
Date: 2021-04-05 18:29
Category: Game Development
Tags: godot, gdscript
Slug: coroutine-callbacks
Authors: Kevin Houlihan
Summary: Using coroutines to call back to the emitter of a signal.

I'm working on a cutscene/dialogue graph editor plugin for the [Godot game engine][godot] (I mentioned using it for the Ludum Dare in a [previous post]({filename}/gophers-post-mortem.md)). When I came to deciding how to actually process the graphs it creates in order to display the dialogue and perform actions in the game, I discovered an interesting use for coroutines that I haven't seen described elsewhere. I'm not all that used to working with coroutines so maybe what I've done is completely normal and everybody does it all the time, or indeed it might be ill-advised for some reason. Either way, I will describe it here and you can ignore me if I'm being an idiot!

[![Graph editor]({static}/images/gophers-post-mortem/graph.png)][graph]

Processing a graph that results in activity in-game is a task which frequently needs to be put on hold - waiting for text to be displayed in the UI in a juicy manner, moving characters around, waiting for input etc. This could be achieved in a `Node` by implementing `_process()` and maintaining state about whether you're currently walking a graph or waiting on something, and having methods that other nodes can use to indicate when processing can continue. I have found such methods to be quite messy in the past.

I decided instead to process the graph in a `while` loop and `yield` as necessary while other nodes perform tasks initiated by a number of signals. Where tasks are expected to take some time to complete, a coroutine state object is passed to the signal which the listener can use to indicate that processing should continue, or in some cases return values.

## Let's See Some Code

Below is an abridged version of the main method that processes the graphs. Processing a dialogue node yields so that the UI that displays the text can wait for player input to continue. Processing a branch node and others like it just proceed directly to the next iteration of the loop.

```python
func process_cutscene(cutscene):
	_local_store = {}
	_current_graph = cutscene
	_current_node = _current_graph.root_node
	while _current_node != null:
		if _current_node is DialogueTextNode:
			yield(_process_dialogue_node(), "completed")
		elif _current_node is BranchNode:
			_process_branch_node()
    ...
```

Here is the code that processes dialogue nodes and raises the signal for their text to be displayed in-game. A coroutine is put in a frozen state to be passed with the signal, and the call to emit the signal is deferred so we can make sure we are waiting for the coroutine to complete before any signal listeners have a chance to resume it.

```python
func _await_response():
	return yield()


func _emit_dialogue_signal(
	text,
	character_name,
	character_variant,
	process
):
	emit_signal(
		"dialogue_display_requested",
		text,
		character_name,
		character_variant,
		process
	)


func _process_dialogue_node():
	var text = _current_node.text

	var process = _await_response()
	call_deferred(
		"_emit_dialogue_signal",
		text,
		_current_node.character.character_name,
		_current_node.character_variant.variant_name,
		process
	)
	yield(process, "completed")

	_current_node = _current_node.next
```

The code that consumes the signal can take however long it likes to do its thing, and when it's ready it can just call `resume()` on the coroutine state and the graph processing will proceed to the next node.

```python
func _on_CutsceneController_dialogue_display_requested(
	text,
	character_name,
	character_variant,
	process
):
	_process = process
	...


func _on_ContinueButton_pressed():
	if _process != null:
		_process.resume()
```

If a node in the graph needs a response in order to know what to do next (e.g. a choice between multiple dialogue options), we can just accept the return value of the coroutine passed in the signal. The consumer can just pass the value to the `resume()` call.

```python
func _process_choice_node():
  ...
	var process = _await_response()
	call_deferred(
		"_emit_choices_signal",
		choices,
		process
	)
	var choice = yield(process, "completed")
	_current_node = _current_node.branches[choice]
```

## Potential Pitfalls

There are two pitfalls that come to mind with this approach, but they're not really any different than what could occur with a `_process()` based approach like the one I described above.

1. Processing of another graph could be triggered while one is still in progress. If the previous one is yielding it would end up processing the new graph as well when it resumes. This is quite easy to avoid by just noping out of the method if there is already work in progress.
2. If there are multiple listeners connected to the signals there could be ambiguity about which one is responsible for resuming. If there are multiple resume calls, all but the first will result in a runtime exception.

In the event that you actually *want* multiple listeners to report in before resuming, it might be possible to craft a different coroutine that takes the [number of listeners][signals] and yields until they have all resumed. I think it would look something like this:

```python
func _await_many(count):
  while count > 0:
    yield()
    count -= 1


func _await_many_responses(count):
  var responses = []
  while count > 0:
    responses.append(yield())
    count -= 1
  return responses
```

I haven't tested that though.

## Conclusion

I don't really have one, I just thought it was a neat pattern that doesn't require the listeners to keep a reference to the node doing the processing or have any knowledge of it aside from the signals it emits. You can check out [the full code on GitHub][graph] as it stands currently. I haven't tested it in a game yet, but I will probably enter the [Ludum Dare][ldjam] later this month and I might get a chance to use it then. I will update afterwards whether it is a disaster or a triumph!

[godot]: https://godotengine.org/ "The game engine you waited for."
[graph]: https://github.com/khoulihan/godot-cutscene-graph "Cutscene Graph Editor"
[signals]: https://docs.godotengine.org/en/stable/classes/class_object.html#class-object-method-get-signal-connection-list "get_signal_connection_list()"
[ldjam]: https://ldjam.com/ "Ludum Dare 48"
