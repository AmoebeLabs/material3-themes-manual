---
template: overrides/main.html
---

##:material-home-floor-3: Where to start?
So, you came here to read how to design your own theme. That's good!

<!---

| Theme | primary | secondary | diff | tertiary | diffp | diffs | neutral | diff | variant | diff |
| ----- |----- |----- |----- |----- |----- |----- |----- |----- |-----|-----
| Cadmium Green | 160| 147 | -13 | 196 | 36 | 49 | 120 | 40 | 135 | 25 |
| Green | 120 | 100 | -20 | 183 | 63 | 83 | 74 | - 46 | 95 | -25 |
| Magenta | 344 | 348 | 4 | 30 | 46 | 42 | 353 | 9 | 352 | 8 |
| Red | 358 | 6 | 8 | 41 | 43 | 35 | 5 | 7 | 6 | 8 |
| Indigo | 221 | 225 | 4 | 304 | 83 | 79 ||||

r-y = 24 - 90 = 66
y-g = 90 - 153 =  63
g-b = 153 - 252 = 99
b-v = 252 - 310 = 58

Als bij elke tertiary een stap wordt gemaakt, dan is dit dus afhankelijk van de primary kleur om te zeggen zoveel % van het verschil...
bij rood zie ik bijv. een verschil van 50. Magenta 60.
rood gaat naar geel/oranje achtig. 50/66 = 0.75
magenta gaat naar oranje/bruin. 66 + 24 = 60/90 = 0.67. Begint wel in de richting te komen... Zal per stap zijn berekend wat het bereik is, en hoeveel procent je dus moet meenemen per stap om deze breuk te kunnen berekenen... Zou M3 75% van een kleurenstap doen?
van blauw naar violet is dan .75 * 58 = 43.5. Dan zou een blauwe kleur dus daar ergens op moeten uitkomen in lch verschil??

wow! klopt dus. zie hieronder. 
en voor secundary kleur. Verschil 8. dat is dus 8/58 = 0.137.

0.137 * 90 = 12.41
0.137 * 6.7 = 0.9179
verschil hieronder is van 6.7 naar 5.86 = 0.84. hmm. Toeval of ben ik gewoon ernaartoe aan het rekenen... Laatste denk ik.

blauw:
primary is #0062a1, hsl(203.48, 100%, 31.57%), 40.09, 40.72, 270.55
secondary is #526070, hsl(212, 15.46%, 38.04%), 40.13, 10.91, 262.82 (8)
tertiary is #695779, hsl(271.76, 16.35%, 40.78%), 39.91, 21.96, 311.33 (41)


https://ninedegreesbelow.com/photography/lch-vs-hsv-for-picking-colors.html

colorfulness = chroma / lightness. Denk dat google dat ook doet om dingen te bepalen...

https://luncheon.github.io/lch-color-wheel/

https://discuss.pixls.us/t/gimp-2-9-now-has-an-lch-hue-chroma-tool-plus-lch-color-sliders/4335/20
Ook hier zie je een colorwheel lch om te begrijpen dat het heel anders in elkaar zit dan een rgb colorwheel...


https://www.maplesoft.com/support/help/maple/view.aspx?path=ColorTools%2FLCHColorWheel

saturation=float
 	
A number between 0 and 5 for the LCH saturation of the colors in the wheel. (The default is 0.66.) In the LCH space, saturation is the ratio of the lightness and chroma coordinates.


cadmium green:
neutral is 5c5f5c, hsl(120,1%,36%), rgb(92,95,92)
variant is 58605a, hsl(135,4%,36%), rgb(88,96,90)

primary is 006c48, hsl(160,100%,21%), rgb(0,108,72), lab 39.6, -35, 12
secundary is 4d6357, hsl(147,12%,34%), rgb(77,99,87)
tertiary is 3d6473, hsl(196,30%,34%), rgb(61,100,115)

sec, 160, 147 = 13 graden
tert, 160, 196 = 36 graden
neutral, 160, 120 = 40 graden
variant, 160, 135 = 25 graden

http://colormine.org/delta-e-calculator
primary secondary 26.9249
primary tertiary 36.2491
secondary tertiary 16.0526


magenta:
neutral is 655c5d, hsl(353,4%,37%), rgb(101,92,93)
variant is 6a5b5d, hsl(352,7%,38%), rgb(106,91,93)

primary is 9b4058, hsl(344,41%,42%), rgb(155,64,88), lch 39, 39, 6.7
secundary is 75565c, hsl(348,15%,39%), rgb(117,86,92) lch 39, 13.5, 5.86 (1) C is 2.9x less
tertiary is 7a5732, hsl(30,41%,33%), rgb(122,87,50), lch 39, 27.6, 68.45 (60)

http://colormine.org/delta-e-calculator
primary secondary 25.9765
primary tertiary 35.852
secondary tertiary 24.5004

sec, 344, 348 = 4 graden
tert, 344, 30 = 46 graden
neutral, 344, 353 = 10 graden
variant, 344, 352 = 8 graden

red:
neutral is 655c5b, hsl(5,5%,37%), rgb(101,92,91)
variant is 6b5a58, hsl(6,9%,38%), rgb(107,90,88)

primary is be1013, hsl(358,84%,40%), rgb(190,16,19) lch 39, 76, 36
secundary is 775652, hsl(6,18%,39%), rgb(119,86,82) lch 39, 15, 30 (6) C is 5x less than primary
tertiary is 715c2e, hsl(41,42%,31%), rgb(113,92,46) lch 39, 29, 85 (50) 

sec, 358, 6 = 8 graden
tert, 358, 41 = 43 graden
neutral, 358, 5 = 7 graden
variant, 358, 6 = 8 graden

http://colormine.org/delta-e-calculator
primary secondary 62.0809
primary tertiary 61.6426
secondary tertiary 24.0175

http://colormine.org/delta-e-calculator/cie2000
primary secondary 15.9121
primary tertiary 35.6556

indigo:
primary is 355ab0, hsl(221,53%,44%), rgb(53,90,176), lch 39, 49, 286 hsv 222, 70, 69
secundary is 585e71, hsl(225,12%,39%), rgb(88,94,113), lch 39, 11, 280 (6) Hmm. C is 4.5x less than primary. See also 63/14 !! hsv 226, 22, 44
tertiary is 735571, hsl(304,15%,39%), rgb(115,85,113), lch 39, 20, 328 (42) hsv 304, 26, 45

sec, 221, 225 = 4 graden
tert, 221, 304 = 83 graden

http://colormine.org/delta-e-calculator
primary secondary 37.74
primary tertiary 35.8193
secondary tertiary 15.6024

http://colormine.org/delta-e-calculator/cie2000
primary secondary 17.6249
primary tertiary ?????

Green:
primary 006f00, hsl(120,100%,21%), lab 38.8, -45, 43, lch 38.8, 63, 136, luv 39, -37, 47
secondary 54634d, hsl(100,12%,34%), lch 39.5, 14, 133, lch 39, 14, 133 (3), luv 39, -7, 14
tertiary 386669, hsl(183,30%,31%), lch 39.5, 16, 202, lch 39, 16, 202 (66), luv 39, -20, -6

5e5f5b hsl(74,2%,36%)
5a6056 hsl(95,5%,35%

http://colormine.org/delta-e-calculator
primary secondary 49.2585
primary tertiary 58.8041
secondary tertiary 17.0897

http://colormine.org/delta-e-calculator/cie2000
primary secondary 19.0495
primary tertiary ?????

red = 0
green = 120
blue = 240

http://colormine.org/color-converter
http://colormine.org/convert/lch-to-luv met GITHUB source!!!!!!!!

CIE-l*ab colors
80 = 120, 100, 45, lab 79.8, -79, 76
60 = 120, 100, 32 lab 58.3, -61, 59
20 = 120, 100, 11 lab 19.4, -29, 26

the CIE-Lch colors have the same L. But C/H is different.
The CIE-Luv colors have the same L, but u/v is different.

https://gist.github.com/Myndex/47c793f8a054041bd2b52caa7ad5271c#:~:text=Luv%20is%20superior%20to%20Lab,more%20uniform%20and%20intuitive%20effect.

Luv is superior to Lab for choosing colors !!

Which is Better?
Again, this is irrelevant, as Lab and Luv have different strengths and weaknesses, depending on the use or application.

Lab is considered better for reflective surface colors illuminated by a standard illuminant like D65 (D50 is used in the printing industry).

**Luv is considered better for emissive, self-illuminated colors. Oh, by the way, that means things like computer monitors and TV sets. Luv is also widely used for information visualization due to it's stable saturation performance.**

Both Lab and Luv use the identical L* (Lstar) for perceptual lightness. And L* is the one part of Lab and Luv that is somewhat perceptually uniform, so long as the surround is white or light grey.

Neither Lab or Luv are "truly" uniform in terms of hue and chroma, but Lab is markedly worse than Luv. Lab suffers from unstable hue that changes due to L* or C and moreover Lab has significant inaccuracies in the blue area. The distribution of Lab colors is also much more uneven than Luv, and the opponents are not at 180• to each other.

The uv of Luv makes up the more modern spectral locus which is a better choice than the 1931 diagram. Luv has more stable hue when L* or C is changed (before clipping) than Lab, though Luv can be more susceptible to clipping. The distribution of Luv colors is also much more even than Lab.

--->