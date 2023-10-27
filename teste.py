from PIL import Image
import os


file = "BAIXO.png" #especified file for the image
ignore_color = (255, 255, 255) #white

class GetIm():
    def __init__(self, img, red, white, black, green):
        self.img = Image.open(file)

        #colors
        self.red = (0, 0, 255)
        self.white = (255, 255, 255)
        self.black =(0, 0, 0)
        self.green = (0, 255, 0)

    def makeGCode(self):
        #G92 X0 Y0 Z0 define a maquina no estado atual como home
        self.output = "M106\n" #start FAN
        print(self.output)
        print("G21 ;") #milimetros
        for y in range(self.img.size[0]):
            for x in range(0, self.img.size[1]):
                if(self.img.getpixel((x, y))[:3] == (237, 40, 30)):
                    print(f"G1 X{y} Y{x} ;")
                    #print(f"G1 x{image.getpixel((x, y))[:3]}")
                    #124750 red's
        print("M2") #finaliza


if __name__ == "__main__":
    iof = Image.open(file)
    getPar = GetIm(Image.open(file), (0,0,255), (255, 255, 255), (0, 0, 0), (0, 255, 0))
    getPar.makeGCode()
