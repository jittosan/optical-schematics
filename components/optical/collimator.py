from pyx import path, style, color, deco, pattern
from .base import OpticalComponent

class Collimator(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.2
        width  = 2
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, 0)),
            path.lineto(*self._rp(width / 2, 0)),
            path.lineto(*self._rp(width / 2, height)),
            path.arc(*self._rp(0, height), width / 2, self.angle + 0, self.angle + 180),
            path.closepath()
        )
        # define shading pattern ? 
        c.fill(outer_box, [color.gray(0.8)])
        c.stroke(outer_box, [style.linewidth.Thick, color.rgb.black])