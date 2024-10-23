import math
from pyx import path

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

## PROPAGATION HELPER FUNCTIONS
def compute_source_beam_out(x, y, angle, x_max, y_max):
    dx = math.sqrt(x_max ** 2 + y_max ** 2) * math.sin(math.radians(angle))
    dy = math.sqrt(x_max ** 2 + y_max ** 2) * math.cos(math.radians(angle))
    if x + dx < 0:
        y_out = y + dy * (-x / dx)
        x_out = 0
    elif x + dx > x_max:
        y_out = y + dy * ((x_max - x) / dx)
        x_out = x_max
    elif y + dy < 0:
        x_out = x + dx * (-y / dy)
        y_out = 0
    elif y + dy > y_max:
        x_out = x + dx * ((y_max - y) / dy)
        y_out = y_max
    else:
        x_out = x + dx
        y_out = y + dy
    return x_out, y_out

def compute_outgoing_beam(beam, angle):
    x, y = beam.atbegin()
    ampl = 9999
    dx = ampl * math.sin(math.radians(angle))
    dy = ampl * math.cos(math.radians(angle))
    x_out, y_out = x+dx, y+dy
    return path.path(path.moveto(x, y), path.lineto(x_out, y_out))

def compute_intersected_beam(beam, component):
    l1, l2 = beam.intersect(component)
    ## FIND ANOTHER INTERSECTION IF THE FIRST ONE IS THE BEGINNING OF THE BEAM
    # if l1 != [] and l1[0] == 0:
    #     l1 = l1[1:]
    # if no intersect
    if l1 == []:
        return None
    # if intersect
    new_beam = path.path(path.moveto(*beam.atbegin()), path.lineto(*beam.at(l1[0])))
    # if new_beam.atend() == new_beam.atbegin():
    #     return None
    return new_beam