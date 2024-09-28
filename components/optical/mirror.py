from pyx import path, style, color, deco
from .base import OpticalComponent
from utils import compute_intersected_beam

class Mirror(OpticalComponent):
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
        
        # inner box that reflects the beam
        inner_box = path.path(
            path.moveto(*self._rp(-width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height / 2)),
            path.lineto(*self._rp(width / 2, -height)),
            path.lineto(*self._rp(-width / 2, -height)),
            path.closepath()
        )

        new_beam = compute_intersected_beam(beam, outer_box)
        if new_beam is None:
            return beam, None
        # print(f"INCIDENT: {angle} | NORMAL : {self.angle} | REFLECTED: {2 * self.angle - angle + 180}")
        return new_beam, [(2 * self.angle - angle + 180) % 360]
        # return new_beam, None
        
    def draw(self, c):
        height = self.dims[0]
        width  = self.dims[1]
        
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
        
        