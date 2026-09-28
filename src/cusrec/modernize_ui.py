#!/usr/bin/env python3
"""
Modern UI upgrade for TWRP — EverpalTweaks "Dual Slot Evergo Engine"
Builds on the OFOX DFox palette (#1e1f22 / #ed6f02) and elevates every
visual asset to a premium Material Design 3 / OFOX-inspired aesthetic.

Strategy
────────
• Buttons   → filled accent pill (not outline) — bolder, more tappable
• Slider    → modern capsule track + large glowing thumb with drop-shadow
• Sort      → slim Ionicons-style chevrons, no background box
• Progress  → ultra-thin 4 px pill, accent fill on dark track
• Navbar    → icon-only bar on a card surface with a soft top border
• Keyboard  → rounded key caps, slightly elevated secondary keys
• Spinner   → orange hue-shifted frames
• Logo      → regenerated with an "E" monogram + device name pill badge
"""

import os, colorsys, math
from PIL import Image, ImageDraw, ImageFont

IMGS = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'

# ─── Palette ───────────────────────────────────────────────────────────────
BG          = (0x1e, 0x1f, 0x22, 255)
BG_SURFACE  = (0x24, 0x25, 0x29, 255)      # slightly lighter card surface
BG_RAISED   = (0x2a, 0x2b, 0x30, 255)
ACCENT      = (0xed, 0x6f, 0x02, 255)
ACCENT_DK   = (0xd8, 0x61, 0x00, 255)
ACCENT_LT   = (0xff, 0x9a, 0x3c, 255)
WHITE       = (0xff, 0xff, 0xff, 255)
DIM         = (0x5f, 0x63, 0x68, 255)
NAVBAR_BG   = (0x18, 0x19, 0x1b, 255)
TRANSP      = (0,   0,   0,   0)

def a(color, alpha):
    return color[:3] + (alpha,)

def hex2rgba(h):
    h = h.lstrip('#')
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return (r, g, b, 255)

# ─── Helper: save ────────────────────────────────────────────────────────────
def save(img, name):
    img.save(f'{IMGS}/{name}')
    print(f'  ✔ {name}  {img.size}')

# ═══════════════════════════════════════════════════════════════════════════
# 1.  MAIN BUTTONS  —  solid filled accent, prominent rounded rect
# ═══════════════════════════════════════════════════════════════════════════
def make_button_filled(w, h, radius=24):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    # subtle drop-shadow layer  (semi-transparent rect offset by 4px)
    shadow_color = (0, 0, 0, 60)
    d.rounded_rectangle([(4, 6), (w-1, h-1)], radius=radius, fill=shadow_color)
    # main fill — accent
    d.rounded_rectangle([(0, 0), (w-5, h-5)], radius=radius, fill=ACCENT)
    # bright top-edge highlight for depth
    d.rounded_rectangle([(2, 2), (w-7, h//4)], radius=radius, fill=ACCENT_LT)
    return img

for fname, w, h in [
    ('main_button.png',                       504, 288),
    ('main_button_half_height.png',           504, 192),
    ('main_button_half_height_full_width.png',1008, 192),
]:
    with Image.open(f'{IMGS}/{fname}') as i:
        w, h = i.size
    save(make_button_filled(w, h), fname)

# ═══════════════════════════════════════════════════════════════════════════
# 2.  TAB BUTTONS  (tab_3 / tab_4)  —  glass-card surface
# ═══════════════════════════════════════════════════════════════════════════
for fname, w, h in [('tab_3.png',312,128), ('tab_4.png',225,128)]:
    with Image.open(f'{IMGS}/{fname}') as i:
        w, h = i.size
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    # card surface
    d.rounded_rectangle([(1, 1), (w-2, h-2)], radius=16,
                        fill=BG_SURFACE, outline=(0x3a,0x3b,0x40,180), width=1)
    save(img, fname)

# ═══════════════════════════════════════════════════════════════════════════
# 3.  SWIPE SLIDER
#     slider.png      — full-width EMPTY track (936 × 192)
#     slider_used.png — FILLED portion track (same size, accent)
#     slider_touch.png — draggable THUMB indicator (288 × 128)
# ═══════════════════════════════════════════════════════════════════════════
def pill_track(w, h, fill_color, border_color=None, track_h=8):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    pad = (h - track_h) // 2
    bc  = border_color or fill_color
    d.rounded_rectangle([(0, pad), (w-1, pad+track_h-1)],
                        radius=track_h, fill=fill_color, outline=bc, width=1)
    return img

def glowing_thumb(w, h):
    img  = Image.new('RGBA', (w, h), TRANSP)
    d    = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    r = min(cx, cy) - 8
    # outer glow ring
    for dr in range(10, 0, -1):
        alpha = int(120 * (1 - dr/10))
        d.ellipse([(cx-r-dr, cy-r-dr), (cx+r+dr, cy+r+dr)],
                  fill=(0xed, 0x6f, 0x02, alpha))
    # main circle — ACCENT
    d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=ACCENT)
    # inner highlight
    hr = r - 8
    d.ellipse([(cx-hr, cy-r+4), (cx+hr, cy-r+4+hr)],
              fill=a(ACCENT_LT, 160))
    return img

with Image.open(f'{IMGS}/slider.png')      as i: sw, sh = i.size
with Image.open(f'{IMGS}/slider_used.png') as i: uw, uh = i.size
with Image.open(f'{IMGS}/slider_touch.png')as i: tw, th = i.size

save(pill_track(sw, sh, (0x2e, 0x2f, 0x34, 255), (0x40, 0x41, 0x48, 255)), 'slider.png')
save(pill_track(uw, uh, ACCENT, ACCENT_DK),   'slider_used.png')
save(glowing_thumb(tw, th),                   'slider_touch.png')

# ═══════════════════════════════════════════════════════════════════════════
# 4.  HANDLE  (slidervalue — settings brightness/display sliders)
# ═══════════════════════════════════════════════════════════════════════════
with Image.open(f'{IMGS}/handle.png') as i: hw, hh = i.size
img = Image.new('RGBA', (hw, hh), TRANSP)
d   = ImageDraw.Draw(img)
cx, cy = hw//2, hh//2
r = min(cx, cy) - 4
for dr in range(6, 0, -1):
    d.ellipse([(cx-r-dr, cy-r-dr), (cx+r+dr, cy+r+dr)],
              fill=(0xed, 0x6f, 0x02, int(80*(1-dr/6))))
d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=WHITE)
d.ellipse([(cx-r+4, cy-r+4), (cx+r-4, cy+r-4)], fill=(0xd0,0xd0,0xd0,255))
save(img, 'handle.png')

# ═══════════════════════════════════════════════════════════════════════════
# 5.  PROGRESS BAR  (operation progress — 1080 × 9)
# ═══════════════════════════════════════════════════════════════════════════
with Image.open(f'{IMGS}/progress_empty.png') as i: pw, ph = i.size
save(pill_track(pw, ph, (0x2e,0x2f,0x34,255), None, track_h=max(4,ph-2)), 'progress_empty.png')
save(pill_track(pw, ph, ACCENT, ACCENT_DK,    track_h=max(4,ph-2)),        'progress_fill.png')

# ═══════════════════════════════════════════════════════════════════════════
# 6.  SORT ICONS  — slim Ionicons-style chevron + text label box
#     (312 × 128 each)
# ═══════════════════════════════════════════════════════════════════════════
def draw_chevron_up(d, x, y, size, color, thick=6):
    """Draw a ∧ chevron."""
    pts = [(x, y + size//2), (x + size//2, y), (x + size, y + size//2)]
    d.line(pts, fill=color, width=thick, joint='curve')

def draw_chevron_down(d, x, y, size, color, thick=6):
    pts = [(x, y), (x + size//2, y + size//2), (x + size, y)]
    d.line(pts, fill=color, width=thick, joint='curve')

for fname, draw_fn in [
    ('sort_asc.png',   draw_chevron_up),
    ('sort_desc.png',  draw_chevron_down),
]:
    with Image.open(f'{IMGS}/{fname}') as i: fw, fh = i.size
    img = Image.new('RGBA', (fw, fh), TRANSP)
    d   = ImageDraw.Draw(img)
    sz  = min(fh - 24, 48)
    cx, cy = fw//2, fh//2
    draw_fn(d, cx - sz//2, cy - sz//4, sz, WHITE, thick=5)
    save(img, fname)

# sort_empty — just a ghost minus-line (unsorted state)
with Image.open(f'{IMGS}/sort_empty.png') as i: fw, fh = i.size
img = Image.new('RGBA', (fw, fh), TRANSP)
d   = ImageDraw.Draw(img)
cy  = fh//2
d.line([(fw//4, cy), (3*fw//4, cy)], fill=DIM, width=4)
save(img, 'sort_empty.png')

# ═══════════════════════════════════════════════════════════════════════════
# 7.  NAVBAR ICONS  — home / back / console (265 × 128 each)
#     Simple geometric icons drawn in WHITE on transparent
# ═══════════════════════════════════════════════════════════════════════════
def navbar_icon(w, h, draw_fn):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    draw_fn(d, w, h)
    return img

def draw_home(d, w, h):
    # House silhouette
    cx, top = w//2, 20
    bot = h - 20
    mid = (top + bot) // 2
    # roof
    d.polygon([(cx, top), (cx-50, mid), (cx+50, mid)], fill=WHITE)
    # body
    d.rectangle([(cx-35, mid), (cx+35, bot)], fill=WHITE)
    # door
    d.rectangle([(cx-14, mid+24), (cx+14, bot)], fill=BG[:3]+(255,))

def draw_back(d, w, h):
    # Left-pointing chevron
    cx, cy = w//2, h//2
    sz = 36
    pts = [(cx+sz//2, cy-sz), (cx-sz//2, cy), (cx+sz//2, cy+sz)]
    d.line(pts, fill=WHITE, width=7, joint='curve')

def draw_console(d, w, h):
    # Terminal ">" prompt
    cx, cy = w//2, h//2
    sz = 28
    pts = [(cx-sz//2, cy-sz//2), (cx+sz//2, cy), (cx-sz//2, cy+sz//2)]
    d.line(pts, fill=WHITE, width=7, joint='curve')
    # underscore cursor
    d.rectangle([(cx+4, cy+sz//2+4), (cx+sz, cy+sz//2+4+6)], fill=WHITE)

with Image.open(f'{IMGS}/home.png') as i: nw, nh = i.size
save(navbar_icon(nw, nh, draw_home),    'home.png')
save(navbar_icon(nw, nh, draw_back),    'back.png')
save(navbar_icon(nw, nh, draw_console), 'console.png')

# ═══════════════════════════════════════════════════════════════════════════
# 8.  KEYBOARD SPECIAL KEYS  (backspace / enter / shift / space)
#     All on transparent bg — single-colour icons
# ═══════════════════════════════════════════════════════════════════════════
def draw_backspace_icon(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    # left-pointing chevron + horizontal bar = ⌫
    pts = [(cx-20, cy-28), (cx-52, cy), (cx-20, cy+28)]
    d.line(pts, fill=WHITE, width=8, joint='curve')
    d.rectangle([(cx-52, cy-6), (cx+30, cy+6)], fill=WHITE)
    # ×
    d.line([(cx+4, cy-20), (cx+40, cy+20)], fill=WHITE, width=7)
    d.line([(cx+4, cy+20), (cx+40, cy-20)], fill=WHITE, width=7)
    return img

def draw_enter_icon(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    # ↵ arrow
    d.rectangle([(cx-50, cy-6), (cx+40, cy+6)], fill=WHITE)
    d.rectangle([(cx+32, cy-30), (cx+40+8, cy+6)], fill=WHITE)
    pts = [(cx-50+6, cy-24), (cx-50-6, cy), (cx-50+6, cy+24)]
    d.line(pts, fill=WHITE, width=8, joint='curve')
    return img

def draw_shift_icon(w, h, filled=False):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy = w//2, h//2
    color = ACCENT if filled else WHITE
    # ⇧ arrow (upward triangle + stem)
    d.polygon([(cx, cy-46), (cx-42, cy+4), (cx+42, cy+4)], fill=color)
    d.rectangle([(cx-22, cy+4), (cx+22, cy+36)], fill=color)
    return img

def draw_space_icon(w, h):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cy = h//2
    # space bar — a flat pill
    d.rounded_rectangle([(w//8, cy-10), (7*w//8, cy+10)], radius=8, fill=DIM)
    return img

with Image.open(f'{IMGS}/backspace.png') as i: kw, kh = i.size
save(draw_backspace_icon(kw, kh), 'backspace.png')

with Image.open(f'{IMGS}/enter.png') as i: kw, kh = i.size
save(draw_enter_icon(kw, kh),    'enter.png')

with Image.open(f'{IMGS}/shift.png') as i: kw, kh = i.size
save(draw_shift_icon(kw, kh, False), 'shift.png')
save(draw_shift_icon(kw, kh, True),  'shift_fill.png')

with Image.open(f'{IMGS}/space.png') as i: kw, kh = i.size
save(draw_space_icon(kw, kh), 'space.png')

# ═══════════════════════════════════════════════════════════════════════════
# 9.  KEYBOARD ARROW KEYS  (154 × 96 each)
# ═══════════════════════════════════════════════════════════════════════════
ARROWS = {
    'kb_arrow_left.png':  [(-1,  0)],
    'kb_arrow_right.png': [( 1,  0)],
    'kb_arrow_up.png':    [( 0, -1)],
    'kb_arrow_down.png':  [( 0,  1)],
}
def draw_arrow(w, h, dx, dy):
    img = Image.new('RGBA', (w, h), TRANSP)
    d   = ImageDraw.Draw(img)
    cx, cy, s = w//2, h//2, 24
    # chevron in direction (dx, dy)
    if dx == -1:   pts = [(cx+s, cy-s),(cx-s, cy),(cx+s, cy+s)]
    elif dx == 1:  pts = [(cx-s, cy-s),(cx+s, cy),(cx-s, cy+s)]
    elif dy == -1: pts = [(cx-s, cy+s),(cx, cy-s),(cx+s, cy+s)]
    else:          pts = [(cx-s, cy-s),(cx, cy+s),(cx+s, cy-s)]
    d.line(pts, fill=WHITE, width=6, joint='curve')
    return img

for fname, dirs in ARROWS.items():
    dx, dy = dirs[0]
    with Image.open(f'{IMGS}/{fname}') as i: aw, ah = i.size
    save(draw_arrow(aw, ah, dx, dy), fname)

# ═══════════════════════════════════════════════════════════════════════════
# 10. LOGO  (184 × 256) — branded "E" monogram on OFOX-tinted background
# ═══════════════════════════════════════════════════════════════════════════
with Image.open(f'{IMGS}/logo.png') as i: lw, lh = i.size
logo = Image.new('RGBA', (lw, lh), TRANSP)
d    = ImageDraw.Draw(logo)

# Background pill / card
d.rounded_rectangle([(4, 4), (lw-4, lh-4)], radius=20,
                    fill=(0x1c,0x1d,0x20,230),
                    outline=ACCENT[:3]+(120,), width=2)

# Bold "E" letterform drawn as rectangles
cx, cy = lw//2, lh//2
ew, eh = 60, 90
ex, ey = cx - ew//2, cy - eh//2
lth = 10
d.rectangle([(ex, ey),          (ex+ew, ey+lth)],        fill=ACCENT)
d.rectangle([(ex, ey+eh//2-lth//2),(ex+ew*3//4, ey+eh//2+lth//2)], fill=ACCENT)
d.rectangle([(ex, ey+eh-lth),   (ex+ew, ey+eh)],         fill=ACCENT)
d.rectangle([(ex, ey),          (ex+lth, ey+eh)],        fill=ACCENT)

# Accent dot beneath
d.ellipse([(cx-6, cy+eh//2+14), (cx+6, cy+eh//2+26)], fill=ACCENT_LT)

save(logo, 'logo.png')

# ═══════════════════════════════════════════════════════════════════════════
# 11. FAB SELECT FOLDER button  (216 × 192) — accent circle with + icon
# ═══════════════════════════════════════════════════════════════════════════
with Image.open(f'{IMGS}/fab_selectfolder.png') as i: fw, fh = i.size
fab = Image.new('RGBA', (fw, fh), TRANSP)
d   = ImageDraw.Draw(fab)
cx, cy = fw//2, fh//2
r = min(cx, cy) - 12
# shadow
for dr in range(8, 0, -1):
    d.ellipse([(cx-r-dr+2, cy-r-dr+4), (cx+r+dr+2, cy+r+dr+4)],
              fill=(0,0,0, int(60*(1-dr/8))))
d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=ACCENT)
bar = 8
d.rectangle([(cx-bar//2, cy-28), (cx+bar//2, cy+28)], fill=WHITE)
d.rectangle([(cx-28, cy-bar//2), (cx+28, cy+bar//2)], fill=WHITE)
save(fab, 'fab_selectfolder.png')

# ═══════════════════════════════════════════════════════════════════════════
# 12. CURSOR  (48 × 48) — a slim accent bar
# ═══════════════════════════════════════════════════════════════════════════
with Image.open(f'{IMGS}/cursor.png') as i: cw, ch = i.size
img = Image.new('RGBA', (cw, ch), TRANSP)
d   = ImageDraw.Draw(img)
d.rectangle([(cw//2-2, 2), (cw//2+2, ch-2)], fill=ACCENT)
save(img, 'cursor.png')

# ═══════════════════════════════════════════════════════════════════════════
# 13. SPINNER hue-shift  (orange) — indeterminate001..012
# ═══════════════════════════════════════════════════════════════════════════
def hue_shift(src, target_hue=28.5/360.0):
    img  = Image.open(src).convert('RGBA')
    data = list(img.getdata())
    out  = []
    for r, g, b, a in data:
        if a < 20:
            out.append((r, g, b, a)); continue
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s > 0.06: h = target_hue
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        out.append((int(nr*255), int(ng*255), int(nb*255), a))
    img.putdata(out)
    return img

for i in range(1, 13):
    p = f'{IMGS}/indeterminate{i:03d}.png'
    if os.path.exists(p):
        hue_shift(p).save(p)
print(f'  ✔ indeterminate spinners hue-shifted')

print('\n✅  Full modern UI upgrade complete.')
