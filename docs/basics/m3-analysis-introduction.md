---
template: main.html
title: A new color space called HCT
description: With Material 3, Google introduces a new color system, called HCT, Hue / Chroma / Tone. A much better color system than Material Design used.
tags:
  - M3
  - Material 3
  - Colorspace
  - Analysis
---

<!-- GT/GMY -->
#A new color space called HCT

With Material 3 for Android 12, Google introduces a new color system, called [HCT][m3-hct-source-url].
<br>HCT is short for:

- <b>H</b>ue, ie the color in degrees (0..360)
- <b>C</b>hroma, ie the colorfulness, and
- <b>T</b>one, ie the lightness from white (100%)to black (0%).

!!! Success "The HCT color system combines the best from CIE-Lab and CAM16 color spaces"
    It is built using CAM16 for Hue and Chroma, and Lightness (L\*) from CIE-Lab.
    
##:material-home-floor-3: How does it work. Why is it so special?

The next two pages are about some experiments to see if I can understand how Material 3 works and if it does what it promises.

For this, I used the [22 examples][AmoebeLabs Material 3 Example introduction] I created to analyze some of the Material 3 aspects.

**TL;DR**
!!! Quote "From the examples, I can conclude that all themes with different colors give excellent displays with consistent readability and contrast."
    That makes the 22 themes interchangeable without any change to the Lovelace view and (custom) card configuration, assuming you use the Material 3 theme color definitions of course!
    <br><br>This, and the fact that I can generate a theme with Figma and a bit of Javascript, makes me very happy with M3, as this highly automated way of creating a theme also saves a _lot_ of time!

But then again, it raised enough questions about what Material 3 does in some cases.

[Read on][Material 3 Analysis Hue Picker], if you're interested :smile:

##:material-home-floor-3: But before, that, the basis of Material 3...

<!-- https://bootcamp.uxdesign.cc/perception-based-color-palettes-for-customizable-ui-themes-33f596faf23d -->
The newly introduced HCT color system combines both CIE-Lab and CAM16 color spaces. The best of both worlds.

The lightness in CIE-Lab is in line with human perception, allowing for very accurate color tones. It is _the_ reason why Material 3 can guarantee contrast differences, and thus the accessibility. The contrast difference between background and foreground is one of the most important factors in the [WCAG guidelines][wcag-guidelines-url].

Where the contrast ratio is non-linear, CIE-L\* is. It means that HCT can use differences to guarantee the contrast ratio. A difference of 40 in HCT tone guarantees a contrast ratio >= 3.0, and a difference of 50 guarantees a contrast ratio >= 4.5.
<br>If you look at the light and dark themes, you see these differences in the background and foreground colors. Material 3 uses a minimum difference of 60 to accomplish a great contrast ratio.

So, once again: Below you see the two examples as to why the combination of CIE-Lab and CAM16 is such a great idea:

![colorio-hue-linearity-ebner-fairchild-png]

_CAM16 shows the best Hue linearity_

<br>![colorio-munsell-lightness-png]

_CAM16 shows the best color circles and chroma lines_

<br>![colorio-lightness-png]
_And the CIELab model with the best lightness prediction_


    
(screenshots taken from [Colorio README][colorio-readme-url])

<!-- Image references -->

[colorio-hue-linearity-ebner-fairchild-png]: ../assets/screenshots/colorio-hue-linearity-ebner-fairchild.png
[colorio-munsell-lightness-png]: ../assets/screenshots/colorio-munsell-lightness.png
[colorio-lightness-png]: ../assets/screenshots/colorio-lightness.png

<!-- Internal  references -->

[AmoebeLabs Material 3 Example introduction]: ../examples/introduction.md
[Material 3 Analysis Hue Picker]: m3-analysis-hue-picker.md

<!-- External references -->

[m3-hct-source-url]: https://github.com/material-foundation/material-color-utilities/blob/main/typescript/hct/hct.ts
[wcag-guidelines-url]: https://www.w3.org/WAI/standards-guidelines/wcag/
[colorio-readme-url]: https://github.com/nschloe/colorio/blob/main/README.md