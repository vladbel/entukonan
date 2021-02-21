"""Python image library"""
import pylab as pl
import PIL as pil


image = pil.Image.open("data/p1.jpeg")
pl.imshow(image)

x = [0, 460] # image width
y = [0, 345] # image height
pl.plot(x[:2], y[:2])

pl.show()

print ("end")
