from components import *
from pyx import canvas, path, color

# position all components
pump_laser = Laser(0, 0, 0)
mirror_1 = Mirror(20, 0, 45)
mirror_2 = Mirror(20, 5, 45+90)
mirror_3 = Mirror(10, 5, -45)
pbs = PolarisingBeamSplitter(10, 10, 0)
end_1 = EndBlock(5, 10, 90)

probe_laser = Laser(0, 5, 90)
mirror_4 = Mirror(0, 25, 180+45)
iris = Iris(5, 25, 90)


# draw out components
c = canvas.canvas()

setup_components = [pump_laser, probe_laser, mirror_1, mirror_2, mirror_3, pbs, end_1, mirror_4, iris]
for component in setup_components:
    component.draw(c)

# save the canvas to a file
c.writeSVGfile("draft_setup")