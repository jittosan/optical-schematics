from .beam_splitter import BeamSplitter
from pyx import path, style, color, deco
from utils import compute_intersected_beam

class PolarisingBeamSplitter(BeamSplitter):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        
    def interact(self, beam, angle):
        size = self.dims[0] / 2
        
        # define surface of interaction
        surface = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2))
        )
        new_beam = compute_intersected_beam(beam, surface)
        if new_beam is None:
            return beam, None
        return new_beam, [angle, (angle + 90) % 360]
        
    def draw(self, c):
        size = 2

        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2)),
            path.lineto(*self._rp(-size / 2, size / 2)),
            path.closepath()
        )
        c.fill(outer_box, [color.gray(0.8)])
        c.stroke(outer_box, [style.linewidth.Thick])
        
        # draw diagonal line
        line = path.path(
            path.moveto(*self._rp(-size / 2, -size / 2)),
            path.lineto(*self._rp(size / 2, size / 2))
        )
        c.stroke(line, [style.linewidth.Thick])
        