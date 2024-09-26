
from math import cos, sin

class OpticalComponent:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle # in degrees
        self.dims = []
        
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def place(self, x, y):
        self.x = x
        self.y = y
        
    def orient(self, angle):
        self.angle = angle % 360
        
    def _rp(self, x, y):
        return self.x + x * cos(self._radians(self.angle)) - y * sin(self._radians(self.angle)), self.y + x * sin(self._radians(self.angle)) + y * cos(self._radians(self.angle))
    
    def _radians(self, angle):
        return angle * 3.14159 / 180
    
    def scale(self, scale):
        self.dims = [dim * scale for dim in self.dims]
    
    def draw(self, c):
        raise NotImplementedError("This method should be overridden by subclasses")