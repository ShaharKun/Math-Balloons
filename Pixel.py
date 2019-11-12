from turtle import Turtle

'''
One of the 784 (28 x 28) Pixels used in the grid
that the digits are drawn at.
A pixel can be either colored (1) or oncolored (0),
eventually, we take all 784 pixels and feed them
to the Neural Network.
'''

class Pixel(Turtle):
    def __init__(self, grid, row, col):
        super().__init__()

        self.grid = grid
        self.row = row
        self.col = col
        self.is_colored = False
        self.neighbors = []

        self.penup()
        self.shape('square')
        self.ht()
        self.shapesize(1)

        self.setpos(self.grid.convert_location(row, col))

        self.grid.pixels[row].append(self)


    def get_neighbors(self):
        ''' Get the neighbors to more easily draw 28 x 28 images '''
        neighbors = []

        # Top Layer
        if not self.row == 0:
            # Up
            neighbors.append(self.grid.pixels[self.row - 1][self.col])

            # Top Right
            if not self.col == self.grid.num_cols - 1:
                neighbors.append(self.grid.pixels[self.row - 1][self.col + 1])

            # Top Left
            if not self.col == 0:
                neighbors.append(self.grid.pixels[self.row - 1][self.col - 1])

        # Right Layer
        if not self.col == self.grid.num_cols - 1:
            # Right
            neighbors.append(self.grid.pixels[self.row][self.col + 1])

            # Bottom Right
            if not self.row == self.grid.num_rows - 1:
                neighbors.append(self.grid.pixels[self.row + 1][self.col + 1])

        # Bottom Layer
        if not self.row == self.grid.num_rows - 1:
            # Bottom
            neighbors.append(self.grid.pixels[self.row + 1][self.col])

            # Bottom Left
            if not self.col == 0:
                neighbors.append(self.grid.pixels[self.row + 1][self.col - 1])

        # Left Layer
        if not self.col == 0:
            # Left
            neighbors.append(self.grid.pixels[self.row][self.col - 1])

        return neighbors


    def draw(self, x, y, on_neighbors=True):
        ''' Color the pixel. '''
        self.st()
        self.is_colored = True

        if on_neighbors:
            for neighbor in self.neighbors:
                if not neighbor.is_colored:
                    neighbor.draw(x, y, on_neighbors=False)
