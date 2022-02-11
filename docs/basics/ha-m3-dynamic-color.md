---
template: overrides/main.html
---

User-generated color schemes are an important feature of the M3 color system. The Home Assistant implementation makes full use of all the possibilities and even extends some of the features. To manifest all features in the HA UI, the cards must be compliant and use the M3 color system too.

##:material-home-floor-3: The HA implementation

The M3 series themes for Home Assistant are mostly 100% M3 compliant. On top of that, it extends the M3 color system to make it more usable in views/cards. 

!!! Note "The main driver (for me) is the Swiss Army Knife custom card, which allows for extensive styling and can therefore use all the M3 color system features and extensions"

| What | Material 3 | HA M3 implementation |
| ---- | ---------- |  ------------------- |
| Palettes | 13 colors per palette | 100% M3 compliant for these 13 colors. <br>Extended with 11 more colors, giving a total of 24 colors per palette showing more usable gradient colors with 12 shades and 12 tints |
| Surfaces | 2 surfaces, neutral and primary based for light and dark themes with 5 elevation levels | 5 surfaces, neutral, primary, secondary, tertiary and error with 10 elevation levels giving more flexibility and choice |
| Reference | Reference colors are uniquely defined for both dark and light mode palettes | 100% M3 compliant. <br>Extended for surfaces |
| System | Light and Dark theme system colors mapping reference colors to the theme mode | 100% M3 compliant. <br>Extended for surfaces and palette colors. The system palette colors are reversed for the Dark mode to maintain color contrast standards |
| Light Theme | Yes | 100% M3 compliant | 
| Dark Theme | Yes | 100% M3 compliant | 

##:material-home-floor-3: The resulting theme colors

The resulting theme colors are shown below. The theme is shown using several Swiss Army Knife cards and templates. The example uses the `M3-07-DarkOliveGreen` theme. This theme is generated from the AmoebeLabs logo :smile:

[![M3 Palettes]][M3 Palettes]
_Primary, secondary, tertiary and error pallettes ranging from white (100) to black (0)_


<br>[![M3 Surfaces]][M3 Surfaces]
_The 5 light and dark surfaces with 10 elevation levels each_


<br>[![M3 Light]][M3 Light]
_The resulting light theme color selection_

<br>[![M3 Dark]][M3 Dark]
_The resulting dark theme color selection_

  [M3 Palettes]: ../assets/screenshots/m3-theme-07-palettes.png
  [M3 Surfaces]: ../assets/screenshots/m3-theme-07-surfaces.png
  [M3 Light]: ../assets/screenshots/m3-theme-07-light.png
  [M3 Dark]: ../assets/screenshots/m3-theme-07-dark.png
  

##:material-home-floor-3: Examples
The dark and light examples show the Swiss Army Knife example \#12 using the above theme colors.

You see the following aspects of the theme:

- The 'Primary' Dark Olive Green color in several shade/tints
- The 'Tertiary Container' and 'On Tertiary Container' colors on the first row with the battery and linkquality
- Some 'Neutral' surface colors on the Hall, Bedroom and Poseidon rows
- The background of the segmented arcs (the circles) are also using a 'Neutral' surface elevation color.

All the above colors adapt to the theme mode. The only exception is visible in the last row: in that case reference colors are used, which are the same in dark and light mode.

[![M3 Example Light]][M3 Example Light]
_A light theme example card_

<br>[![M3 Example Dark]][M3 Example Dark]
_A dark theme example card_

  [M3 Example Light]: ../assets/screenshots/m3-example-07-light.png
  [M3 Example Dark]: ../assets/screenshots/m3-example-07-dark.png
