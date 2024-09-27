from math import sin, cos, pi
from pyx import path, style, color, deco
from .base import OpticalSource

class Laser(OpticalSource):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        
    def propagate(self, c):
        # define point source for laser, and the propagating beam vector
        width = 2
        source_x = self.x + width / 2
        source_y = self.y
        pt = path.path(path.moveto(*self._rp(source_x, source_y)))
        beam_vec = (sin(self.angle), cos(self.angle))

    def draw(self, c):
        height = 1
        width  = 2
        source_height = height / 2
        source_width = width / 10
        
        # Draw the source
        laser_source = path.path(
            path.moveto(*self._rp(width / 2, source_height / 2)),
            path.lineto(*self._rp(width / 2 - source_width, source_height / 2)),
            path.lineto(*self._rp(width / 2 - source_width, -source_height / 2)),
            path.lineto(*self._rp(width / 2, -source_height / 2)),
            path.closepath()
        )
        c.fill(laser_source, [color.rgb.black])
        c.stroke(laser_source, [style.linewidth.Thick])
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2 - source_width, -height / 2)),
            path.lineto(*self._rp(width / 2 - source_width, height / 2)),
            path.lineto(*self._rp(-width / 2, height / 2)),
            path.closepath()
        )
        c.fill(outer_box, [color.rgb.white])
        c.stroke(outer_box, [style.linewidth.Thick])