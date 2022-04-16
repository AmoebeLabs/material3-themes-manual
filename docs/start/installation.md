---
template: main.html
description: Installation of any Home Assistant Material 3 theme can be done either using HACS or a manual install. Both are easy and put the theme in the same folder.
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
