---
template: overrides/main.html
---
The installation can be done in two ways:

- automatic install using HACS
- manual install

## Installation via HACS
TODO

## Manual Installation
Get the theme yaml file from the `themes` folder in Github and put int into your Home Assistant `themes` folder.

If you have the following in your `configuration.yaml`:
```yaml
frontend:
  themes: !include_dir_merge_named themes/
```

The theme will be automatically available once you have reloaded the themes using the Home Assistant 'Developer Tools' > 'Services' > 'frontend.reload_themes' service.

Or just restart Home Assistant!
