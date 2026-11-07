from PIL import Image, ImageEnhance, ImageOps
import numpy as np

# Load doom_bw_test
im = Image.open("doom_bw_test.jpg").convert("L")  # Greyscale

# Target 1920x1080
target_w, target_h = 1920, 1080
# Scale so height fits or width fits
scale = max(target_w / im.width, target_h / im.height)
new_w, new_h = int(im.width * scale), int(im.height * scale)
im_resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Center crop
left = (new_w - target_w) // 2
top = (new_h - target_h) // 2
bg = im_resized.crop((left, top, left + target_w, top + target_h))

# Increase contrast slightly
enh = ImageEnhance.Contrast(bg)
bg = enh.enhance(1.25)

# Convert to RGB
bg = bg.convert("RGB")
arr = np.array(bg, dtype=np.float32)

# Apply bottom gradient from 45% height (y=486) down to 1080
# 0 -> 35% at 65% height -> 70% at 85% height -> 90% at 100% height
grad_start = int(0.40 * target_h)
for y in range(grad_start, target_h):
    factor = (y - grad_start) / (target_h - grad_start)
    # smooth curve: factor^1.5 * 0.90
    darken = 1.0 - (factor ** 1.3) * 0.92
    arr[y, :, :] *= darken

arr = np.clip(arr, 0, 255).astype(np.uint8)
out_im = Image.fromarray(arr)
out_path = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\themes\custom-clean\wallpaper.jpg"
out_im.save(out_path, quality=95)
print("Saved custom wallpaper to", out_path)

