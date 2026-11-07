from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
import os
import math
import random

base_path = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi\fav_lineup_bw.jpg"
out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
im_bw = Image.open(base_path).convert("RGBA")
W, H = im_bw.size  # 800 x 450

def make_character_scene(char_name, bbox, tint_color, aura_color, effect_type):
    base = im_bw.copy()
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    
    cx = (bbox[0] + bbox[2]) // 2
    cy = (bbox[1] + bbox[3]) // 2
    rw = (bbox[2] - bbox[0]) // 2 + 25
    rh = (bbox[3] - bbox[1]) // 2 + 25
    
    # Atmospheric radial aura tightly centered on the character
    for r in range(max(rw, rh), 0, -4):
        alpha = int(120 * (1.0 - (r / max(rw, rh))**1.4))
        c = (aura_color[0], aura_color[1], aura_color[2], alpha)
        glow_draw.ellipse([cx - int(r * 1.1), cy - r, cx + int(r * 1.1), cy + r], fill=c)
    
    if effect_type == "phasing_lightning":
        # Reverse-Flash at (cx=515, cy=280)
        # Piercing glowing red eyes (Reverse Flash iconic red gaze)
        glow_draw.ellipse([cx - 16, cy - 38, cx - 6, cy - 30], fill=(255, 30, 30, 255))
        glow_draw.ellipse([cx + 6, cy - 38, cx + 16, cy - 30], fill=(255, 30, 30, 255))
        # Inner glow for eyes
        glow_draw.ellipse([cx - 13, cy - 36, cx - 9, cy - 32], fill=(255, 230, 230, 255))
        glow_draw.ellipse([cx + 9, cy - 36, cx + 13, cy - 32], fill=(255, 230, 230, 255))
        
        # Phasing speed-force red lightning crackling around body
        random.seed(99)
        for _ in range(12):
            lx, ly = cx + random.randint(-40, 40), cy + random.randint(-60, 60)
            points = [(lx, ly)]
            for _ in range(6):
                lx += random.randint(-16, 16)
                ly += random.randint(-16, 16)
                points.append((lx, ly))
            glow_draw.line(points, fill=(255, 50, 40, 240), width=2)
            glow_draw.line(points, fill=(255, 240, 200, 255), width=1)
            
    elif effect_type == "atomic_rings":
        # Sheldon Cooper at (cx=310, cy=240)
        # Golden atomic orbital rings around Sheldon
        glow_draw.ellipse([cx - 55, cy - 25, cx + 55, cy + 25], outline=(255, 225, 60, 220), width=2)
        glow_draw.ellipse([cx - 35, cy - 50, cx + 35, cy + 50], outline=(255, 190, 40, 200), width=2)
        glow_draw.ellipse([cx - 45, cy - 38, cx + 45, cy + 38], outline=(255, 255, 150, 180), width=1)
        # Golden nucleus spark
        glow_draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 255, 220, 255))
        
    elif effect_type == "heisenberg_cyan":
        # Walter White at (cx=440, cy=180)
        # Blue crystal meth aura & rising chemical vapors
        random.seed(77)
        for _ in range(8):
            rx = cx + random.randint(-35, 35)
            ry = cy + random.randint(-50, 40)
            glow_draw.polygon([(rx, ry), (rx + 7, ry - 12), (rx + 14, ry), (rx + 7, ry + 12)], fill=(40, 230, 255, 200))
            
    elif effect_type == "mass_spotlight":
        # JD Master at (cx=390, cy=290)
        # Fiery orange cinematic rim lighting & embers
        random.seed(55)
        for angle in range(-50, 50, 12):
            rad = math.radians(angle - 90)
            ex = cx + int(110 * math.cos(rad))
            ey = cy + int(110 * math.sin(rad))
            glow_draw.line([(cx, cy - 40), (ex, ey)], fill=(255, 130, 20, 110), width=3)
        # Rising fire embers
        for _ in range(10):
            ex = cx + random.randint(-40, 40)
            ey = cy + random.randint(-60, 40)
            glow_draw.ellipse([ex - 2, ey - 2, ex + 2, ey + 2], fill=(255, 200, 60, 240))
            
    elif effect_type == "suit_up_amber":
        # Barney Stinson at (cx=645, cy=290)
        # Suit Up golden stars & amber pub glow
        for sx, sy in [(cx - 30, cy - 50), (cx + 35, cy - 55), (cx + 25, cy + 15), (cx - 25, cy + 20)]:
            glow_draw.line([(sx - 7, sy), (sx + 7, sy)], fill=(255, 230, 110, 240), width=2)
            glow_draw.line([(sx, sy - 7), (sx, sy + 7)], fill=(255, 230, 110, 240), width=2)
            glow_draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 230, 255))
            
    elif effect_type == "spider_sense":
        # Spider-Man at (cx=585, cy=220)
        # Tingling spider-sense squiggles radiating from his mask
        for angle in [-60, -35, -10, 15, 40, 65]:
            rad = math.radians(angle - 90)
            x1 = cx + int(45 * math.cos(rad))
            y1 = cy - 25 + int(35 * math.sin(rad))
            x2 = cx + int(70 * math.cos(rad))
            y2 = cy - 25 + int(55 * math.sin(rad))
            glow_draw.arc([min(x1, x2) - 5, min(y1, y2) - 5, max(x1, x2) + 5, max(y1, y2) + 5], 0, 360, fill=(255, 240, 50, 240), width=2)
            
    glow = glow.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Highlight character cutout in vibrant color
    char_patch = im_bw.crop(bbox)
    tint_layer = Image.new("RGBA", char_patch.size, tint_color)
    char_colored = ImageChops.screen(char_patch, tint_layer)
    
    # Soft oval mask for character cutout
    mask = Image.new("L", char_patch.size, 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.ellipse([0, 0, char_patch.size[0], char_patch.size[1]], fill=220)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=12))
    
    # Composite
    res = Image.alpha_composite(base, glow)
    res.paste(char_colored, bbox, mask)
    
    out_file = os.path.join(out_dir, f"fav_{char_name}.jpg")
    res.convert("RGB").save(out_file, quality=95)
    print(f"Generated {out_file} ({res.size})")

# 1. Reverse-Flash: yellow suit at (460, 190, 570, 390) with glowing red eyes & phasing tachyon lightning
make_character_scene("flash", (460, 190, 570, 390), (255, 215, 30, 150), (240, 40, 30), "phasing_lightning")

# 2. Sheldon Cooper: yellow Green Lantern shirt at (250, 150, 370, 370) with golden atomic rings
make_character_scene("sheldon", (250, 150, 370, 370), (255, 210, 50, 140), (255, 200, 40), "atomic_rings")

# 3. Walter White: Heisenberg hat at (380, 110, 500, 280) with cyan crystal reaction
make_character_scene("walter", (380, 110, 500, 280), (50, 230, 240, 140), (40, 210, 230), "heisenberg_cyan")

# 4. JD Master: fiery orange mass spotlight at (330, 200, 450, 400)
make_character_scene("master", (330, 200, 450, 400), (255, 140, 30, 150), (255, 120, 20), "mass_spotlight")

# 5. Barney Stinson: sharp suit at (590, 200, 710, 400) with amber pub glow & stars
make_character_scene("barney", (590, 200, 710, 400), (255, 210, 120, 130), (255, 185, 60), "suit_up_amber")

# 6. Spider-Man: crisp red/blue suit at (530, 140, 640, 330) with spider-sense
make_character_scene("spiderman", (530, 140, 640, 330), (240, 50, 50, 130), (240, 40, 40), "spider_sense")
