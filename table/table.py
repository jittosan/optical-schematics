
import matplotlib as plt    

class OpticalTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def draw(self):
        fig, ax = plt.subplots()
        # Draw table as a grid of very small dots
        ax.set_aspect('equal')
        for x in range(self.cols):
            for y in range(self.rows):
                ax.plot(x, y, 'ko', markersize=2)  # Small black dots as mounting holes
        
        # Draw components
        for component in self.components:
            component.draw(ax)
        
        ax.set_xlim(-1, self.cols)
        ax.set_ylim(-1, self.rows)
        plt.show()