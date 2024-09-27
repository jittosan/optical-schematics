from pyx import canvas, path, deco, style, color
import numpy as np
from math import cos, sin

c = canvas.canvas()

# Draw a simple optical schematic with lenses and mirrors

# # Draw a lens
# c.stroke(path.circle(2, 2, 0.5), [style.linewidth.Thick, deco.filled([color.rgb.blue])])

# # Draw a mirror
# c.stroke(path.line(4, 1, 4, 3), [style.linewidth.Thick])
# c.stroke(path.line(4, 1, 3.5, 1.5), [style.linewidth.Thick])
# c.stroke(path.line(4, 3, 3.5, 2.5), [style.linewidth.Thick])

# # Draw a light ray
# c.stroke(path.line(0, 2, 2, 2), [style.linewidth.Thick, style.linestyle.dashed])
# c.stroke(path.line(2, 2, 4, 2), [style.linewidth.Thick, style.linestyle.dashed])

class OpticalComponent:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle # in degrees
        
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def place(self, x, y):
        self.x = x
        self.y = y
        
    def orient(self, angle):
        self.angle = angle
        
    def _rp(self, x, y):
        return (self.x + x * cos(self._radians(self.angle)) - y * sin(self._radians(self.angle)), self.y + x * sin(self._radians(self.angle)) + y * cos(self._radians(self.angle)))
    
    def _radians(self, angle):
        return angle * 3.14159 / 180
    
    def draw(self, c):
        raise NotImplementedError("This method should be overridden by subclasses")

class Iris(OpticalComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 1
        width  = 2
        
        # Draw the rotated lines
        for i in [-1, 1]:
            for j in [-1, 1]:
                x1, y1 = self._rp(i * width / 2, height / 2)
                x2, y2 = self._rp(j * width / 2, -1 * height / 2)
                c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thick])
        
class Mirror(OpticalComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.5
        width  = 2
        
        # Draw the bounding box
        for i in [-1, 1]:
            for j in [-1, 1]:
                x1, y1 = self._rp(i * width / 2, j * height / 2)
                x2, y2 = self._rp(j * width / 2, -i * height / 2)
                c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thick])
                
        # Draw the mirror line
        x1, y1 = self._rp(-1 * width / 2, height / 4)
        x2, y2 = self._rp(1 * width / 2, height / 4)
        c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thick])
        
        # Draw the hashed strokes
        for i in np.linspace(0, width, 20):
            x1, y1 = self._rp(-1 * width / 2 + i, height / 2)
            x2, y2 = self._rp(-1 * width / 2 + i + width* 2/20, height / 4)
            c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thin])
        
        
class BeamSplitter(OpticalComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)

    def draw(self, c):
        size = 2
        
        # Draw the bounding box
        for i in [-1, 1]:
            for j in [-1, 1]:
                x1, y1 = self._rp(i * size / 2, j * size / 2)
                x2, y2 = self._rp(j * size / 2, -i * size / 2)
                c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thick])
                
        # Draw the beam split line
        x1, y1 = self._rp(size / 2, size / 2)
        x2, y2 = self._rp(-1 * size / 2, - size / 2)
        c.stroke(path.line(x1, y1, x2, y2), [style.linewidth.Thick])
        
class Polariser(OpticalComponent):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, c):
        c.stroke(path.rect(self.x, self.y, self.width, self.height), [style.linewidth.Thick])
        for i in range(5):
            c.stroke(path.line(self.x, self.y + i * (self.height / 5), self.x + self.width, self.y + i * (self.height / 5)), [style.linewidth.Thick])

class Collimator(OpticalComponent):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, c):
        c.stroke(path.circle(self.x, self.y, self.radius), [style.linewidth.Thick])

class Grid:
    def __init__(self, x_start, y_start, x_end, y_end, spacing, show_grid=True):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.spacing = spacing
        self.show_grid = show_grid

    def draw(self, c):
        if self.show_grid:
            for x in range(self.x_start, self.x_end + 1, self.spacing):
                for y in range(self.y_start, self.y_end + 1, self.spacing):
                    c.fill(path.circle(x, y, 0.05), [color.rgb.black])

# Draw a white background
c.fill(path.rect(0, 0, 12, 4), [color.rgb.white])

# Create and draw the grid
grid = Grid(0, 0, 12, 4, 1, show_grid=True)
# grid.draw(c)

# Create instances of the components
mirror = Mirror(4, 1, 2)
beam_splitter = BeamSplitter(6, 1, 1)
polariser = Polariser(8, 1, 1, 2)
collimator = Collimator(10, 2, 0.5)
iris = Iris(2, 2, 45)
beam_splitter.rotate(20)
mirror.rotate(30)

# Draw the components
mirror.draw(c)
beam_splitter.draw(c)
# polariser.draw(c)
# collimator.draw(c)
iris.draw(c)

c.writeSVGfile("output.svg")