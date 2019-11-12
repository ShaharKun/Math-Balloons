from turtle import Turtle

'''
A class to create, design and update the score
of the game.
'''

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.setpos(75, 165)

        self.options = ('Comic Sans MS', 45, 'bold')

        self.value = 0

        self.update()


    def increase(self, addition):
        ''' Update the value (score) '''
        self.value += addition


    def update(self):
        ''' Update the score with the current value '''
        self.clear()

        self.write(self.value, align='center', font=self.options)
