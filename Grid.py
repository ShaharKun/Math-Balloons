import turtle as t
import numpy as np
from Pen import Pen, onmove
from Pixel import Pixel

'''
The collection of all 784 pixels,
saved by rows in a list called pixels.
here we export the grid when we need a prediction,
and use the load model to do so.
'''

class Grid:
    def __init__(self, game, screen, rows, cols, model):
        self.wn = screen
        self.num_rows = rows
        self.num_cols = cols
        self.model = model
        self.pixels = [[] for row in range(rows)]

        self.pixel_gap = 560 / self.num_cols

        self.get_x = lambda col: self.pixel_gap * col + 10
        self.get_y = lambda row: -self.pixel_gap * row + 270


        for row in range(rows):
            for col in range(cols):
                pixel = Pixel(self, row, col)

        self.pen = Pen(screen=self.wn, grid=self)
        self.game = game


    def initialize_all_pixels(self):
        ''' One-time only '''
        for row in self.pixels:
            for pixel in row:
                pixel.neighbors = pixel.get_neighbors()



    def listen_to_user(self):
        ''' Use the implemented pen. '''
        onmove(self.pen.wn, self.pen.move_handler)
        self.pen.onclick(self.pen.click_handler)

        t.listen()


    def color_clicked_pixel(self, x, y):
        '''
        Using the mouse cord, find the pixel that
        is clicked, and color it (and it's neighbors).
        '''
        col = int(x - 280) // int(self.pixel_gap)
        row = int(y) // int(self.pixel_gap)

        # Convert to correct values
        row = -row + 13
        col = col + 14

        if row < 0 or col < 0: # Avoid errors and wrong indexing
            return

        self.pixels[row][col].draw(x, y)


    def convert_location(self, row, col):
        x = self.get_x(col)
        y = self.get_y(row)

        return (x, y)


    def export_grid(self):
        '''
        Export the grid to a numpy array that will
        be feeded to the Neural Network.
        '''
        all_pixels = [[] for row in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.pixels[row][col].is_colored:
                    all_pixels[row].append(1)
                else:
                    all_pixels[row].append(0)


        pixel_array = np.array(all_pixels)
        pixel_array = pixel_array.reshape(1, 28, 28, 1)
        pixel_array = pixel_array.astype('float32')

        return pixel_array


    def make_a_prediction(self):

        input_grid = self.export_grid()

        prediction = self.model.predict(input_grid)
        if max(prediction[0]) < 0.25: # Don't take bad decisions
            result = None
        else:
            result = np.argmax(prediction[0])

        if result != None:
            for balloon in self.game.balloons:
                if balloon.value == result:
                    balloon.kill()

        #print("Prediction: {}".format(result))

        # Get ready for the next drawing
        self.reset()


    def reset(self):
        ''' Uncolor all pixels. '''
        for row in self.pixels:
            for pixel in row:
                pixel.is_colored = False
                pixel.ht()
