from turtle import Screen
from Game import Game
from tensorflow.keras.models import load_model

# Screen setup
wn = Screen()
wn.setup(1120, 560)
wn.title('Math Balloons')
wn.tracer(0)

# Load the model
model = load_model('./AI/nn_model.h5')

# Create the game
game = Game(screen=wn, model=model)

# Start the main loop
while True:
    game.update()
