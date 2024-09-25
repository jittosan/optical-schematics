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
        for x in range(self.cols):
            for y in range(self.rows):
                ax.plot(x, y, 'ko', markersize=2)  # Small black dots as mounting holes
        
        # Draw components
        for component in self.components:
            component.draw(ax)
        
        ax.set_xlim(-1, self.cols)
        ax.set_ylim(-1, self.rows)
        plt.show()


# Example usage:
table = OpticalTable(10, 6)

# Components
mirror1 = Mirror(2, 3, 0)
laser = Laser(1, 2, 0)
pbs = PolarizingBeamSplitter(4, 3, 0)
qwp = QuarterWavePlate(6, 2, 0)
hwp = HalfWavePlate(6, 4, 0)
iris = Iris(8, 3, 0)
collimator = Collimator(9, 2, 0)
end_block = EndBlock(9, 4, 0)

# Add components to the table
table.add_component(mirror1)
table.add_component(laser)
table.add_component(pbs)
table.add_component(qwp)
table.add_component(hwp)
table.add_component(iris)
table.add_component(collimator)
table.add_component(end_block)

# Draw the optical setup
table.draw()
