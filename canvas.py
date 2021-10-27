import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with user values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)