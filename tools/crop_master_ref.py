from PIL import Image

im_master = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (2).jpeg")
tv_crop = im_master.crop((0, 200, 739, 850))
tv_crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv_crop_master.jpg")
print("Saved tv_crop_master.jpg")

