from pyx import canvas, path, style, color, deco
from pyx import bitmap
import os

class OpticalTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.components = []
        self.grid = False
        self.points = False
        self.canvas_padding = 3
    
    def add(self, component):
        self.components.append(component)
    
    def draw(self):
        # Create a canvas
        c = canvas.canvas()
        # put a white background
        c.fill(path.rect(-self.canvas_padding, -self.canvas_padding, self.cols+2*self.canvas_padding, self.rows+2*self.canvas_padding), [color.rgb.white])
        # if grid is enabled
        if self.grid:
            for i in range(self.rows):
                c.stroke(path.line(0, i, self.cols, i), [style.linewidth.Thin, color.grey(0.8)])
            for i in range(self.cols):
                c.stroke(path.line(i, 0, i, self.rows), [style.linewidth.Thin, color.grey(0.8)])
        # if points are enabled
        if self.points:
            for i in range(self.rows):
                for j in range(self.cols):
                    c.fill(path.circle(i, j, 0.1), [color.grey(0.8)])
        
        # draw out all components
        for component in self.components:
            component.draw(c)
        # Return the canvas
        # display canvas
        return c
    
    def save(self, filename):
        # Save the canvas as a PNG file
        c = self.draw()
        # filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        # c.writeGSfile(filename, device="png16m")
        c.writeSVGfile(filename)
        
        
    def propagate(self):
        pass