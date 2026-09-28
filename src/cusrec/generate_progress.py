from PIL import Image, ImageDraw

def create_progress(filename, width, height, color):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(
        [(0, int(height/2 - 8)), (width - 1, int(height/2 + 8))],
        radius=8,
        fill=color
    )
    img.save(filename)
    print(f"Generated {filename} ({width}x{height})")

def main():
    base_dir = '/root/Everpal/src/cusrec/ramdisks/twrp_extracted/twres/images'
    
    with Image.open(f"{base_dir}/progress_empty.png") as img: w, h = img.size
    create_progress(f"{base_dir}/progress_empty.png", w, h, color="#1A1A1A")
    
    with Image.open(f"{base_dir}/progress_fill.png") as img: w, h = img.size
    create_progress(f"{base_dir}/progress_fill.png", w, h, color="#FF7A00")
        
if __name__ == '__main__':
    main()
