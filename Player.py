from turtle import Turtle

'''
The player that follows the balloons falling,
it is not effecting the gameplay at any way.
'''

class Player(Turtle):
    def __init__(self, game):
        super().__init__()
        self.penup()
        self.game = game

        # Animation
        self.states = ['./assets/player_standing.gif',
                       './assets/player_right.gif',
                       './assets/player_left.gif']

        for state in self.states:
            self.game.wn.register_shape(state)

        self.shape(self.states[0])

        self.setpos(0, -self.game.HEIGHT / 2 + 75)

        self.direction = 0
        self.acc = 10

    def update_position(self):
        '''
        Follow the game's last popped balloon position.
        '''
        self.decide_direction()
        self.setx(self.xcor() + self.acc * self.direction)

        self.shape(self.states[self.direction])


    def decide_direction(self):
        '''
        Get the direction needed to move the player in.
        '''
        if abs(self.xcor() - self.game.last_pos) < 7.5:
            self.direction = 0
            return

        if self.game.last_pos > self.xcor():
            self.direction = 1
        else:
            self.direction = -1
