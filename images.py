import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
from scipy import ndimage 

def flipUp(img):
    """Flips an image vertically."""
    newimage = img.copy()
    newimage = newimage[::-1]
    return newimage

def flipSide(img):
    """Flips an image horizontally."""
    newimage = img.copy()
    newimage = ndimage.rotate(img, 180) 
    newimage = newimage[::-1]
    return newimage

def flip4ways(img):
    """take an image and create a new image with the original image flipped four ways """
    flipUpImage = flipUp(img)
    flipSideImg = flipSide(img)
    flipUpAndSideImg = flipSide(flipUp(img))
    # Combining the two images horizontally
    top_img = np.concatenate((img, flipSideImg), axis=1)
    bottom_img = np.concatenate((flipUpImage, flipUpAndSideImg), axis=1)
    # Combining the two images vertically
    new_img = np.concatenate((top_img, bottom_img), axis=0)
    return new_img

# add a 30 pixel border of black pixels
def addBorder(img):
    # ((top, bottom),(left, right))
    new_img = np.pad(img, ((30, 30), (30, 30), (0, 0)))
    return new_img
    

def duplicate(img):
    newimage = img.copy()
    return newimage

cat = im.imread("hotcat.jpg")
copycat = duplicate(cat)
plt.imshow(copycat)
plt.show()
print(copycat.shape)

# 2.
# Using the developed functions, create an image with the hotcat flipped in four directions, 
# and with borders around each image 
# and also around the overall image. Print the shapes of the original and final images. (1 mark)
fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(8, 4))
# orignial 
ax1.imshow(cat)
# add pad
padcat = addBorder(cat)
# create image with 4 and add pad
flip4Img = flip4ways(padcat)
flip4ImgPad = addBorder(flip4Img)
ax2.imshow(flip4ImgPad)
plt.show()


print(f"Original image shape {cat.shape}")
#print(padcat.shape)
#print(flip4Img.shape)
print(f"Final image shape {flip4ImgPad.shape}")
