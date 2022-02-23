---
template: overrides/main.html
---

##:material-home-floor-3: M3 Palettes...

One of the main highlights of Material 3 are the tonal palettes that should meet WCGA standards.

As Google says:

!!! Quote "Dynamic color is designed to meet accessibility standards for color contrast. The system of tonal palettes is central to making any color scheme accessible by default."

    Combining color based on tonality, rather than hex value or hue, is one of the key systems that make any color output accessible. Products using dynamic color will meet requirements because the algorithmic combinations that an end-user can experience are designed to meet accessibility standards.

As HCT uses the CIE-L\* colorspace for lightness, lets see if what that does with a generated tonal palette.

##:material-home-floor-3: CIE L* lightness check...

The CIE L\* colorspace aims to show colors as the human eye perceives colors and lightness. Within that space, there are different methods like CIE-Lab + CIE-Lch(ab) and CIE-Luv + CIE-Lch(uv).

The CIE-Lab and CIE-Lch(ab) use the same colorspace, but use different parameters to calculate the colors. The CIE-lch(\*) method is the easiest one to understand, as it uses degrees for the Hue (0..360 degrees), just as the sRGB(hsl) does.

Both CIE-Lab and CIE-Lch use the same Lightness, so we can use either of them to determine the lightness values.

So, lets take some samples from the C1 example and check the lightness values.

![m3-theme-c01-palettes-png]

_Color conversion using CIE-Lab_

| color | hex | m3 | Lightness (sRGB-hsl) | Lightness (CIE-Lch(ab)) |
| ---- | --- | ------- | --| ----------- |
| Primary20 | #68000a | 20% | hsl(354.23°, 100%, **20.39%**) | lch(**19.9%**, 49.32, 32.31°) |
| Primary40 | #bb1826 | 40% | hsl(354.85°, 77.25%, **41.37%**) | lch(**40.17%**, 71.32, 31.31°) |
| Secondary40 | \#775654 | 40% | hsl(3.43°, 17.24%, **39.8%**) | lch(**39.94%**, 14.89, 26.09°) |
| Tertiary40 | #735b2e | 40% | hsl(39.13°, 42.86%, **31.57%**) | lch(**40.12%**, 29.59, 82.25°) |
| Primary60 | #ff5354 | 60% | hsl(359.65°, 100%, **66.27%**) | lch(**59.96%**, 74.62, 29.51°) |
| Primary80 | #ffb3ac | 80% | hsl(5.06°, 100%, **83.73%**) | lch(**79.89%**, 30.53, 28.75°) |
| Primary99 | #fcfcfc | 99% | hsl(0°, 0%, **98.82%**) | lch(**98.96%**, 0.01, 296.81°) |

We see an exact match between the Material 3 lightness and the CIE-Lch(ab) lightness value for primary, secondary and tertiary color palettes.

!!! Success "Material 3 is using the CIE-L* colorspace to determine the lightness for tonal palettes"

So. Lets take a look at the primary, secondary and tertiary palettes. Can we make sense of them?

##:material-home-floor-3: Primary palette

Lets do some observations, and look at the primary palette first!

###:material-home-floor-3: Experiment 1: how do primary palettes compare?

Below you can see all primary pallets from the "custom" color examples. Please note that all x2%, x5% (except 95%) and x7% values ​​do not belong to the original Material 3 palette, but were added by me to have more tonal steps to work with.

Some noticable things from right to left:

- Some colors have less color in the darker area's than other colors: the red/blue/magenta show more color in darker tones than yellow/lime/green/cyan.
- There is a clear "break" visible at the 50%/60% tones: exactly the boundary between the dark and the light tones
- Another "break" is visible in many of the palettes between 80% and 90% (85% was added by me). 
- Some of the colors are very colorfull in the high lightness parts (say above 90%), and other are not. Especially the yellow, limegreen/green and cyan stand out.
<br><br>This is especially visible in the 99% lightness blocks. The above colors are visible, others are barely distinguishable.

![all-primary-palettes-png]

And that is to be expected, as these colors can have more color with high lightness values in the sRGB space when translated from CIE-L\* space than the others. 

The following example shows this effect: yellow, green and cyan are clearly more colorful than any other color at higher lightness! Blue, purple, magenta and red are much more subdued. The reverse is also valid: blue, purple, magenta and red are much more vibrant in darker tones.
<br>Notice that dark orange with high chroma doesn't exist: it turns into brown!

![lch-lightness-examples-png]

!!! Success "Material 3 is palette calculations are again clearly using CIE-L*, but does NOT compensate for the colorful colors in the high lightness parts"


###:material-home-floor-3: Experiment 2: what about palette hue?

As I couldn't find an CAM16 table, I'm using CIE-Lch(ab) and CIE-Lch(uv) to check the hue values with different lightness. Results are less accurate for that reason, but should be close compared to CAM16.

If we look at the next table, we can see that Material 3 is not only varying lightness for the tonal palette, but also varying both chroma and hue. As we have learnt from the above observation, keeping hue stable in the high lightness parts is difficult.

_Color conversion using CIE-L*_

| color | hex | m3 | Lightness (CIE-Lch(ab)) | Lightness (CIE-Lch(uv)) |
| ---- | --- | ------- | --| ----------- |
| Primary20 | #68000a | 20% | lch(19.9%, 49.32, **32.31°**) | lch( 19.9%, 64.81, **10.53°**) |
| Primary40 | #bb1826 | 40% | lch(40.17%, 71.32, **31.31°**) | lch(40.18%, 119.53, **10.59°**) |
| Primary60 | #ff5354 | 60% | lch(59.96%, 74.62, **29.51°**) | lch(59.97%  134.35, **11.99°**) |
| Primary80 | #ffb3ac | 80% | lch(79.89%, 30.53, **28.75°**) | lch(79.88%, 52.92, **17.20°**) |
| Primary99 | #fcfcfc | 99% | lch(98.96%, 0.01, **296.81°**) | lch(98.96%, 0.01, **247.09°**) |

However, the hsl values ​​of the sRGB space show 100% saturation on three of the 5 tones, which may indicate some sort of clipping while calculating the sRGB color from the CIE-Lch(\*) space, which gives a much wider color gamut.

And since I calculated the CIE-Lch(\*) colors from the sRGB hsl colors, the CIE-Lch(\*) colors may not be that accurate with regard to hue and chroma!

Looking at the remarks at the [CIELab site][cielab-io-url], the relation between hue/chroma and luminance means that you can't have all the three parameters at its "best" value, and you have to balance all three:

!!! Quote "Oftentimes, you can sacrifice chroma to make luminance and hue work"

!!! Quote "Usually, you want shades to have roughly the same hue. That way, shades don't seem to "drift" into a different color"

!!! Success "Material 3 HCT palette calculations are doing their best to balance hue, lightness and colorfulness"
    CAM16 seems to do a wonderful job!

##:material-home-floor-3: Secondary and Tertiary palette

For starters, the "normal" way to choose a secondary or tertiary color is to move the color wheel a few degrees. However, since the human eye is non-linear and Google makes a point about accessibility standards, a standard color wheel probably isn't what Material 3 uses.

###:material-home-floor-3: Experiment 3: Can we make sense of secondary and tertiary colors?

Since I couldn't find a CAM16 converter online, I'm using CIE-LCh(uv) for this experiment. It's not very good at predicting chroma and hue, but maybe we can see something. Chroma is better than the Hue Prediction.

Using the mean values ​​and differences, the variations between CAM16 and CIE-LCh(uv) can be smoothed out.

**Secondary color palette:**

- The hue value varies but stays close to the primary hue value with an average difference of **0.05°** (so nearly the same!).
- The chroma value seems to be very constant: **~20** for red and yellow, and around **~16** for the other colors. The chroma for the primary color has all sorts of values, so this can't be a coincidence.

**Tertiary color palette:**

- The hue value hovers between 39° and 83° with an average of **61°**.
- The chroma value hovers between 21 and 38 with an average of: **28**.


| What | hex | Lightness | Chroma | Hue | H Diff |
| ---- | --- | --------- | ------ | - | - |
| **C1, Red** |||||
| Primary | #bb1826  | 40.18% | 119.54 | 10.59° ||
| Secondary | \#775654 |  39.94% |  **21.78** |  15.68° | 5.09° |
| Tertiary | #735b2e  | 40.12% |  35.43 |  58.38° | 47.79° |
| **C5, Yellow** |||||
| Primary | #695f00  |  39.89% | 44.17 |  76.85° | |
| Secondary | #635f41  | 39.94% |  **21.50** |  79.30° | 2.45° |
| Tertiary | \#406652  | 39.91% |  21.32 |  147.29° | 70.44° |
| **C7, Green** |||||
| Primary | #276c00  | 39.84% |  56.92 | 122.67° | |
| Secondary | #55624b |  39.87% |  **16.57** | 112.00° | -10.67° |
| Tertiary | \#386666 |   40.08% |  20.82 | 192.17° | 69.5° |
| **C9, Blue** |||||
| Primary | #0062a1 |  40.09% |   63.78 | 247.40° | |
| Secondary | \#526070 |  40.12% |   **16.38** | 241.81° | -5.59° |
| Tertiary | \#695779 | 39.91% |  25.61 | 286.56° | 39.16° |
| **C11, Purple** |||||
| Primary | #7a3ac5 |  39.90% |   94.37 | 278.45° | |
| Secondary | #655a70 |  39.99% |  **16.55** | 286.00° | 7.55° |
| Tertiary | #80525a |  40.18% |   28.83 |   1.64° | 83.19° |
| **C12, Magenta** |||||
| Primary | #b01a72 |  39.89% |   85.46 |  342.77° | |
| Secondary | \#735762 |  40.15% |  **16.60** | 344.33° | 1.56° |
| Tertiary | #7e5538 |  39.94% | 38.16 |  38.04° | 55.27° |

And finally, lets see how these observerations stack up against he real thing, as the calculations are [known for both palettes][m3-palettes-ts-url]:

**Secondary color palette:**

- Hue is the **same** as for the primary color palette. Matches with the 0.05° difference.
- Chroma is fixed to **16**! I got 2x20 and 4x16 (average of 18.2), so still a good match for some of the colors.

And the **tertiary palette:**

- Hue is shifted **60°** from the primary color palette. The CIE-LCh(uv) averaged at 61°. Again pretty close!
- Chroma is fixed to **24**! I got 28 from CIE-LCh(uv). CAM16 is much better for chroma.

!!! Success "The average CIE-LCh(uv) values and differences are close to the actual CAM16 settings, a nice result!"

<!-- https://bottosson.github.io/posts/oklab/ -->

<!--
The table below shows colors from 6 examples and the difference in degrees for the hues in both CIE-Lch(ab) and CIE-Lch(uv) space

_Color conversion using CIE-Lab_ (conversions using https://www.easyrgb.com/en/convert.php#inputFORM)

| What | hex | H (CIE-Lch(ab)) | H diff | H (CIE-Lch(uv) | H diff |
| ---- | --- | ----------- | ------ | - | - |
| **C1, Red** |||||
| Primary | #bb1826  | **31.31** |  | **10.59** | | 
| Secondary | \#775654 | **26.09** | -5.22 | **15.68** | 5.09 |
| Tertiary | #735b2e  | **82.25** | 50.94 | **58.38** | 47.79 |
| **C5, Yellow** |||||
| Primary | #695f00  | **96.71** |  |**76.85** | |
| Secondary | #635f41  | **101.46** | 4.75 | **79.30** | 2.45 |
| Tertiary | \#406652  | **158.97** | 62.26 | **147.29** | 70.44 |
| **C7, Green** |||||
| Primary | #276c00  | **131.18** |  | **122.67** | |
| Secondary | #55624b | **130.34** | -0.84 | **112.00** | -10.67 |
| Tertiary | #386666 | **197.43** | 66.25 | **192.17** | 69.5 |
| **C9, Blue** |||||
| Primary | #0062a1 | **270.55** |  | **247.40** | |
| Secondary | \#526070 | **262.82** | -7.73 | **241.81** | -5.59 |
| Tertiary | \#695779 | **311.33** | 40.78 | **286.56** | 39.16 |
| **C11, Purple** |||||
| Primary | #7a3ac5 | **311.37** |  | **278.45** | |
| Secondary | #655a70 | **309.93** | -1.44 | **286.00** | 7.55 |
| Tertiary | #80525a | **9.27** | 57.9 | **1.64** | 83.19 |
| **C12, Magenta** |||||
| Primary | #b01a72 | **349.87** |  | **342.77** | |
| Secondary | \#735762 | **352.16** | 2.29 | **344.33** | 1.56 |
| Tertiary | #7e5538 | **60.19** | 70.32 | **38.04** | 55.27 |


Primary to secondary color:

- The difference is small and not equal for all colors
- The direction on the color wheel is sometimes to the left, sometimes to the right

Primary to tertiary color:

- The difference is fairly large and not equal for all colors
- The direction on the color wheel is always to the right

!!! Success "Material 3 is using some special CIE-Lch(\*) calculation to determine secondary and tertiary tonal palettes"
    The secondary color shows that especially with its right/left direction. The tertiary color is always to the right. Both secondary and tertiary colors show a nonlinear difference though!

!!! Fail "Even CIE-Lch(uv) shows different Hue differences, altough this wheel should have evenly distributed colors"

###:material-home-floor-3: Experiment 4: do color wheels show something?

The website [Nine Degrees Below][ndb-lch-colors-url] has done a lot of work in this part, including some nice pictures.

At first it shows "Why 30 degree steps don't work" in both the sRGB and CIE-Lch(ab) colorspace to determine secondary and tertiary colors. Apart from the fact that they don't match, you see a lot of green colors in the sRGB space, and a lot of blue colors in the CIE-Lch(ab) space with even a missing yellow, true green and purple block.

![ndb-HSV-LCh-max-sat-color-palettes-png]


And if you look at both the HSV and CIE-Lch(ab) color distribution wheels, you understand why: the color distribution is totally different. You also see that purple and blue are very close in the Lab space: so no surpise it is missing from the above palettes at 30 degree intervals.
![hsv-lch-color wheel-jpg]

This gives the following color wheel for CIE-Lab space:
![cielab-color wheel-png]

So, they created an adapted CIE-Lch(ab) color palette with 24 colors:

![ndb-color-names-LCh-hues-png]

With the corresponding 24 colorsteps in the color wheel:

![ndb-saturation-0_dot_8]

If I use this color wheel to roughly determine the 'steps' between the primary and secondary/tertiary colors, I get the following:

| Theme | Primary | Secondary | Steps | Tertiary | Steps |
| -|-|-|-|-|-|
| C1, Red | RO(38) | R(24) | -1 | OY(80) | 3 |
| C5, Yellow | GY(100) | GY(100) | 0 | G(162) | 4 |
| C7, Green | YG(130) | YG(130) | 0 | BG(204) | 4 |
| C9, Blue | VB(270) | B(260) | -1 | V(310) | 3 |
| C11, Purple | V(310) | V(310) | 0 | VR(0) | 3 |
| C12, Magenta | VR(342) | VR(0) | 0-1 | YO(65) | 4-5 |

Hmmm. Not more than an indication that there is a certain consistancy in the "distance" between the primary, secondary and tertiary colors, which seem to depend on the primary colors position in the color space.


!!! Fail "It remains unknown how Material 3 is calculating secondary and tertiary colors on the CIE-Lch(\*) color wheel"
    Other people wil do this in the future I guess, as that happened also for Material 2!
-->
<!--
#### Last experiment
The steps are only a rough approximation, so let's calculate the size and percentage for each part of the color wheel using the min/max values ​​of each part:

| Color | Central | Min | Max | Size | Part% | 
| ----- | ------- | --- | --- | ---- | ----- |
| VR | 0 | 351 | 12 | 21 | 5.8% |
| R | 24 | 12 | 31 | 19 | 5.3% |
| RO | 38 | 31 | 45.5 | 14.5 | 4.0% |
| O | 53 | 45.5 | 59 | 13.5 | 3.75% |
| YO | 65 | 59 | 72.5 | 13.5 | 3.75% |
| OY | 80 | 72.5 | 85 | 12.5 | 3.5% |
| Y | 90 | 85 | 95 | 10 | 2.78% |
| GY | 100 | 95 | 107.5 | 12.5 | 3.5% |
| YG | 115 | 107.5 | 122.5 | 15 | 4.2% |
| YG | 130 | 122.5 | 137.5 | 15 |  4.2% |
| G | 145 | 137.5 | 153.5 | 16 | 4.4% |
| G | 162 | 153.5 | 171 | 17.5 | 4.9% |
| BG | 180 | 171 | 192 | 21 | 5.8% |
| BG | 204 | 192 | 211 | 19 | 5.3% |
| GB | 218 | 211 | 225.5 | 14.5 | 4.0% |
| GB | 233 | 225.5 | 239 | 13.5 | 3.75% |
| B | 245 | 239 | 252.5 | 13.5 | 3.75% |
| B | 260 | 252.5 | 265 | 12.5 | 3.5% |
| VB | 270 | 265 | 275 | 10 | 2.78% |
| VB | 280 | 275 | 287.5 | 12.5 | 3.5% |
| BV | 295 | 287.5 | 302.5 | 15 | 4.2% |
| V | 310 | 302.5 | 317.5 | 15 | 4.2% |
| RV | 325 | 317.5 | 333.5 | 16 | 4.4% |
| VR | 342 | 333.5 | 351 | 17.5 | 4.9% |

Now use the real primary and tertiary values ​​and use the normalized size (each part is 4.2% in the color wheel) to calculate the real "distance" between the primary and tertiary color.

The tables shows the CIE-Lch(ab) Hue difference as the "Abs Diff". 

| Theme | Primary | Tertiary | Abs Diff | Steps | Wheel %|
| -|-|-|-|-|-|
| C1, Red | RO(38) | OY(80) | 50.94 | 3 | 15.7% |
| C5, Yellow | GY(100) | G(162) | 62.26 | 4 | 17.4% |
| C7, Green | YG(130) | BG(204) | 66.25 | 4 | 15.5% |
| C9, Blue | VB(270) | V(310) | 40.78 | 3 | 12.6% |

The percentages are pretty close together, with an exception again for the blue part. Of course I don't know how accurate Nine Degrees Below's CIE-Lch(ab) color wheel is, meaning there are differences where expected. Material may use a 15% color wheel shift in the CIE-Lch(ab) domain for the tertiary color.

For the secondary color I have no idea, because the direction is to the right in some cases and left in other cases.

!!! Fail "It remains unknown how Material 3 is calculating secondary and tertiary colors on the CIE-Lch(ab) color wheel"
-->

<!--- References to pictures... --->

[mtb-blue-1-png]: ../assets/screenshots/material-theme-builder-blue.png
[mtb-blue-2-png]: ../assets/screenshots/material-theme-builder-blue2.png
[mtb-blue-3-png]: ../assets/screenshots/material-theme-builder-blue3.png

[m3-theme-c01-palettes-png]: ../assets/screenshots/m3-theme-c01-palettes.png

[all-primary-palettes-png]: ../assets/screenshots/all-primary-palettes.png

[hsluv-l90-example-png]: ../assets/screenshots/hsluv-l90-example.png

[lch-lightness-examples-png]: ../assets/screenshots/lch-lightness-examples.png

[ndb-HSV-LCh-max-sat-color-palettes-png]: ../assets/screenshots/HSV-LCh-max-sat-color-palettes.png
[ndb-color-names-LCh-hues-png]: ../assets/screenshots/color-names-LCh-hues.png
[ndb-saturation-0_dot_8]: ../assets/screenshots/saturation-0_dot_8.png

[hsv-lch-colorwheel-jpg]: ../assets/screenshots/hsv-lch-colorwheel.jpg
[cielab-colorwheel-png]:  ../assets/screenshots/cielab-colorwheel.png

<!--- External links... --->

[colormine-url]: http://colormine.org/color-converter
[css-land-lch-color-picker-url]: https://css.land/lch/
[lea-verou-lch-colors-in-css-url]: https://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/
[ndb-lch-colors-url]: https://ninedegreesbelow.com/photography/gimp-srgb-lch-color-palettes.html
[cielab-io-url]: https://cielab.io/
[m3-palettes-ts-url]: https://github.com/material-foundation/material-color-utilities/blob/main/typescript/palettes/core_palette.ts
<!--

cie2000
red
primary40 en sec = 14.4576
primary40 en tert = 50

yellow
primary 695f00, hsl(54.29, 100%, 20.59%)
secondary #636341, rgb 99,95,65 hsl(52.94, 20.73%, 32.16%), de2000 = 12.87
406652 , hsl(148.42, 22.89%, 32.55%), de2000 = 31.6654

https://convertingcolors.com/hex-color-636341.html


2022.02.20
Test met rood in de hoek, c50001.
p40=#c00000, 80=#ffb4a7, 90=#ffdad3, 99=#fcfcfc, luv40=39.932  131.267   28.319  (134), lchuv= 39.932  134.287   12.174°
s40=#775752, 80=#e7bdb6, 90=#ffdad3, 99=#fcfcfc, luv40=40.161   20.643    7.849 (22.08), 40.161   22.085   20.819°
t40=#705c2e, 80=#dec48c, 90=#fbdfa5, 99=#fffbf8, luv40=40.076   15.726   30.441

00fbff
p40=#00696c, 80=#02dce0, 90=#02fbff, 99=#efffff, luv40=39.890  -30.547   -9.129 (31.88), 39.890   31.882  196.638°
s40=#4a6393, 80=#b0cccc, 90=#cce8e8, 99=#efffff, luv40=41.977  -12.795  -42.562 (44.44), 41.977   44.444  253.268°
t40=#4c5f7c, 80=#b4c8e9, 90=#d3e3ff, 99=#fdfcff, luv40=39.875  -10.150  -25.817


-->