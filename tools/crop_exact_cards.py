from PIL import Image

im = Image.open(r"C:/Users/Kaysan Shaikh/.gemini/antigravity/brain/548dbb22-49fb-4e2d-b345-aa366e28e011/.user_uploaded/media_1794055315885_3ec2e4b3.jpg")
out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable-nodpi"

# The cards in the screenshot are exactly 216 x 128
# 1. Netflix (white card)
c_net = im.crop((68, 388, 276, 508))
c_net.resize((320, 180), Image.Resampling.LANCZOS).save(f"{out_dir}/banner_netflix.png")

# 2. Prime Video (blue card)
c_prime = im.crop((306, 388, 514, 508))
c_prime.resize((320, 180), Image.Resampling.LANCZOS).save(f"{out_dir}/banner_prime.png")

# 3. JioHotstar (gradient card)
c_hot = im.crop((532, 388, 740, 508))
c_hot.resize((320, 180), Image.Resampling.LANCZOS).save(f"{out_dir}/banner_hotstar.png")

# 4. YouTube (white card)
c_yt = im.crop((758, 388, 966, 508))
c_yt.resize((320, 180), Image.Resampling.LANCZOS).save(f"{out_dir}/banner_youtube.png")

print("Cropped authentic cards from user reference photo!")
