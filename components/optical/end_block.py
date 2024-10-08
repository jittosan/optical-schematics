from pyx import path, style, color, deco
from .base import OpticalComponent

class EndBlock(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.5
        width  = 2
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, 0)),
            path.lineto(*self._rp(width / 2, 0)),
            path.lineto(*self._rp(width / 2, height)),
            path.lineto(*self._rp(-width / 2, height)),
            path.closepath()
        )
        c.stroke(outer_box, [style.linewidth.Thick, deco.filled([color.rgb.black])])