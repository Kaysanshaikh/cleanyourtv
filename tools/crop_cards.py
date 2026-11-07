from PIL import Image

im = Image.open(r"C:/Users/Kaysan Shaikh/.gemini/antigravity/brain/548dbb22-49fb-4e2d-b345-aa366e28e011/.user_uploaded/media_1794055315885_3ec2e4b3.jpg")
W, H = im.size  # 1024 x 576

# Netflix card
c_netflix = im.crop((60, 395, 275, 505))
c_netflix.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_netflix.png")

# Prime Video card
c_prime = im.crop((300, 395, 515, 505))
c_prime.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_prime.png")

# JioHotstar card
c_hotstar = im.crop((525, 395, 740, 505))
c_hotstar.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_hotstar.png")

# YouTube card
c_youtube = im.crop((750, 395, 965, 505))
c_youtube.save(r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\card_youtube.png")

print("Cropped cards from screenshot!")
