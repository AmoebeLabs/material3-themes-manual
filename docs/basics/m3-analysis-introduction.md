---
template: overrides/main.html
---

<!-- GT/GMY -->

##:material-home-floor-3: Material 3 analyzed!

This chapter is about some experiments to see if I can understand how Material 3 works and if it does what it promises.

For this, I used the 22 examples I created to analyze some of the Material 3 aspects.

From the examples, I can conclude that all themes with different colors give excellent displays with consistent readability and contrast.

That makes the 22 themes interchangeable without any change to the view and card configuration if you use theme colors of course!

But then again, it raised enough questions about what Material 3 does in some cases.

Read on, if you're interested :smile:

##:material-home-floor-3: But before, that, the basis of Material 3...

<!-- https://bootcamp.uxdesign.cc/perception-based-color-palettes-for-customizable-ui-themes-33f596faf23d -->

With Material 3 for Android 12 a new color system, called [HCT (hue, chroma (= colorfulness), tone)][m3-hct-source-url] is introduced. A color system built using CAM16 hue and chroma, and L\* from CIE-Lab.

The lightness in CIE-Lab is in line with human perception. If L\* is 0, the value corresponds to black and 100 to white, allowing for very accurate color tones. Using L\* creates a link between the color system, the contrast, and thus the accessibility. The contrast difference between background and foreground is one of the most important factors in the [WCAG guidelines][wcag-guidelines-url].

Where the contrast ratio is non-linear, CIE-L\* is. It means that HCT can use differences to guarantee the contrast ratio. A difference of 40 in HCT tone guarantees a contrast ratio >= 3.0, and a difference of 50 guarantees a contrast ratio >= 4.5.

Below you see two examples as to why CAM16 is such a great system regarding colors linearity and distribution:

![colorio-hue-linearity-ebner-fairchild-png]

CAM16 shows the best color circles and chroma lines:

![colorio-munsell-lightness-png]

And the reason for Google to use CIELab as the method to calculate lightness:

![colorio-lightness-png]

!!! Success "The mix from CIELab and CAM16 seems to be a great choice for the new Material guidelines"
    It uses the best from CIELab - Lightness, and the best from CAM16 - Hue and Chroma!
    
(screenshots taken from [Colorio README][colorio-readme-url])

<!--- References to pictures... --->

[colorio-hue-linearity-ebner-fairchild-png]: ../assets/screenshots/colorio-hue-linearity-ebner-fairchild.png
[colorio-munsell-lightness-png]: ../assets/screenshots/colorio-munsell-lightness.png
[colorio-lightness-png]: ../assets/screenshots/colorio-lightness.png

<!--- External links... --->

[m3-hct-source-url]: https://github.com/material-foundation/material-color-utilities/blob/main/typescript/hct/hct.ts
[wcag-guidelines-url]: https://www.w3.org/WAI/standards-guidelines/wcag/
[colorio-readme-url]: https://github.com/nschloe/colorio/blob/main/README.md