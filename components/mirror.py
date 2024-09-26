from pyx import path, style, color, deco
from .base import OpticalComponent

class Mirror(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.5
        width  = 2
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height)),
            path.lineto(*self._rp(width / 2, -height)),
            path.lineto(*self._rp(width / 2, 0)),
            path.lineto(*self._rp(-width / 2, 0)),
            path.closepath()
        )
        c.fill(outer_box, [color.rgb.white])
        c.stroke(outer_box, [style.linewidth.Thick])
        
        # Draw the inner box
        inner_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height)),
            path.lineto(*self._rp(-width / 2, -height)),
            path.closepath()
        )
        c.fill(inner_box, [color.rgb.black])
        c.stroke(inner_box, [style.linewidth.Thick])
        
        