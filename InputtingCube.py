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

#Getting White side
OrangeWhiteBlue[1] = input("Top left of White face (with Blue on top): ")
WhiteBlue[0] = input("Top middle of White face: ")
BlueWhiteRed[1] = input("Top right of White face: ")
WhiteOrange[0] = input("Middle left of White face: ")
WhiteRed[0] = input("Middle right of White face: ")
GreenOrangeWhite[2] = input("Bottom left of White face: ")
WhiteGreen[0] = input("Bottom middle of White face: ")
GreenWhiteRed[1] = input("Bottom right of White face: ")
WhiteFace = [[OrangeWhiteBlue[1],WhiteBlue[0],BlueWhiteRed[1]],[WhiteOrange[0],"White",WhiteRed[0]],[GreenOrangeWhite[2],WhiteGreen[0],GreenWhiteRed[1]]]


#Getting Blue side
OrangeBlueYellow[1] = input("Top left  of Blue face (with Yellow on top): ")
YellowBlue[1] = input("Top middle of Blue face: ")
RedBlueYellow[1] = input("Top right of Blue face: ")
BlueOrange[0] = input("Middle left of Blue face: ")
BlueRed[0] = input("Middle right of Blue face: ")
OrangeWhiteBlue[2] = input("Bottom left of Blue face: ")
WhiteBlue[1] = input("Bottom middle of Blue face: ")
BlueWhiteRed[0] = input("Bottom right of Blue face: ")
BlueFace = [[OrangeBlueYellow[1],YellowBlue[1],RedBlueYellow[1]],[BlueOrange[0],"Blue",BlueRed[0]],[OrangeWhiteBlue[2],WhiteBlue[1],BlueWhiteRed[0]]]

#Getting Yellow side
GreenOrangeYellow[2] = input("Top left of Yellow face (with Green on top): ")
YellowGreen[0] = input("Top middle of Yellow face: ")
GreenRedYellow[2] = input("Top right of Yellow face: ")
YellowOrange[0] = input("Middle left of Yellow face: ")
YellowRed[0] = input("Middle right of Yellow face: ")
OrangeBlueYellow[2] = input("Bottom left of Yellow face: ")
YellowBlue[0] = input("Bottom middle of Yellow face: ")
RedBlueYellow[2] = input("Bottom right of Yellow face: ")
YellowFace = [[GreenOrangeYellow[2],YellowGreen[0],GreenRedYellow[2]],[YellowOrange[0],"Yellow",YellowRed[0]],[OrangeBlueYellow[2],YellowBlue[0],RedBlueYellow[2]]]


#Getting Green side
GreenOrangeWhite[0] = input("Top left of Green face (with White on top): ")
WhiteGreen[1] = input("Top middle of Green face: ")
GreenWhiteRed[0] = input("Top right of Green face: ")
GreenOrange[0] = input("Middle left of Green face: ")
RedGreen[1] = input("Middle right of Green face: ")
GreenOrangeYellow[0] = input("Bottom left of Green face: ")
YellowGreen[1] = input("Bottom middle of Green face: ")
GreenRedYellow[0] = input("Bottom right of Green face: ")
GreenFace = [[GreenOrangeWhite[0],WhiteGreen[1],GreenWhiteRed[0]],[GreenOrange[0],"Green",RedGreen[1]],[GreenOrangeYellow[0],YellowGreen[1],GreenRedYellow[0]]]


#Getting Orange side
GreenOrangeYellow[1] = input("Top left of Orange face (with Yellow on top): ")
YellowOrange[1] = input("Top middle of Orange face: ")
OrangeBlueYellow[0] = input("Top right of Orange face: ")
GreenOrange[1] = input("Middle left of Orange face: ")
BlueOrange[1] = input("Middle right of Orange face: ")
GreenOrangeWhite[1] = input("Bottom right of Orange face: ")
WhiteOrange[1] = input("Bottom middle of Orange face: ")
OrangeWhiteBlue[0] = input("Bottom right of Orange face: ")
OrangeFace = [[GreenOrangeYellow[1],YellowOrange[1],OrangeBlueYellow[0]],[GreenOrange[1],"Orange",BlueOrange[1]],[GreenOrangeWhite[1],WhiteOrange[1],OrangeWhiteBlue[0]]]


#Getting Red side
RedBlueYellow[0] = input("Top left of Red face (with Yellow on top): ")
YellowRed[1] = input("Top middle of Red face: ")
GreenRedYellow[1] = input("Top right of Red face: ")
BlueRed[1] = input("Middle left of Red face: ")
RedGreen[0] = input("Middle right of Red face: ")
BlueWhiteRed[2] = input("Bottom left of Red face: ")
WhiteRed[1] = input("Bottom middle of Red face: ")
GreenWhiteRed[2] = input("Bottom right of Red face: ")
RedFace = [[RedBlueYellow[0],YellowRed[1],GreenRedYellow[1]],[BlueRed[1],"Red",RedGreen[0]],[BlueWhiteRed[2],WhiteRed[1],GreenWhiteRed[2]]]

Cube = [YellowFace, OrangeFace, BlueFace, RedFace, GreenFace, WhiteFace]