from PIL import Image

im_bb = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.38 PM.jpeg")
tv_crop = im_bb.crop((0, 320, 739, 900))
tv_crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv_crop_bb.jpg")
print("Saved tv_crop_bb.jpg")

