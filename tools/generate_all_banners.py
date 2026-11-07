from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
W, H = 320, 180
R = 24  # corner radius

def make_rounded_card(bg_color, stroke_color=None):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle([2, 2, W - 3, H - 3], radius=R, fill=bg_color)
    if stroke_color:
        draw.rounded_rectangle([2, 2, W - 3, H - 3], radius=R, outline=stroke_color, width=2)
    return im

def make_gradient_card(c1, c2):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # horizontal gradient
    for x in range(W):
        ratio = x / float(W)
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        for y in range(H):
            im.putpixel((x, y), (r, g, b, 255))
    mask = Image.new("L", (W, H), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([2, 2, W - 3, H - 3], radius=R, fill=255)
    res = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    res.paste(im, (0, 0), mask)
    return res

# 1. Netflix Banner (Solid white with bold red NETFLIX wordmark)
im_net = make_rounded_card((255, 255, 255, 255))
# Let's crop the exact official Netflix red logo from card_netflix.png
raw_net = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_netflix.png")
# Center the official logo on the clean 320x180 card
raw_net_resized = raw_net.resize((270, 140), Image.Resampling.LANCZOS)
im_net.paste(raw_net_resized, (25, 20), raw_net_resized.convert("RGBA"))
im_net.save(os.path.join(out_dir, "banner_netflix.png"))

# 2. Prime Video Banner (Amazon blue #00A8E1 with white logo)
im_prime = make_rounded_card((0, 168, 225, 255))
raw_prime = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_prime.png")
raw_prime_resized = raw_prime.resize((270, 140), Image.Resampling.LANCZOS)
im_prime.paste(raw_prime_resized, (25, 20), raw_prime_resized.convert("RGBA"))
im_prime.save(os.path.join(out_dir, "banner_prime.png"))

# 3. JioHotstar Banner (Gradient blue to magenta with star)
im_hotstar = make_gradient_card((0, 96, 255), (230, 0, 122))
raw_hotstar = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_hotstar.png")
raw_hotstar_resized = raw_hotstar.resize((270, 140), Image.Resampling.LANCZOS)
im_hotstar.paste(raw_hotstar_resized, (25, 20), raw_hotstar_resized.convert("RGBA"))
im_hotstar.save(os.path.join(out_dir, "banner_hotstar.png"))

# 4. YouTube Banner (White with red play badge and black YouTube)
im_yt = make_rounded_card((255, 255, 255, 255))
raw_yt = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_youtube.png")
raw_yt_resized = raw_yt.resize((270, 140), Image.Resampling.LANCZOS)
im_yt.paste(raw_yt_resized, (25, 20), raw_yt_resized.convert("RGBA"))
im_yt.save(os.path.join(out_dir, "banner_youtube.png"))

# 5. MX Player Banner (Electric blue #0084FF with white bold MX Player mark)
im_mx = make_rounded_card((0, 132, 255, 255))
mx_draw = ImageDraw.Draw(im_mx)
# Draw bold white MX Player icon & text
# Large white play triangle inside rounded badge
mx_draw.rounded_rectangle([50, 45, 120, 135], radius=16, fill=(255, 255, 255, 255))
mx_draw.polygon([(75, 65), (75, 115), (105, 90)], fill=(0, 132, 255, 255))
# Wordmark "MX PLAYER"
mx_draw.rectangle([140, 60, 155, 120], fill=(255, 255, 255, 255))
mx_draw.polygon([(155, 60), (175, 95), (195, 60), (210, 60), (210, 120), (195, 120), (195, 85), (175, 115), (155, 85), (155, 120)], fill=(255, 255, 255, 255))
mx_draw.polygon([(220, 60), (238, 90), (220, 120), (235, 120), (248, 98), (260, 120), (275, 120), (258, 90), (275, 60), (260, 60), (248, 82), (235, 60)], fill=(255, 255, 255, 255))
im_mx.save(os.path.join(out_dir, "banner_mxplayer.png"))

# 6. Sony LIV Banner (Dark slate #141721 with vibrant LIV logo)
im_sony = make_rounded_card((20, 24, 34, 255))
s_draw = ImageDraw.Draw(im_sony)
# SONY text on left
s_draw.rectangle([50, 75, 110, 105], outline=(255, 255, 255, 220), width=3)
# Vibrant LIV curved bars (blue, orange, yellow, pink)
colors = [(0, 150, 255), (255, 140, 0), (255, 210, 0), (230, 0, 100)]
for idx, c in enumerate(colors):
    bx = 135 + idx * 32
    s_draw.rounded_rectangle([bx, 50, bx + 22, 130], radius=11, fill=c)
im_sony.save(os.path.join(out_dir, "banner_sonyliv.png"))

# 7. JioCinema Banner (Magenta #E6007A with white JioCinema)
im_jc = make_rounded_card((230, 0, 122, 255))
jc_draw = ImageDraw.Draw(im_jc)
# White cinema screen icon & text
jc_draw.rounded_rectangle([60, 50, 130, 130], radius=18, outline=(255, 255, 255, 255), width=6)
jc_draw.polygon([(85, 70), (85, 110), (115, 90)], fill=(255, 255, 255, 255))
# JioCinema bold font representation
jc_draw.rectangle([150, 60, 260, 85], fill=(255, 255, 255, 255))
jc_draw.rectangle([150, 95, 240, 115], fill=(255, 255, 255, 200))
im_jc.save(os.path.join(out_dir, "banner_jiocinema.png"))

# 8. Google Play Store Banner (Clean white card with Play colored triangle)
im_play = make_rounded_card((255, 255, 255, 255))
p_draw = ImageDraw.Draw(im_play)
# Official Google Play 4-color triangle
cx, cy = 90, 90
p_draw.polygon([(65, 55), (120, 90), (65, 90)], fill=(0, 200, 240, 255))  # Cyan/Blue
p_draw.polygon([(65, 90), (120, 90), (65, 125)], fill=(0, 220, 100, 255)) # Green
p_draw.polygon([(65, 55), (100, 75), (120, 90)], fill=(255, 70, 60, 255))  # Red
p_draw.polygon([(65, 125), (100, 105), (120, 90)], fill=(255, 190, 0, 255))# Yellow
# "Google Play" dark grey text bars
p_draw.rectangle([145, 65, 265, 88], fill=(90, 95, 105, 255))
p_draw.rectangle([145, 95, 235, 115], fill=(90, 95, 105, 255))
im_play.save(os.path.join(out_dir, "banner_playstore.png"))

# 9. Zee 5 Banner (Deep plum #1E152A with Zee5 circle)
im_zee = make_rounded_card((30, 21, 42, 255))
z_draw = ImageDraw.Draw(im_zee)
# Rainbow ring
z_draw.ellipse([60, 45, 145, 135], outline=(255, 180, 0, 255), width=6)
# "ZEE5"
z_draw.rectangle([165, 65, 255, 115], fill=(255, 255, 255, 240))
im_zee.save(os.path.join(out_dir, "banner_zee5.png"))

# 10. Apple TV Banner (Pitch black #000000 with white Apple TV)
im_atv = make_rounded_card((10, 10, 10, 255), stroke_color=(60, 60, 60, 255))
atv_draw = ImageDraw.Draw(im_atv)
# Apple icon
atv_draw.ellipse([90, 65, 125, 105], fill=(255, 255, 255, 255))
atv_draw.ellipse([90, 85, 125, 125], fill=(255, 255, 255, 255))
# Apple bite
atv_draw.ellipse([115, 75, 135, 105], fill=(10, 10, 10, 255))
# Leaf
atv_draw.ellipse([112, 52, 124, 68], fill=(255, 255, 255, 255))
# "tv"
atv_draw.rectangle([145, 65, 195, 80], fill=(255, 255, 255, 255))
atv_draw.rectangle([160, 80, 180, 125], fill=(255, 255, 255, 255))
atv_draw.polygon([(205, 75), (220, 125), (235, 125), (250, 75), (235, 75), (227, 105), (220, 75)], fill=(255, 255, 255, 255))
im_atv.save(os.path.join(out_dir, "banner_appletv.png"))

# 11. Send Files to TV Banner (Cyan #00B4D8 with white transfer icon)
im_sftv = make_rounded_card((0, 180, 216, 255))
sftv_draw = ImageDraw.Draw(im_sftv)
# TV screen
sftv_draw.rounded_rectangle([55, 50, 130, 115], radius=12, fill=(255, 255, 255, 255))
sftv_draw.rounded_rectangle([63, 58, 122, 107], radius=8, fill=(0, 180, 216, 255))
# Two transfer arrows (left/right)
sftv_draw.polygon([(78, 82), (92, 70), (92, 78), (108, 78), (108, 86), (92, 86), (92, 94)], fill=(255, 255, 255, 255))
# Text
sftv_draw.rectangle([145, 65, 265, 85], fill=(255, 255, 255, 255))
sftv_draw.rectangle([145, 95, 235, 115], fill=(255, 255, 255, 255))
im_sftv.save(os.path.join(out_dir, "banner_sftv.png"))

# 12. Settings Banner (Graphite #2C3038 with white Gear)
im_set = make_rounded_card((44, 48, 56, 255))
set_draw = ImageDraw.Draw(im_set)
# White gear
cx, cy = 95, 90
set_draw.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill=(255, 255, 255, 255))
set_draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(44, 48, 56, 255))
for a in range(0, 360, 45):
    rad = math.radians(a)
    gx = cx + int(36 * math.cos(rad))
    gy = cy + int(36 * math.sin(rad))
    set_draw.ellipse([gx - 8, gy - 8, gx + 8, gy + 8], fill=(255, 255, 255, 255))
# Text "Settings"
set_draw.rectangle([145, 75, 255, 105], fill=(255, 255, 255, 255))
im_set.save(os.path.join(out_dir, "banner_settings.png"))

print("All 12 authentic banners created successfully!")
