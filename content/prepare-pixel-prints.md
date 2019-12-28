Title: Prepare Pixel Prints README
Date: 2019-12-24 11:06
Modified: 2019-12-24 11:06
Category: Art
Tags: python, pixelart, automation
Slug: prepare-pixel-prints
Authors: Kevin Houlihan
Summary: A readme for my prepare-pixel-prints script

A script for generating print files from pixel art for various print-on-demand services.

The currently supported services include RedBubble, Displate, InPRNT, and Printful (selected canvas and poster products only). The RedBubble output files may be general enough to be used with other services.

Copyright (c) 2019 by Kevin Houlihan

License: MIT, see LICENSE for more details.

## Prerequisites

The script depends on Python 3.6 (though possibly earlier versions of Python 3 will work fine), and the imaging library [Pillow](https://pillow.readthedocs.io/en/stable/index.html).

## Usage

At minimum, the script requires a pixel art file at the art's original resolution. Any file type supported by the Pillow library should work, but lossless formats are recommended (such as PNG). This will output files for all services & products in a directory called "prints" next to the input file.

```bash
prepareprints.py portrait.png
```

### Destination

A different destination can be specified with the `--destination` switch. If a relative path is specified, it will be assumed to be relative to the input file location.

```bash
prepareprints.py --destination ~/kevin/artprints/portrait portrait.png
```

Whether an explicit destination is specified or not, the output directory will be created if it doesn't exist.

### Cropping

Where an image must be cropped to meet the criteria of a product or service, by default the crop will be performed on both sides of whatever axis is required to match the target aspect ratio. If one side of the art is more important than the other then the `--retain` switch can be used to prevent it from being cropped. Available options are `top`, `bottom`, `left`, and `right`. For example, this command will cause the top of the art to be retained during any cropping:

```bash
prepareprints.py --retain top -- portrait.png
```

### Service Selection

If you only want to prepare files for certain services, you can use the switches `--redbubble`, `--displate`, `--printful`, and `--inprnt` to specify which ones you want. More than one of these can be specified at a time.

```bash
prepareprints.py --redbubble --displate portrait.png
```

### RedBubble / Miscellaneous

For RedBubble, the input file is scaled by the lowest integer factor that will put it over 7632 x 6480, as per RedBubble's guidelines. Two rotated versions are also generated, one clockwise and the other counter-clockwise, as these are often a better fit for certain types of products. The files are output in PNG format.

As the output for this service is the least specific, it is recommended for other print services that are not explicitly covered by this script, such as Society6.

RedBubble output can be specified using the `--redbubble` switch as mentioned above. There are no additional service-specific options.

### Displate

For Displate, the input file is cropped to a 1.4:1 ratio, and then scaled by the smallest integer factor that will put the shortest side over 10000 pixels. The output is in JPEG format as per Displate's requirements.

The output for this service has some known issues, and currently is sometimes not accepted by Displate.

Displate output can be specified using the `--displate` switch as mentioned above. The cropping directives described above are taken into account during the cropping, where possible. There are no additional service-specific options.

### InPRNT

InPRNT requires a file that is less than 6600 x 10200 in size, so the art is scaled by the largest integer factor that will fit it within that resolution. The art is not currently cropped to that ratio. The output is in JPEG format.

InPRNT output can be specified using the `--inprnt` switch as mentioned above. There are no additional service-specific options.

### Printful

The output for the Printful service attempts to fit the art within the templates provided by them for their canvas, poster, and poster+mat wall art products. Other products are not included at this time. The exact operations performed on the input varies per product, but generally involves cropping to a specific ratio, and scaling by an integer factor to a target size or DPI. Files are output in PNG format.

Printful output can be specified using the `--printful` switch as mentioned above.

If only specific products are required, the service-specific `--products` switch can be used. It accepts `poster`, `canvas`, and `poster_with_mat` as options, and more than one can be specified. The default, however, is to prepare files for all product types.

```bash
prepareprints.py --products poster poster_with_mat -- portrait.png
```

In addition to limiting the output to specific products, it can be limited to specific sizes of products with the `--sizes` switch. The sizes are specified as `widthxheight`, but always in portrait orientation, even if the art is landscape. The output will still be oriented correctly. The sizes available vary by product, as shown in the following table. Different sizes of posters that have the same aspect ratio only output one file that is suitable for all sizes.

Product | Units | Aspect Ratio | Sizes
------- | ----- | ------------ | -----
Posters | Inches | 1:1 | 10x10, 12x12, 14x14, 16x16, 18x18
Posters | Inches | 2:3 | 12x18, 24x36
Posters | Inches | 3:4 | 12x16, 18x24
Posters | Inches | 4:5 | 8x10, 16x20
Posters | Centimeters | 3:4 | 30x40
Posters | Centimeters | 5:7 | 50x70
Posters | Centimeters | 7:10 | 21x30, 70x100
Posters with mat | Centimeters | Various | 21x30, 30x40, 50x70, 61x91
Canvases | Inches | Various | 12x12, 12x16, 16x16, 16x20, 18x24, 24x36

```bash
prepareprints.py --products poster --sizes 12x16 12x18 -- portrait.png
```

The default is to prepare files for all product sizes.

#### Canvas Options

There are a number of options specifically to tailor the output of the canvas product files.

The `--logo` switch (`-l` for short) takes an image file as input. This will be rotated 180 degrees, scaled, and placed in the location specified for logos on the [canvas templates](https://printful.s3.amazonaws.com/upload/guideline/CANVAS.zip).

The `--edge` switch can be used to control how the edges of the canvas will look. There are a number of options, and they can be combined to create different effects (though not all combinations may make sense). The default edge type is `extend`.

Edge Type | Effect
--------- | ------
solid | The edges will be filled with a solid colour.
extend | A single pixel width of the art at each border will be extended across the edge.
blur | The art is scaled up to cover the canvas edges, then blurred.
blurextend | The art is scaled up to cover the canvas edges, then blurred, and then a single pixel of the original art is extended across the edge. In effect, the corners of the edges are covered in blurred art, with the actual edges as per `extend`.
extendblur | The edges are filled with a solid colour, then covered as per `extend`, and the result is then blurred.

There is also an `--edgecolour` switch to specify a colour for the `solid` and `extendblur` edge types. It accepts colours in #rgb and #rrggbb as well as standard HTML colour names. There is no default, so a colour must be specified if one of these edge types is being used.

```bash
prepareprints.py --products canvas --edge solid extend --edgecolour #2cb --logo hyh_logo.png portrait.png
```