---
template: overrides/main.html
---

##:material-home-floor-3: HA M3 Theme colors

- Palettes
- Surfaces
- Light theme color mapping
- Dark theme color mapping

##:material-home-floor-3: Reference colors
The HA M3 implementation defines no less than **244** reference colors. Some are theme mode independent, others are specific for light or dark modes.

###:material-home-floor-3: Palette Reference colors

Reference palette colors use the `theme-ref-palette-` naming scheme and are theme mode independent.

Palette color schemes use 24 colors per palette and are available for:

- Neutral colors
- Neutral variant colors
- Primary colors
- Secondary colors
- Tertiary colors
- Error colors

??? "M3 Reference palette colors (from example theme 07):"
    ```yaml linenums="1"
      theme-ref-palette-primary100: '#ffffff'
      theme-ref-palette-primary99: '#fbffda'
      theme-ref-palette-primary95: '#e2fc8c'
      theme-ref-palette-primary90: '#d4ee7f'
      theme-ref-palette-primary80: '#b8d166'
      theme-ref-palette-primary70: '#9db54e'
      theme-ref-palette-primary60: '#839a36'
      theme-ref-palette-primary50: '#697f1c'
      theme-ref-palette-primary40: '#526600'
      theme-ref-palette-primary30: '#3c4d00'
      theme-ref-palette-primary20: '#283500'
      theme-ref-palette-primary10: '#161f00'
      theme-ref-palette-primary0: '#000000'
      theme-ref-palette-secondary100: '#ffffff'
      theme-ref-palette-secondary99: '#faffdd'
      theme-ref-palette-secondary95: '#eef4d1'
      theme-ref-palette-secondary90: '#e0e6c3'
      theme-ref-palette-secondary80: '#c4caa9'
      theme-ref-palette-secondary70: '#a8ae8e'
      theme-ref-palette-secondary60: '#8e9476'
      theme-ref-palette-secondary50: '#747a5d'
      theme-ref-palette-secondary40: '#5b6146'
      theme-ref-palette-secondary30: '#444930'
      theme-ref-palette-secondary20: '#2e331c'
      theme-ref-palette-secondary10: '#191d08'
      theme-ref-palette-secondary0: '#000000'
      theme-ref-palette-tertiary100: '#ffffff'
      theme-ref-palette-tertiary99: '#f0fffb'
      theme-ref-palette-tertiary95: '#cafaef'
      theme-ref-palette-tertiary90: '#bdece1'
      theme-ref-palette-tertiary80: '#a1d0c5'
      theme-ref-palette-tertiary70: '#86b4aa'
      theme-ref-palette-tertiary60: '#6c9a90'
      theme-ref-palette-tertiary50: '#527f76'
      theme-ref-palette-tertiary40: '#3a665e'
      theme-ref-palette-tertiary30: '#214e46'
      theme-ref-palette-tertiary20: '#033730'
      theme-ref-palette-tertiary10: '#00201b'
      theme-ref-palette-tertiary0: '#000000'
      theme-ref-palette-neutral100: '#ffffff'
      theme-ref-palette-neutral99: '#fefcf4'
      theme-ref-palette-neutral95: '#f3f1e9'
      theme-ref-palette-neutral90: '#e5e3db'
      theme-ref-palette-neutral80: '#c8c7bf'
      theme-ref-palette-neutral70: '#acaba4'
      theme-ref-palette-neutral60: '#92918a'
      theme-ref-palette-neutral50: '#787771'
      theme-ref-palette-neutral40: '#5f5f59'
      theme-ref-palette-neutral30: '#474742'
      theme-ref-palette-neutral20: '#30312b'
      theme-ref-palette-neutral10: '#1b1c17'
      theme-ref-palette-neutral0: '#000000'
      theme-ref-palette-neutral-variant100: '#ffffff'
      theme-ref-palette-neutral-variant99: '#fdfeec'
      theme-ref-palette-neutral-variant95: '#f1f2e1'
      theme-ref-palette-neutral-variant90: '#e3e4d3'
      theme-ref-palette-neutral-variant80: '#c7c8b8'
      theme-ref-palette-neutral-variant70: '#abac9d'
      theme-ref-palette-neutral-variant60: '#909283'
      theme-ref-palette-neutral-variant50: '#77786b'
      theme-ref-palette-neutral-variant40: '#5e6053'
      theme-ref-palette-neutral-variant30: '#46483c'
      theme-ref-palette-neutral-variant20: '#2f3126'
      theme-ref-palette-neutral-variant10: '#1a1d12'
      theme-ref-palette-neutral-variant0: '#000000'
      theme-ref-palette-error100: '#ffffff'
      theme-ref-palette-error99: '#fcfcfc'
      theme-ref-palette-error95: '#ffede9'
      theme-ref-palette-error90: '#ffdad4'
      theme-ref-palette-error80: '#ffb4a9'
      theme-ref-palette-error70: '#ff897a'
      theme-ref-palette-error60: '#ff5449'
      theme-ref-palette-error50: '#dd3730'
      theme-ref-palette-error40: '#ba1b1b'
      theme-ref-palette-error30: '#930006'
      theme-ref-palette-error20: '#680003'
      theme-ref-palette-error10: '#410001'
      theme-ref-palette-error0: '#000000'
      theme-ref-palette-primary5: '#0b0f00ff'
      theme-ref-palette-primary15: '#1f2a00ff'
      theme-ref-palette-primary25: '#324100ff'
      theme-ref-palette-primary35: '#475900ff'
      theme-ref-palette-primary45: '#5d720eff'
      theme-ref-palette-primary65: '#90a742ff'
      theme-ref-palette-primary75: '#aac35aff'
      theme-ref-palette-primary85: '#c6df72ff'
      theme-ref-palette-primary7: '#101700ff'
      theme-ref-palette-primary92: '#dbf585ff'
      theme-ref-palette-primary97: '#eefdb3ff'
      theme-ref-palette-secondary5: '#0c0e04ff'
      theme-ref-palette-secondary15: '#232812ff'
      theme-ref-palette-secondary25: '#393e26ff'
      theme-ref-palette-secondary35: '#4f553bff'
      theme-ref-palette-secondary45: '#676d51ff'
      theme-ref-palette-secondary65: '#9ba182ff'
      theme-ref-palette-secondary75: '#b6bc9bff'
      theme-ref-palette-secondary85: '#d2d8b6ff'
      theme-ref-palette-secondary7: '#121506ff'
      theme-ref-palette-secondary92: '#e7edcaff'
      theme-ref-palette-secondary97: '#f4f9d7ff'
      theme-ref-palette-tertiary5: '#00100dff'
      theme-ref-palette-tertiary15: '#012b25ff'
      theme-ref-palette-tertiary25: '#12423bff'
      theme-ref-palette-tertiary35: '#2d5a52ff'
      theme-ref-palette-tertiary45: '#46726aff'
      theme-ref-palette-tertiary65: '#79a79dff'
      theme-ref-palette-tertiary75: '#93c2b7ff'
      theme-ref-palette-tertiary85: '#afded3ff'
      theme-ref-palette-tertiary7: '#001814ff'
      theme-ref-palette-tertiary92: '#c3f3e8ff'
      theme-ref-palette-tertiary97: '#ddfcf5ff'
      theme-ref-palette-error5: '#200000ff'
      theme-ref-palette-error15: '#540002ff'
      theme-ref-palette-error25: '#7d0004ff'
      theme-ref-palette-error35: '#a60d10ff'
      theme-ref-palette-error45: '#cb2925ff'
      theme-ref-palette-error65: '#ff6e61ff'
      theme-ref-palette-error75: '#ff9e91ff'
      theme-ref-palette-error85: '#ffc7beff'
      theme-ref-palette-error7: '#300000ff'
      theme-ref-palette-error92: '#ffe3deff'
      theme-ref-palette-error97: '#fdf4f2ff'
      theme-ref-palette-neutral5: '#0d0e0bff'
      theme-ref-palette-neutral15: '#252621ff'
      theme-ref-palette-neutral25: '#3b3c36ff'
      theme-ref-palette-neutral35: '#53534dff'
      theme-ref-palette-neutral45: '#6b6b65ff'
      theme-ref-palette-neutral65: '#9f9e97ff'
      theme-ref-palette-neutral75: '#bab9b1ff'
      theme-ref-palette-neutral85: '#d6d5cdff'
      theme-ref-palette-neutral7: '#141511ff'
      theme-ref-palette-neutral92: '#eceae2ff'
      theme-ref-palette-neutral97: '#f8f6eeff'
      theme-ref-palette-neutral-variant5: '#0d0e09ff'
      theme-ref-palette-neutral-variant15: '#24271cff'
      theme-ref-palette-neutral-variant25: '#3a3c31ff'
      theme-ref-palette-neutral-variant35: '#525447ff'
      theme-ref-palette-neutral-variant45: '#6a6c5fff'
      theme-ref-palette-neutral-variant65: '#9d9f90ff'
      theme-ref-palette-neutral-variant75: '#b9baaaff'
      theme-ref-palette-neutral-variant85: '#d5d6c5ff'
      theme-ref-palette-neutral-variant7: '#13150dff'
      theme-ref-palette-neutral-variant92: '#eaebdaff'
      theme-ref-palette-neutral-variant97: '#f7f8e6ff'
    ```

###:material-home-floor-3: Elevation surface Reference colors

Reference elevation surface colors use the `theme-ref-elevation-surface-` naming scheme and are specific per theme mode by using `-light` and `-dark` suffixes in the name.

Surface color schemes are available for:

- Neutral colors
- Neutral base color mixed with the primary color
- Neutral base color mixed with the secundary color
- Neutral base color mixed with the tertiary color
- Neutral base color mixed with the error color


??? "M3 Reference elevation surface colors (from example theme 07):"
    ```yaml linenums="1"
      theme-ref-elevation-surface-neutral1-light: rgb(249,247,239)
      theme-ref-elevation-surface-neutral2-light: rgb(246,244,236)
      theme-ref-elevation-surface-neutral3-light: rgb(241,239,232)
      theme-ref-elevation-surface-neutral4-light: rgb(237,235,227)
      theme-ref-elevation-surface-neutral5-light: rgb(230,228,221)
      theme-ref-elevation-surface-neutral6-light: rgb(224,222,215)
      theme-ref-elevation-surface-neutral7-light: rgb(216,214,207)
      theme-ref-elevation-surface-neutral8-light: rgb(208,206,199)
      theme-ref-elevation-surface-neutral9-light: rgb(198,197,190)
      theme-ref-elevation-surface-neutral10-light: rgb(190,189,182)
      theme-ref-elevation-surface-primary1-light: rgb(249,248,237)
      theme-ref-elevation-surface-primary2-light: rgb(245,244,232)
      theme-ref-elevation-surface-primary3-light: rgb(240,240,224)
      theme-ref-elevation-surface-primary4-light: rgb(235,236,217)
      theme-ref-elevation-surface-primary5-light: rgb(228,230,207)
      theme-ref-elevation-surface-primary6-light: rgb(221,224,198)
      theme-ref-elevation-surface-primary7-light: rgb(213,216,185)
      theme-ref-elevation-surface-primary8-light: rgb(204,209,173)
      theme-ref-elevation-surface-primary9-light: rgb(194,200,159)
      theme-ref-elevation-surface-primary10-light: rgb(185,192,146)
      theme-ref-elevation-surface-secondary1-light: rgb(249,247,239)
      theme-ref-elevation-surface-secondary2-light: rgb(246,244,235)
      theme-ref-elevation-surface-secondary3-light: rgb(241,240,230)
      theme-ref-elevation-surface-secondary4-light: rgb(236,235,225)
      theme-ref-elevation-surface-secondary5-light: rgb(230,229,218)
      theme-ref-elevation-surface-secondary6-light: rgb(223,223,211)
      theme-ref-elevation-surface-secondary7-light: rgb(215,215,202)
      theme-ref-elevation-surface-secondary8-light: rgb(207,207,194)
      theme-ref-elevation-surface-secondary9-light: rgb(197,198,183)
      theme-ref-elevation-surface-secondary10-light: rgb(189,190,174)
      theme-ref-elevation-surface-tertiary1-light: rgb(248,248,240)
      theme-ref-elevation-surface-tertiary2-light: rgb(244,244,236)
      theme-ref-elevation-surface-tertiary3-light: rgb(238,240,232)
      theme-ref-elevation-surface-tertiary4-light: rgb(232,236,228)
      theme-ref-elevation-surface-tertiary5-light: rgb(225,230,222)
      theme-ref-elevation-surface-tertiary6-light: rgb(217,224,216)
      theme-ref-elevation-surface-tertiary7-light: rgb(207,216,208)
      theme-ref-elevation-surface-tertiary8-light: rgb(197,209,200)
      theme-ref-elevation-surface-tertiary9-light: rgb(185,200,192)
      theme-ref-elevation-surface-tertiary10-light: rgb(176,192,184)
      theme-ref-elevation-surface-error1-light: rgb(252,245,237)
      theme-ref-elevation-surface-error2-light: rgb(251,241,233)
      theme-ref-elevation-surface-error3-light: rgb(249,234,227)
      theme-ref-elevation-surface-error4-light: rgb(247,227,220)
      theme-ref-elevation-surface-error5-light: rgb(244,218,211)
      theme-ref-elevation-surface-error6-light: rgb(241,209,203)
      theme-ref-elevation-surface-error7-light: rgb(238,198,192)
      theme-ref-elevation-surface-error8-light: rgb(234,187,181)
      theme-ref-elevation-surface-error9-light: rgb(230,173,168)
      theme-ref-elevation-surface-error10-light: rgb(227,162,157)
      theme-ref-elevation-surface-neutral1-dark: rgb(36,37,31)
      theme-ref-elevation-surface-neutral2-dark: rgb(41,42,36)
      theme-ref-elevation-surface-neutral3-dark: rgb(46,47,41)
      theme-ref-elevation-surface-neutral4-dark: rgb(53,54,48)
      theme-ref-elevation-surface-neutral5-dark: rgb(60,60,55)
      theme-ref-elevation-surface-neutral6-dark: rgb(69,69,63)
      theme-ref-elevation-surface-neutral7-dark: rgb(77,78,72)
      theme-ref-elevation-surface-neutral8-dark: rgb(88,88,82)
      theme-ref-elevation-surface-neutral9-dark: rgb(96,96,90)
      theme-ref-elevation-surface-neutral10-dark: rgb(105,105,99)
      theme-ref-elevation-surface-primary1-dark: rgb(35,37,27)
      theme-ref-elevation-surface-primary2-dark: rgb(40,42,29)
      theme-ref-elevation-surface-primary3-dark: rgb(44,48,32)
      theme-ref-elevation-surface-primary4-dark: rgb(51,55,35)
      theme-ref-elevation-surface-primary5-dark: rgb(57,62,38)
      theme-ref-elevation-surface-primary6-dark: rgb(65,71,42)
      theme-ref-elevation-surface-primary7-dark: rgb(73,80,46)
      theme-ref-elevation-surface-primary8-dark: rgb(82,91,51)
      theme-ref-elevation-surface-primary9-dark: rgb(90,100,55)
      theme-ref-elevation-surface-primary10-dark: rgb(98,109,59)
      theme-ref-elevation-surface-secondary1-dark: rgb(35,37,30)
      theme-ref-elevation-surface-secondary2-dark: rgb(41,42,35)
      theme-ref-elevation-surface-secondary3-dark: rgb(46,47,39)
      theme-ref-elevation-surface-secondary4-dark: rgb(52,54,45)
      theme-ref-elevation-surface-secondary5-dark: rgb(59,61,51)
      theme-ref-elevation-surface-secondary6-dark: rgb(68,70,58)
      theme-ref-elevation-surface-secondary7-dark: rgb(76,78,65)
      theme-ref-elevation-surface-secondary8-dark: rgb(86,89,74)
      theme-ref-elevation-surface-secondary9-dark: rgb(95,98,81)
      theme-ref-elevation-surface-secondary10-dark: rgb(103,106,89)
      theme-ref-elevation-surface-tertiary1-dark: rgb(34,37,32)
      theme-ref-elevation-surface-tertiary2-dark: rgb(38,42,37)
      theme-ref-elevation-surface-tertiary3-dark: rgb(42,48,42)
      theme-ref-elevation-surface-tertiary4-dark: rgb(47,55,49)
      theme-ref-elevation-surface-tertiary5-dark: rgb(52,62,56)
      theme-ref-elevation-surface-tertiary6-dark: rgb(59,71,65)
      theme-ref-elevation-surface-tertiary7-dark: rgb(66,80,73)
      theme-ref-elevation-surface-tertiary8-dark: rgb(74,91,84)
      theme-ref-elevation-surface-tertiary9-dark: rgb(81,100,93)
      theme-ref-elevation-surface-tertiary10-dark: rgb(87,109,101)
      theme-ref-elevation-surface-error1-dark: rgb(38,36,30)
      theme-ref-elevation-surface-error2-dark: rgb(45,40,35)
      theme-ref-elevation-surface-error3-dark: rgb(52,45,39)
      theme-ref-elevation-surface-error4-dark: rgb(61,51,45)
      theme-ref-elevation-surface-error5-dark: rgb(70,57,51)
      theme-ref-elevation-surface-error6-dark: rgb(82,64,58)
      theme-ref-elevation-surface-error7-dark: rgb(93,72,65)
      theme-ref-elevation-surface-error8-dark: rgb(107,81,74)
      theme-ref-elevation-surface-error9-dark: rgb(118,89,81)
      theme-ref-elevation-surface-error10-dark: rgb(130,96,89)
    ```

##:material-home-floor-3: System colors
M3 System colors are by definition **independent** of the theme mode. Their actual value adapts to the light or dark mode.

###:material-home-floor-3: Standard M3 light and dark system colors

??? "M3 System colors mapping for LIGHT mode"
    ```yaml linenums="1"
    # light theme...
    #
    # --------------------------------------------------------------------------
    light:
      theme-sys-color-primary: var(--theme-ref-palette-primary40)
      theme-sys-color-on-primary: var(--theme-ref-palette-primary100)
      theme-sys-color-primary-container: var(--theme-ref-palette-primary90)
      theme-sys-color-on-primary-container: var(--theme-ref-palette-primary10)

      theme-sys-color-secondary: var(--theme-ref-palette-secondary40)
      theme-sys-color-on-secondary: var(--theme-ref-palette-secondary100)
      theme-sys-color-secondary-container: var(--theme-ref-palette-secondary90)
      theme-sys-color-on-secondary-container: var(--theme-ref-palette-secondary10)

      theme-sys-color-tertiary: var(--theme-ref-palette-tertiary40)
      theme-sys-color-on-tertiary: var(--theme-ref-palette-tertiary100)
      theme-sys-color-tertiary-container: var(--theme-ref-palette-tertiary90)
      theme-sys-color-on-tertiary-container: var(--theme-ref-palette-tertiary10)

      theme-sys-color-error: var(--theme-ref-palette-error40)
      theme-sys-color-on-error: var(--theme-ref-palette-error100)
      theme-sys-color-error-container: var(--theme-ref-palette-error90)
      theme-sys-color-on-error-container: var(--theme-ref-palette-error10)

      theme-sys-color-background: var(--theme-ref-palette-neutral99)
      theme-sys-color-on-background:  var(--theme-ref-palette-neutral20)

      theme-sys-color-surface: var(--theme-ref-palette-neutral99)
      theme-sys-color-on-surface: var(--theme-ref-palette-neutral10)
      theme-sys-color-surface-variant: var(--theme-ref-palette-neutral-variant90)
      theme-sys-color-on-surface-variant: var(--theme-ref-palette-neutral-variant30)

      theme-sys-color-outline: var(--theme-ref-palette-neutral-variant50)

      # Guessing for these 3
      theme-sys-color-inverse-surface: var(--theme-ref-palette-neutral10)
      theme-sys-color-inverse-on-surface: var(--theme-ref-palette-neutral99)
      theme-sys-color-inverse-primary: var(--theme-ref-palette-primary100)

      # No idea with this one...
      theme-sys-color-shadow: black

    ```
    
??? "M3 System colors mapping for DARK mode"
    ```yaml linenums="1"
    # dark theme...
    #
    # --------------------------------------------------------------------------
    dark:
      # Start with the M3 generated colors for dark mode...
      #
      theme-sys-color-primary: var(--theme-ref-palette-primary80)
      theme-sys-color-on-primary: var(--theme-ref-palette-primary20)
      theme-sys-color-primary-container: var(--theme-ref-palette-primary30)
      theme-sys-color-on-primary-container: var(--theme-ref-palette-primary90)

      theme-sys-color-secondary: var(--theme-ref-palette-secondary80)
      theme-sys-color-on-secondary: var(--theme-ref-palette-secondary20)
      theme-sys-color-secondary-container: var(--theme-ref-palette-secondary30)
      theme-sys-color-on-secondary-container: var(--theme-ref-palette-secondary90)

      theme-sys-color-tertiary: var(--theme-ref-palette-tertiary80)
      theme-sys-color-on-tertiary: var(--theme-ref-palette-tertiary20)
      theme-sys-color-tertiary-container: var(--theme-ref-palette-tertiary30)
      theme-sys-color-on-tertiary-container: var(--theme-ref-palette-tertiary90)

      theme-sys-color-error: var(--theme-ref-palette-error80)
      theme-sys-color-on-error: var(--theme-ref-palette-error20)
      theme-sys-color-error-container: var(--theme-ref-palette-error30)
      theme-sys-color-on-error-container: var(--theme-ref-palette-error90)

      theme-sys-color-background: var(--theme-ref-palette-neutral10)
      theme-sys-color-on-background:  var(--theme-ref-palette-neutral90)

      theme-sys-color-surface: var(--theme-ref-palette-neutral10)
      theme-sys-color-on-surface: var(--theme-ref-palette-neutral80)
      theme-sys-color-surface-variant: var(--theme-ref-palette-neutral-variant30)
      theme-sys-color-on-surface-variant: var(--theme-ref-palette-neutral-variant80)

      theme-sys-color-outline: var(--theme-ref-palette-neutral-variant60)

      # Guessing for these 3
      theme-sys-color-inverse-surface: var(--theme-ref-palette-neutral80)
      theme-sys-color-inverse-on-surface: var(--theme-ref-palette-neutral10)
      theme-sys-color-inverse-primary: var(--theme-ref-palette-primary80)

      # No idea with this one...
      theme-sys-color-shadow: black
    ```
###:material-home-floor-3: Standard M3 elevation surface light and dark colors

??? "M3 elevation surface color mapping for LIGHT mode"
    ```yaml linenums="1"
      # Surfaces
      # -----------------------------------------------------------------------

      theme-sys-elevation-color-neutral1: var(--theme-ref-elevation-surface-neutral1-light)
      theme-sys-elevation-color-neutral2: var(--theme-ref-elevation-surface-neutral2-light)
      theme-sys-elevation-color-neutral3: var(--theme-ref-elevation-surface-neutral3-light)
      theme-sys-elevation-color-neutral4: var(--theme-ref-elevation-surface-neutral4-light)
      theme-sys-elevation-color-neutral5: var(--theme-ref-elevation-surface-neutral5-light)
      theme-sys-elevation-color-neutral6: var(--theme-ref-elevation-surface-neutral6-light)
      theme-sys-elevation-color-neutral7: var(--theme-ref-elevation-surface-neutral7-light)
      theme-sys-elevation-color-neutral8: var(--theme-ref-elevation-surface-neutral8-light)
      theme-sys-elevation-color-neutral9: var(--theme-ref-elevation-surface-neutral9-light)
      theme-sys-elevation-color-neutral10: var(--theme-ref-elevation-surface-neutral10-light)

      theme-sys-elevation-color-primary1: var(--theme-ref-elevation-surface-primary1-light)
      theme-sys-elevation-color-primary2: var(--theme-ref-elevation-surface-primary2-light)
      theme-sys-elevation-color-primary3: var(--theme-ref-elevation-surface-primary3-light)
      theme-sys-elevation-color-primary4: var(--theme-ref-elevation-surface-primary4-light)
      theme-sys-elevation-color-primary5: var(--theme-ref-elevation-surface-primary5-light)
      theme-sys-elevation-color-primary6: var(--theme-ref-elevation-surface-primary6-light)
      theme-sys-elevation-color-primary7: var(--theme-ref-elevation-surface-primary7-light)
      theme-sys-elevation-color-primary8: var(--theme-ref-elevation-surface-primary8-light)
      theme-sys-elevation-color-primary9: var(--theme-ref-elevation-surface-primary9-light)
      theme-sys-elevation-color-primary10: var(--theme-ref-elevation-surface-primary10-light)

      theme-sys-elevation-color-secondary1: var(--theme-ref-elevation-surface-secondary1-light)
      theme-sys-elevation-color-secondary2: var(--theme-ref-elevation-surface-secondary2-light)
      theme-sys-elevation-color-secondary3: var(--theme-ref-elevation-surface-secondary3-light)
      theme-sys-elevation-color-secondary4: var(--theme-ref-elevation-surface-secondary4-light)
      theme-sys-elevation-color-secondary5: var(--theme-ref-elevation-surface-secondary5-light)
      theme-sys-elevation-color-secondary6: var(--theme-ref-elevation-surface-secondary6-light)
      theme-sys-elevation-color-secondary7: var(--theme-ref-elevation-surface-secondary7-light)
      theme-sys-elevation-color-secondary8: var(--theme-ref-elevation-surface-secondary8-light)
      theme-sys-elevation-color-secondary9: var(--theme-ref-elevation-surface-secondary9-light)
      theme-sys-elevation-color-secondary10: var(--theme-ref-elevation-surface-secondary10-light)

      theme-sys-elevation-color-tertiary1: var(--theme-ref-elevation-surface-tertiary1-light)
      theme-sys-elevation-color-tertiary2: var(--theme-ref-elevation-surface-tertiary2-light)
      theme-sys-elevation-color-tertiary3: var(--theme-ref-elevation-surface-tertiary3-light)
      theme-sys-elevation-color-tertiary4: var(--theme-ref-elevation-surface-tertiary4-light)
      theme-sys-elevation-color-tertiary5: var(--theme-ref-elevation-surface-tertiary5-light)
      theme-sys-elevation-color-tertiary6: var(--theme-ref-elevation-surface-tertiary6-light)
      theme-sys-elevation-color-tertiary7: var(--theme-ref-elevation-surface-tertiary7-light)
      theme-sys-elevation-color-tertiary8: var(--theme-ref-elevation-surface-tertiary8-light)
      theme-sys-elevation-color-tertiary9: var(--theme-ref-elevation-surface-tertiary9-light)
      theme-sys-elevation-color-tertiary10: var(--theme-ref-elevation-surface-tertiary10-light)

      theme-sys-elevation-color-error1: var(--theme-ref-elevation-surface-error1-light)
      theme-sys-elevation-color-error2: var(--theme-ref-elevation-surface-error2-light)
      theme-sys-elevation-color-error3: var(--theme-ref-elevation-surface-error3-light)
      theme-sys-elevation-color-error4: var(--theme-ref-elevation-surface-error4-light)
      theme-sys-elevation-color-error5: var(--theme-ref-elevation-surface-error5-light)
      theme-sys-elevation-color-error6: var(--theme-ref-elevation-surface-error6-light)
      theme-sys-elevation-color-error7: var(--theme-ref-elevation-surface-error7-light)
      theme-sys-elevation-color-error8: var(--theme-ref-elevation-surface-error8-light)
      theme-sys-elevation-color-error9: var(--theme-ref-elevation-surface-error9-light)
      theme-sys-elevation-color-error10: var(--theme-ref-elevation-surface-error10-light)

    ```

??? "M3 elevation surface color mapping for DARK mode"
    ```yaml linenums="1"
      # Surfaces
      # -----------------------------------------------------------------------

      theme-sys-elevation-color-neutral1: var(--theme-ref-elevation-surface-neutral1-dark)
      theme-sys-elevation-color-neutral2: var(--theme-ref-elevation-surface-neutral2-dark)
      theme-sys-elevation-color-neutral3: var(--theme-ref-elevation-surface-neutral3-dark)
      theme-sys-elevation-color-neutral4: var(--theme-ref-elevation-surface-neutral4-dark)
      theme-sys-elevation-color-neutral5: var(--theme-ref-elevation-surface-neutral5-dark)
      theme-sys-elevation-color-neutral6: var(--theme-ref-elevation-surface-neutral6-dark)
      theme-sys-elevation-color-neutral7: var(--theme-ref-elevation-surface-neutral7-dark)
      theme-sys-elevation-color-neutral8: var(--theme-ref-elevation-surface-neutral8-dark)
      theme-sys-elevation-color-neutral9: var(--theme-ref-elevation-surface-neutral9-dark)
      theme-sys-elevation-color-neutral10: var(--theme-ref-elevation-surface-neutral10-dark)

      theme-sys-elevation-color-primary1: var(--theme-ref-elevation-surface-primary1-dark)
      theme-sys-elevation-color-primary2: var(--theme-ref-elevation-surface-primary2-dark)
      theme-sys-elevation-color-primary3: var(--theme-ref-elevation-surface-primary3-dark)
      theme-sys-elevation-color-primary4: var(--theme-ref-elevation-surface-primary4-dark)
      theme-sys-elevation-color-primary5: var(--theme-ref-elevation-surface-primary5-dark)
      theme-sys-elevation-color-primary6: var(--theme-ref-elevation-surface-primary6-dark)
      theme-sys-elevation-color-primary7: var(--theme-ref-elevation-surface-primary7-dark)
      theme-sys-elevation-color-primary8: var(--theme-ref-elevation-surface-primary8-dark)
      theme-sys-elevation-color-primary9: var(--theme-ref-elevation-surface-primary9-dark)
      theme-sys-elevation-color-primary10: var(--theme-ref-elevation-surface-primary10-dark)

      theme-sys-elevation-color-secondary1: var(--theme-ref-elevation-surface-secondary1-dark)
      theme-sys-elevation-color-secondary2: var(--theme-ref-elevation-surface-secondary2-dark)
      theme-sys-elevation-color-secondary3: var(--theme-ref-elevation-surface-secondary3-dark)
      theme-sys-elevation-color-secondary4: var(--theme-ref-elevation-surface-secondary4-dark)
      theme-sys-elevation-color-secondary5: var(--theme-ref-elevation-surface-secondary5-dark)
      theme-sys-elevation-color-secondary6: var(--theme-ref-elevation-surface-secondary6-dark)
      theme-sys-elevation-color-secondary7: var(--theme-ref-elevation-surface-secondary7-dark)
      theme-sys-elevation-color-secondary8: var(--theme-ref-elevation-surface-secondary8-dark)
      theme-sys-elevation-color-secondary9: var(--theme-ref-elevation-surface-secondary9-dark)
      theme-sys-elevation-color-secondary10: var(--theme-ref-elevation-surface-secondary10-dark)

      theme-sys-elevation-color-tertiary1: var(--theme-ref-elevation-surface-tertiary1-dark)
      theme-sys-elevation-color-tertiary2: var(--theme-ref-elevation-surface-tertiary2-dark)
      theme-sys-elevation-color-tertiary3: var(--theme-ref-elevation-surface-tertiary3-dark)
      theme-sys-elevation-color-tertiary4: var(--theme-ref-elevation-surface-tertiary4-dark)
      theme-sys-elevation-color-tertiary5: var(--theme-ref-elevation-surface-tertiary5-dark)
      theme-sys-elevation-color-tertiary6: var(--theme-ref-elevation-surface-tertiary6-dark)
      theme-sys-elevation-color-tertiary7: var(--theme-ref-elevation-surface-tertiary7-dark)
      theme-sys-elevation-color-tertiary8: var(--theme-ref-elevation-surface-tertiary8-dark)
      theme-sys-elevation-color-tertiary9: var(--theme-ref-elevation-surface-tertiary9-dark)
      theme-sys-elevation-color-tertiary10: var(--theme-ref-elevation-surface-tertiary10-dark)

      theme-sys-elevation-color-error1: var(--theme-ref-elevation-surface-error1-dark)
      theme-sys-elevation-color-error2: var(--theme-ref-elevation-surface-error2-dark)
      theme-sys-elevation-color-error3: var(--theme-ref-elevation-surface-error3-dark)
      theme-sys-elevation-color-error4: var(--theme-ref-elevation-surface-error4-dark)
      theme-sys-elevation-color-error5: var(--theme-ref-elevation-surface-error5-dark)
      theme-sys-elevation-color-error6: var(--theme-ref-elevation-surface-error6-dark)
      theme-sys-elevation-color-error7: var(--theme-ref-elevation-surface-error7-dark)
      theme-sys-elevation-color-error8: var(--theme-ref-elevation-surface-error8-dark)
      theme-sys-elevation-color-error9: var(--theme-ref-elevation-surface-error9-dark)
      theme-sys-elevation-color-error10: var(--theme-ref-elevation-surface-error10-dark)
    ```

##:material-home-floor-3: M3 Mapping to HA/Material 2 color names

TBD.

Color mappings :

- primary-background-color
- secondary-background-color
- ...
- primary-color
- secondary-color
- accent-color
- ...
- primary-text-color
- secondary-text-color
- card-background-color
- box-shadow-light/dark-color

And more, like icon, switch, label stuff too??
