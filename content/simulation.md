Title: Sim-Universe
Date: 2022-04-16 15:43
Modified: 2022-04-16 15:43
Category: Philosophy
Tags: sci-fi, religion
Slug: simulation
Authors: Kevin Houlihan
Summary: Thoughts on the simulation argument.
Status: published

I just done watched [Thought Slime's][tschannel] [video about the simulation argument][tsvideo] (actually many months ago by the time I'm actually publising this), and it's a topic about which I've had some thoughts myself, so I thought maybe it was time to write some of them down.

Like comrade Slime, I think that it's an interesting thought experiment, but a lot of what is said about it is poorly thought through at best. It's particularly frustrating when [Nick Bostrom's argument][nbarg] is held up as "proof" of the "certainty" that we are living in a simulation, alongside arguments and assertions that completely contradict it. The argument itself doesn't claim to be proof of any such thing - it presents three possibilities based on premises about which we have almost no information.

## Why would we simulate?

> One thing that later generations might do with their super-powerful computers is run detailed simulations of their forebears or of people like their forebears.

This is Nick's description of *what* futuristic super-computing civilisations would do with their computational power, but he doesn't really get into *why* they might do this. Into this absence people pour all sorts of ideas. A common one is that we are equivalent to NPCs in a video-game. A related one is that we exist so that the simulators can pop in and out of our minds and ride us around for some reason - historical educational purposes perhaps, or the thrill of slumming it in the stupid-ages.

These are interesting concepts for science-fiction, but I don't find them compelling as claims about the reality of our world. Video-games are indeed able to present more visually convincing realities than in the past, but they don't do that by simulating entire physical universes in minute detail. They might run physics simulations for a variety of things in the vicinity of the player - beyond the bare minimum necessary to convince, they are hollow, simplified facades, and anything not relevant to the context of the current gameplay is non-existent. Similarly, what would it add to a player's experience to have NPCs living lives outside of that context and having inner lives?

Nick Bostrum actually gets into some of the mechanisms that could be used to reduce the computational requirements of a simulation:

> If the environment is included in the simulation, this will require additional computing power – how much depends on the scope and granularity of the simulation. Simulating the entire universe down to the quantum level is obviously infeasible... But in order to get a realistic simulation of human experience, much less is needed – only whatever is required to ensure that the simulated humans, interacting in normal human ways with their simulated environment, don’t notice any irregularities.

> Distant astronomical objects can have highly compressed representations: verisimilitude need extend to the narrow band of properties that we can observe from our planet or solar system spacecraft. On the surface of Earth, macroscopic objects in inhabited areas may need to be continuously simulated, but microscopic phenomena could likely be filled in ad hoc. What you see through an electron microscope needs to look unsuspicious, but you usually have no way of confirming its coherence with unobserved parts of the microscopic world

The implicit assumption here is that the simulation is being made convincing for the benefit of the simulated minds (i.e. us), which always run at full resolution. Video-games are not run for the entertainment of NPCs however. If simulations are being run for the amusement of posthuman "players", and they are interested in reducing the computational requirements, as Nick assumes, why would they not prune the most computationally expensive component - simulated human minds that are not immediately relevant to the player's current experience? Would they even need to simulate fully conscious humans at all to provide convincing NPCs to players?

Nick does suggest something akin to such pruning in his original argument:

> In addition to ancestor-simulations, one may also consider the possibility of more selective simulations that include only a small group of humans or a single individual. The rest of humanity would then be zombies or “shadow-people” – humans simulated only at a level sufficient for the fully simulated people not to notice anything suspicious.

However, it is again expressed as if the purpose of the simulation is solely to fool its unwitting inhabitant(s), with no proposed utility for the creators of the simulation.

I submit to you that if you are experiencing a private and mundane moment right now, and are conscious of it, you are probably not a character simulated on some posthuman equivalent of a PlayStation.

A more reasonable suggestion, to my mind, is that we would run such simulations in order to study our own civilisation at different stages of development, or to see how civilisations might develop under different circumstances. Would these simulations even require fully conscious simulated participants in order to be useful? Would they need to simulate the full lives of everybody who has ever lived? Or would they drastically reduce the number of minds needing to be simulated by cutting out all the boring parts? Would there really even be anything to be learned from such simulations?

This lack of clarity about why a posthuman civilisation would run ancestor simulations is at the heart of a lot of my issues with the argument. Without that understanding, we can't really say whether such a civilisation would run them or not, or how many, or what their parameters would be. It's just sort of assumed that they probably will because it would be a cool thing to be able to do, and some people say they would do it right now if it were possible. But that's an easy thing to say when it's impossible, and you don't have to worry about the ethical concerns or the resources involved.

Another type of simulation we might run are of universes with different physical laws, but as the quotes above about simplifying the simulations suggest, these would have a different set of priorities, and wouldn't really qualify as "ancestor simulations". Whether they would even result in conscious entities would probably depend on the parameters of the simulation - they wouldn't be the goal. If we take seriously the suggestion that we live in this kind of simulation, we can't even assume that the simulators are anything like us, not even in their remote past, or that the simulating universe resembles ours in any way - so how can we possibly speculate about their motives, or what is computationally possible in their universe?

## Simulations Within Simulations

One of the silliest suggestions that some people seem to take seriously is that the posthuman civilisation in the base reality would run simulations beyond the point where the simulated civilisations would be running their own simulations, with those simulations running further simulations, and so on.

Nick likens this scenario to running code in a virtual machine:

> It may be possible for simulated civilizations to become posthuman. They may then run their own ancestor-simulations on powerful computers they build in their simulated universe. Such computers would be “virtual machines”, a familiar concept in computer science. (Java script web-applets, for instance, run on a virtual machine – a simulated computer – inside your desktop.)

His example is terrible, but the basic assertion is correct, a computer can simulate another computer in various ways, with varying levels of overhead. In the best case, code running in the virtual machine runs directly on the host hardware with no translation necessary. Obviously, this doesn't add any processing power - software running in the host has to share its resources with the software running in the virtual machine.

Now, let's think through this scenario a little bit.

Say you are a posthuman civilisation that has converted an entire planet into a giant computer. All the computation you decide to do is running on this computer. For some reason, you decide to run an ancestor simulation of your quite recent past, such that the simulated universe is on the cusp of achieving their own planet-computer. All of the computation of that universe would actually be running on *your* computer, alongside all the existing computation of your civilisation, and all the other work required for the simulation, all the fake stars and physics and advanced posthuman minds. Then you let them run their own simulation of their own recent past - now you have to support the load of three civilisations with planet-sized computers on only one actual physical planet-sized computer. And then four, and then five, and on and on.

A little while ago we were talking about cutting corners to save resources and focus on running our ancestors minds, and now here we are supporting an infinite regress of posthuman computers for no obvious purpose. There wouldn't be any shortcuts here - if a computer 10 levels down wants to compute a hash or calculate millions of primes you would actually have to do the work or *they would know*.

There are two possible workarounds/objections to this that I can think of:

1. Simulations could be run slower than the host reality to allow room for it. Would a time-dilated simulation be useful? I guess that depends on what you're running it for!
2. Posthuman level simulations would only be allowed to develop once the host reality had converted enough matter to *pure computer* that supporting them was not a burden. In other words, the simulations would always have to lag behind by some significant amount.

Fair enough, I guess that would do it, if keeping the simulations going is really important, you might always dedicate a proportional amount of your ever increasing computational resources to them. I do come back to the why though - would a simulation of a posthuman-level civilisation be a fun game for posthumans? Would there be anything to learn from it that you didn't document when you were going through that phase?

> One consideration that counts against the multi-level hypothesis is that the computational cost for the basement-level simulators would be very great. Simulating even a single posthuman civilization might be prohibitively expensive. If so, then we should expect our simulation to be terminated when we are about to become posthuman

Oh, well. Better to return to monke then, lest techno-god smite us for our arrogance.

## If God Did Not Exist...

One possibility for why a posthuman civilization might choose not to run ancestor simulations is that doing so would raise some thorny ethical concerns. Take it away Nick:

> One can speculate that advanced civilizations all develop along a trajectory that leads to the recognition of an ethical prohibition against running ancestor-simulations because of the suffering that is inflicted on the inhabitants of the simulation

Yes I think that might be likely... wait, what are you...

> However, from our present point of view, it is not clear that creating a human race is immoral

*Ooof*. It's not just *creating a human race* that we're talking about here, it's *creating a human race and trapping them in a false reality for our own edification or amusement*, and in some hypothetical scenarios, *instantly terminating billions of them when they reach a certain level of development*. I think most people today would baulk at the prospect of treating even a single person like that, much less generation after generation of unwitting playthings.

Even worse are the moral implications for us, today, of taking some of Nick's proposals seriously. In relation to the idea that many minds might be simulated only partially some amount of the time in order to save resources (discussed above), he suggests that it would also be a way for the simulators to avoid inflicting suffering:

> There is also the possibility of simulators abridging certain parts of the mental lives of simulated beings and giving them false memories of the sort of experiences that they would typically have had during the omitted interval. If so, one can consider the following (farfetched) solution to the problem of evil: that there is no suffering in the world and all memories of suffering are illusions. Of course, this hypothesis can be seriously entertained only at those times when you are not currently suffering.

You weren't traumatised, you see, you just have a false memory of trauma. And no need to worry about the consequences if you feel compelled to abuse, murder or rape: those are just zombie shadow-people you're hurting, and they don't really feel pain! Nothing is real and nothing matters!

But wait! Maybe our simulators will take it upon themselves to reward or punish us for our behaviour in their simulation (without informing us that they will do so, or on what basis), and dedicate ludicrous amounts of resources to simulating all the minds they have ever simulated, indefinitely, in an afterlife:

> Further rumination on these themes could climax in a naturalistic theogony that would study the structure of this hierarchy, and the constraints imposed on its inhabitants by the possibility that their actions on their own level may affect the treatment they receive from dwellers of deeper levels. For example, if nobody can be sure that they are at the basement-level, then everybody would have to consider the possibility that their actions will be rewarded or punished, based perhaps on moral criteria, by their simulators. An afterlife would be a real possibility.

It genuinely disturbs me that there are people who are only good because they believe there is some force outside the universe that will reward them for it, or punish them for misbehaviour - and, even worse, people who would take on the role of cosmic arbiter themselves if given the chance.

## Postsingular Posthumans

Inevitably, discussions about the simulation argument are little more than speculation based on almost no information. The kind of civilisation that would be capable of running such simulations would be one that has passed through a technological singularity - a point at which technological progress becomes so rapid that its path is impossible to predict. In fact the simulation argument requires that a civilisation has achieved the ability to simulate a human-equivalent mind - an Artificial General Intelligence - widely considered to be the invention that will instigate the singularity, since such an intelligence would probably be able to improve itself at an exponential rate.

We have zero examples of a post-singularity, posthuman civilisation, and only one example of a human-level civilisation, on which to base our speculations. What will super-intelligent posthumans value? Almost by definition such a civilisation would be beyond our comprehension.

The simulation argument seems mostly, to me, to be an attempt to imagine God in a way that is appealing to 21st century techies. I'm inclined to think that such a god, like all others, is not just unknowable, but non-existent. 

[tschannel]: https://www.youtube.com/channel/UCrr7y8rEXb7_RiVniwvzk9w "Thought Slime"
[tsvideo]: https://www.youtube.com/watch?v=erkM0abWBfQ "Elon Musk is wrong about simulation theory, how uncharacteristic of him."
[nbarg]: https://www.simulation-argument.com/simulation.html "Simulation Argument"
