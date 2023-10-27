from PIL import Image, ImagePalette, ImageColor
import PIL
import numpy as np

file = "BAIXO.png"

image = Image.open(file)
imSize = image.size
im = image.load()

print(image.getpixel((250, 250))[:3], image.mode, image.size, image.format) #(0, 0, 0) RGBA (500, 500) none


for y in range(0, imSize[0]):
    for x in range(0, imSize[1]):
        if(image.getpixel((x, y))[:3] == (237, 40, 30)):
            print(f"RGB == {image.getpixel((x, y))[:3]}")
            #124750 red's