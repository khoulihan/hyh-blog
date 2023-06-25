Title: All My Yield()s, Gone!
Date: 2023-06-23 17:10
Category: Game Development
Tags: godot, gdscript, godot4
Slug: all-my-yields
Authors: Kevin Houlihan
Summary: The removal of yield() in Godot 4 means a new approach is required for some of its use cases.

In a [previous post][previous] I described a way to use the state object returned by a `yield()` call to control the traversal of a graph - specifically, a graph describing a cutscene or dialogue - where some nodes in the graph require waiting on input from the user or some other event before proceeding.

In [Godot 4][godot] the `yield` function was replaced with the `await` keyword. This has the same basic purpose: to suspend execution of the current function and return to the caller, to be resumed at a later time. However, it does not return the state object that `yield` did, so there is no built-in way to resume the function from the caller (that I can see, anyway).

Fortunately, it is not difficult to recreate the functionality. The first thing we need to do is define a very simple class that we can include instances of in the signals from the graph controller:

```python
class ProceedSignal:
	signal ready_to_proceed(choice)
	
	func proceed(choice: int = -1):
		ready_to_proceed.emit(choice)
```

This class includes a signal and a method that the consumer of the graph can call to tell the graph controller that it can proceed to the next node - similar to the `resume()` method on the coroutine state object in Godot 3.

The `_await_response` function which previously yielded to create a resumable coroutine state, now just returns a new instance of this class. It could alternatively just be created directly where this function is called:

```python
func _await_response():
	return ProceedSignal.new()
```

In `process_cutscene()` we now `await` calls to process node types that require waiting on the consumer, rather than `yield`ing them:

```python
func process_cutscene(cutscene):
	_graph_stack = []
	_local_store = {}
	_current_graph = cutscene
	_current_node = _current_graph.root_node
    
    ...
    
	while _current_node != null:
		
		if _current_node is DialogueTextNode:
			await _process_dialogue_node()
		elif _current_node is BranchNode:
			_process_branch_node()
        ...
```

And when processing such a node, we just create the `ProceedSignal` object, emit the relevant signal with it, and then await the `ready_to_proceed` signal from it:

```python
func _process_dialogue_node():
	
    ...
    
	text = _current_node.text
	
	var character_name = null
	var variant_name = null
	if _current_node.character != null:
		character_name = _current_node.character.character_name
	if _current_node.character_variant != null:
		variant_name = _current_node.character_variant.variant_name
	
	var process = _await_response()
	call_deferred(
		"_emit_dialogue_signal",
		text,
		character_name,
		variant_name,
		process
	)
	await process.ready_to_proceed
	
    _current_node = _get_node_by_id(_current_node.next)
```

Nothing much changes from the consumer's point of view, it just needs to store the object and then call the `proceed()` method when it's ready:

```python
func _on_cutscene_controller_dialogue_display_requested(
	text,
	character_name,
	character_variant,
	process
):
	# Hang on to the process object so we can tell the cutscene controller
	# to continue when we're ready to proceed
	_current_process = process
	
    ...


func _on_dialogue_display_continue_clicked():
	DialogueDisplay.hide()
	_current_process.proceed()
```

That's all the changes required for this project! Of course, the coroutine state object also had a property indicating if it was resumable or not, `is_valid`. It would not be difficult at all to reproduce this by simply adding such a property (perhaps behind a setter that would make it read-only except internally), and setting it to false once `proceed()` is called.

It could also be expanded to allow more complex communication between the coroutine and the consumer, or to make a long running coroutine cancellable. The controller can only `await` one type of signal to continue, but you could have it pass different instructions when resuming e.g. you could give it `stop()` and `proceed()` methods. Additional properties on the signal object could be used to pass back other data without having to pass it in the signal at all.

```python
enum ProceedSignalType {
    STOP,
    PROCEED
}

class ProceedSignal:
	signal ready_to_proceed(signal_type)
	
    var consumer_state
    
	func stop():
		ready_to_proceed.emit(ProceedSignalType.STOP)
    
	func proceed():
		ready_to_proceed.emit(ProceedSignalType.PROCEED)
```

## Cutscene Graph Editor Status

The cutscene graph editor has been upgraded to support Godot 4, at a [new home][github]. I've also added a bunch of minor features, such as multi-node deletion, copy & paste and duplication support, and support for dragging from an output port to create a new node.

I'm now working on improving some parts of the tool that were lacking in flexibility. My current task is improving the addition of conditions to the choice and random nodes, which previously only allowed a single variable to be compared for equality to determine if a branch should be considered. The new system moves the condition specification UI out of the nodes themselves and into a dialog box, and allows any number of variables to be evaluated using a variety of different operators.

![The Farnsworth Condition]({static}/images/all-my-yields/graph.png "The Farnsworth Condition")

Future plans include new ways of defining and interacting with sub-graphs, more flexible ways of manipulating variables, built-in variables and meta-data, and better ways of defining characters.

## Update: Pure Signals

It occurred to me after posting this that there is an even easier way to achieve this - as long as you don't need to keep any state in the signalling object. Because Godot 4 allows you to pass signals and callables, you could just pass the signal to proceed with the signal that initiates the action. When the consumer is ready to proceed they can then just call `emit` on it.

I might still prefer the other way of doing it because `_current_process.proceed()` reads a little better than `_current_process_proceed_signal.emit()`.


[godot]: https://godotengine.org/ "The game engine you waited for."
[previous]: {filename}/coroutine-callbacks.md  "Coroutine Callbacks post"
[github]: https://github.com/khoulihan/godot4-cutscene-graph-editor "Cutscene Graph Editor project on GitHub"
