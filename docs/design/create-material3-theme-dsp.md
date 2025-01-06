---
template: main.html
title: Create the Material 3 Theme
description: Create your own Material 3 theme using the free Figma Material 3 builder using an image or by defining your own primary color. Then export it.
status: depricated
tags:
  - Theme Design
  - Figma
  - Color definitions
---

!!! Warning "The Material Theme Builder does not export DSP files anymore"
    This part of the manual is only there for existing DSP export files.
    
##:material-home-floor-3: Step 1: Open the plugin

Open the Material Theme Builder plugin from the menu

![Figma Open Material Theme Builder plugin]

You will be welcomed with the plugin popup. Click on "Get started"
![Figma Welcome Screen Material Theme Builder plugin]

##:material-home-floor-3: Step 2: Create theme based on image

The builder defaults to the Dynamic mode where you can use an image to create a theme. Remember that only ONE (1) source color will be derived from the image.

<br>In this case, I used another theme to create this dynamic theme...

| Dynamic example ||
|---|---|
|![Figma Material Theme Builder Dynamic Color]|![Figma Material Theme Builder Select Image]|

##:material-home-floor-3: Step 3: Look at the result
The Material Theme Builder will show the result on the background. This may take some time depending on your PC, as this is all done in the browser!

First, the full result:
![Figma Material Theme Builder Result Full]

And from left to right some details, starting with the Tonal Palettes.
![Figma Material Theme Builder Result Palettes]

Then the Light and Dark themes.

![Figma Material Theme Builder Result LightDark]

And finally the surfaces. The typography is NOT used for Home Assistant.

![Figma Material Theme Builder Result Surfaces]

##:material-home-floor-3: Step 4 (Final): Export the DSP file
Once you are ready, go to the "Custom" tab of the Material Theme Builder, and click the "Export" button on the bottom, and select "Export Material Tokes (DSP)", and save the resulting ZIP file on your computer.

![Figma Material Theme Builder Export Theme]


<!-- Image references -->

[mtb-blue-1-png]: ../assets/screenshots/material-theme-builder-blue.png
[mtb-blue-2-png]: ../assets/screenshots/material-theme-builder-blue2.png
[mtb-blue-3-png]: ../assets/screenshots/material-theme-builder-blue3.png

<!-- Internal References -->
[Create Material 3 Theme]: ../create-material3-theme/
[Convert to Home Assistant Theme]: ../convert-to-homeassistant-theme/

<!-- External References -->
[figma-url]: https://www.figma.com/

<!-- Image References -->

[Figma Open Material Theme Builder plugin]: ../assets/screenshots/figma-open-material-theme-builder-plugin.png
[Figma Welcome Screen Material Theme Builder plugin]: ../assets/screenshots/figma-material-theme-builder-plugin-welcome.png
[Figma Material Theme Builder Dynamic Color]: ../assets/screenshots/figma-material-theme-builder-plugin-dynamic.png
[Figma Material Theme Builder Select Image]: ../assets/screenshots/figma-material-theme-builder-plugin-dynamic-c07.png
[Figma Material Theme Builder Export Theme]: ../assets/screenshots/figma-material-theme-builder-plugin-export-dsp.png

[Figma Material Theme Builder Result Full]: ../assets/screenshots/figma-material-theme-builder-plugin-full-result.png
[Figma Material Theme Builder Result Palettes]: ../assets/screenshots/figma-material-theme-builder-plugin-part-palettes.png
[Figma Material Theme Builder Result LightDark]: ../assets/screenshots/figma-material-theme-builder-plugin-part-light-dark.png
[Figma Material Theme Builder Result Surfaces]: ../assets/screenshots/figma-material-theme-builder-plugin-part-surfaces.png

