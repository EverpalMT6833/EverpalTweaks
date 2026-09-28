from PIL import Image, ImageDraw

def create_modern_button(filename, width, height, radius=12, bg_color="#1A1A1A", outline_color="#FF7A00"):
    # Create transparent image
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    
    # Draw rounded rectangle
    draw.rounded_rectangle(
        [(0, 0), (width - 1, height - 1)],
        radius=radius,
        fill=bg_color,
        outline=outline_color,
        width=2
    )
    
    img.save(filename)
    print(f"Generated {filename} ({width}x{height})")

def main():
    base_dir = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'
    
    # Read existing sizes
    for btn in ['main_button.png', 'main_button_half_height.png', 'main_button_half_height_full_width.png']:
        path = f"{base_dir}/{btn}"
        with Image.open(path) as img:
            w, h = img.size
        
        create_modern_button(path, w, h)
        
if __name__ == '__main__':
    main()
