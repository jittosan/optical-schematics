from .beam_splitter import BeamSplitter
from pyx import path, style, color, deco

class PolarisingBeamSplitter(BeamSplitter):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        
    def draw(self, c):
        size = 2
        
        # draw diagonal line
        line = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2))
        )
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2)),
            path.lineto(*self._rp(-size / 2, size / 2)),
            path.closepath()
        )
        c.stroke(outer_box, [style.linewidth.Thick, deco.filled([deco.stroked([color.rgb.grey])])])