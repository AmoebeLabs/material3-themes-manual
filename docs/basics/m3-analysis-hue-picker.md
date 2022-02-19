---
template: overrides/main.html
---

The Figma Material Theme Builder offers both dynamic color based primary color picking as custom color picking. So let's see what they do!

###:material-home-floor-3: Dynamic color

I started my experiments with Google to find some random images for me, drag them into the Material Theme Builder and see what primary color (and secondary/tertiary colors of course) Material 3 appears with.

In doing so, I sometimes got confused because the theme didn't always really change. So I had to look more closely.

Take the following example. I dragged three different bluish images from the internet with a single color. And as you can see, the resulting source color - the extracted shade of Material 3 - is **exactly** the same (\#4285f4) :confused:.

| Dynamic example |||
|---|---|---|
|![mtb-blue-1-png]|![mtb-blue-2-png]|![mtb-blue-3-png]|

If I translate the hex RGB colors to HSL colors (Hue, Saturation, Lightness) I get from left to right:

| Position | hex | hsl | M3 hex | M3 hue |
| -------- | --- | --- | ------ | ------ |
| left | \#cbd5e1 | hsl(**212.73**, 26.83%, 83.92%) | \#4285f4 | **217.42** |
| middle | \#2d3945 | hsl(**210**, 21.05%, 22.35%) | \#4285f4 | **217.42** |
| right | \#aaadb2 | hsl(**217.5**, 4.94%, 68.24%) | \#4285f4 | **217.42** |

So, slightly different hues (212, 210 and 217), give the exact same Material 3 hue!

Converting the colors to CIE-Lch(ab) (Lightness, Chroma, Hue) using [ColorMine][colormine-url] also results in different hues for the three input images with yet another Material 3 hue:

| Position | hex | L | c | h | M3 h |
| -------- | --- | - | - | - | ---- |
| left | \#cbd5e1 | 84,85 | 7,15 | **261,54** | **284,36** |
| middle| \#2d3945 | 23,38 | 9,14 | **260,29** | **284,36** |
| left | \#aaadb2 | 70,63 | 2,93 | **268,29** | **284,36** |

!!! Success "Material 3 is NOT using the exact hue from the example, but definately using some secret color-fu"
    This at least explains the fact that I was sometimes not seeing any change in the color palettes!

###:material-home-floor-3: Custom color

Okay, so Material 3 uses some calculations to extract the hue from an image. I'm okay with that. But what about the Material Theme Builder's "Custom Color" option? It has to use YOUR color, yes?

_Color conversion using CIE-Lab_

| Theme | Custom | CIE-Lch(ab) | Primary | CIE-Lch(ab)|
| ---- | --- | ------- | ----------- | ------ |
| C1, Red | #ff4d4f <!--255,77,79-->| lch(59.10, 77.17, **29.93**) | #bb1826 | lch(40.17, 71.32, **31.31**) |
| C5, Yellow| #ffec3d <!--255,236,61-->| lch(92.40, 81.33, **97.95**) | #695f00 | lch(39.90, 47.34, **96.71**) |
| C7, Green | #73d13d <!--115,209,61--> | lch(75.81, 80.90, **130.59**)| #276c00 | lch(39.85, 59.90, **131.18**) |
| C9, Blue | #40a9ff <!--64,169,255--> | lch(67.04, 51.18, **268.01**) | #0062a1 | lch(40.09, 40.72, **270.55**) |

_Color conversion using CIE-Luv_

| Theme | Custom | CIE-Lch(uv) | Primary | CIE-Lch(uv)|
| ---- | --- | ------- | ----------- | ------ |
| C1, Red | #ff4d4f <!--255,77,79-->| lch(59.10, 139.18, **11.85**) | #bb1826 | lch(40.18, 119.53, **10.60**) |
| C5, Yellow| #ffec3d <!--255,236,61-->| lch(92.39, 95.30, **77.98**) | #695f00 | lch(39.89, 44.17, **76.85**) |
| C7, Green | #73d13d <!--115,209,61--> | lch(75.81, 92.48, **119.67**)| #276c00 | lch( 39.84, 56.92, **122.67**) |
| C9, Blue | #40a9ff <!--64,169,255--> | lch(67.03, 90.63, **245.90**) | #0062a1 | lch(40.09, 63.78, **247.40**) |

So the short answer is NO: Material 3 does NOT use its own color. On the other hand, the differences in CIE-Lch(ab) and CIE-Lch(uv) values ​​seem small. But what if I keep the lc part of the lch value and use the primary h value to recalculate the input color?

Taking the last example: Blue with `rgb(64, 169, 255)` becomes `rgb(76, 168, 255)`: In other words, MORE red, slightly less green, and no difference in blue.

On the left, the custom color, and on the right the extracted source color:

<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg" width="600px">
  <rect x="10" y="10" height="80" width="150" rx="0" fill="rgb(64, 169, 255)" stroke="var(--md-primary-fg-color--dark)" stroke-width="2"/>
  <rect x="200" y="10"height="80" width="150" rx="0" fill="rgb(76, 168, 255)" stroke="var(--md-primary-fg-color--dark)" stroke-width="2"/>
</svg>

!!! Success "Material 3 is NOT using the exact hue from your custom color input, but again some secret color-fu"
    The WHY remains unknown, but the difference is not that noticable...
<!--- References to pictures... --->

[mtb-blue-1-png]: ../assets/screenshots/material-theme-builder-blue.png
[mtb-blue-2-png]: ../assets/screenshots/material-theme-builder-blue2.png
[mtb-blue-3-png]: ../assets/screenshots/material-theme-builder-blue3.png

<!--- External links... --->

[colormine-url]: http://colormine.org/color-converter
[css-land-lch-color-picker-url]: https://css.land/lch/
[lea-verou-lch-colors-in-css-url]: https://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/
[ndb-lch-colors-url]: https://ninedegreesbelow.com/photography/gimp-srgb-lch-color-palettes.html