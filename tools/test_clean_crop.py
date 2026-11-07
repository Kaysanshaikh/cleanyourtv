from PIL import Image

# Test cropping top 45px on img_3 and img_4
im3 = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/doc_images/img_3.jpg')
crop3 = im3.crop((0, 45, 800, 450))
crop3.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/test_crop_jane.jpg')

im4 = Image.open('c:/Users/Kaysan Shaikh/Desktop/Claude/doc_images/img_4.jpg')
crop4 = im4.crop((0, 45, 800, 450))
crop4.save('c:/Users/Kaysan Shaikh/Desktop/Claude/cleanyourtv/launcher/app/src/main/res/drawable-nodpi/test_crop_spiderman.jpg')

print("Cropped successfully!")

