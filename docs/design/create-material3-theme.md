---
template: main.html
title: Create the Material 3 Theme
description: Create your own Material 3 theme using the free Figma Material 3 builder using an image or by defining your own primary color. Then export it.
tags:
  - Theme Design
  - Figma
  - Color definitions
---

!!! Warning "The Material Theme Builder does not export DSP files anymore"
    Therefore, the export/import as described here does **NOT** work anymore!

    As an added bonus, the `tokens.json` file is incompatible with the new `.json` export~~

    I'm investigating if the new format can be converted to the old format, and thus into an M3 theme for Home Assistant.
    
##:material-home-floor-3: Step 1: Open the plugin

Open the Material Theme Builder plugin from the menu

![Figma Open Material Theme Builder plugin]

You will be welcomed with the plugin popup. Click on "Get started"
![Figma Welcome Screen Material Theme Builder plugin Light]
![Figma Welcome Screen Material Theme Builder plugin Dark]

##:material-home-floor-3: Step 2: Option A: Create theme based on image

The builder defaults to the Source image mode where you can use an image to create a theme. Remember that only ONE (1) source color will be derived from the image.

<br>In this case, I used another theme to create this source image theme...

| Source image example ||
|---|---|
|![Figma Material Theme Builder Source Image Dark]|![Figma Material Theme Builder Select Image Dark]|
|![Figma Material Theme Builder Source Image LIght]|![Figma Material Theme Builder Select Image Light]|


!!! Info "Click on the Update button to let the builder build the theme"

##:material-home-floor-3: Step 2: Option B: Create theme based on source color

Another way to make a thme is to pick a source color. You can either pick the exact color yourself, or get a random color from the builder.

| Source color example ||
|---|---|
|![Figma Material Theme Builder Source Color HCT Color Picker Dark]|![Figma Material Theme Builder Source Color Random Dark]|
|![Figma Material Theme Builder Source Color HCT Color Picker Light]|![Figma Material Theme Builder Source Color Random Light]|

!!! Info "Click on the Update button to let the builder build the theme"

##:material-home-floor-3: Step 3: Look at the result

!!! Warning "The new way to show the theme is to use the M3 Design Kit"
    However that one is broken. I still use the old theme overview as you can see.

The Material Theme Builder will show the result on the background. This may take some time depending on your PC, as this is all done in the browser!

First, the full result:
![Figma Material Theme Builder Result Full]

And from left to right some details, starting with the Tonal Palettes.
![Figma Material Theme Builder Result Palettes]

Then the Light and Dark themes.

![Figma Material Theme Builder Result LightDark]

And finally the surfaces. The typography is NOT used for Home Assistant.

![Figma Material Theme Builder Result Surfaces]

##:material-home-floor-3: Step 4 (Final): Export the JSON file
Once you are ready, click the "Export" button on the bottom, and select "Material Theme (JSON)", and save the resulting `.json` file on your computer.

![Figma Material Theme Builder Export Theme Light]
![Figma Material Theme Builder Export Theme Dark]

Now go to the next page to convert the `.json` file to something that Home Assistant can use as a theme!

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

[Figma Welcome Screen Material Theme Builder plugin Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-welcome-light.png#only-light
[Figma Welcome Screen Material Theme Builder plugin Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-welcome-dark.png#only-dark

[Figma Material Theme Builder Source Image Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-image-dark.png#only-light
[Figma Material Theme Builder Source Image Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-image-dark.png#only-dark

[Figma Material Theme Builder Select Image Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-select-image-light.png#only-light
[Figma Material Theme Builder Select Image Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-select-image-dark.png#only-dark

[Figma Material Theme Builder Export Theme Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-export-json-small-light.png#only-light
[Figma Material Theme Builder Export Theme Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-export-json-small-dark.png#only-dark


[Figma Material Theme Builder Source Color HCT Color Picker Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-color-hct-color-picker-light.png#only-light
[Figma Material Theme Builder Source Color HCT Color Picker Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-color-hct-color-picker-dark.png#only-dark

[Figma Material Theme Builder Source Color Random Light]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-color-random-light.png#only-light
[Figma Material Theme Builder Source Color Random Dark]: ../assets/screenshots/figma-material-theme-builder2-plugin-source-color-random-dark.png#only-dark

[Figma Material Theme Builder Result Full]: ../assets/screenshots/figma-material-theme-builder-plugin-full-result.png
[Figma Material Theme Builder Result Palettes]: ../assets/screenshots/figma-material-theme-builder-plugin-part-palettes.png
[Figma Material Theme Builder Result LightDark]: ../assets/screenshots/figma-material-theme-builder-plugin-part-light-dark.png
[Figma Material Theme Builder Result Surfaces]: ../assets/screenshots/figma-material-theme-builder-plugin-part-surfaces.png

