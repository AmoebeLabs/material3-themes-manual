---
template: overrides/main.html
---

##:material-home-floor-3: Home Assistant Theme Structure

Every Home Assistant Theme follows the same structure:

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

```yaml linenums="1" hl_lines="1 19"
  Theme Name:
    #
    # M3 Theme generated definitions
    #
    # This is the ONLY part of the theme that is changed
    # The rest of the theme definition is GENERIC!!!!!!!
    #
    theme-ref-palette-* light and dark definitions
    theme-ref-elevation-* light and dark definitions

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

    #
    # Generic CSS Material 2 / Home Assistant definitions using
    # definitions from the light or dark mode colors
    #
    primary-color: var(--theme-sys-color-primary)
    ...
```

##:material-home-floor-3: HA M3 Theme Template
As the HA M3 Theme structure is mainly mapping M3 reference colors to system (light/dark independent) colors and existing Home Assistant theme settings, it is very easy to use an M3 theme template and only add the generated M3 reference color definitions to create a whole new theme.

The use of a generic theme part where you only have to insert the M3 reference colors has proven to be very effective: The 7 theme examples where created within one hour and used a picture to generate the M3 color definition.

!!! Warning "To keep compatibility between HA M3 themes, it is strongly advised NOT to change generic theme parts!"
