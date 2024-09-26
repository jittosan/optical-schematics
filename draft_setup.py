from components import *
from table import OpticalTable
from pyx import path, color

setup = OpticalTable(30, 30)
setup.points = True

# position all components
setup.add(Laser(0, 0, 0))
setup.add(Mirror(20, 0, 45))
setup.add(Mirror(20, 5, 45+90))
setup.add(Mirror(10, 5, -45))
setup.add(PolarisingBeamSplitter(10, 10, 0))
setup.add(EndBlock(5, 10, 90))

setup.add(Laser(0, 5, 90))
setup.add(Mirror(0, 25, 180+45))
setup.add(Iris(5, 25, 90))

# save
setup.save("draft_setup")