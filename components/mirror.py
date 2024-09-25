import matplotlib.pyplot as plt
import numpy as np
from .base import OpticalComponent

class Mirror(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__('Mirror', x, y, angle)

    def draw(self, ax):
        width = 0.2
        height = 0.6
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='lightgray', hatch='//', lw=2)
        ax.add_patch(rect) 