from PIL import Image, ImageDraw

def create_slider(filename, width, height, radius=16, bg_color="#1A1A1A", outline_color="#FF7A00"):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(
        [(0, 0), (width - 1, height - 1)],
        radius=radius,
        fill=bg_color,
        outline=outline_color,
        width=2
    )
    img.save(filename)
    print(f"Generated {filename} ({width}x{height})")

def create_handle(filename, width, height, color="#FF7A00"):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    # Circle handle
    margin = 4
    draw.ellipse([(margin, margin), (width - 1 - margin, height - 1 - margin)], fill=color)
    img.save(filename)
    print(f"Generated {filename} ({width}x{height})")

def main():
    base_dir = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'
    
    with Image.open(f"{base_dir}/slider.png") as img: w, h = img.size
    create_slider(f"{base_dir}/slider.png", w, h, bg_color="#111111", outline_color="#333333")
    
    with Image.open(f"{base_dir}/slider_used.png") as img: w, h = img.size
    create_slider(f"{base_dir}/slider_used.png", w, h, bg_color="#FF7A00", outline_color="#FF7A00")
    
    with Image.open(f"{base_dir}/slider_touch.png") as img: w, h = img.size
    create_slider(f"{base_dir}/slider_touch.png", w, h, bg_color="#FF8A20", outline_color="#FF8A20")
    
    with Image.open(f"{base_dir}/handle.png") as img: w, h = img.size
    create_handle(f"{base_dir}/handle.png", w, h, color="#FFFFFF")
        
if __name__ == '__main__':
    main()
