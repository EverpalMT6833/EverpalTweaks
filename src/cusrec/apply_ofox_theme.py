#!/usr/bin/env python3
"""
Apply OrangeFox DFox-identical theme to TWRP ramdisk.
Colors sourced pixel-perfect from OFOX Night/DFox theme:
  background:  #1e1f22
  accent:      #ed6f02
  text:        #FFFFFF
  dim text:    #5F6368
  highlight:   #1e1f2266
  linecolor:   #5F636844
  status bg:   #18191B
  title bg:    #1C1D20
  keyboard bg: #1e1f22
  keyboard dk: #1C1D20
"""
import os
import re
import shutil
from PIL import Image, ImageDraw

TWRP = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres'
OFOX  = '/root/Everpal/src/cusrec/ramdisks/ofox_extracted/twres'
TWRP_IMGS = f'{TWRP}/images'
OFOX_IMGS = f'{OFOX}/images'

# ── OFOX DFox exact palette ──────────────────────────────────────────────────
BG          = '#1e1f22'
ACCENT      = '#ed6f02'
ACCENT_DARK = '#D86100'
TEXT        = '#FFFFFF'
TEXT_DIM    = '#5F6368'
HIGHLIGHT   = '#1e1f2266'
HIGHLIGHT_F = '#11111144'
LINECOLOR   = '#5F636844'
STATUS_BG   = '#18191B'
TITLE_BG    = '#1C1D20'
KB_BG       = '#1e1f22'
KB_DARK     = '#1C1D20'
KB_HL       = '#1e1f2266'
TEXT_FAIL   = '#FF0101'
TEXT_OK     = '#68B60B'
WARNING     = '#FF6600'
TRANSPARENT = '#00000000'

# ─────────────────────────────────────────────────────────────────────────────
# 1.  Copy OFOX control assets directly into TWRP images
# ─────────────────────────────────────────────────────────────────────────────
COPY_MAP = {
    # (OFOX relative path, TWRP filename)
    'DFox/Controls/checkbox_true_d.png':    'checkbox_true.png',
    'Default/Controls/checkbox_false_d.png':'checkbox_false.png',
    'DFox/Controls/radio_true_d.png':       'radio_true.png',
    'Default/Controls/radio_false_d.png':   'radio_false.png',
    'DFox/Controls/handle.png':             'handle.png',
    'DFox/Controls/handle_h_classic.png':   'slider_touch.png',
    'Default/Progress/progress_empty.png':  'progress_empty.png',
    'Default/Progress/progress_fill.png':   'progress_fill.png',
}

for ofox_rel, twrp_name in COPY_MAP.items():
    src = f'{OFOX_IMGS}/{ofox_rel}'
    dst = f'{TWRP_IMGS}/{twrp_name}'
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'  ✔ copied {ofox_rel} → {twrp_name}')
    else:
        print(f'  ✘ missing {src}')

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Re-generate main_button, half-height button, full-width button
#     to match OFOX btn_raised style: #1e1f22 fill + #ed6f02 border
# ─────────────────────────────────────────────────────────────────────────────
def make_button(path, w, h, fill=BG, border=ACCENT, radius=20, border_w=2):
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([(0,0),(w-1,h-1)], radius=radius,
                        fill=fill, outline=border, width=border_w)
    img.save(path)
    print(f'  ✔ generated {os.path.basename(path)} ({w}x{h})')

for fname in ['main_button.png', 'main_button_half_height.png',
              'main_button_half_height_full_width.png']:
    path = f'{TWRP_IMGS}/{fname}'
    with Image.open(path) as i:
        w, h = i.size
    make_button(path, w, h)

# ─────────────────────────────────────────────────────────────────────────────
# 3.  Re-generate slider (base track) to match OFOX slider_classic look
# ─────────────────────────────────────────────────────────────────────────────
def make_slider_track(path, w, h, fill, border, radius=999):
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d   = ImageDraw.Draw(img)
    lh  = max(8, h // 12)
    pad = (h - lh) // 2
    d.rounded_rectangle([(0, pad),(w-1, pad+lh-1)],
                        radius=radius, fill=fill, outline=border, width=1)
    img.save(path)

with Image.open(f'{TWRP_IMGS}/slider.png') as i:
    sw, sh = i.size
make_slider_track(f'{TWRP_IMGS}/slider.png',      sw, sh, fill='#2E2F33', border='#3E3F43')
with Image.open(f'{TWRP_IMGS}/slider_used.png') as i:
    sw, sh = i.size
make_slider_track(f'{TWRP_IMGS}/slider_used.png', sw, sh, fill=ACCENT,    border=ACCENT_DARK)
print(f'  ✔ generated slider tracks')

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Re-colour tab_3 / tab_4 (button-width background bars) → OFOX card style
# ─────────────────────────────────────────────────────────────────────────────
for fname in ['tab_3.png', 'tab_4.png']:
    path = f'{TWRP_IMGS}/{fname}'
    with Image.open(path) as i:
        w, h = i.size
    img = Image.new('RGBA', (w, h), (0,0,0,0))
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([(0,0),(w-1,h-1)], radius=12,
                        fill='#2A2B2F', outline='#3A3B40', width=1)
    img.save(path)
print(f'  ✔ recoloured tab buttons')

# ─────────────────────────────────────────────────────────────────────────────
# 5.  Progress-bar indeterminate spinner — hue-shift cyan→orange in TWRP set
# ─────────────────────────────────────────────────────────────────────────────
import colorsys

def hueshift_image(src_path, dst_path, target_hue=28.5/360.0):
    img = Image.open(src_path).convert('RGBA')
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        if a < 20:
            new_data.append((r, g, b, a))
            continue
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s > 0.08:
            h = target_hue
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        new_data.append((int(nr*255), int(ng*255), int(nb*255), a))
    img.putdata(new_data)
    img.save(dst_path)

for i in range(1, 13):
    fname = f'indeterminate{i:03d}.png'
    path  = f'{TWRP_IMGS}/{fname}'
    if os.path.exists(path):
        hueshift_image(path, path)
print(f'  ✔ hue-shifted indeterminate spinner frames')

# ─────────────────────────────────────────────────────────────────────────────
# 6.  Patch ui.xml — replace ALL color variables with OFOX equivalents
# ─────────────────────────────────────────────────────────────────────────────
ui_path = f'{TWRP}/ui.xml'
with open(ui_path, 'r') as f:
    ui = f.read()

# Colour variable map (name → new_value)
COLOR_VARS = {
    'background_color':             BG,
    'accent_color':                 ACCENT,
    'accent_color_semitransparent': f'{ACCENT}30',
    'text_color':                   TEXT,
    'text_button_color':            TEXT,
    'text_success_color':           TEXT_OK,
    'text_fail_color':              TEXT_FAIL,
    'highlight_color':              '#2A2B30',
    'caps_highlight_color':         f'{ACCENT}40',
    'transparent':                  TRANSPARENT,
    'semi_transparent':             '#00000099',
    'warning':                      WARNING,
    'error':                        TEXT_FAIL,
    'highlight':                    ACCENT,
    'fileselector_linecolor':       '#2E2F34',
    'fileselector_highlight_color': '#28292E',
    'fileselector_separatorheight': '2',
}

def set_var(xml, name, value):
    pattern = rf'(<variable name="{re.escape(name)}" value=")[^"]*(")'
    replacement = rf'\g<1>{value}\g<2>'
    return re.sub(pattern, replacement, xml)

for name, value in COLOR_VARS.items():
    ui = set_var(ui, name, value)

# ── Fix navbar background: pure OFOX uses #18191B, not #000000 ──────────────
ui = re.sub(r'<fill color="#000000">\s*<condition var1="tw_busy" var2="0"/>\s*<placement x="0" y="%navbar_y%"',
            f'<fill color="{STATUS_BG}">\n\t\t\t\t<condition var1="tw_busy" var2="0"/>\n\t\t\t\t<placement x="0" y="%navbar_y%"',
            ui)

# ── Fix header: OFOX uses a darker header bg, thin accent underline ──────────
ui = re.sub(
    r'<fill color="#050505">\s*<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\s*</fill>\s*<fill color="%accent_color%">\s*<placement x="0" y="252" w="%screen_width%" h="4"/>\s*</fill>',
    f'<fill color="{TITLE_BG}">\n\t\t\t\t<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\n\t\t\t</fill>\n\t\t\t<fill color="%accent_color%">\n\t\t\t\t<placement x="0" y="252" w="%screen_width%" h="3"/>\n\t\t\t</fill>',
    ui
)

# ── Fix any leftover OLED-black accent header remnants (safety pass) ─────────
ui = re.sub(
    r'<fill color="#050505">\s*<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\s*</fill>',
    f'<fill color="{TITLE_BG}">\n\t\t\t\t<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\n\t\t\t</fill>',
    ui
)

# ── Fix tab bars: OFOX uses a slightly lighter bg, NOT solid accent ──────────
ui = re.sub(
    r'<fill color="#08080A">\s*<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>\s*</fill>\s*<fill color="%accent_color%">\s*<placement x="0" y="350" w="%screen_width%" h="2"/>\s*</fill>',
    f'<fill color="{STATUS_BG}">\n\t\t\t\t<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>\n\t\t\t</fill>\n\t\t\t<fill color="%accent_color%">\n\t\t\t\t<placement x="0" y="350" w="%screen_width%" h="2"/>\n\t\t\t</fill>',
    ui
)

# ── Keyboard colours → OFOX Night keyboard ───────────────────────────────────
# background
ui = ui.replace('<background color="#000000"/>', f'<background color="{KB_BG}"/>')
# key alphanumeric
ui = re.sub(r'<key-alphanumeric color="#111111"', f'<key-alphanumeric color="{KB_DARK}"', ui)
ui = re.sub(r'<key-other color="#151515"',         f'<key-other color="{KB_BG}"',           ui)
# key text colours
ui = ui.replace('textcolor="#EEEEEE"', 'textcolor="#FFFFFF"')
ui = ui.replace('textcolor="#888888"', f'textcolor="{TEXT_DIM}"')
# keyboard ctrl highlight
ui = re.sub(r'<ctrlhighlight color="#FF7A0080"/>',
            f'<ctrlhighlight color="{ACCENT}80"/>', ui)

# ── Status bar: transparent overlay to match OFOX ───────────────────────────
ui = ui.replace('<fill color="#00000000">', '<fill color="#00000033">')

with open(ui_path, 'w') as f:
    f.write(ui)
print(f'  ✔ ui.xml fully patched with OFOX colour map')

# ─────────────────────────────────────────────────────────────────────────────
# 7.  Patch portrait.xml — fix any remaining hardcoded #000000 navbar fills
# ─────────────────────────────────────────────────────────────────────────────
portrait_path = f'{TWRP}/portrait.xml'
with open(portrait_path, 'r') as f:
    portrait = f.read()

# Replace hardcoded #000000 slideout backgrounds
portrait = portrait.replace('<fill color="#000000">', f'<fill color="{STATUS_BG}">')

with open(portrait_path, 'w') as f:
    f.write(portrait)
print(f'  ✔ portrait.xml hardcoded fills patched')

print('\n✅  OFOX DFox theme fully applied to TWRP ramdisk.')
