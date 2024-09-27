from pyx import canvas, path, style, color, unit
from utils import compute_source_beam_out, compute_outgoing_beam
from math import sin, cos, radians, sqrt
# import os

class OpticalTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.components = {}
        self.activated = []
        self.grid = False
        self.points = False
        self.canvas_padding = 3
        
    def get(self, name):
        return self.components[name][0]
    
    def attach(self, name, component):
        self.components[name] = component
        
    def detach(self, name):
        self.components.pop(name)
        
    def activate(self, name):
        self.activated.append(name)
        
    def deactivate(self, name):
        self.activated.remove(name)
    
    def draw(self):
        # Create a canvas
        bg = path.rect(-self.canvas_padding, -self.canvas_padding, self.cols+2*self.canvas_padding, self.rows+2*self.canvas_padding)
        c = canvas.canvas([canvas.clip(bg)])
        # put a white background
        c.fill(bg, [color.rgb.white])
        
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
        

            
        # propagate the beams
        for item in self.activated:
            component = self.components[item]
            try:
                x, y, angle = component.source()
                beam = compute_outgoing_beam(path.path(path.moveto(x, y)), angle)
            except AttributeError:
                raise AttributeError(f"Component {item} is not a radiation source")
            
            def propagate(beam, angle, skip_comp=None):
                # compute the end point of the beam if it were to go all the way across the table
                beam = compute_outgoing_beam(beam, angle)
                print(beam)
                new_angle = None
                new_skip_comp = skip_comp
                # check intersection of beam with all components
                for comp_name, component in self.components.items():
                    if comp_name == skip_comp:
                        continue
                    try:
                        intersection = component.interact(beam, angle, c)
                        # beam interacts with component
                        if intersection is not None:
                            int_beam, int_angle = intersection
                            # print(int_beam)
                            if int_beam is not beam:
                                beam = int_beam
                                new_angle = int_angle
                                new_skip_comp = comp_name
                    except AttributeError:
                        pass
                print('DONE:', beam, new_angle)
                # draw current beam segment
                c.stroke(beam, [color.rgb.red, style.linewidth(0.2)])
                # end propagation if new_angle is None
                if new_angle is None:
                    return
                # for each new angle, propagate the beam
                for a in new_angle:
                    return propagate(path.path(path.moveto(*beam.atend())), a, new_skip_comp)
                    pass
                
            # propagate from currently selected source component
            propagate(beam, angle, item)
            
            # draw out all components
            for component in self.components.values():
                component.draw(c)
        # Return the canvas
        return c
    
    def save(self, filename):
        # Save the canvas as a PNG file
        c = self.draw()
        # filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        # c.writeGSfile(filename, device="png16m")
        c.writeSVGfile(filename)
        