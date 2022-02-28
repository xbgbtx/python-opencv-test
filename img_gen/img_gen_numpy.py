import numpy as np


class ImgGenNumpy:

    def __init__(self, shape):
        self.img = np.zeros(shape, dtype=np.uint8)

    def get_frame(self):
        return self.img

    def add_frame(self, frame):
        np.copyto(self.img, frame)
