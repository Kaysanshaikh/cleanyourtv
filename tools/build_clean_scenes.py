from PIL import Image, ImageDraw, ImageFilter, ImageChops
import os
import math
import random

res_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
doc_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\doc_images"

# 1. Base clean crops (y=75 to 450 -> 800 x 375)
im_jane_raw = Image.open(os.path.join(doc_dir, "img_3.jpg"))
im_jane_clean = im_jane_raw.crop((0, 75, 800, 450))
im_jane_clean.save(os.path.join(res_dir, "fav_mentalist.jpg"), quality=95)

im_spider_raw = Image.open(os.path.join(doc_dir, "img_4.jpg"))
im_spider_clean = im_spider_raw.crop((0, 75, 800, 450))
im_spider_clean.save(os.path.join(res_dir, "fav_spiderman.jpg"), quality=95)

# Create base black and white lineup (convert Spider-Man color to B&W)
# Slicing Spider-Man area in B&W
bw_base = im_spider_clean.convert("L").convert("RGBA")
# But keep the subtle background tones
im_base = Image.open(os.path.join(doc_dir, "img_4.jpg")).crop((0, 75, 800, 450)).convert("RGBA")
# Desaturate Spider-Man region (460 to 570)
sp_patch = im_base.crop((460, 50, 580, 240)).convert("L").convert("RGBA")
im_base.paste(sp_patch, (460, 50))
im_base.convert("RGB").save(os.path.join(res_dir, "fav_lineup_bw.jpg"), quality=95)
print("Base lineup and Mentalist/Spider-Man saved!")

W, H = im_base.size  # 800 x 375

def make_scene(char_name, cx, cy, rad_x, rad_y, tint_color, effect_type):
    base = im_base.copy()
    
    # 1. Atmospheric Bloom
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    
    max_r = max(rad_x, rad_y)
    for r in range(max_r, 0, -4):
        pct = 1.0 - (r / max_r)
        alpha = int(170 * (pct ** 1.6))
        c = (tint_color[0], tint_color[1], tint_color[2], alpha)
        rx = int(r * (rad_x / max_r))
        ry = int(r * (rad_y / max_r))
        glow_draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=c)
        
    glow = glow.filter(ImageFilter.GaussianBlur(radius=8))
    
    # 2. 3D Signature Effects
    fx = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fx_draw = ImageDraw.Draw(fx)
    
    if effect_type == "reverse_flash":
        # Piercing glowing red eyes
        eye_y = cy - 35
        # Left eye
        fx_draw.ellipse([cx - 15, eye_y - 4, cx - 5, eye_y + 4], fill=(255, 30, 30, 255))
        fx_draw.ellipse([cx - 12, eye_y - 2, cx - 8, eye_y + 2], fill=(255, 250, 240, 255))
        # Right eye
        fx_draw.ellipse([cx + 5, eye_y - 4, cx + 15, eye_y + 4], fill=(255, 30, 30, 255))
        fx_draw.ellipse([cx + 8, eye_y - 2, cx + 12, eye_y + 2], fill=(255, 250, 240, 255))
        
        # Red and white tachyon speed-force crackles
        random.seed(42)
        for _ in range(18):
            lx, ly = cx + random.randint(-40, 40), cy + random.randint(-65, 65)
            pts = [(lx, ly)]
            for _ in range(5):
                lx += random.randint(-16, 16)
                ly += random.randint(-16, 16)
                pts.append((lx, ly))
            fx_draw.line(pts, fill=(255, 40, 30, 240), width=3)
            fx_draw.line(pts, fill=(255, 240, 180, 255), width=1)
            
    elif effect_type == "atomic_rings":
        # Golden orbital rings
        fx_draw.ellipse([cx - 60, cy - 20, cx + 60, cy + 20], outline=(255, 225, 60, 230), width=2)
        fx_draw.ellipse([cx - 35, cy - 50, cx + 35, cy + 50], outline=(255, 195, 40, 210), width=2)
        fx_draw.ellipse([cx - 45, cy - 35, cx + 45, cy + 35], outline=(255, 255, 160, 190), width=1)
        fx_draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 255, 230, 255))
        
    elif effect_type == "mass_spotlight":
        # Fiery rim lighting & embers
        random.seed(77)
        for angle in range(-50, 50, 12):
            rad = math.radians(angle - 90)
            ex = cx + int(115 * math.cos(rad))
            ey = cy + int(115 * math.sin(rad))
            fx_draw.line([(cx, cy - 45), (ex, ey)], fill=(255, 130, 20, 120), width=3)
        for _ in range(16):
            ex = cx + random.randint(-40, 40)
            ey = cy + random.randint(-60, 40)
            fx_draw.ellipse([ex - 2, ey - 2, ex + 2, ey + 2], fill=(255, 220, 70, 255))
            
    elif effect_type == "heisenberg_cyan":
        # Crystal vapors
        random.seed(33)
        for _ in range(12):
            rx = cx + random.randint(-35, 35)
            ry = cy + random.randint(-50, 40)
            fx_draw.polygon([(rx, ry), (rx + 7, ry - 12), (rx + 14, ry), (rx + 7, ry + 12)], fill=(40, 240, 255, 220))
            
    elif effect_type == "suit_up_amber":
        # Suit Up golden stars
        for sx, sy in [(cx - 32, cy - 55), (cx + 35, cy - 60), (cx + 28, cy + 18), (cx - 26, cy + 22)]:
            fx_draw.line([(sx - 9, sy), (sx + 9, sy)], fill=(255, 235, 120, 255), width=2)
            fx_draw.line([(sx, sy - 9), (sx, sy + 9)], fill=(255, 235, 120, 255), width=2)
            fx_draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 240, 255))
            
    lit = ImageChops.screen(base, glow)
    res = Image.alpha_composite(lit, fx)
    
    out_file = os.path.join(res_dir, f"fav_{char_name}.jpg")
    res.convert("RGB").save(out_file, quality=95)
    print(f"Generated {out_file} ({res.size})")

make_scene("sheldon", 270, 105, 55, 85, (255, 210, 50), "atomic_rings")
make_scene("master", 355, 190, 60, 95, (255, 140, 30), "mass_spotlight")
make_scene("walter", 410, 85, 50, 80, (40, 220, 240), "heisenberg_cyan")
make_scene("flash", 465, 190, 55, 90, (255, 215, 30), "reverse_flash")
make_scene("barney", 565, 190, 55, 90, (255, 200, 110), "suit_up_amber")
print("All clean scenes generated!")

