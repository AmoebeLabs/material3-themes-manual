---
template: main.html
title: Home Assistant Material 3 implementation
description: The Material 3 implementation for Home Assistant themes are 100% compatible. It further extends the M3 color system to make it more usable in views/cards. 
tags:
  - M3
  - Material 3
  - Themes
  - Implementation
---

<!-- GT/GML -->

HAM3 series themes are usually 100% Material 3 compatible. In addition, it extends the Material 3 color system to make it more usable in views/cards. 

!!! Note "The main driver (for me) is the Swiss Army Knife custom card, which allows for extensive styling and can therefore use all the M3 color system features and extensions"

Below is an overview of the features and extensions that HAM3 provides for Home Assistant themes.

##:material-home-floor-3: The Material 3 for Home Assistant implementation

| What | Material 3 | HAM3 implementation |
| ---- | ---------- |  ------------------- |
| Palettes | 13 colors per palette | 100% M3 compliant for these 13 colors. <br>Extended with 11 more colors, giving a total of 24 colors per palette showing more usable gradient colors with 12 shades and 12 tints |
| Surfaces | 2 surfaces, neutral and primary based for light and dark themes with 5 elevation levels | 5 surfaces, neutral, primary, secondary, tertiary and error with 10 elevation levels giving more flexibility and choice |
| Reference | Reference colors are uniquely defined for both dark and light mode palettes | 100% M3 compliant. <br>Extended for surfaces |
| System | Light and Dark theme system colors mapping reference colors to the theme mode | 100% M3 compliant. <br>Extended for surfaces and palette colors. The system palette colors are reversed for the Dark mode to maintain color contrast standards |
| Light Theme | Yes | 100% M3 compliant | 
| Dark Theme | Yes | 100% M3 compliant | 

##:material-home-floor-3: The resulting theme colors

The resulting theme colors are shown below. The theme is rendered using several [Swiss Army Knife][sak-docs-url] custom cards and templates. The example uses the dynamic [`Material 3 D07, DarkOliveGreen`][example-d7-md] theme. This theme is generated from the AmoebeLabs logo :smile:

[![Home Assistant Material 3 Theme Palette]][Home Assistant Material 3 Theme Palette]
_Primary, secondary, tertiary and error pallettes ranging from white (100) to black (0)_


<br>[![Home Assistant Material 3 Theme Surface]][Home Assistant Material 3 Theme Surface]
_The 5 light and dark surfaces with 10 elevation levels each_


<br>[![Home Assistant Material 3 Theme Light]][Home Assistant Material 3 Theme Light]
_The resulting light theme color selection_

<br>[![Home Assistant Material 3 Theme Dark]][Home Assistant Material 3 Theme Dark]
_The resulting dark theme color selection_


##:material-home-floor-3: Examples
The dark and light examples show the [Swiss Army Knife][sak-docs-url] [example \#12][sak-docs-example-12-url] using the above theme colors.

You see the following aspects of the theme:

- The 'Primary' Dark Olive Green color in several shade/tints
- The 'Tertiary Container' and 'On Tertiary Container' colors on the first row with the battery and linkquality
- Some 'Neutral' surface colors on the Hall, Bedroom and Poseidon rows
- The background of the segmented arcs (the circles) are also using a 'Neutral' surface elevation color.

All the above colors adapt to the theme mode. The only exception is (barely) visible in the last row: that row uses reference colors that are the same in dark and light mode.

[![Home Assistant Material 3 Theme Example Light]][Home Assistant Material 3 Theme Example Light]
_A light theme example card ([Theme D07 - DarkOliveGreen][example-d7-md])_

<br>[![Home Assistant Material 3 Theme Example Dark]][Home Assistant Material 3 Theme Example Dark]
_A dark theme example card ([Theme D07 - DarkOliveGreen][example-d7-md])_

<!-- Image References -->

[Home Assistant Material 3 Theme Palette]: ../assets/screenshots/m3-theme-d07-palettes.png "Home Assistant Material 3 Theme Palette definition for example D07, Dark Olive Green"
[Home Assistant Material 3 Theme Surface]: ../assets/screenshots/m3-theme-d07-surfaces.png "Home Assistant Material 3 Theme Surface definitionfor example D07, Dark Olive Green"
[Home Assistant Material 3 Theme Light]: ../assets/screenshots/m3-theme-d07-light.png "Home Assistant Material 3 Theme Light definition for example D07, Dark Olive Green"
[Home Assistant Material 3 Theme Dark]: ../assets/screenshots/m3-theme-d07-dark.png "Home Assistant Material 3 Theme Dark definition for example D07, Dark Olive Green"

[Home Assistant Material 3 Theme Example Light]: ../assets/screenshots/m3-example-d07-light.png "Home Assistant Material 3 Theme Light card example for D07, Dark Olive Green"
[Home Assistant Material 3 Theme Example Dark]: ../assets/screenshots/m3-example-d07-dark.png "Home Assistant Material 3 Theme Dark card example for D07, Dark Olive Green"

<!-- Internal References -->
[example-d7-md]: ../examples/material3-example-theme-d07-darkolivegreen.md

<!-- External References -->
[sak-docs-url]: https://swiss-army-knife-card-manual.amoebelabs.com
[sak-docs-example-12-url]: https://swiss-army-knife-card-manual.amoebelabs.com/examples/example-12/
