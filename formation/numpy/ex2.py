import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def zoom(image, factor):
    x, y = image.shape
    newX = int(x * factor)
    newY = int(y * factor)

    image = image[newX:x - newX, newY:y - newY]
    plt.imshow(image, cmap=plt.cm.gray)
    plt.show()

def main():
    face = misc.face(gray=True)
    zoom(face, 0.25)

if __name__ == "__main__":
    main()