from PIL import Image, ImageOps, ImageEnhance
import os
import shutil

res_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"
os.makedirs(res_dir, exist_ok=True)

# 1. Patrick Jane selected
shutil.copy("doc_images/img_3.jpg", os.path.join(res_dir, "fav_mentalist.jpg"))

# 2. Spider-Man selected
shutil.copy("doc_images/img_4.jpg", os.path.join(res_dir, "fav_spiderman.jpg"))

# 3. All B&W lineup (convert img_4 to full grayscale)
im_spidey = Image.open("doc_images/img_4.jpg").convert("L")
enh = ImageEnhance.Contrast(im_spidey)
im_bw = enh.enhance(1.2).convert("RGB")
im_bw.save(os.path.join(res_dir, "fav_lineup_bw.jpg"), quality=95)

# 4. Mood cards banner / assets
shutil.copy("doc_images/img_6.jpg", os.path.join(res_dir, "mood_roulette_capes.jpg"))
shutil.copy("doc_images/img_7.jpg", os.path.join(res_dir, "mood_roulette_sitcom.jpg"))

print("Copied and processed all favourite & mood drawables!")

