Title: Syncthing Update
Date: 2023-04-08 23:15
Category: Technology
Tags: foss, privacy
Slug: syncthing
Authors: Kevin Houlihan
Summary: Joplin sync didn't work out long term, but I'm still using Syncthing
Status: published

In a [previous instalment][previous], I described how I used [Syncthing][syncthing] to sync my notes in [Joplin][joplin] on my laptop to Joplin on my phone. Unfortunately that arrangement didn't last long - updates to different versions of Joplin on different devices resulted in incompatible versions of the notes database being synced, and at one point the Android version became unable to export to the filesystem at all. I never got to the bottom of that, but I had moved to using [Logseq][logseq] for most of my notes on the computer anyway, so it didn't really matter much.

I also mostly fell out of using Syncthing, since I no longer required it for its primary purpose. However I got a Framework laptop recently and had the need to sync my Logseq graphs to it, as well as my music collection, work files, etc. It was such a joy to get it set up and watch files start to zip across to the new machine that I once again had to sing the praises of this amazing piece of software.

Some shares I have set up so far:

* **The camera roll on my phone** - send only so that remote devices can't add or delete photos. It's great to have photos zip across to whichever computer I'm using without having to involve Google Photos.
* **The Default sync folder** - why not? If some random file is needed everywhere it can go in there. It always throws me a bit that these create a common shared folder rather than each device's folder being it's own thing, but it's cool, it's fine, I'll get used to it.
* **My Logseq graph folders** - I set these up to backup any changes just in case, because Syncthing will not perform merges. However I'm not really that worried about it because I will only work on one machine at a time, and if the sync runs regularly it shouldn't be a problem.
* **My music collection** - I set this up to ignore `*.zip` and `*.part` for uh... reasons. One of the nuisances of a collection of downloaded music is ensuring that every new acquisition gets to every device where you might want to listen to it *before* you want to listen to it. Well, problem solved! And no more shaming from Spotify for streaming the same album on repeat for several months! (It was Manu Chao)
* **Several shares specifically between two particular devices** e.g. huge desktop replacement laptop to the Framework, for when I want to share files specifically between those but not my phone.

I'm considering syncing some specific work folders as well so I can more easily untether from my desk, but... haven't decided yet.

[previous]: {filename}/joplin.md "Previous Joplin & Syncthing post"
[joplin]: https://joplinapp.org/ "Joplin's website"
[syncthing]: https://syncthing.net/ "Syncthing website"
[logseq]: https://logseq.com/ "Logseq website"
