Title: Prepare Timelapse Clips README
Date: 2019-12-24 11:43
Modified: 2019-12-24 11:43
Category: Programming
Tags: python, video, automation
Slug: prepare-timelapse-clips
Authors: Kevin Houlihan
Summary: A readme for my prepare-timelapse-clips script

A script for preparing video clips of a timelapse captured as a sequence of frames (as by my other script, [capture-timelapse](https://github.com/khoulihan/capture-timelapse)).

Copyright (c) 2019 by Kevin Houlihan

License: MIT, see LICENSE for more details.

## Prerequisites

The script depends on Python 3.6 (though possibly earlier versions of Python 3 will work fine). The ffmpeg command line utility must be installed and available to the script.

## Usage

At minimum, the script just takes a source directory as input. The source is expected to contain subdirectories, each containing a sequence of images in PNG format. An mp4 video clip will be generated for each subdirectory at 20 FPS and placed in an output directory called "clips".

An extra clip will also be generated based on the final frame of the last subdirectory, stretched out to a minute in length, to be used as padding at the end of the video.

```bash
prepareclips.py ~/timelapses/ldjam/
```

An alternative destination can be specified with the `--destination` switch. If a relative path is provided, it will be assumed to be relative to the source directory.

The framerate can be specified with the `--framerate` (`-f` for short) switch.

Finally, if a padding clip is not required, it can be skipped with the switch `--skippadclip` (`-s` for short).