from PIL import Image

im = Image.open("doc_images/img_0.jpg")
w, h = im.size
after = im.crop((int(w * 0.5), 0, w, h))
after.save("doc_images/after_home.png")
print("Saved after_home.png:", after.size)

