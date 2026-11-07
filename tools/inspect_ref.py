from PIL import Image
import glob
import os

files = glob.glob(r"c:\Users\Kaysan Shaikh\Desktop\Claude\user_ref\*.jpeg")
for f in sorted(files):
    im = Image.open(f)
    print(os.path.basename(f), im.size)
