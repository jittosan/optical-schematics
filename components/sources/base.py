from ..optical import OpticalComponent


class OpticalSource(OpticalComponent):
    def __init__(self, x=0, y=0, angle=0):
        super().__init__(x, y, angle)
        
    def draw(self, c):
        raise NotImplementedError("This method must be implemented by the subclass.")
    