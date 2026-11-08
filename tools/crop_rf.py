from PIL import Image

im = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (3).jpeg")
crop = im.crop((300, 500, 600, 750))
crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\rf_cutout.jpg")
print("Saved rf_cutout.jpg")

