from PIL import Image

im = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/fav_lineup_bw.jpg')

# Let's crop candidate regions
crops = {
    'jane': (160, 150, 270, 300),
    'sheldon': (270, 110, 370, 240),
    'walter': (420, 80, 520, 220),
    'spiderman': (570, 100, 680, 240),
    'jd': (350, 170, 470, 310),
    'flash_figure': (490, 200, 620, 340),
    'barney': (640, 200, 760, 340)
}

for name, box in crops.items():
    c = im.crop(box)
    c.save(f'c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/face_{name}.jpg')
    print(f'Saved face_{name}.jpg {box}')

