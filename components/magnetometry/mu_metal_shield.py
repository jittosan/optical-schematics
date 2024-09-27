from .base import MagnetometryComponent
from pyx import path, color, style

class MuMetalShield(MagnetometryComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)
        
    def draw(self, c):
        outer_height = 20
        outer_width = 14
        layer_gap = 0.2
        optical_access_width = 2
        
        # draw outline of box with optical gaps in the middle of each axis
        # innermost box
        for i in range(3):
            height = outer_height - 2*i*layer_gap
            width = outer_width - 2*i*layer_gap
            c.stroke(path.path(path.moveto(*self._rp(-width/2, -height/2)),
                            path.lineto(*self._rp(-width/2, -optical_access_width/2)),
                            path.moveto(*self._rp(-width/2, optical_access_width/2)),
                            path.lineto(*self._rp(-width/2, height/2)),
                            path.lineto(*self._rp(-optical_access_width/2, height/2)), 
                            path.moveto(*self._rp(optical_access_width/2, height/2)), 
                            path.lineto(*self._rp(width/2, height/2)),
                            path.lineto(*self._rp(width/2, optical_access_width/2)),
                            path.moveto(*self._rp(width/2, -optical_access_width/2)),
                            path.lineto(*self._rp(width/2, -height/2)),
                            path.lineto(*self._rp(optical_access_width/2, -height/2)), 
                            path.moveto(*self._rp(-optical_access_width/2, -height/2)),
                            path.lineto(*self._rp(-width/2, -height/2)), 
                            path.closepath()),
                        [style.linewidth.Thick, color.rgb.black])