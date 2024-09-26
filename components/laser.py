from pyx import path, style, color, deco
from .base import OpticalComponent

class Laser(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def draw(self, c):
        height = 0.5
        width  = 2
        source_height = height / 2
        source_width = source_height / 2
        
        # Draw the source
        laser_source = path.path(
            path.moveto(*self._rp(width / 2, source_height / 2)),
            path.lineto(*self._rp(width / 2 + source_width, source_height / 2)),
            path.lineto(*self._rp(width / 2 + source_width, -source_height / 2)),
            path.lineto(*self._rp(width / 2, -source_height / 2)),
            path.closepath()
        )
        c.stroke(laser_source, [style.linewidth.Thick, deco.filled([color.rgb.black])])
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, height / 2)),
            path.lineto(*self._rp(-width / 2, height / 2)),
            path.closepath()
        )
        c.stroke(outer_box, [style.linewidth.Thick])