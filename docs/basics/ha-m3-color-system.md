---
template: overrides/main.html
---

The Material 3 color system contains a few important new features. All these features are described on the [m3 website.](https://m3.material.io/styles/color/overview)

The most important aspects are described below.

##:material-home-floor-3: Material 3 color design aspects...

| **Dynamic color**| .|
| ---- | ---- |
| The color system in M3 enables user preferences and needs to interact with an app’s colors. <br><br>Dynamic color specifically describes the convergence of user settings with the system UI and in-app color experiences | ![dynamic color](https://lh3.googleusercontent.com/NGUL0eR9CX4ztNMVnfEoDODDlNqWKc0SzdKBIyzVNmPwmqwSRJj0gXXiM8f0TwUfnmWZiVreM9Vy-p_r8ThO2ThXVH1DJr_5s6L1V1J3pEnA=s0) |
| **Design tokens & tool** ||
| Design tokens enable flexibility and consistency across a product by allowing designers to assign an element's color role in a UI, rather than a set value.<br><br>Tokens act as a bridge between an element's assigned role and the chosen color value for a role. With the addition of tokens, designing for relationships of elements is more fundamental than selecting specific colors | ![tokens]( https://lh3.googleusercontent.com/6AeOFxLCf_u2S5X9xTe7BjB7f7-b8FN4ypCMoJKBO7eUTHjSkXqc0F1kykSBYwze9Rdn9-dggVszNj68iyciGH6z9qLXZbYF5gsDXUCncOfA=s0)|
| **Accessibility** ||
| Dynamic color is designed to meet accessibility standards for color contrast. The system of tonal palettes is central to making any color scheme accessible by default. <br><br>Combining color based on tonality, rather than hex value or hue, is one of the key systems that make any color output accessible. Products using dynamic color will meet requirements because the algorithmic combinations that an end-user can experience are designed to meet accessibility standards. | ![access]( https://lh3.googleusercontent.com/aF8CvgyX659D64Wim3zFsTgd63wXh1HBQ_XTyaMX6lARG7VEDkH-0KhmQmPgBOpqOwS6RMQZHRXUQ8qZITmaI4hF7vfexRA7kZhAAE61nd1Mxg=s0)|

##:material-home-floor-3: ...and its use in HA


| <div style="min-width:125px">**Dynamic color**</div>| <div style="width:170px">.</div>|
| ---- | ----- |
| One of the nicest things is that dynamic color allows the user to use a photo or background as the basis for a Theme: M3 generates a compatible theme out of this. So just (as we see later) upload a photo, and a theme is created! | ![dynamic color](https://lh3.googleusercontent.com/NGUL0eR9CX4ztNMVnfEoDODDlNqWKc0SzdKBIyzVNmPwmqwSRJj0gXXiM8f0TwUfnmWZiVreM9Vy-p_r8ThO2ThXVH1DJr_5s6L1V1J3pEnA=s0) |
| **Design tokens & tool** ||
| The Design tokens are used to generate the CSS color variables for the HA theme.<br><br>As long as you use these CSS color variables in your cards, colors follow the Theme colors and behave as expected when switching between dark and light mode.<br><br>The M3 colors are mapped to the existing M2 color names that Home Assistant is using in order to have the M3 theme displayed by HA | ![tokens]( https://lh3.googleusercontent.com/6AeOFxLCf_u2S5X9xTe7BjB7f7-b8FN4ypCMoJKBO7eUTHjSkXqc0F1kykSBYwze9Rdn9-dggVszNj68iyciGH6z9qLXZbYF5gsDXUCncOfA=s0)|
| **Accessibility** ||
| The fact that dynamic color is designed to meet accessibility standards for color contrast is a very nice feature. This means that even when you switch to another theme, or switch between dark and light mode, everything is still readable. No more fiddling with this in the views/cards! <br><br>Because of this, so far any M3 theme will work with HA! This saves a lot of time designing a theme. | ![access]( https://lh3.googleusercontent.com/aF8CvgyX659D64Wim3zFsTgd63wXh1HBQ_XTyaMX6lARG7VEDkH-0KhmQmPgBOpqOwS6RMQZHRXUQ8qZITmaI4hF7vfexRA7kZhAAE61nd1Mxg=s0)|