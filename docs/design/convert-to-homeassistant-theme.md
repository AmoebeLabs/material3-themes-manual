---
template: main.html
title: Convert M3 theme to Home Assistant
description: Import the Figma export, and use the Swiss Army Knife to convert the Figma export to a Material 3 theme for Home Assistant.
status: new
tags:
  - Theme Design
  - Figma
  - Swiss Army Knife
---

!!! Warning "This conversion is based on the new JSON format"
    The old DSP format is not supported anymore by the Material Theme Builder as an export option!

    
##:material-home-floor-3: Introduction
As I don't create a theme every day, the conversion is a bit primitive, but it works for me!

Using this method, I was able to create & convert about 7 themes per hour. Normally I need several hours to create a theme.

##:material-home-floor-3: The short version of the how-to
The conversion uses the following steps, which are explained more visually further on:

**Step 1:**

- Get the Python conversion script `json2theme.py` from [Github][json2theme-script].

**Step 2:**

- Run the script `Python json2theme.py material-theme.json output.txt`

**Step 3:**

- Copy the translated theme definitions in the `output.txt` file into the new theme and save.

**Step 4:**

- Reload Home Assistant themes 
- And now you can select the newly created theme. The `sake99` view should now display your new theme!

##:material-home-floor-3: The long version of the how-to

###:material-home-floor-3: Step 1: Get the Python conversion script `json2theme.py` from [Github][json2theme-script].

You can open that file with any editor. It contains the theme definitions in json format.

```JSON title="material-theme.json excerpt"
{
    "description": "TYPE: CUSTOM\nMaterial Theme Builder export 2025-01-03 04:51:47",
    "seed": "#93DDFF",
    "coreColors": {
        "primary": "#93DDFF",
        "secondary": "#84939B",
        "tertiary": "#908EAA",
        "error": "#FF5449",
        "neutral": "#909192",
        "neutralVariant": "#8C9195"
    },
    "extendedColors": [],
    "schemes": {
        "light": {

    ...

          },
        "neutral-variant": {
            "0": "#000000",
            "5": "#111111",
            "10": "#1B1B1C",
            "15": "#262626",
            "20": "#303031",
            "25": "#3C3B3B",
            "30": "#474747",
            "35": "#535252",
            "40": "#5F5E5E",
            "50": "#787777",
            "60": "#929090",
            "70": "#ADABAB",
            "80": "#C8C6C6",
            "90": "#E5E2E2",
            "95": "#F3F0F0",
            "98": "#FCF9F8",
            "99": "#FFFBFB",
            "100": "#FFFFFF"
        }
    }
}
    
```
###:material-home-floor-3: Step 2: Use the Python script to convert the json file

```console
Python json2theme.py material-theme.json output.txt
```

###:material-home-floor-3: Step 4: Copy the output.txt into the new theme

Open both your theme and the `output.txt` file and copy and paste the contents of the `output.txt` file into a Material 3 theme template file between the START and END markers.

!!! Warning "Make sure that you've got your indentation right with 2 spaces!"

```YAML
#
# Theme     : m3-07-darkolivegreen.yaml
# Project   : Home Assistant
# Repository: https://github.com/AmoebeLabs/HA-Theme_M3-07-DarkOliveGreen
#
# Author    : Mars @ AmoebeLabs.com
# 
# License   : CC BY-SA, https://creativecommons.org/licenses/by/4.0/
#
# -----
# Description:
#   Dark / Light theme based on Material 3 for Home Assistant.
#
# According to: https://encycolorpedia.com/526600
#   - Dark Olive Green
#   
###############################################################################
#
M3-07-DarkOliveGreen:
  # Colors generated via Material Design 3 (Material You) JSON export
  # of figma Material Theme Builder and converted by json2theme.py script.
  #
  # --------------------------------------------------------------------------
  # ==================== START of M3 copy/paste configuration ================
  # --------------------------------------------------------------------------
  
  theme-ref-elevation-surface-neutral1-light: rgb(249,247,239)
  theme-ref-elevation-surface-neutral2-light: rgb(246,244,236)
  theme-ref-elevation-surface-neutral3-light: rgb(241,239,232)
  theme-ref-elevation-surface-neutral4-light: rgb(237,235,227)
  theme-ref-elevation-surface-neutral5-light: rgb(230,228,221)
  theme-ref-elevation-surface-neutral6-light: rgb(224,222,215)
  theme-ref-elevation-surface-neutral7-light: rgb(216,214,207)
  theme-ref-elevation-surface-neutral8-light: rgb(208,206,199)
  theme-ref-elevation-surface-neutral9-light: rgb(198,197,190)
  theme-ref-elevation-surface-neutral10-light: rgb(190,189,182)
  
  ...
  
  # --------------------------------------------------------------------------
  # ==================== END of M3 copy/paste configuration ==================
  # --------------------------------------------------------------------------
```

###:material-home-floor-3: Step 5: Reload themes and enjoy!
Now reload the Home Assistant themes with the Developer Tools' > 'Services' > 'frontend.reload_themes' service.

Then select your just created theme and start using it.

You can validate the theme using the `sake99` view, as it displays the active Material 3 theme.

![SAK Material 3 converter Theme Card Light]
![SAK Material 3 converter Theme Card Dark]

<!-- Image references -->

[SAK Material 3 converter Theme Card Light]: ../assets/screenshots/sak-view99-theme-card-light.png#only-light
[SAK Material 3 converter Theme Card Dark]: ../assets/screenshots/sak-view99-theme-card-dark.png#only-dark

[SAK Material 3 converter Chrome Console Output]: ../assets/screenshots/sak-view99-console-output.png

<!-- Internal References -->
[Create Material 3 Theme]: create-material3-theme.md
[Convert to Home Assistant Theme]: convert-to-homeassistant-theme.md

<!-- External References -->
[figma-url]: https://www.figma.com/
[json2theme-script]: https://github.com/AmoebeLabs/material3-themes-manual/tree/master/src
