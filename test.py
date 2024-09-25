import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import Affine2D

class OpticalComponent:
    def __init__(self, name, x, y, orientation):
        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation
    
    def draw(self, ax, rotation_angle=0):
        pass  # To be overridden by subclasses for different components

    def rotate_symbol(self, ax, patch, angle):
        """ Rotate the symbol of a component around its center by an angle. """
        transform = Affine2D().rotate_deg_around(self.x, self.y, angle) + ax.transData
        patch.set_transform(transform)
        return patch

# Mirror component
class Mirror(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Mirror', x, y, orientation)

    def draw(self, ax, rotation_angle=0):
        width = 0.2
        height = 0.6
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='lightgray', lw=2)
        # Rotate the symbol by the specified rotation angle
        rect = self.rotate_symbol(ax, rect, rotation_angle)
        ax.add_patch(rect)

# Laser component with green beam
class Laser(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Laser', x, y, orientation)
    
    def draw(self, ax, rotation_angle=0):
        width = 0.5
        height = 0.2
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='darkgray', lw=2)
        rect = self.rotate_symbol(ax, rect, rotation_angle)
        ax.add_patch(rect)

        # Draw laser beam in green (this stays horizontal for simplicity, but can also be rotated)
        if rotation_angle == 0:  # Horizontal beam
            ax.plot([self.x + width/2, self.x + 1.5], [self.y, self.y], color='green', lw=2)
        # If you'd like to rotate the beam, apply the same rotation to the beam direction

# Optical Table class (with rotation at the component level)
class OpticalTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)

    def draw(self, rotation_angle=0):
        fig, ax = plt.subplots()
        # Draw table as a grid of very small dots
        ax.set_aspect('equal')
        for x in range(self.cols):
            for y in range(self.rows):
                ax.plot(x, y, 'ko', markersize=2)  # Small black dots as mounting holes
        
        # Draw components with their rotation angle
        for component in self.components:
            component.draw(ax, rotation_angle)
        
        ax.set_xlim(-1, self.cols)
        ax.set_ylim(-1, self.rows)
        plt.show()

# Example usage:
table = OpticalTable(10, 6)

# Add components
mirror = Mirror(2, 3, 0)  # Horizontal mirror
laser = Laser(5, 4, 0)    # Horizontal laser

table.add_component(mirror)
table.add_component(laser)

# Draw table with components rotated by 45 degrees around their centers
table.draw(rotation_angle=20)
