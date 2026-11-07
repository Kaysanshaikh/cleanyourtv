from PIL import Image

im = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (2).jpeg")
crop = im.crop((100, 500, 550, 950))
crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\master_body.jpg")
print("Saved master_body.jpg")
