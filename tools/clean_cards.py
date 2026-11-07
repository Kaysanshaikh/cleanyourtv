from PIL import Image, ImageDraw

out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
W, H = 320, 180
R = 24

def make_card(bg):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle([2, 2, W - 3, H - 3], radius=R, fill=bg)
    return im

# 1. Netflix: crop inner red text (tight bounding box inside the card)
raw_net = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_netflix.png")
# Inner red text is at x=20 to 195, y=30 to 85 in card_netflix.png
crop_net = raw_net.crop((24, 30, 195, 85))
card_net = make_card((255, 255, 255, 255))
# Scale inner logo to fit beautifully (e.g. 210 x 70)
nw = 210
nh = int(crop_net.size[1] * (nw / crop_net.size[0]))
crop_net_resized = crop_net.resize((nw, nh), Image.Resampling.LANCZOS)
card_net.paste(crop_net_resized, ((W - nw) // 2, (H - nh) // 2), crop_net_resized.convert("RGBA"))
card_net.save(f"{out_dir}/banner_netflix.png")

# 2. Prime Video: inner logo from card_prime.png
raw_prime = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_prime.png")
crop_prime = raw_prime.crop((20, 20, 195, 90))
card_prime = make_card((0, 168, 225, 255))
pw = 210
ph = int(crop_prime.size[1] * (pw / crop_prime.size[0]))
crop_prime_resized = crop_prime.resize((pw, ph), Image.Resampling.LANCZOS)
card_prime.paste(crop_prime_resized, ((W - pw) // 2, (H - ph) // 2), crop_prime_resized.convert("RGBA"))
card_prime.save(f"{out_dir}/banner_prime.png")

# 3. JioHotstar: inner logo from card_hotstar.png
raw_hot = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_hotstar.png")
crop_hot = raw_hot.crop((15, 20, 200, 90))
# Horizontal gradient
card_hot = Image.new("RGBA", (W, H), (0, 0, 0, 0))
for x in range(W):
    ratio = x / float(W)
    r = int(0 * (1 - ratio) + 230 * ratio)
    g = int(96 * (1 - ratio) + 0 * ratio)
    b = int(255 * (1 - ratio) + 122 * ratio)
    for y in range(H):
        card_hot.putpixel((x, y), (r, g, b, 255))
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).rounded_rectangle([2, 2, W - 3, H - 3], radius=R, fill=255)
final_hot = Image.new("RGBA", (W, H), (0, 0, 0, 0))
final_hot.paste(card_hot, (0, 0), mask)

hw = 220
hh = int(crop_hot.size[1] * (hw / crop_hot.size[0]))
crop_hot_resized = crop_hot.resize((hw, hh), Image.Resampling.LANCZOS)
final_hot.paste(crop_hot_resized, ((W - hw) // 2, (H - hh) // 2), crop_hot_resized.convert("RGBA"))
final_hot.save(f"{out_dir}/banner_hotstar.png")

# 4. YouTube: inner logo from card_youtube.png
raw_yt = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_youtube.png")
crop_yt = raw_yt.crop((20, 25, 195, 85))
card_yt = make_card((255, 255, 255, 255))
yw = 210
yh = int(crop_yt.size[1] * (yw / crop_yt.size[0]))
crop_yt_resized = crop_yt.resize((yw, yh), Image.Resampling.LANCZOS)
card_yt.paste(crop_yt_resized, ((W - yw) // 2, (H - yh) // 2), crop_yt_resized.convert("RGBA"))
card_yt.save(f"{out_dir}/banner_youtube.png")

print("Pristine cards saved!")
