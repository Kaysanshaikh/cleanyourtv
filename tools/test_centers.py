from PIL import Image, ImageDraw

im = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/fav_lineup_bw.jpg')
draw = ImageDraw.Draw(im)

centers = {
    'Jane': (225, 230),
    'Sheldon': (330, 185),
    'JD': (415, 245),
    'Walter': (480, 160),
    'Flash': (565, 270),
    'SpiderMan': (645, 205),
    'Barney': (715, 280)
}

for name, (cx, cy) in centers.items():
    draw.line([(cx - 20, cy), (cx + 20, cy)], fill='red', width=3)
    draw.line([(cx, cy - 20), (cx, cy + 20)], fill='red', width=3)
    draw.text((cx - 15, cy - 35), name, fill='yellow')

im.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/test_centers.jpg')
print('Saved test_centers.jpg')

