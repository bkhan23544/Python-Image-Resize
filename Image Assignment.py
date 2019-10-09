import PIL
from PIL import Image
import numpy as np
import glob
import matplotlib.pylab as plt


def plti (im,h=8,**kwargs):
    y=im.shape[0]
    x=im.shape[1]
    w=(y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im,interpolation="none", **kwargs)
    plt.axis("on")
    plt.show()


arr=[]
image_list = []
for filename in glob.glob('Pics/*.jpg'):
    im=Image.open(filename)
    image_list.append(im)
    maxsize = (500, 500)
    im.thumbnail(maxsize, PIL.Image.ANTIALIAS)
    a=np.array(im)
    # convertback = Image.fromarray(a)
    arr.append(a)

for i in range(len(arr)):
    plti(arr[i])




