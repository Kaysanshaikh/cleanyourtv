from PIL import Image

im_s7 = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (1).jpeg")
tv_crop = im_s7.crop((0, 360, 739, 1150))
tv_crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv_crop_s7_full.jpg")
print("Saved tv_crop_s7_full.jpg")
