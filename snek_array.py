# generate frame array from image

from PIL import Image
import numpy as np
im = Image.open("input.png")
p = np.array(im)

f1 = open("output.txt", 'w')

f1.write("byte snek[][")
f1.write(str(im.size[1]))
f1.write("][3] = {")

for i in range(0, im.size[0]):
    f1.write("{")
    for j in range(0, im.size[1]):
         f1.write("{")
         f1.write(str(im.getpixel((i, j))[0]))
         f1.write(", ")
         f1.write(str(im.getpixel((i, j))[1]))
         f1.write(", ")
         f1.write(str(im.getpixel((i, j))[2]))
         f1.write("}")
         if(j < im.size[1]-1):
           f1.write(",")
    f1.write("}")
    if(i < im.size[0]-1):
           f1.write(",\n")
f1.write("};")
f1.close()

