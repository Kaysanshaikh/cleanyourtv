from PIL import Image

# Let's inspect the coordinates of the TV bezel in the phone images
# In WhatsApp Image 2026-11-07 at 5.59.37 PM (3).jpeg (739 x 1600)
im = Image.open(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\WhatsApp Image 2026-11-07 at 5.59.37 PM (3).jpeg")
print("Size:", im.size)

# The TV screen bezel:
# Top bezel is around y=300
# Bottom bezel is around y=880
# Left bezel is around x=0
# Right bezel is around x=739
crop = im.crop((0, 310, 739, 875))
crop.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv_exact_flash.jpg")
print("Saved tv_exact_flash.jpg:", crop.size)

