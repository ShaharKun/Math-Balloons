import turtle as t

'''
This is the pen that draws on the grid.
To make it follow the mouse,
we rewrite turtle's onmove function (from the Screen object)
to follow the mouse.
whenever the left-mouse-button is clicked (or dragged)
we color the pixel (and it's neighbors) that are wanted.
'''

def onmove(self, fun, add=None):
    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)


class Pen(t.Turtle):
    def __init__(self, screen, grid):
        super().__init__()
        self.wn = screen
        self.grid = grid
        self.penup()
        self.moving, self.dragging = 0, 1

        self.state = self.moving

        # Get the pencil image
        self.pencil_image = './assets/pencil.gif'
        self.wn.register_shape(self.pencil_image)

        self.shape(self.pencil_image)


    def move_handler(self, x, y):
        if self.state != self.moving:  # ignore stray events
            return

        onmove(self.wn, None)  # avoid overlapping events
        self.goto(x + self.shapesize()[0] * 3, y)
        onmove(self.wn, self.move_handler)


    def click_handler(self, x, y):
        self.onclick(None)  # disable until release
        onmove(self.wn, None)  # disable competing handler

        self.onrelease(self.release_handler)  # watch for release event
        self.ondrag(self.drag_handler)  # motion is now dragging until release

        self.state = self.dragging


    def release_handler(self, x, y):
        self.onrelease(None)  # disable until click
        self.ondrag(None)

        self.onclick(self.click_handler)
        onmove(self.wn, self.move_handler)

        self.state = self.moving

        # When the pen is released, make a prediction on the current grid.
        self.grid.make_a_prediction()


    def drag_handler(self, x, y):
        if self.state != self.dragging:
            return

        self.ondrag(None)

        # Follow the mouse
        self.goto(x + self.shapesize()[0] * 3, y)
        # Color the pixels
        self.grid.color_clicked_pixel(x, y)

        self.ondrag(self.drag_handler)
