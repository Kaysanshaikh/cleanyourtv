from PIL import Image, ImageDraw

im = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/fav_lineup_bw.jpg')
draw = ImageDraw.Draw(im)

chars = {
    'Jane': (160, 180, 310, 430),
    'Sheldon': (260, 135, 380, 400),
    'JD': (320, 200, 480, 440),
    'Walter': (415, 90, 535, 320),
    'Flash': (490, 210, 630, 440),
    'SpiderMan': (570, 125, 710, 350),
    'Barney': (625, 220, 775, 440)
}

for name, box in chars.items():
    draw.rectangle(box, outline='yellow', width=2)
    draw.text((box[0] + 5, box[1] + 5), name, fill='cyan')

im.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/test_char_boxes.jpg')
print('Saved test_char_boxes.jpg')

