---
template: overrides/main.html
---

##:material-home-floor-3: Home Assistant Theme Structure

Each Home Assistant dark/light theme follows the same structure. It has definitions for both dark and light mode, and a specific section to define colors specific to dark or light mode:

```yaml linenums="1" hl_lines="1 11"
  Theme Name:
    #
    # Generic definitions
    #
    css-var-1: #123456
    css-var-2: var(--css-var-1)

    #
    # Light and Dark specific definitions
    #
    modes:
      light:
        css-text-color: black
      dark:
        css-text-color: white
```

##:material-home-floor-3: HA M3 Theme Structure
The HA M3 theme structure is no different, it has to comply with the HA structure.

An M3 theme is divided into 3 blocks:

```yaml title="Block 1 - Copy/paste Material 3 Theme generated definitions" linenums="1" hl_lines="1 19"
  Theme Name:
    #
    # M3 Theme generated definitions
    #
    # This is the ONLY part of the theme that is changed
    # The rest of the theme definition is GENERIC!!!!!!!
    #
    theme-ref-palette-* light and dark definitions
    theme-ref-elevation-* light and dark definitions

    ...
```
_Block with the M3 Theme definitions_

```yaml title="Block 2 - Generic Dark/Light mappings of the reference colors using Material 3 guidelines" linenums="1" hl_lines="1 19"
    #
    # Light and Dark specific definitions
    # Derived from theme-ref-palette-* definitions
    #
    # NOT to be changed on a per theme basis.
    # The Light and Dark modes map a M3 reference color
    # to a M3 system color!
    #
    modes:
      light:
        theme-sys-color-* light theme definitions
        theme-sys-palette-* light theme definitions
        theme-sys-elevation-* light theme definitions

        theme-* definitions for use with Material 2 / HA
      dark:
        theme-sys-color-* dark theme definitions
        theme-sys-palette-* dark theme definitions
        theme-sys-elevation-* dark theme definitions

        theme-* definitions for use with Material 2 / HA
    ...
```
_Block with the Dark/Light mode mappings, including dark mode modifications for some HA colors_

```yaml title="Block 3 - Mapping of Material 2 and Home Assistant CSS variables" linenums="1" hl_lines="1 19"
    #
    # Generic CSS Material 2 / Home Assistant definitions using
    # definitions from the light or dark mode colors
    #
    primary-color: var(--theme-sys-color-primary)
    <etcetera>
    ...
```
_Block with the Material 2 and Home Assistant color mappings._

##:material-home-floor-3: HA M3 Theme Template

:material-github: [Github repository][ha-m3-template-url]

Since the HA M3 theme mainly maps M3 reference colors to system colors (light/dark independent) and existing Home Assistant theme settings, it is very easy to use an M3 theme template and add only the generated M3 reference color definitions on an entirely new theme.

Using a generic theme section where you only need to enter the M3 reference colors has proven to be very effective: the 7 theme examples were created within an hour and used an image from my own picture library to generate the M3 color definition.

The following parts should be changed and filled in by you:

- the `hacs.json` file if you want to publish your theme on HACS
- the `.github` actions if you want to publish your theme on HACS (just rename the hacs-action file to `.yml`
- the READme
- the main one: the `themes/m3-xx-yyyy.yaml` file. It should be renamed of course, and the generated m3 reference definitions should be inserted (see comments in that file where that should be done)

!!! Warning "To keep compatibility between HA M3 themes, it is strongly advised NOT to change generic theme parts!"



[ha-m3-template-url]: https://github.com/AmoebeLabs/HA-Theme_M3-Template