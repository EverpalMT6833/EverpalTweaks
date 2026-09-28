#!/usr/bin/env python3
"""
EverpalTweaks TWRP — Material 3 Green Edition
Palette seed: #006200  (deep forest green)

Material You tonal palette derived from #006200:
  Primary         #006200   → main accent (buttons, active tabs, slider)
  Primary bright  #00A300   → glow, highlight, lighter fills
  Primary dim     #004800   → pressed/dark variant
  Primary tint    #00E676   → success / active state ring
  On-primary      #FFFFFF

  Background      #0D110D   → OLED-friendly near-black w/ green tint
  Surface 1       #131813   → base card surface
  Surface 2       #192019   → slightly elevated card
  Surface 3       #1E281E   → further elevated / tab bar
  Outline         #2A3D2A   → subtle separator
  Outline bright  #3B5C3B   → active separator / border

  Text primary    #FFFFFF
  Text secondary  #8FA88F   → muted/secondary labels
  Text success    #00E676
  Text fail       #FF4444
  Warning         #FF9800
"""

import os, colorsys, re
from PIL import Image, ImageDraw

BASE = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres'
IMGS = f'{BASE}/images'

# ─── Palette (RGBA tuples) ────────────────────────────────────────────────────
BG         = (0x0D, 0x11, 0x0D, 255)
SURF1      = (0x13, 0x18, 0x13, 255)
SURF2      = (0x19, 0x20, 0x19, 255)
SURF3      = (0x1E, 0x28, 0x1E, 255)
OUTLINE    = (0x2A, 0x3D, 0x2A, 255)
OUTLINE_BR = (0x3B, 0x5C, 0x3B, 255)

PRIMARY    = (0x00, 0x62, 0x00, 255)   # #006200
PRIMARY_BR = (0x00, 0xA3, 0x00, 255)   # #00A300 brighter
PRIMARY_DK = (0x00, 0x48, 0x00, 255)   # #004800 darker
PRIMARY_TT = (0x00, 0xE6, 0x76, 255)   # #00E676 tint/glow
ON_PRIMARY = (0xFF, 0xFF, 0xFF, 255)

TEXT       = (0xFF, 0xFF, 0xFF, 255)
TEXT_DIM   = (0x8F, 0xA8, 0x8F, 255)
TEXT_FAIL  = (0xFF, 0x44, 0x44, 255)
TEXT_OK    = (0x00, 0xE6, 0x76, 255)
WARNING    = (0xFF, 0x98, 0x00, 255)
TRANSP     = (0,   0,   0,   0  )

def a(rgba, alpha):
    return rgba[:3] + (alpha,)

def rgb_hex(rgba):
    return '#{:02X}{:02X}{:02X}'.format(*rgba[:3])

def save(img, name):
    img.save(f'{IMGS}/{name}')
    print(f'  ✔  {name}  {img.size}')

# ─────────────────────────────────────────────────────────────────────────────
# 1. ui.xml  — replace ALL colour variables with green M3 palette
# ─────────────────────────────────────────────────────────────────────────────
ui_path = f'{BASE}/ui.xml'
with open(ui_path) as f:
    ui = f.read()

def set_var(xml, name, val):
    return re.sub(
        rf'(<variable name="{re.escape(name)}" value=")[^"]*(")',
        rf'\g<1>{val}\g<2>', xml)

VAR_MAP = {
    'background_color':             rgb_hex(BG),
    'accent_color':                 rgb_hex(PRIMARY),
    'accent_color_semitransparent': rgb_hex(PRIMARY) + '30',
    'text_color':                   rgb_hex(TEXT),
    'text_button_color':            rgb_hex(TEXT),
    'text_success_color':           rgb_hex(TEXT_OK),
    'text_fail_color':              rgb_hex(TEXT_FAIL),
    'highlight_color':              rgb_hex(SURF3),
    'caps_highlight_color':         rgb_hex(PRIMARY) + '40',
    'transparent':                  '#00000000',
    'semi_transparent':             '#00000099',
    'warning':                      rgb_hex(WARNING),
    'error':                        rgb_hex(TEXT_FAIL),
    'highlight':                    rgb_hex(PRIMARY),
    'fileselector_linecolor':       rgb_hex(OUTLINE),
    'fileselector_highlight_color': rgb_hex(SURF2),
    'fileselector_separatorheight': '2',
}
for name, val in VAR_MAP.items():
    ui = set_var(ui, name, val)

# ── Header: dark surface card + 3px green accent underline ───────────────────
ui = re.sub(
    r'<fill color="[^"]+">[\s\n\r\t]*<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>[\s\n\r\t]*</fill>[\s\n\r\t]*<fill color="%accent_color%">[\s\n\r\t]*<placement x="0" y="252" w="%screen_width%" h="\d+"/>[\s\n\r\t]*</fill>',
    f'<fill color="{rgb_hex(SURF1)}">\n\t\t\t\t<placement x="0" y="0" w="%screen_width%" h="%header_height%"/>\n\t\t\t</fill>\n\t\t\t<fill color="%accent_color%">\n\t\t\t\t<placement x="0" y="252" w="%screen_width%" h="3"/>\n\t\t\t</fill>',
    ui)

# ── Tab bars ─────────────────────────────────────────────────────────────────
ui = re.sub(
    r'<fill color="[^"]+">[\s\n\r\t]*<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>[\s\n\r\t]*</fill>[\s\n\r\t]*<fill color="%accent_color%">[\s\n\r\t]*<placement x="0" y="350" w="%screen_width%" h="\d+"/>[\s\n\r\t]*</fill>',
    f'<fill color="{rgb_hex(SURF2)}">\n\t\t\t\t<placement x="0" y="%row1_y%" w="%screen_width%" h="%tab_height%"/>\n\t\t\t</fill>\n\t\t\t<fill color="%accent_color%">\n\t\t\t\t<placement x="0" y="350" w="%screen_width%" h="2"/>\n\t\t\t</fill>',
    ui)

# ── Navbar background ────────────────────────────────────────────────────────
ui = re.sub(
    r'<fill color="[^"]+">\s*\n\s*<condition var1="tw_busy" var2="0"/>\s*\n\s*<placement x="0" y="%navbar_y%"',
    f'<fill color="{rgb_hex(SURF1)}">\n\t\t\t\t<condition var1="tw_busy" var2="0"/>\n\t\t\t\t<placement x="0" y="%navbar_y%"', ui)

# ── Status bar semi-transparent overlay ─────────────────────────────────────
ui = ui.replace('<fill color="#00000033">', '<fill color="#00000044">')

# ── Keyboard ─────────────────────────────────────────────────────────────────
ui = re.sub(r'<background color="[^"]+"/>',
            f'<background color="{rgb_hex(SURF1)}"/>', ui)
ui = re.sub(r'<key-alphanumeric color="[^"]+"',
            f'<key-alphanumeric color="{rgb_hex(SURF2)}"', ui)
ui = re.sub(r'<key-other color="[^"]+"',
            f'<key-other color="{rgb_hex(SURF3)}"', ui)
ui = ui.replace('textcolor="#FFFFFF"', 'textcolor="#FFFFFF"')
ui = re.sub(r'textcolor="[^"]*5[Ff]6368[^"]*"', f'textcolor="{rgb_hex(TEXT_DIM)}"', ui)
ui = re.sub(r'<ctrlhighlight color="[^"]+"/>',
            f'<ctrlhighlight color="{rgb_hex(PRIMARY)}80"/>', ui)

with open(ui_path, 'w') as f:
    f.write(ui)
print(f'  ✔  ui.xml → green M3 palette')

# ── portrait.xml hardcoded fills ─────────────────────────────────────────────
portrait_path = f'{BASE}/portrait.xml'
with open(portrait_path) as f:
    port = f.read()
port = re.sub(r'<fill color="#[0-9A-Fa-f]{6}">', f'<fill color="{rgb_hex(SURF1)}">', port)
with open(portrait_path, 'w') as f:
    f.write(port)
print(f'  ✔  portrait.xml → green surface')

# ─────────────────────────────────────────────────────────────────────────────
# 2. MAIN BUTTONS  — M3 filled pill (solid PRIMARY, full-pill radius)
#    Text will render on top by TWRP engine — button is just the background shape
# ─────────────────────────────────────────────────────────────────────────────
def m3_button(w, h, fill=PRIMARY, glow=True, radius=None):
    r = radius if radius is not None else min(h // 2, 36)
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    # Subtle drop shadow
    d.rounded_rectangle([(3, 5), (w-1, h-1)], radius=r,
                        fill=(0, 0, 0, 50))
    # Main fill
    d.rounded_rectangle([(0, 0), (w-4, h-4)], radius=r, fill=fill)
    # Top-left gloss for depth (M3 tonal surface)
    if glow:
        gloss = Image.new('RGBA', (w, h), TRANSP)
        gd    = ImageDraw.Draw(gloss)
        gd.rounded_rectangle([(0, 0), (w-4, h//3)], radius=r,
                             fill=a(PRIMARY_BR, 50))
        img = Image.alpha_composite(img, gloss)
    return img

for fname in ['main_button.png', 'main_button_half_height.png',
              'main_button_half_height_full_width.png']:
    with Image.open(f'{IMGS}/{fname}') as i: w, h = i.size
    save(m3_button(w, h), fname)

# ─────────────────────────────────────────────────────────────────────────────
# 3. TAB BUTTONS  — M3 secondary container card
# ─────────────────────────────────────────────────────────────────────────────
for fname in ['tab_3.png', 'tab_4.png']:
    with Image.open(f'{IMGS}/{fname}') as i: w, h = i.size
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([(1, 1), (w-2, h-2)], radius=18,
                        fill=SURF2, outline=OUTLINE_BR, width=1)
    save(img, fname)

# ─────────────────────────────────────────────────────────────────────────────
# 4. SWIPE SLIDER  — M3 pill track + glowing thumb
# ─────────────────────────────────────────────────────────────────────────────
def pill_track(w, h, fill, border, th=8):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    pad = (h - th) // 2
    d.rounded_rectangle([(0, pad), (w-1, pad+th-1)],
                        radius=th, fill=fill, outline=border, width=1)
    return img

def m3_thumb(w, h):
    """Glowing pill thumb — M3 style."""
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    r = min(cx, cy) - 6
    # glow rings
    for dr in range(12, 0, -1):
        alpha = int(100 * (1 - dr/12))
        d.ellipse([(cx-r-dr, cy-r-dr), (cx+r+dr, cy+r+dr)],
                  fill=a(PRIMARY_BR, alpha))
    # solid fill
    d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=PRIMARY)
    # inner highlight
    hr = r - 10
    d.ellipse([(cx-hr, cy-r+6), (cx+hr, cy-r+6+hr)],
              fill=a(PRIMARY_BR, 160))
    return img

with Image.open(f'{IMGS}/slider.png')       as i: sw, sh = i.size
with Image.open(f'{IMGS}/slider_used.png')  as i: uw, uh = i.size
with Image.open(f'{IMGS}/slider_touch.png') as i: tw, th = i.size

save(pill_track(sw, sh, SURF3, OUTLINE),         'slider.png')
save(pill_track(uw, uh, PRIMARY, PRIMARY_DK),    'slider_used.png')
save(m3_thumb(tw, th),                           'slider_touch.png')

# ─────────────────────────────────────────────────────────────────────────────
# 5. HANDLE  (settings sliders)
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/handle.png') as i: hw, hh = i.size
img = Image.new('RGBA', (hw, hh), TRANSP)
d   = ImageDraw.Draw(img)
cx, cy = hw//2, hh//2
r = min(cx, cy) - 4
for dr in range(8, 0, -1):
    d.ellipse([(cx-r-dr, cy-r-dr), (cx+r+dr, cy+r+dr)],
              fill=a(PRIMARY_BR, int(80*(1-dr/8))))
d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=TEXT)
d.ellipse([(cx-r+5, cy-r+5), (cx+r-5, cy+r-5)], fill=(0xCC,0xCC,0xCC,255))
save(img, 'handle.png')

# ─────────────────────────────────────────────────────────────────────────────
# 6. PROGRESS BAR  — ultra-thin M3 linear progress
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/progress_empty.png') as i: pw, ph = i.size
track_h = max(4, ph - 2)
save(pill_track(pw, ph, SURF3, OUTLINE, th=track_h),         'progress_empty.png')
save(pill_track(pw, ph, PRIMARY, PRIMARY_DK, th=track_h),    'progress_fill.png')

# ─────────────────────────────────────────────────────────────────────────────
# 7. CHECKBOXES  — M3 style: rounded-square, accent fill when checked
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/checkbox_false.png') as i: cbw, cbh = i.size

def m3_checkbox(w, h, checked):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    m   = 4
    r   = 8
    if checked:
        d.rounded_rectangle([(m,m),(w-m,h-m)], radius=r, fill=PRIMARY)
        # checkmark
        cx, cy = w//2, h//2
        d.line([(cx-10, cy),(cx-2, cy+9),(cx+12, cy-9)],
               fill=TEXT, width=5)
    else:
        d.rounded_rectangle([(m,m),(w-m,h-m)], radius=r,
                            fill=SURF3, outline=OUTLINE_BR, width=2)
    return img

save(m3_checkbox(cbw, cbh, False), 'checkbox_false.png')
save(m3_checkbox(cbw, cbh, True),  'checkbox_true.png')

# ─────────────────────────────────────────────────────────────────────────────
# 8. RADIO BUTTONS  — M3 style circles
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/radio_false.png') as i: rw, rh = i.size

def m3_radio(w, h, checked):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    m   = 4
    cx, cy = w//2, h//2
    r  = min(cx,cy) - m
    if checked:
        d.ellipse([(cx-r, cy-r),(cx+r, cy+r)],
                  fill=SURF3, outline=PRIMARY, width=3)
        ir = r - 10
        d.ellipse([(cx-ir, cy-ir),(cx+ir, cy+ir)], fill=PRIMARY)
    else:
        d.ellipse([(cx-r, cy-r),(cx+r, cy+r)],
                  fill=SURF3, outline=OUTLINE_BR, width=2)
    return img

save(m3_radio(rw, rh, False), 'radio_false.png')
save(m3_radio(rw, rh, True),  'radio_true.png')

# ─────────────────────────────────────────────────────────────────────────────
# 9. SORT ICONS  — slim chevrons on transparent
# ─────────────────────────────────────────────────────────────────────────────
def sort_icon(w, h, direction):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy, s = w//2, h//2, 22
    if direction == 'asc':
        pts = [(cx-s, cy+s//2), (cx, cy-s//2), (cx+s, cy+s//2)]
    elif direction == 'desc':
        pts = [(cx-s, cy-s//2), (cx, cy+s//2), (cx+s, cy-s//2)]
    else:
        d.line([(cx-s, cy), (cx+s, cy)], fill=TEXT_DIM, width=4)
        return img
    d.line(pts, fill=TEXT, width=5, joint='curve')
    return img

with Image.open(f'{IMGS}/sort_asc.png') as i: sw2, sh2 = i.size
save(sort_icon(sw2, sh2, 'asc'),   'sort_asc.png')
save(sort_icon(sw2, sh2, 'desc'),  'sort_desc.png')
save(sort_icon(sw2, sh2, 'empty'), 'sort_empty.png')

# ─────────────────────────────────────────────────────────────────────────────
# 10. NAVBAR ICONS  — geometric, rounded M3 style
# ─────────────────────────────────────────────────────────────────────────────
def navbar(w, h, draw_fn):
    img = Image.new('RGBA', (w, h), TRANSP)
    draw_fn(ImageDraw.Draw(img), w, h)
    return img

def home_fn(d, w, h):
    cx, top, bot = w//2, 18, h - 18
    mid = top + (bot - top) * 44 // 100
    # roof — filled triangle
    d.polygon([(cx, top), (cx-46, mid+2), (cx+46, mid+2)], fill=TEXT)
    # body
    d.rounded_rectangle([(cx-32, mid), (cx+32, bot)], radius=6, fill=TEXT)
    # door cutout
    d.rounded_rectangle([(cx-13, mid+22), (cx+13, bot)], radius=4,
                        fill=BG[:3]+(255,))

def back_fn(d, w, h):
    cx, cy = w//2, h//2
    pts = [(cx+30, cy-28), (cx-16, cy), (cx+30, cy+28)]
    d.line(pts, fill=TEXT, width=7, joint='curve')

def console_fn(d, w, h):
    cx, cy = w//2, h//2
    # > prompt chevron
    pts = [(cx-22, cy-26), (cx+14, cy), (cx-22, cy+26)]
    d.line(pts, fill=TEXT, width=7, joint='curve')
    # underscore
    d.rounded_rectangle([(cx+4, cy+20), (cx+30, cy+26)], radius=3, fill=TEXT)

with Image.open(f'{IMGS}/home.png') as i: nw, nh = i.size
save(navbar(nw, nh, home_fn),    'home.png')
save(navbar(nw, nh, back_fn),    'back.png')
save(navbar(nw, nh, console_fn), 'console.png')

# ─────────────────────────────────────────────────────────────────────────────
# 11. KEYBOARD SPECIAL KEYS
# ─────────────────────────────────────────────────────────────────────────────
def key_backspace(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    # ← shaft
    d.rectangle([(cx-46, cy-5), (cx+32, cy+5)], fill=TEXT)
    # arrowhead
    d.polygon([(cx-46, cy), (cx-22, cy-22), (cx-22, cy+22)], fill=TEXT)
    # × mark on right half
    ox, s = cx+10, 16
    d.line([(ox-s, cy-s),(ox+s, cy+s)], fill=TEXT, width=5)
    d.line([(ox-s, cy+s),(ox+s, cy-s)], fill=TEXT, width=5)
    return img

def key_enter(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    # horizontal shaft
    d.rectangle([(cx-40, cy-5), (cx+40, cy+5)], fill=TEXT)
    # vertical drop on right
    d.rectangle([(cx+35, cy-30), (cx+40, cy+5)], fill=TEXT)
    # arrowhead left
    d.polygon([(cx-40, cy), (cx-18, cy-18), (cx-18, cy+18)], fill=TEXT)
    return img

def key_shift(w, h, active=False):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    col = PRIMARY if active else TEXT
    # ⇧ upward arrow
    d.polygon([(cx, cy-42), (cx-38, cy-2), (cx+38, cy-2)], fill=col)
    d.rounded_rectangle([(cx-20, cy-2), (cx+20, cy+34)], radius=4, fill=col)
    return img

def key_space(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cy  = h // 2
    d.rounded_rectangle([(w//8, cy-10), (7*w//8, cy+10)],
                        radius=10, fill=TEXT_DIM)
    return img

def key_arrow(w, h, dx, dy):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy, s = w//2, h//2, 22
    if   dx == -1: pts = [(cx+s,cy-s),(cx-s,cy),(cx+s,cy+s)]
    elif dx ==  1: pts = [(cx-s,cy-s),(cx+s,cy),(cx-s,cy+s)]
    elif dy == -1: pts = [(cx-s,cy+s),(cx,cy-s),(cx+s,cy+s)]
    else:          pts = [(cx-s,cy-s),(cx,cy+s),(cx+s,cy-s)]
    d.line(pts, fill=TEXT, width=6, joint='curve')
    return img

with Image.open(f'{IMGS}/backspace.png') as i: kw, kh = i.size
save(key_backspace(kw, kh), 'backspace.png')
with Image.open(f'{IMGS}/enter.png') as i: kw, kh = i.size
save(key_enter(kw, kh), 'enter.png')
with Image.open(f'{IMGS}/shift.png') as i: kw, kh = i.size
save(key_shift(kw, kh, False), 'shift.png')
save(key_shift(kw, kh, True),  'shift_fill.png')
with Image.open(f'{IMGS}/space.png') as i: kw, kh = i.size
save(key_space(kw, kh), 'space.png')

ARROW_MAP = {'kb_arrow_left.png':(-1,0),'kb_arrow_right.png':(1,0),
             'kb_arrow_up.png':(0,-1),'kb_arrow_down.png':(0,1)}
for fname,(dx,dy) in ARROW_MAP.items():
    with Image.open(f'{IMGS}/{fname}') as i: aw, ah = i.size
    save(key_arrow(aw, ah, dx, dy), fname)

# ─────────────────────────────────────────────────────────────────────────────
# 12. LOGO  (184 × 256) — M3 card with "E" lettermark in green
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/logo.png') as i: lw, lh = i.size
logo = Image.new('RGBA', (lw, lh), TRANSP)
d    = ImageDraw.Draw(logo)

# outer glow
for dr in range(16, 0, -2):
    d.rounded_rectangle([(4-dr//2, 4-dr//2), (lw-4+dr//2, lh-4+dr//2)],
                        radius=24+dr//2,
                        fill=a(PRIMARY, int(25*(1-dr/16))))
# card bg
d.rounded_rectangle([(4, 4), (lw-4, lh-4)], radius=22,
                    fill=SURF2, outline=a(PRIMARY, 160), width=2)

# "E" letterform — thick slab strokes
ex, ey = lw//2 - 32, lh//2 - 48
ew, eh = 64, 96
lth = 12
bar_clr = PRIMARY
# vertical spine
d.rounded_rectangle([(ex, ey), (ex+lth, ey+eh)], radius=4, fill=bar_clr)
# top bar
d.rounded_rectangle([(ex, ey), (ex+ew, ey+lth)], radius=4, fill=bar_clr)
# mid bar (shorter — 3/4 width)
mid_y = ey + eh//2 - lth//2
d.rounded_rectangle([(ex, mid_y), (ex+ew*3//4, mid_y+lth)],
                    radius=4, fill=bar_clr)
# bottom bar
d.rounded_rectangle([(ex, ey+eh-lth), (ex+ew, ey+eh)], radius=4, fill=bar_clr)

# tiny "EverpalTweaks" pill badge at bottom
badge_y = ey + eh + 20
d.rounded_rectangle([(lw//2-46, badge_y), (lw//2+46, badge_y+22)],
                    radius=11, fill=PRIMARY_DK)
# "ET" text via dots — just a small green indicator dot
d.ellipse([(lw//2-5, badge_y+6), (lw//2+5, badge_y+16)],
          fill=PRIMARY_BR)

save(logo, 'logo.png')

# ─────────────────────────────────────────────────────────────────────────────
# 13. FAB  — M3 FAB with green + shadow
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/fab_selectfolder.png') as i: fw, fh = i.size
fab = Image.new('RGBA', (fw, fh), TRANSP)
d   = ImageDraw.Draw(fab)
cx, cy = fw//2, fh//2
r = min(cx, cy) - 10
# shadow
for dr in range(10, 0, -1):
    d.ellipse([(cx-r-dr+3, cy-r-dr+5),(cx+r+dr+3, cy+r+dr+5)],
              fill=(0,0,0, int(50*(1-dr/10))))
d.ellipse([(cx-r, cy-r),(cx+r, cy+r)], fill=PRIMARY)
# + icon
b = 8
d.rounded_rectangle([(cx-b//2, cy-28),(cx+b//2, cy+28)], radius=3, fill=TEXT)
d.rounded_rectangle([(cx-28, cy-b//2),(cx+28, cy+b//2)], radius=3, fill=TEXT)
save(fab, 'fab_selectfolder.png')

# ─────────────────────────────────────────────────────────────────────────────
# 14. CURSOR
# ─────────────────────────────────────────────────────────────────────────────
with Image.open(f'{IMGS}/cursor.png') as i: cw, ch = i.size
img = Image.new('RGBA', (cw, ch), TRANSP)
d   = ImageDraw.Draw(img)
d.rounded_rectangle([(cw//2-2, 2),(cw//2+2, ch-2)], radius=2, fill=PRIMARY)
save(img, 'cursor.png')

# ─────────────────────────────────────────────────────────────────────────────
# 15. SPINNER hue-shift → green (#006200 hue ≈ 120°)
# ─────────────────────────────────────────────────────────────────────────────
import colorsys

def hue_shift_green(src, target_hue=120/360.0):
    img  = Image.open(src).convert('RGBA')
    data = list(img.getdata())
    out  = []
    for r, g, b, a in data:
        if a < 20:
            out.append((r,g,b,a)); continue
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s > 0.06:
            h = target_hue
            # boost saturation for vivid green
            s = min(1.0, s * 1.2)
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        out.append((int(nr*255), int(ng*255), int(nb*255), a))
    img.putdata(out)
    return img

for i in range(1, 13):
    p = f'{IMGS}/indeterminate{i:03d}.png'
    if os.path.exists(p):
        hue_shift_green(p).save(p)
print('  ✔  indeterminate spinners → green')

print('\n✅  Material 3 Green Edition complete.')
