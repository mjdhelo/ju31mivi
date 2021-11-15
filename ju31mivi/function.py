import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):

    img = Image.fromarray(X)
    if resize is not None:
        img = img.resize(resize)
    img.show()
    return img
    