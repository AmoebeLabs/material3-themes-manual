---
template: overrides/main.html
---
<!-- GT/GML -->

##:material-home-floor-3: M3 and HA
As mentioned, Home Assistant has no idea that a Material 3 theme is being used.

HAM3 integrates the Material 3 color definitions with the Home Assistant themes by mapping the Material 2 and Home Assistant CSS definitions to the Material 3 definitions.

Cards are not limited to the Material 2 color system and can take full advantage of the possibilities offered by material 3. Of course, these cards must have the possibility to be styled by the user.


##:material-home-floor-3: Translating Material 3 color concepts...

HAM3 makes explicit use of some great design considerations of the Material 3 color system.

The main aspects are described below.

| **Dynamic color**| | |
| ---- | ---- | ---- |
| Material 3 | | M3 Themes for HA |
| The color system in M3 enables user preferences and needs to interact with an app’s colors. <br><br>Dynamic color specifically describes the convergence of user settings with the system UI and in-app color experiences | ![dynamic color]One of the nicest things is that dynamic color allows the user to use an image as the basis for a theme. Material 3 generates a compatible theme from this. |
| **Design tokens & tool** ||
| Material 3 | | M3 Themes for HA |
| Design tokens enable flexibility and consistency across a product by allowing designers to assign an element's color role in a UI, rather than a set value.<br><br>Tokens act as a bridge between an element's assigned role and the chosen color value for a role. With the addition of tokens, designing for relationships of elements is more fundamental than selecting specific colors | ![tokens]( https://lh3.googleusercontent.com/6AeOFxLCf_u2S5X9xTe7BjB7f7-b8FN4ypCMoJKBO7eUTHjSkXqc0F1kykSBYwze9Rdn9-dggVszNj68iyciGH6z9qLXZbYF5gsDXUCncOfA=s0)|HAM3 uses the Design tokens to generate the CSS color variables for the HA theme.<br><br>As long as you use these CSS color variables in your cards, colors will follow the theme colors and behave as expected when switching between dark and light modes.<br><br>HAM3 also maps the M3 colors to the existing M2 color names that Home Assistant uses to render the M3 theme by HA |
| **Accessibility** ||
| Material 3 | | Home Assistant |
| Dynamic color is designed to meet accessibility standards for color contrast. The system of tonal palettes is central to making any color scheme accessible by default. <br><br>Combining color based on tonality, rather than hex value or hue, is one of the key systems that make any color output accessible. Products using dynamic color will meet requirements because the algorithmic combinations that an end-user can experience are designed to meet accessibility standards. | ![access]( https://lh3.googleusercontent.com/aF8CvgyX659D64Wim3zFsTgd63wXh1HBQ_XTyaMX6lARG7VEDkH-0KhmQmPgBOpqOwS6RMQZHRXUQ8qZITmaI4hF7vfexRA7kZhAAE61nd1Mxg=s0)|Meeting accessibility standards for color contrast is one of the best features of Material 3. It allows HAM3 to create interchangeable dark and light themes without worrying about readability.
No more fiddling with the views/cards! <br><br>Because of this, every M3 example theme I created works with HA! It saves a lot of time when designing a theme. |


##:material-home-floor-3: ...and extending the possibilities

In addition to trying to be 100% compatible, HAM3 extends and adapts the color definitions with more palettes, more surfaces, and more color steps. HAM3 also maps reference colors to the dark and light themes without requiring changes to the M3-compatible stylized cards.

- Apparent compatibility between M3 themes by mapping dark and light colors
- Maintain readability between dark and light modes


Of course, your cards must use CSS theme variables and not fixed colors names or hex codes to get compatible light and dark color modes!

