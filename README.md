# Rubiks-Cube-Solver
My attempt at a 3x3 Rubik's Cube Solver

Designed so that all moves are based on Blue on the front side and Yellow on top. Also, all moves are clockwise unless noted as ', in which case it is counterclockwise (i.e. B' = Back Prime = Turn the back (Green) side counterclockwise; L = Left = Turn the left side (Orange) side clockwise)

U = Up (Yellow)
R = Right (Red)
F = Front (Blue)
D = Down (White)
L = Left (Orange)
B = Back (Green)

When entering cube pieces' colors, enter exactly either "Yellow", "Orange", "Blue", "Red", "Green", or "White" (without the quotation marks; case-sensitive). 

For clarification when entering the scrambled cube: the White face is the face with the White center, since the centers of a 3x3 are fixed. When entering the scrambled cube, the code will also tell you which face to have on the top side to correctly orient the cube. For example, when asked "Top left of the White face (with Blue on top)", enter the color of the top left corner of the side with the White center when the Blue center is on the top side of the cube. In a solved cube that corner would be a White, Orange, and Blue corner piece. Once you orient and start entering the colors for a side, don't rotate the cube and make sure that the same side is at the top while you enter that face. 

Also, I haven't optimized the moves yet so often times you will see three of the same moves in a row instead of just one in the other direction (U U U instead of U') or one move followed by the opposite of that move instead of no moves (U U' or D D' etc. instead of no moves).

Download the three .py files and run "Cube.py" to use.
