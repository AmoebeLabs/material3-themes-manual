---
template: main.html
description: How to use Home Assistant Material 3 themes in your views and cards. Start by using the standard light and dark theme definitions, and extend this with specific colors.
---
\#TODO

##:material-home-floor-3: Use the Theme!
The most important point in using all the features of the HAM3 themes is to _use_ the theme color definitions, and never to use fixed colors!

=== "Do"
    ```yaml
      style:
        fill: var(--primary-text-color)           # Material text color
        stroke: var(--theme-sys-color-primary60)  # M3 theme system color
    ```

=== "Do'nt"
    ```yaml
      style:
        fill: red                                 # Hard coded red color
        stroke: #456712                           # Hard coded hex color
    ```
It can't get any easier :smile:


##:material-home-floor-3: Using material colors
Primary and secondary colors

##:material-home-floor-3: Using dedicated colors

Traffic light.


##:material-home-floor-3: Using M3 colors
The M3 primary, secondary, tertiary and error reference and system color palettes and surface elevation colors.

###:material-home-floor-3: Reference colors


###:material-home-floor-3: System colors
