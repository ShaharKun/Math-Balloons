import turtle as t
from turtle import Turtle
from Grid import Grid
from Player import Player
from Balloon import Balloon
from ScoreBoard import ScoreBoard
from Background import Bg
from EndScreen import *

'''
Main Class.
Use all necessary classes and objects to make
the logic, gameplay and order of the game.
'''

class Game:
    def __init__(self, screen, model):
        self.wn = screen

        self.WIDTH = screen.window_width()
        self.HEIGHT = screen.window_height()
        self.model = model

        self.bg = Bg(self, math_pos=(-289, 0), sign_pos=(282, 220))

        self.grid = Grid(self, self.wn, 28, 28, model)
        self.grid.initialize_all_pixels()

        self.player = Player(self)
        self.last_pos = -self.WIDTH // 4

        self.balloons = []
        self.balloon_speed = 0.3
        self.static_balloon_speed = 0.3
        self.new_balloon_cord = 100
        self.score = ScoreBoard()

        Balloon(self, self.balloon_speed)

        # Register the collective dead balloon image
        self.wn.register_shape('./assets/dead_balloon.gif')


    def update(self):
        ''' Update the game. '''
        self.grid.listen_to_user()
        self.player.update_position()

        for balloon in self.balloons:
            balloon.update_position()

            if not balloon.passed_cord:
                if balloon.ycor() <= self.new_balloon_cord:
                    balloon.passed_cord = True

                    # Check if there's a need to increase difficulty
                    if not self.balloon_speed > 0.75:
                        self.balloon_speed += 0.01
                        self.static_balloon_speed += 0.01

                    if not self.new_balloon_cord > 250:
                        self.new_balloon_cord += 0.5

                    Balloon(self, self.balloon_speed)


        # Listen for the events
        self.wn.listen()

        # Update the frame
        self.wn.update()


    def restart(self):
        ''' Reset all necessary variables. '''
        remove_end_screen()

        self.last_pos = -self.WIDTH // 4
        for balloon in self.balloons:
            self.balloons.remove(balloon)
            balloon.ht()

        self.balloon_speed = 0.3
        self.static_balloon_speed = 0.3
        self.new_balloon_cord = 100

        self.score.clear() # Remove the old score
        self.score = ScoreBoard()

        # remain the game
        Balloon(self, self.balloon_speed)

        while True:
            self.update()



    # Restart and Quit options at the end of the game.
    def wait_for_restart(self, x, y):
        if 55 < x < 235 and -60 < y < 30:
            self.restart()


    def wait_for_quit(self, x, y):
        if 305 < x < 490 and -60 < y < 30:
            # Terminate the program
            self.wn.bye()


    def get_actions(self, x, y):
        self.wait_for_quit(x, y)
        self.wait_for_restart(x, y)


    def end_screen(self):
        create_end_screen(self)

        while True:
            t.onscreenclick(self.get_actions)

            t.listen()
            self.wn.update()
