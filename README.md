# Math-Balloons
AI-based game of simple math problems.
Built with the turtle module, tensorflow, and keras.

## Requirements
- Python 3
- Turtle (preinstalled with the python base library)
- Tensorflow
- keras 2.2.4 (see 'model')

## How to run
To run the game, simply execute 'run.py' which can be found in the main directory.
* If you want to use a different model, please make the necessary changes to this file.

## Project structure
### Balloons
The 'balloons' folder stores all images of all math questions.
The name of the subfolder is the answer key to all questions within it.
This is how questions are generated and asnwer keys are stored.

### Drawing
Drawing is done on the right-hand side of the screen, on the dedicated space.
The 'Pen' class is controlling mouse events, and it writes the changes of the grid to the 'Grid' class.
The grid stores the image as an array of shape (28, 28), and can then export the grid as an array of shape (28, 28, 1)
That the model requires.

### Player
This is  the small man walking under the balloons, catching them as they fall.
It adds no necessary value to the game, although it makes the game more playable, and interesting.

### Scoring
Your score can be seen at the top, next to the sign.
Each time a balloon is popped, and successfully reaches the bottom, you gain a point.
The game ends whenever you fail to pop a balloon before it reaches the bottom.

### Combining it all
The 'Game' class stores the main logic and flow of the game, and includes all discussed features.
A 'Game' object is firstly initialized in the 'run.py' file.

## Model
The built-in model was trained with keras version 2.2.4-tf.
If you wish to use a different version of keras, retrain the model on your machine using 'AI/model_creator.py'.
You can see the built-in model's structure and layers in 'model_creator.py'.
The model is called to make predictions within the 'Grid.py' file, and expects an input image of shape (24, 24, 1).
When making your own model for this game, make sure to keep input shape and dtype settings that are preset in 'model_craetor.py'.


> The model is not perfect, and might make mistakes over time.
> Try drawing as clearly as possible, and use as much of your drawing space as you can.
