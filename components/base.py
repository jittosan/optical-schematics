
import numpy as np
from matplotlib.transforms import Affine2D

class OpticalComponent():
    def __init__(self, name, x, y, angle):
        self.name = name
        self.x = x
        self.y = y
        self.angle = angle
    
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def place(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, ax):
        pass  # To be overridden by subclasses for different components
        
    def _compute_rotation(self, patch):
        """ Rotate the symbol of a component around its center by an angle. """
        transform = Affine2D().rotate_deg_around(self.x, self.y, angle) + ax.transData
        patch.set_transform(transform)
        return patch