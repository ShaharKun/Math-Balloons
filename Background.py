from turtle import Turtle

'''
Background elements that are called from the Game class.
'''

class Bg:
    def __init__(self, game, math_pos, sign_pos):
        # Create the math background
        math = Turtle()
        math.penup()

        math.image = './assets/math.gif'
        game.wn.register_shape(math.image)
        math.shape(math.image)

        math.setpos(math_pos)

        # Create the sign element
        sign = Turtle()
        sign.penup()

        sign.image = './assets/grid_sign.gif'
        game.wn.register_shape(sign.image)
        sign.shape(sign.image)

        sign.setpos(sign_pos)


        # frames
        frame = Turtle()
        frame.penup()

        frame.image = './assets/frame.gif'
        game.wn.register_shape(frame.image)
        frame.shape(frame.image)

        frame.setpos(game.WIDTH / 4 - 10, 5)
