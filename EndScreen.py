from turtle import Turtle

'''
Create the buttons at the end screen, and be able to remove them.
'''

def create_end_screen(game):
    global restart, quit

    game.wn.register_shape('./assets/restart_button.gif')
    game.wn.register_shape('./assets/quit_button.gif')

    restart = Turtle()
    restart.penup()
    restart.shape('./assets/restart_button.gif')
    restart.setpos(145, 0)

    quit = Turtle()
    quit.penup()
    quit.shape('./assets/quit_button.gif')
    quit.setpos(400, 0)


def remove_end_screen():
    global restart, quit

    restart.ht()
    quit.ht()
