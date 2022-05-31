---
template: main.html
title: Convert M3 theme to Home Assistant
description: Import the Figma export, and use the Swiss Army Knife to convert the Figma export to a Material 3 theme for Home Assistant.
tags:
  - Theme Design
  - Figma
  - Swiss Army Knife
---


##:material-home-floor-3: From zipped file to working theme!

- Export DSP (button is only available from custom tab for some reason...)

###Using SAK to convert the tokens...

- Get the `tokens.json` from `material\theme\data` folder inside the zip file.
- Add to `m3.yaml` and save.
- Select the converter view
- Hit ctrl-F5 to refresh/reload HA. This includes the `m3.yaml` template.
- Check the Chrome console for the output of the converter
- You can see a large block, with a "copy" button as the list is long (thank you Chrome for this!)
- Copy the translated theme definitions into the theme and save.
- Reload HA themes 
- And now you can select the newly created theme!


