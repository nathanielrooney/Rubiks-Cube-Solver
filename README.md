# Rubiks-Cube-Solver
My attempt at a 3x3 Rubik's Cube Solver

Designed so that all moves are based on Blue on the front side and Yellow on top. Also, all moves are clockwise unless noted as ', in which case it is counterclockwise (i.e. B' = Back Prime = Turn the back (Green) side counterclockwise; L = Left = Turn the left side (Orange) side clockwise)

U = Up (Yellow)
R = Right (Red)
F = Front (Blue)
D = Down (White)
L = Left (Orange)
B = Back (Green)

When entering cube pieces' colors, enter exactly either "Yellow", "Orange", "Blue", "Red", "Green", or "White" (without the quotation marks; case-sensitive). I haven't implemented any real checks that the inputted cube is possible (or that the inputted colors are in the cases that work for the code), so if you enter in wrong information you will have to redo the entire process. 

Also, I haven't optimized the moves yet so often times you will see three of the same moves in a row instead of just one in the other direction (U U U instead of U') or one move followed by the opposite of that move instead of no moves (U U' or D D' etc. instead of no moves).

Download the three .py files and run "Cube.py" to use.
