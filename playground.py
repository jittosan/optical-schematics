from components import *
from setup import OpticalSystem
from pyx import canvas, path, color

c = canvas.canvas()
# Draw a white background
# c.fill(path.rect(0, 0, 12, 4), [color.rgb.white])

# Draw a simple optical schematic with lenses and mirrors
mirror = Mirror(4, -6, 30)
# mirror.draw(c)
laser = Laser(8, 2, 0)
laser.draw(c)
collimator = Collimator(4, 2, 130)
# collimator.draw(c)
iris = Iris(0, 2, 0)
# iris.draw(c)



# save the canvas to a file
c.writeSVGfile("playground")