from pyx import path, style, color, deco
from .base import OpticalComponent

class Mirror(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.5
        width  = 2
        
        # Draw the inner box
        inner_box = path.path(
            path.moveto(*self._rp(-width / 2, height / 2)),
            path.lineto(*self._rp(width / 2, height / 2)),
            path.lineto(*self._rp(width / 2, height / 4)),
            path.lineto(*self._rp(-width / 2, height / 4)),
            path.closepath()
        )
        c.stroke(inner_box, [style.linewidth.Thick, deco.stroked([color.grey(0.5)])])
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, height / 2)),
            path.lineto(*self._rp(-width / 2, height / 2)),
            path.closepath()
        )
        c.stroke(outer_box, [style.linewidth.Thick])