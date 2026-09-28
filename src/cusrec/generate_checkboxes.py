from PIL import Image, ImageDraw

def create_checkbox(filename, width, height, checked=False):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    margin = 8
    rect = [(margin, margin), (width - 1 - margin, height - 1 - margin)]
    
    if checked:
        draw.rounded_rectangle(rect, radius=8, fill="#FF7A00")
        # Draw checkmark
        draw.line([(width*0.3, height*0.5), (width*0.45, height*0.65), (width*0.7, height*0.35)], fill="#000000", width=4)
    else:
        draw.rounded_rectangle(rect, radius=8, fill="#111111", outline="#555555", width=2)
        
    img.save(filename)
    print(f"Generated {filename}")

def create_radio(filename, width, height, checked=False):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    margin = 8
    rect = [(margin, margin), (width - 1 - margin, height - 1 - margin)]
    
    if checked:
        draw.ellipse(rect, fill="#111111", outline="#FF7A00", width=3)
        inner = [(margin+8, margin+8), (width - 1 - margin - 8, height - 1 - margin - 8)]
        draw.ellipse(inner, fill="#FF7A00")
    else:
        draw.ellipse(rect, fill="#111111", outline="#555555", width=2)
        
    img.save(filename)
    print(f"Generated {filename}")

def main():
    base_dir = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'
    
    for cb in ['checkbox_false.png', 'checkbox_true.png']:
        with Image.open(f"{base_dir}/{cb}") as img: w, h = img.size
        create_checkbox(f"{base_dir}/{cb}", w, h, checked=("true" in cb))
        
    for rb in ['radio_false.png', 'radio_true.png']:
        with Image.open(f"{base_dir}/{rb}") as img: w, h = img.size
        create_radio(f"{base_dir}/{rb}", w, h, checked=("true" in rb))

if __name__ == '__main__':
    main()
