from PIL import Image

# Let's inspect the TV bounding box in the phone photos
# The TV is located roughly in the middle vertical region
im_flash = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (3).jpeg")
# Crop TV region: x from 0 to 739, y from 300 to 1250
tv_crop = im_flash.crop((0, 300, 739, 1250))
tv_crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv_crop_flash.jpg")
print("Saved tv_crop_flash.jpg")

