---
template: overrides/main.html
---
The installation can be done in two ways:

- Install using HACS
- Manual install

## Installation via HACS
Go to the HACS panel in your Home Assistant installation, choose frontend / themes, and search for the Material 3 themes, and install the one you want.

## Manual Installation
Get the Material 3 theme yaml file from the `themes` folder in Github and put it into your Home Assistant `themes` folder.

If you have the following in your `configuration.yaml`:
```yaml
frontend:
  themes: !include_dir_merge_named themes/
```

The theme will be available automatically once you reload the themes with the Home Assistant 'Developer Tools' > 'Services' > 'frontend.reload_themes' service.

Or just restart Home Assistant!
