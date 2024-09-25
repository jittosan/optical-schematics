import matplotlib.pyplot as plt
import numpy as np

class OpticalComponent:
    def __init__(self, name, x, y, orientation):
        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation
    
    def draw(self, ax):
        pass  # To be overridden by subclasses for different components

    def rotate(self, angle, center):
        """ Rotate component position and orientation """
        # Rotation matrix
        angle_rad = np.radians(angle)
        cos_theta, sin_theta = np.cos(angle_rad), np.sin(angle_rad)

        # Translate point to origin
        x_new = self.x - center[0]
        y_new = self.y - center[1]

        # Rotate coordinates
        x_rot = x_new * cos_theta - y_new * sin_theta
        y_rot = x_new * sin_theta + y_new * cos_theta

        # Translate point back
        self.x = x_rot + center[0]
        self.y = y_rot + center[1]

        # Rotate orientation (optional, if applicable)
        self.orientation = (self.orientation + angle) % 360
# Mirror component with shading
class Mirror(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Mirror', x, y, orientation)

    def draw(self, ax):
        width = 0.2
        height = 0.6
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='lightgray', hatch='//', lw=2)
        ax.add_patch(rect)

# Laser component with green beam
class Laser(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Laser', x, y, orientation)
    
    def draw(self, ax):
        width = 0.5
        height = 0.2
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='darkgray', hatch='x', lw=2)
        ax.add_patch(rect)
        ax.plot([self.x + width/2, self.x + 1.5], [self.y, self.y], color='green', lw=2)

# Polarizing Beam Splitter (PBS) as a rectangle with cross hatching
class PolarizingBeamSplitter(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Polarizing Beam Splitter', x, y, orientation)

    def draw(self, ax):
        width = 0.4
        height = 0.4
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='white', hatch='++', lw=2)
        ax.add_patch(rect)

# Quarter Wave Plate as a circle with dotted fill
class QuarterWavePlate(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Quarter Wave Plate', x, y, orientation)

    def draw(self, ax):
        circle = plt.Circle((self.x, self.y), 0.3, edgecolor='black', facecolor='none', hatch='..', lw=2)
        ax.add_patch(circle)

# Half Wave Plate as a circle with diagonal hatching
class HalfWavePlate(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Half Wave Plate', x, y, orientation)

    def draw(self, ax):
        circle = plt.Circle((self.x, self.y), 0.3, edgecolor='black', facecolor='none', hatch='//', lw=2)
        ax.add_patch(circle)

# Iris as a black circle with an empty center
class Iris(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Iris', x, y, orientation)

    def draw(self, ax):
        outer_circle = plt.Circle((self.x, self.y), 0.4, edgecolor='black', facecolor='black', lw=2)
        inner_circle = plt.Circle((self.x, self.y), 0.1, edgecolor='black', facecolor='white', lw=2)
        ax.add_patch(outer_circle)
        ax.add_patch(inner_circle)

# Collimator as a rectangle with horizontal hatching
class Collimator(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('Collimator', x, y, orientation)

    def draw(self, ax):
        width = 0.4
        height = 0.2
        rect = plt.Rectangle((self.x - width/2, self.y - height/2), width, height, edgecolor='black', facecolor='none', hatch='-', lw=2)
        ax.add_patch(rect)

# End Block as a solid black square
class EndBlock(OpticalComponent):
    def __init__(self, x, y, orientation):
        super().__init__('End Block', x, y, orientation)

    def draw(self, ax):
        width = 0.4
        rect = plt.Rectangle((self.x - width/2, self.y - width/2), width, width, edgecolor='black', facecolor='black', lw=2)
        ax.add_patch(rect)


class OpticalTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def draw(self):
        fig, ax = plt.subplots()
        # Draw table as a grid of very small dots
        ax.set_aspect('equal')
        for x in range(1, self.cols+1):
            for y in range(1, self.rows+1):
                ax.plot(x, y, 'ko', markersize=2)  # Small black dots as mounting holes
        
        # Draw components
        for component in self.components:
            component.draw(ax)
        
        ax.set_xlim(0, self.cols+1)
        ax.set_ylim(0, self.rows+1)
        # plt.grid()
        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
        ax.tick_params(left=False, bottom=False, labelleft=True, labelbottom=False)
        plt.show()
        
    def rotate(self, angle):
        """ Rotate all components and the optical grid by an angle """
        center = (self.cols / 2, self.rows / 2)  # Rotate around the center of the grid
        for component in self.components:
            component.rotate(angle, center)


table = OpticalTable(10, 6)

# Components (You can use any of the previously defined components like Mirror, Laser, etc.)
mirror1 = Mirror(2, 3, 0)
laser = Laser(1, 2, 0)

# Add components to the table
table.add_component(mirror1)
table.add_component(laser)

# Rotate the optical table and components by 45 degrees
table.rotate(45)

# Draw the rotated optical setup
table.draw()