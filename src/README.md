The `json2theme.py` script converts a .json file exported by the Material Theme Builder on Figma to a file that can be inserted in a Material 3 Theme for Home Assistant.

The output has to be inserted at the same position as with the other converter.

##Usage

`python json2theme.py exported.json converted.txt`

Copy/paste the output between:

```yaml
M3-JsonTest:
  # Colors generated via Material Design 3 (Material You) JSON export of Figma
  # And imported using a Python script...
  #
  # --------------------------------------------------------------------------
  # ==================== START of M3 copy/paste configuration ================
  # --------------------------------------------------------------------------
```
...and...
```yaml
  # --------------------------------------------------------------------------
  # ==================== END of M3 copy/paste configuration ==================
  # --------------------------------------------------------------------------
```
