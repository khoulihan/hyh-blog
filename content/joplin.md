Title: Joplin & Syncthing
Date: 2021-08-27 13:11
Category: Technology
Tags: foss, privacy
Slug: joplin
Authors: Kevin Houlihan
Summary: I recently switched from Evernote to Joplin, using Syncthing to sync my notes between devices.
Status: draft

I've been using Evernote for quite a few years now for keeping work and personal notes, despite never really being happy with it. Aside from the fact of entrusting my data to a private company, most of my issues with it were minor nuisances, and momentum kept me using it because I didn't see a good alternative that seemed impressive enough to be worth the hassle of migration. I considered writing my own alternative many times, but of course there were even greater barriers to that!

A few weeks ago I decided to finally take the plunge and try out Joplin, a FOSS note-taking desktop and mobile app.

## Joplin

Migrating to Joplin was relatively easy, as it can import Evernote's "ENEX" export format. Unfortunately Evernote made me [jump through a few hoops][export] to create these files - the web app, which I usually use, wouldn't do it, and the export had to be done notebook by notebook.

Joplin did a fairly good job of converting the formatting to its native Markdown, but my notes were a mess anyway so it hardly mattered. The main thing that seemed to go wrong was headers being converted to bold text instead of actual header lines. I also had to reorganise the notebook hierarchy since the notebooks were exported and imported individually. With that done I was about where I had been with Evernote, albeit only on my main computer.

Joplin includes both a Markdown editor and a WYSIWYG editor. I haven't tried the WYSIWYG editor because I like writing in Markdown these days, and I'm hoping using it will result in more structured notes than I've been keeping in the past. The default layout has the Markdown and rendered output side by side which I do find a little strange - I can never decide which side I should be reading. However, there is a button in the top right corner of the window to switch between dedicated editing, reading and side-by-side modes.

## Sync That Thing

Joplin can sync between instances using all of the main cloud storage services as well as its own cloud offering. However, the method that appealed to me, because it keeps my notes out of anybody else's hands, was to use [Syncthing][syncthing].

Syncthing is a P2P file synchronisation protocol and app that supports all major operating systems, and doesn't require any complex network configuration.

Joplin is actually unaware of Syncthing - to use it, you need to select the "File system" sync target and point it to a directory. It will periodically export changes to this directory and import any changes it finds there.

![Joplin sync settings]({static}/images/joplin/joplinsettings.png "Joplin sync settings")

Syncthing is managed via a web interface on localhost port 8384 by default. There are two main tasks to perform here - connecting your devices, and sharing your notes directory.

Devices in Syncthing are identified by quite unwieldy SHA-256 hashes, but it provides a number of ways to simplify exchanging these. Devices on the LAN are listed in the add device dialog, and if you're using it on mobile there is an option to scan a QR code for the device you're connecting. Devices have to grant permission to other devices that add them, and once they do you can choose which folders to share.

![Add device]({static}/images/joplin/adddevice.png "Add device")

Adding a folder is just a matter of entering the path to it on the file system, and giving it a name. You can select existing remote devices to sharing with on the "Sharing" tab, or share it later. Devices have to approve shared folders as well, and you will have an opportunity to choose a target location at that point as well.

![Add folder]({static}/images/joplin/addfolder.png "Add folder")

Syncthing on Android actually has two user interfaces, a native one and the same web UI as is available on desktop, which is a bit confusing. I found I had to drop down to the web UI to approve remote device and folder connections.

The Joplin configuration should be basically the same on any devices you want to sync - just choose the "File system" target and point to the synced notes folder. On desktop there is an option to clear the local notes and take everything fresh from the sync target, but the Android app seems to be missing this. As such, you might end up with multiple copies of Joplin's initial documentation notes.

## Beyond Notes

Syncthing has actually been a revelation for me. As well as my notes I've been using it to sync photos from my phone to my laptop (previously I was relying on Google Photos), and for sending miscellaneous files from my laptop to my phone (previously Google Drive's job). I've also been using it to send video files to my phone, something I wasn't even bothering with before.

It feels great to be able to cut Google out of the loop, and so far it has been working away flawlessly in the background without me having to think about it after the initial setup.

[Joplin]: https://joplinapp.org/ "Joplin's website"
[export]: https://help.evernote.com/hc/en-us/articles/209005557-Export-notes-and-notebooks-as-ENEX-or-HTML "How to export notes from Evernote"
[syncthing]: https://syncthing.net/ "Syncthing website"
