---
template: main.html
title: Material 3 Hue Picker
description: The free Figma Material Theme Builder plugin provides both dynamic color-based primary color selection and custom color selection. Let's see what they do!
tags:
  - Hue Picker
  - M3 Analysis
---
<!-- GT/GMY -->

Google offers the free Material Theme Builder plugin on its Figma platform.
<br>This builder provides both dynamic color-based primary color selection and custom color selection. So let's see what they do!

###:material-home-floor-3: Dynamic color

I started my experiments with Google to find some random images for me, drag them into the Material Theme Builder, and see what primary color (and secondary/tertiary colors of course) Material 3 appears with.

In doing so, I sometimes got confused because the theme didn't always really change. So I had to look more closely.

Take the following example. I dragged three different bluish images from the internet with a single color. And as you can see, the resulting source color - the extracted shade of Material 3 - is **exactly** the same (RGB color \#4285f4) :confused:.

| Dynamic example |||
|---|---|---|
|![mtb-blue-1-png]|![mtb-blue-2-png]|![mtb-blue-3-png]|

If I translate the hex RGB colors to HSL colors (Hue, Saturation, Lightness) I get from left to right:

| Position | Image hex | Image RGB-hsl | M3 hex | M3 hue |
| -------- | --- | --- | ------ | ------ |
| left | \#cbd5e1 | hsl(**212.7°**, 26.83%, 83.92%) | \#4285f4 | **217.4°** |
| middle | \#2d3945 | hsl(**210°**, 21.05%, 22.35%) | \#4285f4 | **217.4°** |
| right | \#aaadb2 | hsl(**217.5°**, 4.94%, 68.24%) | \#4285f4 | **217.4°** |

So, slightly different hues (212°, 210° and 217°), give the exact same Material 3 hue!

Converting the colors to CIE-Lch(ab) (Lightness, Chroma, Hue) using [ColorMine][colormine-url] also results in different hues for the three input images with yet another Material 3 hue:

| Position | Image hex | Image CIE-Lch | M3 Hue |
| -------- | --- | - | ---- |
| left | \#cbd5e1 | lch(84,8%, 7,15, **261,5°**) | **284,3°** |
| middle| \#2d3945 | lch(23,3%, 9,14, **260,2°**) | **284,3°** |
| left | \#aaadb2 | lch(70,3%, 2,93, **268,2°**) | **284,3°** |

!!! Success "Material 3 is NOT using the exact hue from the example, but definately using some HCT-fu here"
    This at least explains the fact that I was sometimes not seeing any change in the color palettes!

###:material-home-floor-3: Custom color

Okay, so Material 3 uses some calculations to extract the hue from an image. I'm okay with that. But what about the Material Theme Builder's "Custom Color" option? It has to use YOUR color, yes?

For this experiment, I took 4 colors from the cielab.io website and compared them with the Hue that HCT selected for the primary color.

_Color conversion using CIE-Lab_

| Theme | Custom | CIE-Lch(ab) | Primary | CIE-Lch(ab)|
| ---- | --- | ------- | ----------- | ------ |
| C1, Red | #ff4d4f <!--255,77,79-->| lch(59.1%, 77.17, **29.9°**) | #bb1826 | lch(40.1%, 71.3, **31.3°**) |
| C5, Yellow| #ffec3d <!--255,236,61-->| lch(92.4%, 81.33, **97.9°**) | #695f00 | lch(39.9%, 47.3, **96.7°**) |
| C7, Green | #73d13d <!--115,209,61--> | lch(75.8%, 80.90, **130.5°**)| #276c00 | lch(39.5%, 59.9, **131.1°**) |
| C9, Blue | #40a9ff <!--64,169,255--> | lch(67.0%, 51.18, **268.0°**) | #0062a1 | lch(40.0%, 40.7, **270.5°**) |

_Color conversion using CIE-Luv_

| Theme | Custom | CIE-Lch(uv) | Primary | CIE-Lch(uv)|
| ---- | --- | ------- | ----------- | ------ |
| C1, Red | #ff4d4f <!--255,77,79-->| lch(59.1%, 139.1, **11.8°**) | #bb1826 | lch(40.1%, 119.5, **10.6°**) |
| C5, Yellow| #ffec3d <!--255,236,61-->| lch(92.3%, 95.3, **77.9°**) | #695f00 | lch(39.8%, 44.1, **76.8°**) |
| C7, Green | #73d13d <!--115,209,61--> | lch(75.8%, 92.4, **119.6°**)| #276c00 | lch( 39.8%, 56.9, **122.6°**) |
| C9, Blue | #40a9ff <!--64,169,255--> | lch(67.0%, 90.6, **245.9°**) | #0062a1 | lch(40.0%, 63.7, **247.4°**) |

So the short answer is NO: Material 3 does NOT exactly use YOUR custom color. On the other hand, the differences in CIE-Lch(ab) and CIE-Lch(uv) values ​​are small. 

If I use the HCT result from the C9, Blue example and reverse the calculation to get an RGB color, I get a different kind of blue: where the custom color is `rgb(64, 169, 255)`, the selected primary color becomes `rgb(76, 168, 255)`: In other words, a bit more red, slightly less green, and no difference in blue.

On the left, the custom color, and on the right the extracted source color by HCT:

<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg" width="600px">
  <rect x="10" y="10" height="80" width="150" rx="0" fill="rgb(64, 169, 255)" stroke="var(--md-primary-fg-color--dark)" stroke-width="2"/>
  <rect x="200" y="10"height="80" width="150" rx="0" fill="rgb(76, 168, 255)" stroke="var(--md-primary-fg-color--dark)" stroke-width="2"/>
</svg>

!!! Success "Material 3 is NOT using the exact hue from your custom color input, but again some HCT-fu"
    The WHY remains unknown (haven't checked the sources at this moment), but the difference is not that noticable...

<!--- References to pictures... --->

[mtb-blue-1-png]: ../assets/screenshots/material-theme-builder-blue.png
[mtb-blue-2-png]: ../assets/screenshots/material-theme-builder-blue2.png
[mtb-blue-3-png]: ../assets/screenshots/material-theme-builder-blue3.png

<!--- External links... --->

[colormine-url]: http://colormine.org/color-converter
[css-land-lch-color-picker-url]: https://css.land/lch/
[lea-verou-lch-colors-in-css-url]: https://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/
[ndb-lch-colors-url]: https://ninedegreesbelow.com/photography/gimp-srgb-lch-color-palettes.html