from PIL import Image, ImageOps
import os
for filename in os.listdir():
    pic = Image.open('.\\'+filename)
    new_pic = ImageOps.grayscale(pic)
    new_pic.save(f'.\\{filename}')