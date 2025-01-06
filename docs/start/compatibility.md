---
template: main.html
description: Any Home Assistant Material 3 theme should be 100% compatible with Home Assistant itself and its built-in cards. HAM3 maps all definitions to existing HA color definitions.
---
<!-- GT/GMY -->
#A word on compatibility

##:material-home-floor-3: In general, compatibility should be 100%

!!! Success "Material 3 is 100% compatible with Home Assistant themes"

Home Assistant has _no_ idea that a Material 3 theme is used!

HAM3 integrates Material 3 color definitions with the Home Assistant theme definitions by mapping the Material 2 and Home Assistant CSS definitions to the Material 3 definitions.

##:material-home-floor-3: Home Assistant's main UI and built-in cards

!!! Success "Material 3 supports Light and Dark mode out-of-the-box"

Since the introduction of light and dark theme modes, the Home Assistant UI takes full advantage of the theme definitions. Therefore, and because of the mapping of Material 3 definitions to Material 2 definitions, a HAM3-based theme should integrate seamlessly with the Home Assistant user interface, but with all the capabilities that HAM3 offers:

- Seemless compatibility between HAM3 themes
- Keeping readability between dark and light modes
- The ability to create a theme from your favorite image

As with the main UI, the built-in cards should integrate seamlessly with any HAM3 Theme.

!!! Question "I did not test ALL the built-in cards, so there might still be some bugs present!"

##:material-home-floor-3: Custom Cards

###:material-home-floor-3: Theme mode compatible custom cards

If the custom card is already fully compatible with dark and light theme modes, then, as with Home Assistant itself and the built-in cards, I wouldn't expect any problems with the HAM3 themes, unless the custom card requires its own dedicated theme.

###:material-home-floor-3: Any other case...

If the custom card is not compatible with light and dark modes, it highly depends on what the custom card is using:

- Its own CSS variables that you should adapt to light and dark modes
- Fixed colors that won't adapt to light and dark modes

The last case is a difficult one, and can only be changed by the developer of the custom card. But if the card is using its own CSS variables, you can define a light and dark variant in the M3 theme.

###:material-home-floor-3: Note on custom card styling

If you use a custom card to style the CSS of your card, it depends how the styling is done:

- Your own CSS variables that you should adapt to light and dark modes
- Fixed colors that won't adapt to light and dark modes

The problem is the same as above: you should use CSS variables, and define them in the light and dark modes of the theme.


