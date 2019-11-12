import random
from turtle import Turtle

'''
The Class for the balloons.
'''

class Balloon(Turtle):
    def __init__(self, game, speed):
        super().__init__()
        self.penup()

        self.game = game
        self.speed = speed
        self.dead = False
        self.passed_cord = False
        self.balloons = []

        self.value = random.randint(0, 9)
        self.equation = random.randint(0, 11)

        self.image = './balloons/{}/{}.gif'.format(self.value, self.equation)
        self.game.wn.register_shape(self.image)
        self.shape(self.image)

        x = random.randint(-self.game.WIDTH // 2 + 75, - 75)
        self.setpos(x, self.game.HEIGHT / 2 + 100)

        self.game.balloons.append(self)


    def kill(self):
        self.dead = True
        self.shape('./assets/dead_balloon.gif')
        self.sety(self.ycor() - 75) # Fit the change of the shape

        # For the player movement
        self.game.last_pos = self.xcor()


    def update_position(self):
        ''' Update the position of the instance in the next frame. '''
        if self.dead:
            self.sety(self.ycor() - self.speed * 5)

            if self.ycor() <= self.game.player.ycor():
                self.remove_from_screen()
                self.game.score.increase(1)
                self.game.score.update()

        else:
            self.sety(self.ycor() - self.speed)

            if self.ycor() - 75 <= self.game.player.ycor():
                self.remove_from_screen()
                self.game.end_screen()


    def remove_from_screen(self):
        self.ht()
        self.game.balloons.remove(self)
