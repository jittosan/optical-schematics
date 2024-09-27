from .base import MagnetometryComponent
from pyx import path, color, style

class RbCell(MagnetometryComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)
        
    def draw(self, c):
        size = 1

        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2)),
            path.lineto(*self._rp(-size / 2, size / 2)),
            path.closepath()
        )
        c.fill(outer_box, [color.rgb.blue, color.transparency(0.8)])
        c.stroke(outer_box, [style.linewidth.Thick])