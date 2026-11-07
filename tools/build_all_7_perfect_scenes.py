from PIL import Image, ImageDraw, ImageFilter, ImageChops
import os
import math
import random

res_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
bw_path = os.path.join(res_dir, "fav_lineup_bw.jpg")
im_orig = Image.open(bw_path).convert("RGBA")
W, H = im_orig.size

# Clean top text seamlessly by blurring only the small text glyphs with nearby texture
clean_base = im_orig.copy()

# Sample nearby smoke texture at y=85-95 (just below the text)
patch_left = clean_base.crop((20, 85, 170, 115))
clean_base.paste(patch_left.resize((150, 40)), (20, 15))

patch_right = clean_base.crop((340, 85, 660, 125))
clean_base.paste(patch_right.resize((320, 40)), (340, 45))

# Soft blend filter on patched regions
clean_base = clean_base.filter(ImageFilter.UnsharpMask(radius=1, percent=100))

# Clean mentalist scene top as well
ment_path = os.path.join(res_dir, "fav_mentalist.jpg")
if os.path.exists(ment_path):
    im_ment = Image.open(ment_path).convert("RGBA")
    p_ment = im_ment.crop((20, 85, 170, 115))
    im_ment.paste(p_ment.resize((150, 40)), (20, 15))
    p_ment2 = im_ment.crop((120, 85, 400, 125))
    im_ment.paste(p_ment2.resize((280, 40)), (120, 45))
    im_ment.convert("RGB").save(ment_path, quality=95)

clean_base.convert("RGB").save(bw_path, quality=95)

def make_organic_3d_scene(char_name, cx, cy, rad_x, rad_y, tint_color, effect_type):
    # Base dark scene
    base = clean_base.copy()
    
    # Atmospheric lighting layer
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    
    # Smooth multi-layer radial spotlight
    max_r = max(rad_x, rad_y)
    for r in range(max_r, 0, -4):
        pct = 1.0 - (r / max_r)
        alpha = int(160 * (pct ** 1.6))
        c = (tint_color[0], tint_color[1], tint_color[2], alpha)
        rx = int(r * (rad_x / max_r))
        ry = int(r * (rad_y / max_r))
        glow_draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=c)
        
    glow = glow.filter(ImageFilter.GaussianBlur(radius=8))
    
    # Foreground effects layer (crisp lines & 3D effects)
    fx = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fx_draw = ImageDraw.Draw(fx)
    
    if effect_type == "reverse_flash":
        # Glowing piercing red eyes
        eye_y = cy - 35
        # Left eye
        fx_draw.ellipse([cx - 15, eye_y - 4, cx - 5, eye_y + 4], fill=(255, 30, 30, 255))
        fx_draw.ellipse([cx - 12, eye_y - 2, cx - 8, eye_y + 2], fill=(255, 250, 240, 255))
        # Right eye
        fx_draw.ellipse([cx + 5, eye_y - 4, cx + 15, eye_y + 4], fill=(255, 30, 30, 255))
        fx_draw.ellipse([cx + 8, eye_y - 2, cx + 12, eye_y + 2], fill=(255, 250, 240, 255))
        
        # Red tachyon speed-force crackles
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
            
    elif effect_type == "spider_sense":
        # Radiating spider-sense squiggles
        mask_y = cy - 25
        for angle in [-70, -45, -20, 5, 30, 55, 80]:
            rad = math.radians(angle - 90)
            x1 = cx + int(42 * math.cos(rad))
            y1 = mask_y + int(38 * math.sin(rad))
            x2 = cx + int(68 * math.cos(rad))
            y2 = mask_y + int(60 * math.sin(rad))
            fx_draw.line([(x1, y1), ((x1+x2)//2 + 4, (y1+y2)//2 - 4), (x2, y2)], fill=(255, 240, 60, 255), width=2)
            fx_draw.line([(x1, y1), ((x1+x2)//2 + 4, (y1+y2)//2 - 4), (x2, y2)], fill=(255, 70, 50, 200), width=4)
            
    elif effect_type == "suit_up_amber":
        # Suit Up golden stars
        for sx, sy in [(cx - 32, cy - 55), (cx + 35, cy - 60), (cx + 28, cy + 18), (cx - 26, cy + 22)]:
            fx_draw.line([(sx - 9, sy), (sx + 9, sy)], fill=(255, 235, 120, 255), width=2)
            fx_draw.line([(sx, sy - 9), (sx, sy + 9)], fill=(255, 235, 120, 255), width=2)
            fx_draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 240, 255))
            
    # Composite: Base + Soft Radial Glow (Screen) + Crisp FX
    lit = ImageChops.screen(base, glow)
    res = Image.alpha_composite(lit, fx)
    
    out_file = os.path.join(res_dir, f"fav_{char_name}.jpg")
    res.convert("RGB").save(out_file, quality=95)
    print(f"Generated {out_file} ({res.size})")

make_organic_3d_scene("sheldon", 270, 180, 55, 90, (255, 210, 50), "atomic_rings")
make_organic_3d_scene("master", 355, 265, 60, 95, (255, 140, 30), "mass_spotlight")
make_organic_3d_scene("walter", 410, 160, 50, 80, (40, 220, 240), "heisenberg_cyan")
make_organic_3d_scene("flash", 465, 265, 55, 90, (255, 215, 30), "reverse_flash")
make_organic_3d_scene("spiderman", 515, 165, 55, 80, (240, 50, 50), "spider_sense")
make_organic_3d_scene("barney", 565, 265, 55, 90, (255, 200, 110), "suit_up_amber")
print("Organic 3D scenes complete!")
