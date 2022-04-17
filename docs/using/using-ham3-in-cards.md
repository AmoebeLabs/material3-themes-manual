---
template: main.html
description: How to use Home Assistant Material 3 themes in your views and cards. Start by using the standard light and dark theme definitions, and extend this with specific colors.
---
#Using Home Assistant Material 3 themes

##:material-home-floor-3: Use the Theme!
The most important point in using all the features of the HAM3 themes is to _use_ the theme color definitions where possible and applicable. In this case, your card will follow the theme in both light and dark mode!

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

I will use [teal blue example theme d06][example-d06-md] to show how you can use a Material 3 theme. The card shown is [example 12 from the Swiss Army Knife custom card][swiss-army-knife-documentation-example-12-url].

![AmoebeLabs Material 3 Theme Example D06 Light]
_The light variant._

<br>![AmoebeLabs Material 3 Theme Example D06 Dark]
_The dark variant._

##:material-home-floor-3: Using standard material colors
The Material 3 themes map the color definitions to the standard material color definitions Home Assistant is using.
This means you can use the Primary and secondary font and background colors as before to style your cards.

If fonts use the `var(--primary-text-color)` css variable, both light and dark themes should work out of the box!

!!! Info "The above example uses these default font and background colors for the cards background and text parts."

##:material-home-floor-3: Using dedicated colors
In some cases you can't use the Theme colors, you need to use dedicated colors. Traffic light colors or the Airvisual colors are a good example of that use case.

You have 3 options to use dedicated colors in your cards:

- Use hard coded colors (hex, rgb, hsl, etc.)
- Clone the theme you want to use, and define the colors in the theme, and use those custom color names in your cards.
  <br><br>Say you define them as
  ```yaml
  traffic-light-red: red
  traffic-light-yellow: yellow
  traffic-light-green: green
  ```
  You can use the colors in the card using the css variable `var(--traffic-light-red)`
- If the card is made with the [Swiss Army Knife custom card][swiss-army-knife-documentation-url], you can define those colors in the user css definitions, and use them in your card as css variables. 

!!! Info "The above example uses dedicated colors (green, yellow, orange, red, purple) for the AirVisual representation in the first wide card."


##:material-home-floor-3: Using Material 3 colors
The Material 3 themes define more colors: primary, secondary, tertiary and error reference and system color palettes and surface elevation colors.

All these colors can be used as css variables.

All Material 3 themes support light and dark mode. It does this by redefining the `system` colors with theme mode dependant `reference` colors.

!!! Note "If you use Material 3 color names in your cards, non Material 3 themes will show fallback colors (mostly black and white)"

###:material-home-floor-3: System colors
The Material 3 `system` colors are dependent of the theme mode (light or dark). Use this colors if you want to adapt the color to the theme mode.

| **Light variant** | **Dark variant**|
| ------------ | ---------------- |
| **[Example d06, Teal Blue Light][example-d06-md]:** [![AmoebeLabs Material 3 Theme Example D06 Light]][example-d06-md] | **[Example d06, Teal Blue Dark][example-d06-md]:** [![AmoebeLabs Material 3 Theme Example D06 Dark]][example-d06-md] |

System colors are used throughout this example:

- The background of the circles use a `surface` `system` color: this color is darker than the background in a light theme, and lighter than the background in a dark theme.
<br><br>This surface color is also used in the half circle in the 'Hall' card, the circle around the icon in the 'Bedroom' card and the background of the first part of the "Poseidon" card.
- The same is done for the actual value of the circles: these use the `primary` dark variants in the light theme, and the light variants in the dark theme.
- The circles for battery and linkquality use `tertiary` `system` colors.


Check the [Theme colors page][ha-m3-theme-colors-url] for these `system` colors you can use.


###:material-home-floor-3: Reference colors
The Material 3 `reference` colors are independent of the theme mode (light or dark). Use this colors if you want to keep the same color.

| **Light variant** | **Dark variant**|
| ------------ | ---------------- |
| **[Example d06, Teal Blue Light][example-d06-md]:** [![AmoebeLabs Material 3 Theme Example D06 Light]][example-d06-md] | **[Example d06, Teal Blue Dark][example-d06-md]:** [![AmoebeLabs Material 3 Theme Example D06 Dark]][example-d06-md] |

Reference colors are used only in the last card (hardly visible in the lower right of the image):

- The segments of the circles use `primary` reference colors: you can see they remain the same for both the light and dark mode.

Check the [Theme colors page][ha-m3-theme-colors-url] for these 264 `reference` colors you can use.


<!--- References to external sites... -->

[swiss-army-knife-documentation-url]: https://swiss-army-knife.docs.amoebelabs.com/
[swiss-army-knife-documentation-example-12-url]: https://swiss-army-knife.docs.amoebelabs.com/examples/example-12/

<!--- Internal References... -->
[ha-m3-theme-colors-url]: ../../basics/ha-m3-theme-colors/
[example-d06-md]: ../examples/example-theme-d06-tealblue.md

<!--- References to pictures... -->

[AmoebeLabs Material 3 Theme Example D06 Light]: ../assets/screenshots/m3-example-d06-light.png
[AmoebeLabs Material 3 Theme Example D06 Dark]: ../assets/screenshots/m3-example-d06-dark.png