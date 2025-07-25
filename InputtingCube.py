#CORNERS
GreenOrangeYellow = ["","",""]
GreenRedYellow = ["","",""]
OrangeBlueYellow = ["","",""]
RedBlueYellow = ["","",""]
GreenOrangeWhite = ["","",""]
OrangeWhiteBlue = ["","",""]
BlueWhiteRed = ["","",""]
GreenWhiteRed = ["","",""]

#EDGES
YellowBlue = ["", ""]
YellowRed = ["", ""]
YellowGreen = ["", ""]
YellowOrange = ["", ""]
BlueOrange = ["", ""]
BlueRed = ["", ""]
RedGreen = ["", ""]
GreenOrange = ["", ""]
WhiteBlue = ["", ""]
WhiteRed = ["", ""]
WhiteGreen = ["", ""]
WhiteOrange = ["", ""]

Colors = ["Yellow", "Blue", "Green", "Orange", "Red", "White"]
#Getting White side
print("Input scrambled cube:")
print("Note that White face refers to the side with the White center")
print("Also note that with Blue on top means that the top side of the cube should have a Blue center.")
OrangeWhiteBlue[1] = input("Top left of White face (with Blue on top): ")
while OrangeWhiteBlue[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeWhiteBlue[1] = input("Top left of White face (with Blue on top): ")
WhiteBlue[0] = input("Top middle of White face: ")
while WhiteBlue[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteBlue[0] = input("Top middle of White face: ")
BlueWhiteRed[1] = input("Top right of White face: ")
while BlueWhiteRed[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueWhiteRed[1] = input("Top right of White face: ")
WhiteOrange[0] = input("Middle left of White face: ")
while WhiteOrange[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteOrange[0] = input("Middle left of White face: ")
WhiteRed[0] = input("Middle right of White face: ")
while WhiteRed[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteRed[0] = input("Middle right of White face: ")
GreenOrangeWhite[2] = input("Bottom left of White face: ")
while GreenOrangeWhite[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeWhite[2] = input("Bottom left of White face: ")
WhiteGreen[0] = input("Bottom middle of White face: ")
while WhiteGreen[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteGreen[0] = input("Bottom middle of White face: ")
GreenWhiteRed[1] = input("Bottom right of White face: ")
while GreenWhiteRed[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenWhiteRed[1] = input("Bottom right of White face: ")
WhiteFace = [[OrangeWhiteBlue[1],WhiteBlue[0],BlueWhiteRed[1]],[WhiteOrange[0],"White",WhiteRed[0]],[GreenOrangeWhite[2],WhiteGreen[0],GreenWhiteRed[1]]]


#Getting Blue side
OrangeBlueYellow[1] = input("Top left  of Blue face (with Yellow on top): ")
while OrangeBlueYellow[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeBlueYellow[1] = input("Top left  of Blue face (with Yellow on top): ")
YellowBlue[1] = input("Top middle of Blue face: ")
while YellowBlue[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowBlue[1] = input("Top middle of Blue face: ")
RedBlueYellow[1] = input("Top right of Blue face: ")
while RedBlueYellow[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    RedBlueYellow[1] = input("Top right of Blue face: ")
BlueOrange[0] = input("Middle left of Blue face: ")
while BlueOrange[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueOrange[0] = input("Middle left of Blue face: ")
BlueRed[0] = input("Middle right of Blue face: ")
while BlueRed[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueRed[0] = input("Middle right of Blue face: ")
OrangeWhiteBlue[2] = input("Bottom left of Blue face: ")
while OrangeWhiteBlue[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeWhiteBlue[2] = input("Bottom left of Blue face: ")
WhiteBlue[1] = input("Bottom middle of Blue face: ")
while WhiteBlue[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteBlue[1] = input("Bottom middle of Blue face: ")
BlueWhiteRed[0] = input("Bottom right of Blue face: ")
while BlueWhiteRed[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueWhiteRed[0] = input("Bottom right of Blue face: ")
BlueFace = [[OrangeBlueYellow[1],YellowBlue[1],RedBlueYellow[1]],[BlueOrange[0],"Blue",BlueRed[0]],[OrangeWhiteBlue[2],WhiteBlue[1],BlueWhiteRed[0]]]

#Getting Yellow side
GreenOrangeYellow[2] = input("Top left of Yellow face (with Green on top): ")
while GreenOrangeYellow[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeYellow[2] = input("Top left of Yellow face (with Green on top): ")
YellowGreen[0] = input("Top middle of Yellow face: ")
while YellowGreen[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowGreen[0] = input("Top middle of Yellow face: ")
GreenRedYellow[2] = input("Top right of Yellow face: ")
while GreenRedYellow[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenRedYellow[2] = input("Top right of Yellow face: ")
YellowOrange[0] = input("Middle left of Yellow face: ")
while YellowOrange[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowOrange[0] = input("Middle left of Yellow face: ")
YellowRed[0] = input("Middle right of Yellow face: ")
while YellowRed[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowRed[0] = input("Middle right of Yellow face: ")
OrangeBlueYellow[2] = input("Bottom left of Yellow face: ")
while OrangeBlueYellow[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeBlueYellow[2] = input("Bottom left of Yellow face: ")
YellowBlue[0] = input("Bottom middle of Yellow face: ")
while YellowBlue[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowBlue[0] = input("Bottom middle of Yellow face: ")
RedBlueYellow[2] = input("Bottom right of Yellow face: ")
while RedBlueYellow[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    RedBlueYellow[2] = input("Bottom right of Yellow face: ")
YellowFace = [[GreenOrangeYellow[2],YellowGreen[0],GreenRedYellow[2]],[YellowOrange[0],"Yellow",YellowRed[0]],[OrangeBlueYellow[2],YellowBlue[0],RedBlueYellow[2]]]


#Getting Green side
GreenOrangeWhite[0] = input("Top left of Green face (with White on top): ")
while GreenOrangeWhite[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeWhite[0] = input("Top left of Green face (with White on top): ")
WhiteGreen[1] = input("Top middle of Green face: ")
while WhiteGreen[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteGreen[1] = input("Top middle of Green face: ")
GreenWhiteRed[0] = input("Top right of Green face: ")
while GreenWhiteRed[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenWhiteRed[0] = input("Top right of Green face: ")
GreenOrange[0] = input("Middle left of Green face: ")
while GreenOrange[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrange[0] = input("Middle left of Green face: ")
RedGreen[1] = input("Middle right of Green face: ")
while RedGreen[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    RedGreen[1] = input("Middle right of Green face: ")
GreenOrangeYellow[0] = input("Bottom left of Green face: ")
while GreenOrangeYellow[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeYellow[0] = input("Bottom left of Green face: ")
YellowGreen[1] = input("Bottom middle of Green face: ")
while YellowGreen[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowGreen[1] = input("Bottom middle of Green face: ")
GreenRedYellow[0] = input("Bottom right of Green face: ")
while GreenRedYellow[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenRedYellow[0] = input("Bottom right of Green face: ")
GreenFace = [[GreenOrangeWhite[0],WhiteGreen[1],GreenWhiteRed[0]],[GreenOrange[0],"Green",RedGreen[1]],[GreenOrangeYellow[0],YellowGreen[1],GreenRedYellow[0]]]


#Getting Orange side
GreenOrangeYellow[1] = input("Top left of Orange face (with Yellow on top): ")
while GreenOrangeYellow[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeYellow[1] = input("Top left of Orange face (with Yellow on top): ")
YellowOrange[1] = input("Top middle of Orange face: ")
while YellowOrange[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowOrange[1] = input("Top middle of Orange face: ")
OrangeBlueYellow[0] = input("Top right of Orange face: ")
while OrangeBlueYellow[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeBlueYellow[0] = input("Top right of Orange face: ")
GreenOrange[1] = input("Middle left of Orange face: ")
while GreenOrange[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrange[1] = input("Middle left of Orange face: ")
BlueOrange[1] = input("Middle right of Orange face: ")
while BlueOrange[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueOrange[1] = input("Middle right of Orange face: ")
GreenOrangeWhite[1] = input("Bottom right of Orange face: ")
while GreenOrangeWhite[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenOrangeWhite[1] = input("Bottom right of Orange face: ")
WhiteOrange[1] = input("Bottom middle of Orange face: ")
while WhiteOrange[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteOrange[1] = input("Bottom middle of Orange face: ")
OrangeWhiteBlue[0] = input("Bottom right of Orange face: ")
while OrangeWhiteBlue[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    OrangeWhiteBlue[0] = input("Bottom right of Orange face: ")
OrangeFace = [[GreenOrangeYellow[1],YellowOrange[1],OrangeBlueYellow[0]],[GreenOrange[1],"Orange",BlueOrange[1]],[GreenOrangeWhite[1],WhiteOrange[1],OrangeWhiteBlue[0]]]


#Getting Red side
RedBlueYellow[0] = input("Top left of Red face (with Yellow on top): ")
while RedBlueYellow[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    RedBlueYellow[0] = input("Top left of Red face (with Yellow on top): ")
YellowRed[1] = input("Top middle of Red face: ")
while YellowRed[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    YellowRed[1] = input("Top middle of Red face: ")
GreenRedYellow[1] = input("Top right of Red face: ")
while GreenRedYellow[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenRedYellow[1] = input("Top right of Red face: ")
BlueRed[1] = input("Middle left of Red face: ")
while BlueRed[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueRed[1] = input("Middle left of Red face: ")
RedGreen[0] = input("Middle right of Red face: ")
while RedGreen[0] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    RedGreen[0] = input("Middle right of Red face: ")
BlueWhiteRed[2] = input("Bottom left of Red face: ")
while BlueWhiteRed[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    BlueWhiteRed[2] = input("Bottom left of Red face: ")
WhiteRed[1] = input("Bottom middle of Red face: ")
while WhiteRed[1] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    WhiteRed[1] = input("Bottom middle of Red face: ")
GreenWhiteRed[2] = input("Bottom right of Red face: ")
while GreenWhiteRed[2] not in Colors:
    print("Please enter a valid color (Yellow, Orange, Blue, Red, Green, or White)")
    GreenWhiteRed[2] = input("Bottom right of Red face: ")
RedFace = [[RedBlueYellow[0],YellowRed[1],GreenRedYellow[1]],[BlueRed[1],"Red",RedGreen[0]],[BlueWhiteRed[2],WhiteRed[1],GreenWhiteRed[2]]]

Cube = [YellowFace, OrangeFace, BlueFace, RedFace, GreenFace, WhiteFace]

#Valid cube basic check:
EdgePieces = [YellowBlue,YellowRed, YellowGreen,YellowOrange, BlueOrange, BlueRed, RedGreen, GreenOrange, WhiteBlue, WhiteRed, WhiteGreen, WhiteOrange]
YellowEdges = 0
OrangeEdges = 0
BlueEdges = 0 
RedEdges = 0
GreenEdges = 0
WhiteEdges = 0
for EdgePiece in EdgePieces:
    for Color in EdgePiece:
        if Color == "Yellow":
            YellowEdges += 1
        elif Color == "Orange":
            OrangeEdges += 1
        elif Color == "Blue":
            BlueEdges += 1
        elif Color == "Red":
            RedEdges += 1
        elif Color == "Green":
            GreenEdges += 1
        elif Color == "White":
            WhiteEdges += 1
for Colors in [YellowEdges, OrangeEdges, BlueEdges, RedEdges, GreenEdges, WhiteEdges]:
    if Colors != 4:
        print("Invalid inputted cube. Please try again!")
        quit()

CornerPieces = [GreenOrangeYellow, GreenRedYellow, OrangeBlueYellow, RedBlueYellow, GreenOrangeWhite, OrangeWhiteBlue, BlueWhiteRed, GreenWhiteRed]
YellowCorners = 0
OrangeCorners = 0
BlueCorners = 0 
RedCorners = 0
GreenCorners = 0
WhiteCorners = 0
for CornerPiece in CornerPieces:
    for Color in CornerPiece:
        if Color == "Yellow":
            YellowCorners += 1
        elif Color == "Orange":
            OrangeCorners += 1
        elif Color == "Blue":
            BlueCorners += 1
        elif Color == "Red":
            RedCorners += 1
        elif Color == "Green":
            GreenCorners += 1
        elif Color == "White":
            WhiteCorners += 1
for Colors in [YellowCorners, OrangeCorners, BlueCorners, RedCorners, GreenCorners, WhiteCorners]:
    if Colors != 4:
        print("Invalid inputted cube. Please try again!")
        quit()
