from components import *
from setup import OpticalTable
from pyx import path, color

setup = OpticalTable(50, 50)
setup.points = True

# position all components
setup.attach("Pump Laser", Laser(14, 0, 90))
setup.attach("Mirror1", Mirror(30, 0, -45))
setup.attach("Mirror2", Mirror(30, 5, -135))
setup.attach("Mirror3", Mirror(24, 5, 45))
setup.attach("Polariser1", Polariser(24, 8, 0))
setup.attach("PBS1", PolarisingBeamSplitter(24, 12, 0))
setup.attach("Polariser2", Polariser(24, 16, 0))
setup.attach("EndBlock1", EndBlock(30, 12, -90))
setup.attach("EndBlock2", EndBlock(20, 12, 90))
setup.attach("Mirror4", Mirror(24, 42, 180))

setup.attach("Probe Laser", Laser(1, 10, 0))
setup.attach("Mirror5", Mirror(1, 25, 135))
setup.attach("Mirror6", Mirror(5, 25, -45))
setup.attach("Mirror7", Mirror(5, 30, 135))
setup.attach("Polariser3", Polariser(8, 30, 90))
setup.attach("PBS2", PolarisingBeamSplitter(11, 30, -90))
setup.attach("Collimator1", Collimator(14, 30, 90))
setup.attach("EndBlock3", EndBlock(11, 25, 0))

# include magnetometry components
setup.attach("MuMetalShield1", MuMetalShield(24, 30, 0))
setup.attach("FerriteShield1", FerriteShield(24, 30, 0))
setup.attach("RbCell1", RbCell(24, 30, 0))

# activate pump and probe beams
setup.activate("Pump Laser")
setup.activate("Probe Laser")

# save
setup.save("draft_setup")