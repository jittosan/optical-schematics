from pyx import path, style, color, deco
from .base import OpticalComponent
from utils import compute_intersected_beam

class EndBlock(OpticalComponent):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        # [height, width]
        self.dims = [0.5, 2]
        
    def interact(self, beam, angle):
        height = self.dims[0]
        width  = self.dims[1]
        
        # outer box that stops propagation
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height)),
            path.lineto(*self._rp(width / 2, -height)),
            path.lineto(*self._rp(width / 2, 0)),
            path.lineto(*self._rp(-width / 2, 0)),
            path.closepath()
        )

        new_beam = compute_intersected_beam(beam, outer_box)
        if new_beam is None:
            return beam, None
        return new_beam, None

    def draw(self, c):
        height = self.dims[0]
        width  = self.dims[1]
        
        # Draw the bounding box
        outer_box = path.path(
            path.moveto(*self._rp(-width / 2, -height/2)),
            path.lineto(*self._rp(width / 2, -height/2)),
            path.lineto(*self._rp(width / 2, height/2)),
            path.lineto(*self._rp(-width / 2, height/2)),
            path.closepath()
        )
        c.stroke(outer_box, [style.linewidth.Thick, deco.filled([color.rgb.black])])