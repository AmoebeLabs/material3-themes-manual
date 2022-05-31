---
template: main.html
title: Theme Installation
description: Installation of any Home Assistant Material 3 theme can be done either using HACS or a manual install. Both are easy and put the theme in the same folder.
tags:
  - Installation
  - Theme
---
The installation can be done in two ways:

- Install using HACS
- Manual install

##:material-home-floor-3: Installation via HACS
Go to the HACS panel in your Home Assistant installation, choose frontend / themes, and search for the Material 3 themes, and install the one you want.

##:material-home-floor-3: Manual Installation
Get the Material 3 theme yaml file from the `themes` folder in Github and put it into your Home Assistant `themes` folder.

If you have the following in your `configuration.yaml`:
```yaml
frontend:
  themes: !include_dir_merge_named themes/
```

The theme will be available automatically once you reload the themes with the Home Assistant 'Developer Tools' > 'Services' > 'frontend.reload_themes' service.

Or just restart Home Assistant!

##:material-home-floor-3: How to use these themes to style your (custom) cards

Once installed, learn how to use the full functionality of the Material 3 themes in your cards [here][How to use Material 3 themes].

For one of the 22 available example themes, check [this page][Material 3 example themes].

<!--- Internal References... -->
[How to use Material 3 themes]: ../../using/using-ham3-in-cards/
[Material 3 example themes]: ../../examples/introduction/
