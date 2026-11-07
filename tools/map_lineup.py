from PIL import Image

im = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/fav_lineup_bw.jpg')

# The lineup is 800 wide, 450 tall
# Let's crop 7 distinct character regions across the width:
# 1. Patrick Jane: far left (140 to 240)
c1 = im.crop((130, 180, 240, 360))
c1.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_1_jane.jpg')

# 2. Sheldon Cooper: (220 to 320)
c2 = im.crop((220, 100, 320, 300))
c2.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_2_sheldon.jpg')

# 3. Master JD: (280 to 410)
c3 = im.crop((290, 180, 420, 380))
c3.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_3_master.jpg')

# 4. Walter White: (360 to 460)
c4 = im.crop((360, 80, 460, 260))
c4.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_4_walter.jpg')

# 5. Glowing Figure / Reverse Flash: (410 to 520)
c5 = im.crop((410, 190, 520, 370))
c5.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_5_flash.jpg')

# 6. Spider-Man: (460 to 570)
c6 = im.crop((460, 90, 570, 260))
c6.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_6_spiderman.jpg')

# 7. Barney Stinson: (510 to 620)
c7 = im.crop((510, 190, 620, 370))
c7.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/char_7_barney.jpg')

print("Saved all 7 character crops!")

