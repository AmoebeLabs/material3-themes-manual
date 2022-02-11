---
template: overrides/main.html
---

##:material-home-floor-3: Use the Theme!
The most important point in using all the features of the HA M3 themes is to _use_ the theme color definitions, and never to use fixed colors!

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