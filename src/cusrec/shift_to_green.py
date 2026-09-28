#!/usr/bin/env python3
"""
Hue-shift all TWRP PNG assets from orange to green (#006200).
"""
import os
import colorsys
from PIL import Image

IMGS = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'
GREEN_HUE = 120 / 360.0

def hue_shift_to_green(src_path):
    try:
        img = Image.open(src_path).convert('RGBA')
    except Exception as e:
        print(f"Skipping {src_path}: {e}")
        return False
        
    data = list(img.getdata())
    out = []
    changed = False
    
    for r, g, b, a in data:
        if a < 10:
            out.append((r, g, b, a))
            continue
            
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        # Only shift pixels that have some color (saturation > 0.05)
        # And are in the orange/red/yellow spectrum (hue < 60/360 or > 340/360)
        if s > 0.05 and (h < 60/360.0 or h > 340/360.0):
            h = GREEN_HUE
            changed = True
            nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
            out.append((int(nr*255), int(ng*255), int(nb*255), a))
        else:
            out.append((r, g, b, a))
            
    if changed:
        img.putdata(out)
        img.save(src_path)
        return True
    return False

if __name__ == '__main__':
    count = 0
    for fname in sorted(os.listdir(IMGS)):
        if fname.endswith('.png'):
            path = os.path.join(IMGS, fname)
            if hue_shift_to_green(path):
                print(f"  ✔ Shifted {fname}")
                count += 1
    print(f"✅ Shifted {count} images to green.")
