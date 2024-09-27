from math import sin, cos, pi
from pyx import path, style, color, deco
from .base import OpticalSource

class Laser(OpticalSource):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        # [height, width, source_height, source_width]
        self.dims = [2, 1, 0.2, 0.5]
        
    def source(self):
        x, y = self._rp(0, self.dims[0] / 2)
        return x, y, self.angle

    def draw(self, c):
        height = self.dims[0]
        width  = self.dims[1]
        source_height = self.dims[2]
        source_width = self.dims[3]
        
        # Draw the source
        laser_source = path.path(
            path.moveto(*self._rp(-source_width / 2, height / 2 - source_height)),
            path.lineto(*self._rp(source_width / 2, height / 2 - source_height)),
            path.lineto(*self._rp(source_width / 2, height / 2)),
            path.lineto(*self._rp(-source_width / 2, height / 2)),
            path.closepath()
        )
        c.fill(laser_source, [color.rgb.black])
        c.stroke(laser_source, [style.linewidth.Thick])
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, height / 2 - source_height)),
            path.lineto(*self._rp(-width / 2, height / 2 - source_height)),
            path.closepath()
        )
        c.fill(outer_box, [color.rgb.white])
        c.stroke(outer_box, [style.linewidth.Thick])