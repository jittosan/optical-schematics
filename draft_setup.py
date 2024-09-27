from components import *
from setup import OpticalTable
from pyx import path, color

setup = OpticalTable(50, 50)
setup.points = True

# position all components
setup.add(Laser(14, 0, 0))
setup.add(Mirror(30, 0, 45))
setup.add(Mirror(30, 5, 45+90))
setup.add(Mirror(24, 5, -45))
setup.add(Polariser(24, 8, 0))
setup.add(PolarisingBeamSplitter(24, 12, 0))
setup.add(Polariser(24, 16, 0))
setup.add(EndBlock(30, 12, 90))
setup.add(Mirror(24, 42, 180))

setup.add(Laser(1, 10, 90))
setup.add(Mirror(1, 25, 180+45))
setup.add(Mirror(5, 25, 45))
setup.add(Mirror(5, 30, 180+45))
setup.add(Polariser(8, 30, 90))
setup.add(PolarisingBeamSplitter(11, 30, -90))
setup.add(Collimator(14, 30, -90))
setup.add(EndBlock(11, 25, 0))

# include magnetometry components
setup.add(MuMetalShield(24, 30, 0))
setup.add(FerriteShield(24, 30, 0))
setup.add(RbCell(24, 30, 0))

# save
setup.save("draft_setup")