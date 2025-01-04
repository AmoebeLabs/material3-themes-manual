import json
import argparse

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return ','.join(str(int(hex_color[i:i+2], 16)) for i in (0, 2, 4))

def get_surfaces(surface_color, palette_color, opacities, css_name, mode):
    def hex_to_rgb_dict(hex_color):
        return {
            'r': int(hex_color[1:3], 16),
            'g': int(hex_color[3:5], 16),
            'b': int(hex_color[5:7], 16)
        }
    
    bg_col = hex_to_rgb_dict(surface_color)
    fg_col = hex_to_rgb_dict(palette_color)
    
    surface_colors = []
    for index, opacity in enumerate(opacities, start=1):
        r = round(opacity * fg_col['r'] + (1 - opacity) * bg_col['r'])
        g = round(opacity * fg_col['g'] + (1 - opacity) * bg_col['g'])
        b = round(opacity * fg_col['b'] + (1 - opacity) * bg_col['b'])
        
        surface_colors.append(f"{css_name}{index}-{mode}: rgb({r},{g},{b})")
        surface_colors.append(f"{css_name}{index}-{mode}-rgb: {r},{g},{b}")
    
    return surface_colors

def generate_surface_colors(data):
    opacity_surface_light = [0.03, 0.05, 0.08, 0.11, 0.15, 0.19, 0.24, 0.29, 0.35, 0.4]
    opacity_surface_dark = [0.05, 0.08, 0.11, 0.15, 0.19, 0.24, 0.29, 0.35, 0.4, 0.45]
    
    themes = data.get('schemes', {})
    light_theme = themes.get('light', {})
    dark_theme = themes.get('dark', {})
    
    palettes = data.get('palettes')
    neutral = palettes.get('neutral')
    neutralvariant = palettes.get('neutral-variant')


    surfacelight = light_theme.get('surface', '#FFFFFF')
    primarylight = light_theme.get('primary', '#FFFFFF')
    neutrallight = neutral.get('40', '#FFFFFF')
    neutralvariantlight = neutral.get('40', '#A0A0A0')
    secondarylight = light_theme.get('secondary', '#B0B0B0')
    tertiarylight = light_theme.get('tertiary', '#C0C0C0')
    errorlight = light_theme.get('error', '#D0D0D0')
    
    surfacedark = dark_theme.get('surface', '#121212')
    primarydark = dark_theme.get('primary', '#121212')
    neutraldark = neutral.get('80', '#121212')
    neutralvariantdark = neutralvariant.get('80', '#707070')
    secondarydark = dark_theme.get('secondary', '#606060')
    tertiarydark = dark_theme.get('tertiary', '#505050')
    errordark = dark_theme.get('error', '#404040')
    
    css_lines = []
    # Light surfaces
    css_lines.extend(get_surfaces(surfacelight, neutrallight, opacity_surface_light, 'theme-ref-elevation-surface-neutral', 'light'))
    css_lines.extend(get_surfaces(surfacelight, neutralvariantlight, opacity_surface_light, 'theme-ref-elevation-surface-neutral-variant', 'light'))
    css_lines.extend(get_surfaces(surfacelight, primarylight, opacity_surface_light, 'theme-ref-elevation-surface-primary', 'light'))
    css_lines.extend(get_surfaces(surfacelight, secondarylight, opacity_surface_light, 'theme-ref-elevation-surface-secondary', 'light'))
    css_lines.extend(get_surfaces(surfacelight, tertiarylight, opacity_surface_light, 'theme-ref-elevation-surface-tertiary', 'light'))
    css_lines.extend(get_surfaces(surfacelight, errorlight, opacity_surface_light, 'theme-ref-elevation-surface-error', 'light'))
    
    # Dark surfaces
    css_lines.extend(get_surfaces(surfacedark, neutraldark, opacity_surface_dark, 'theme-ref-elevation-surface-neutral', 'dark'))
    css_lines.extend(get_surfaces(surfacedark, neutralvariantdark, opacity_surface_dark, 'theme-ref-elevation-surface-neutral-variant', 'dark'))
    css_lines.extend(get_surfaces(surfacedark, primarydark, opacity_surface_dark, 'theme-ref-elevation-surface-primary', 'dark'))
    css_lines.extend(get_surfaces(surfacedark, secondarydark, opacity_surface_dark, 'theme-ref-elevation-surface-secondary', 'dark'))
    css_lines.extend(get_surfaces(surfacedark, tertiarydark, opacity_surface_dark, 'theme-ref-elevation-surface-tertiary', 'dark'))
    css_lines.extend(get_surfaces(surfacedark, errordark, opacity_surface_dark, 'theme-ref-elevation-surface-error', 'dark'))
    
    return css_lines

def get_gradient_value(arg_color_a, arg_color_b, arg_value):
    def hex_to_rgba(hex_color):
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)] + [255]
    
    def pad_zero(value):
        return f'{value:02x}'
    
    result_color_a = hex_to_rgba(arg_color_a)
    result_color_b = hex_to_rgba(arg_color_b)
    
    v1 = 1 - arg_value
    v2 = arg_value
    r_dec = int((result_color_a[0] * v1) + (result_color_b[0] * v2))
    g_dec = int((result_color_a[1] * v1) + (result_color_b[1] * v2))
    b_dec = int((result_color_a[2] * v1) + (result_color_b[2] * v2))
    a_dec = int((result_color_a[3] * v1) + (result_color_b[3] * v2))
    
    return f"#{pad_zero(r_dec)}{pad_zero(g_dec)}{pad_zero(b_dec)}{pad_zero(a_dec)}"

def json_to_css(json_file, css_file):
    with open(json_file, 'r') as infile:
        data = json.load(infile)
    fixed_error_scheme = {"error": {
          "0": "#000000",
          "10": "#410002",
          "20": "#690005",
          "30": "#93000A",
          "40": "#B81F1E",
          "50": "#BA1B1B",
          "60": "#FF5449",
          "70": "#FF897D",
          "80": "#FFB4AB",
          "90": "#FFDAD6",
          "95": "#FFEDEA",
          "99": "#FFFBFF",
          "100": "#FFFFFF"
        }
    }
    css_lines = []
    
    palettes = data.get('palettes', {});
    palettes.update(fixed_error_scheme);

    for palette_name, variants in palettes.items():
        for variant, color in variants.items():
            rgb = hex_to_rgb(color)
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")
        for variant in [45, 55, 65, 75, 85]:
            color = get_gradient_value(variants[str(variant-5)], variants[str(variant+5)], 0.5)
            rgb = hex_to_rgb(color)
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")
        if palette_name in ['error']:
            for variant in [5, 15, 25, 35]:
              color = get_gradient_value(variants[str(variant-5)], variants[str(variant+5)], 0.5)
              rgb = hex_to_rgb(color)
              css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
              css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")
        for variant in [7]:
            color = get_gradient_value(variants['0'], variants['10'], 0.7)
            rgb = hex_to_rgb(color)
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")
        for variant in [92]:
            color = get_gradient_value(variants['90'], variants['95'], 0.5)
            rgb = hex_to_rgb(color)
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")
        for variant in [97]:
            color = get_gradient_value(variants['95'], variants['99'], 0.5)
            rgb = hex_to_rgb(color)
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}: rgb({rgb})")
            css_lines.append(f"theme-ref-palette-{palette_name}{variant}-rgb: {rgb}")    

    css_lines.extend(generate_surface_colors(data))
    
    with open(css_file, 'w') as outfile:
        outfile.write("\n".join(css_lines))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert JSON theme to CSS.')
    parser.add_argument('input_file', help='Path to input JSON file')
    parser.add_argument('output_file', help='Path to output CSS file')
    args = parser.parse_args()
    
    json_to_css(args.input_file, args.output_file)
