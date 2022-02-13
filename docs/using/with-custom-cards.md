---
template: overrides/main.html
---

##:material-home-floor-3: Theme mode compatible custom cards

If the custom card is already fully compatible with dark and light theme modes, then, as with Home Assistant itself and the built-in cards, I wouldn't expect any problems with the HA M3 themes, unless the custom card requires its own dedicated theme.

##:material-home-floor-3: Any other case...

If the custom card is not compatible with light and dark modes, it highly depends on what the custom card is using:

- Its own CSS variables that you should adapt to light and dark modes
- Fixed colors that won't adapt to light and dark modes

The last case is a difficult one, and can only be changed by the developer of the custom card. But if the card is using its own CSS variables, you can define a light and dark variant in the M3 theme.

##:material-home-floor-3: Note on custom card styling

If you use a custom card to style the CSS of your card, it depends how the styling is done:

- Your own CSS variables that you should adapt to light and dark modes
- Fixed colors that won't adapt to light and dark modes

The problem is the same as above: you should use CSS variables, and define them in the light and dark modes of the theme.


