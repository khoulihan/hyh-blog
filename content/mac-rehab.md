Title: iRehabilitation
Date: 2021-06-21 23:55
Category: Technology
Tags: mac, linux, blogging
Slug: mac-rehab
Authors: Kevin Houlihan
Summary: Attempting to keep an old-ish MacBook useful and interesting with Xubuntu.
Status: published

I've been plagued by temptation lately to buy a [Pinebook Pro][pbpro]. My current laptop is really a desktop replacement, a beast that can hardly last an hour untethered from a power socket. It's usually not worth the hassle of extracting it from its tangled nest of cables when I want to compute elsewhere, and that's fine - it's the workhorse. But as a result, the idea of a light, efficient laptop is alluring, especially when it's one that runs Linux.

## Out with the New

However, I don't really like to buy new devices without good reason. I already have another laptop that meets the criteria of being relatively light and portable - the MacBook Pro that served as my main work machine between 2015 and 2019 when my wife and I were floating around Ireland, France and Spain and living out of the back of our car. I have been using it as a more portable option already on occasion, but it has a few annoying problems:

* The battery isn't in great shape, so while it's a lot better than my main laptop, it's nothing like that expected of the Pinebook Pro.
* The OS is outdated. It's demanding constantly that I update to a newer version of MacOS, but I don't want to. Apparently it could run the latest version, but I don't trust Apple to preserve the usability of old devices.
* It runs MacOS. MacOS is fine - it's a Unix, it's not Windows... but it still has a lot of little annoyances, it's proprietary, and to be honest, I'm bored with it.

Basically it's lost its shine, and isn't fun to use anymore.

![Happier times house-sitting in Belfast]({static}/images/mac-rehab/early-days.jpg "Happier times house-sitting in Belfast")

## A Cunning Plan

One of Linux's oft-heralded killer use-cases is in giving old hardware new life. I've never really used it for that explicit purpose - whenever I use Linux, it's just because I prefer to use Linux, even if it happens to be on old or low-powered machines. This one isn't exactly an ancient artifact, but I thought maybe installing a Linux distro with a lightweight desktop environment would help stretch the battery life and make it feel a bit snappier, more like a new machine.

The two distros I considered were [ElementaryOS][elementary] and [Xubuntu][xubuntu]. I'm not sure how lightweight Elementary's DE is, but I liked the look of it, so I decided to try it out with an eye to maybe using it as my main OS some day.

First impressions were great - it only used 700MB of RAM after booting (compared to nearly 4GB for MacOS!), and the degree of visual flair and polish were incredibly impressive. Unfortunately a couple of things put me off - when I cut the CPU frequency to 800MHz I began to experience occasional lag, and at one point the shell crashed with no way to recover it!

I didn't have any experiences like that with Xubuntu. I ran it for a whole day from a USB stick, installed a bunch of software, worked on a blog post, and had no issues - so that was that decision made! It's definitely not as visually impressive as Elementary, but I'd rather a responsive system than a pretty one in this case.

## Installation

Installation was pretty smooth, especially compared to installing Linux on PowerPC Macs back in the day. The only snag was with the proprietary wireless driver. This was easily enough installed using the "Additional Drivers" settings dialog when running from the USB stick, but after installation the required driver was no longer available. Having no other means to connect to a network, this was a serious problem!

Solving this involved a couple of steps. First I enabled the "CDROM" source in the Software & Updates settings, under the "Other Software" tab. This caused the driver to become available in the Additional Drivers dialog, but it wouldn't install. The problem was that the live USB stick was mounted somewhere under `/media/kevin`, but apt expected it to be mounted at `/media/cdrom`, which didn't even exist. Unmounting the USB stick and running the following commands sorted it out, and allowed me to connect to the WiFi to install and upgrade other packages.

```
sudo mkdir /media/cdrom
sudo mount /dev/sdb1 /media/cdrom
sudo apt install bcmwl-kernel-source
```

## Results

Unfortunately the results were not quite what I'd hoped. I performed a test where I played a movie and music on a loop under both OSes, and Xubuntu was down to 10% battery in 1 hour 46 minutes, while Mac OS took 2 hours and 28 minutes to reach the same level. This was with all cores throttled to 800MHz under Xubuntu, and MacOS doing whatever it does naturally to save energy, but full screen and keyboard backlight brightness on both.

While Xubuntu runs great, and is much more pleasant to use for me, it doesn't seem to achieve the same battery life under similar loads. I'm torn now between the user experience I prefer under Xubuntu and the superior energy efficiency of MacOS... Or perhaps buying a Pinebook after all!

![Cheers on a game-jam well done]({static}/images/mac-rehab/game-jam.jpg "Cheers on a game-jam well done")

[pbpro]: https://www.pine64.org/pinebook-pro/ "Pinebook Pro"
[elementary]: https://elementary.io/ "Elementary OS"
[xubuntu]: https://xubuntu.org/ "Xubuntu"
