#Cube = List of 6 faces of 3x3. Orientation of cube is White on bottom, Blue is front
#Maybe try with Cube as being a List of two dictionaries, Edges and Corners.
#Cube = [YellowFace, OrangeFace, BlueFace, RedFace, GreenFace, WhiteFace]

def Right(Cube, Ledger):
    EdgeFiller = Cube[3][0][1] 
    Cube[3][0][1] = Cube[3][1][0]
    Cube[3][1][0] = Cube[3][2][1]
    Cube[3][2][1] = Cube[3][1][2]
    Cube[3][1][2] = EdgeFiller
    CornerFiller = Cube[3][0][0]
    Cube[3][0][0] = Cube[3][2][0]
    Cube[3][2][0] = Cube[3][2][2]
    Cube[3][2][2] = Cube[3][0][2]
    Cube[3][0][2] = CornerFiller
    SideFiller0 = Cube[0][0][2]
    SideFiller1 = Cube[0][1][2]
    SideFiller2 = Cube[0][2][2]
    Cube[0][0][2] = Cube[2][0][2]
    Cube[0][1][2] = Cube[2][1][2]
    Cube[0][2][2] = Cube[2][2][2]
    Cube[2][0][2] = Cube[5][0][2]
    Cube[2][1][2] = Cube[5][1][2]
    Cube[2][2][2] = Cube[5][2][2]
    Cube[5][0][2] = Cube[4][0][2]
    Cube[5][1][2] = Cube[4][1][2]
    Cube[5][2][2] = Cube[4][2][2]
    Cube[4][0][2] = SideFiller0
    Cube[4][1][2] = SideFiller1
    Cube[4][2][2] = SideFiller2
    Ledger.append("R")
    return Cube, Ledger
def RightPrime(Cube, Ledger):
    Cube, Ledger = Right(*Right(*Right(Cube, Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("R'")
    return Cube, Ledger

def Left(Cube, Ledger):
    EdgeFiller = Cube[1][0][1] 
    Cube[1][0][1] = Cube[1][1][0]
    Cube[1][1][0] = Cube[1][2][1]
    Cube[1][2][1] = Cube[1][1][2]
    Cube[1][1][2] = EdgeFiller
    CornerFiller = Cube[1][0][0]
    Cube[1][0][0] = Cube[1][2][0]
    Cube[1][2][0] = Cube[1][2][2]
    Cube[1][2][2] = Cube[1][0][2]
    Cube[1][0][2] = CornerFiller
    SideFiller0 = Cube[0][0][0]
    SideFiller1 = Cube[0][1][0]
    SideFiller2 = Cube[0][2][0]
    Cube[0][0][0] = Cube[4][0][0]
    Cube[0][1][0] = Cube[4][1][0]
    Cube[0][2][0] = Cube[4][2][0]
    Cube[4][0][0] = Cube[5][0][0]
    Cube[4][1][0] = Cube[5][1][0]
    Cube[4][2][0] = Cube[5][2][0]
    Cube[5][0][0] = Cube[2][0][0]
    Cube[5][1][0] = Cube[2][1][0]
    Cube[5][2][0] = Cube[2][2][0]
    Cube[2][0][0] = SideFiller0
    Cube[2][1][0] = SideFiller1
    Cube[2][2][0] = SideFiller2
    Ledger.append("L")
    return Cube, Ledger
def LeftPrime(Cube, Ledger):
    Cube, Ledger = Left(*Left(*Left(Cube,Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("L'")
    return Cube, Ledger

def Up(Cube, Ledger):
    EdgeFiller = Cube[0][0][1] 
    Cube[0][0][1] = Cube[0][1][0]
    Cube[0][1][0] = Cube[0][2][1]
    Cube[0][2][1] = Cube[0][1][2]
    Cube[0][1][2] = EdgeFiller
    CornerFiller = Cube[0][0][0]
    Cube[0][0][0] = Cube[0][2][0]
    Cube[0][2][0] = Cube[0][2][2]
    Cube[0][2][2] = Cube[0][0][2]
    Cube[0][0][2] = CornerFiller
    SideFiller0 = Cube[4][2][0]
    SideFiller1 = Cube[4][2][1]
    SideFiller2 = Cube[4][2][2]
    Cube[4][2][0] = Cube[1][0][2]
    Cube[4][2][1] = Cube[1][0][1]
    Cube[4][2][2] = Cube[1][0][0]
    Cube[1][0][2] = Cube[2][0][2]
    Cube[1][0][1] = Cube[2][0][1]
    Cube[1][0][0] = Cube[2][0][0]
    Cube[2][0][2] = Cube[3][0][2]
    Cube[2][0][1] = Cube[3][0][1]
    Cube[2][0][0] = Cube[3][0][0]
    Cube[3][0][2] = SideFiller0
    Cube[3][0][1] = SideFiller1
    Cube[3][0][0] = SideFiller2
    Ledger.append("U")
    return Cube, Ledger
def UpPrime(Cube, Ledger):
    Cube, Ledger = Up(*Up(*Up(Cube, Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("U'")
    return Cube, Ledger

def Down(Cube, Ledger):
    EdgeFiller = Cube[5][0][1] 
    Cube[5][0][1] = Cube[5][1][0]
    Cube[5][1][0] = Cube[5][2][1]
    Cube[5][2][1] = Cube[5][1][2]
    Cube[5][1][2] = EdgeFiller
    CornerFiller = Cube[5][0][0]
    Cube[5][0][0] = Cube[5][2][0]
    Cube[5][2][0] = Cube[5][2][2]
    Cube[5][2][2] = Cube[5][0][2]
    Cube[5][0][2] = CornerFiller
    SideFiller0 = Cube[2][2][0]
    SideFiller1 = Cube[2][2][1]
    SideFiller2 = Cube[2][2][2]
    Cube[2][2][0] = Cube[1][2][0]
    Cube[2][2][1] = Cube[1][2][1]
    Cube[2][2][2] = Cube[1][2][2]
    Cube[1][2][0] = Cube[4][0][2]
    Cube[1][2][1] = Cube[4][0][1]
    Cube[1][2][2] = Cube[4][0][0]
    Cube[4][0][2] = Cube[3][2][0]
    Cube[4][0][1] = Cube[3][2][1]
    Cube[4][0][0] = Cube[3][2][2]
    Cube[3][2][0] = SideFiller0
    Cube[3][2][1] = SideFiller1
    Cube[3][2][2] = SideFiller2
    Ledger.append("D")
    return Cube, Ledger
def DownPrime(Cube, Ledger):
    Cube, Ledger = Down(*Down(*Down(Cube, Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("D'")
    return Cube, Ledger

def Back(Cube, Ledger):
    EdgeFiller = Cube[4][0][1] 
    Cube[4][0][1] = Cube[4][1][0]
    Cube[4][1][0] = Cube[4][2][1]
    Cube[4][2][1] = Cube[4][1][2]
    Cube[4][1][2] = EdgeFiller
    CornerFiller = Cube[4][0][0]
    Cube[4][0][0] = Cube[4][2][0]
    Cube[4][2][0] = Cube[4][2][2]
    Cube[4][2][2] = Cube[4][0][2]
    Cube[4][0][2] = CornerFiller
    SideFiller0 = Cube[5][2][0]
    SideFiller1 = Cube[5][2][1]
    SideFiller2 = Cube[5][2][2]
    Cube[5][2][0] = Cube[1][0][0]
    Cube[5][2][1] = Cube[1][1][0]
    Cube[5][2][2] = Cube[1][2][0]
    Cube[1][0][0] = Cube[0][0][2]
    Cube[1][1][0] = Cube[0][0][1]
    Cube[1][2][0] = Cube[0][0][0]
    Cube[0][0][2] = Cube[3][2][2]
    Cube[0][0][1] = Cube[3][1][2]
    Cube[0][0][0] = Cube[3][0][2]
    Cube[3][2][2] = SideFiller0
    Cube[3][1][2] = SideFiller1
    Cube[3][0][2] = SideFiller2
    Ledger.append("B")
    return Cube, Ledger
def BackPrime(Cube, Ledger):
    Cube, Ledger = Back(*Back(*Back(Cube, Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("B'")
    return Cube, Ledger

def Front(Cube, Ledger):
    EdgeFiller = Cube[2][0][1] 
    Cube[2][0][1] = Cube[2][1][0]
    Cube[2][1][0] = Cube[2][2][1]
    Cube[2][2][1] = Cube[2][1][2]
    Cube[2][1][2] = EdgeFiller
    CornerFiller = Cube[2][0][0]
    Cube[2][0][0] = Cube[2][2][0]
    Cube[2][2][0] = Cube[2][2][2]
    Cube[2][2][2] = Cube[2][0][2]
    Cube[2][0][2] = CornerFiller
    SideFiller0 = Cube[0][2][0]
    SideFiller1 = Cube[0][2][1]
    SideFiller2 = Cube[0][2][2]
    Cube[0][2][0] = Cube[1][2][2]
    Cube[0][2][1] = Cube[1][1][2]
    Cube[0][2][2] = Cube[1][0][2]
    Cube[1][2][2] = Cube[5][0][2]
    Cube[1][1][2] = Cube[5][0][1]
    Cube[1][0][2] = Cube[5][0][0]
    Cube[5][0][2] = Cube[3][0][0]
    Cube[5][0][1] = Cube[3][1][0]
    Cube[5][0][0] = Cube[3][2][0]
    Cube[3][0][0] = SideFiller0
    Cube[3][1][0] = SideFiller1
    Cube[3][2][0] = SideFiller2
    Ledger.append("F")
    return Cube, Ledger
def FrontPrime(Cube,Ledger):
    Cube, Ledger = Front(*Front(*Front(Cube, Ledger)))
    Ledger = Ledger[:-3]
    Ledger.append("F'")
    return Cube, Ledger

def Fish(Cube,Ledger):
    Cube, Ledger = RightPrime(*Up(*Up(*Right(*Up(*RightPrime(*Up(*Right(Cube,Ledger))))))))
    return Cube, Ledger

def ReverseFish(Cube, Ledger):
    Cube, Ledger = RightPrime(*UpPrime(*Right(*UpPrime(*RightPrime(*Up(*Up(*Right(Cube, Ledger))))))))
    return Cube, Ledger

def LastLayerAlg(Cube, Ledger):
    Cube, Ledger = Right(*Right(*Back(*Back(*RightPrime(*FrontPrime(*Right(*Back(*Back(*RightPrime(*Front(*RightPrime(Cube, Ledger))))))))))))
    return Cube, Ledger

def UPermUp(Cube, Ledger):
    Cube, Ledger = Front(*Front(*Up(*Right(*LeftPrime(*Front(*Front(*RightPrime(*Left(*Up(*Front(*Front(Cube,Ledger))))))))))))
    return Cube, Ledger

def UPermUpPrime(Cube, Ledger):
    Cube, Ledger = Front(*Front(*UpPrime(*Right(*LeftPrime(*Front(*Front(*RightPrime(*Left(*UpPrime(*Front(*Front(Cube, Ledger))))))))))))
    return Cube, Ledger

def Hook(Cube,Ledger):
    Cube, Ledger = BackPrime(*LeftPrime(*UpPrime(*Left(*Up(*Back(Cube,Ledger))))))
    return Cube, Ledger

def Bar(Cube, Ledger):
    Cube, Ledger = FrontPrime(*UpPrime(*RightPrime(*Up(*Right(*Front(Cube, Ledger))))))
    return Cube, Ledger

def BlueF2LRight(Cube, Ledger):
    Cube, Ledger = Front(*Up(*FrontPrime(*UpPrime(*RightPrime(*UpPrime(*Right(*Up(Cube, Ledger))))))))
    return Cube, Ledger

def BlueF2LLeft(Cube,Ledger):
    Cube, Ledger = FrontPrime(*UpPrime(*Front(*Up(*Left(*Up(*LeftPrime(*UpPrime(Cube, Ledger))))))))
    return Cube, Ledger

def RedF2LRight(Cube, Ledger):
    Cube, Ledger = Right(*Up(*RightPrime(*UpPrime(*BackPrime(*UpPrime(*Back(*Up(Cube, Ledger))))))))
    return Cube, Ledger

def RedF2LLeft(Cube, Ledger):
    Cube, Ledger = RightPrime(*UpPrime(*Right(*Up(*Front(*Up(*FrontPrime(*UpPrime(Cube, Ledger))))))))
    return Cube, Ledger

def GreenF2LRight(Cube, Ledger):
    Cube, Ledger = Back(*Up(*BackPrime(*UpPrime(*LeftPrime(*UpPrime(*Left(*Up(Cube, Ledger))))))))
    return Cube, Ledger

def GreenF2LLeft(Cube, Ledger):
    Cube, Ledger = BackPrime(*UpPrime(*Back(*Up(*Right(*Up(*RightPrime(*UpPrime(Cube, Ledger))))))))
    return Cube, Ledger

def OrangeF2LRight(Cube, Ledger):
    Cube, Ledger = Left(*Up(*LeftPrime(*UpPrime(*FrontPrime(*UpPrime(*Front(*Up(Cube, Ledger))))))))
    return Cube, Ledger

def OrangeF2LLeft(Cube, Ledger):
    Cube, Ledger = LeftPrime(*UpPrime(*Left(*Up(*Back(*Up(*BackPrime(*UpPrime(Cube, Ledger))))))))
    return Cube, Ledger

# def LocateEdge(Cube,Edge):
#     return 

# def LocateCorner(Cube,Corner):
#     return 

# def EdgePieceOnTop(Cube, Edge):
#     return

# def EdgePieceInMiddle(Cube, Edge):
#     return

# def EdgePieceOnBottom(Cube, Edge):
#     return

def InsertWhiteBlue(Cube, Ledger):
    TopEdges = [{Cube[0][0][1], Cube[4][2][1]}, {Cube[0][1][0], Cube[1][0][1]}, {Cube[0][2][1], Cube[2][0][1]},{Cube[0][1][2], Cube[3][0][1]}]
    if {"White", "Blue"} in TopEdges:
        while TopEdges[2] != {"White","Blue"}:
            Cube, Ledger = Up(Cube, Ledger)
            #Ledger.append("Up")
            TopEdges = [{Cube[0][0][1], Cube[4][2][1]}, {Cube[0][1][0], Cube[1][0][1]}, {Cube[0][2][1], Cube[2][0][1]},{Cube[0][1][2], Cube[3][0][1]}]
    
        if [Cube[0][2][1], Cube[2][0][1]] == ["White", "Blue"]:
            Cube, Ledger = Front(*Front(Cube, Ledger))
            #Ledger.append("Front")
            #Ledger.append("Front")
            return Cube, Ledger
        Cube, Ledger = DownPrime(*RightPrime(*Front(Cube, Ledger)))
        #Ledger.append("Front")
        #Ledger.append("RightPrime")
        #Ledger.append("DownPrime")
        return Cube, Ledger
    MiddleEdges = [{Cube[2][1][2], Cube[3][1][0]}, {Cube[3][1][2], Cube[4][1][2]}, {Cube[4][1][0], Cube[1][1][0]},{Cube[1][1][2], Cube[2][1][0]}] #BlueRed, RedGreen, GreenOrange, OrangeBlue

    if {"White", "Blue"} in MiddleEdges:
        if {Cube[2][1][2], Cube[3][1][0]} == {"White", "Blue"}:
            Cube, Ledger = Front(Cube, Ledger)
            #Ledger.append("Front")
        elif {Cube[3][1][2], Cube[4][1][2]} == {"White", "Blue"}:
            Cube, Ledger = BackPrime(Cube, Ledger)
            #Ledger.append("BackPrime")
        elif {Cube[4][1][0], Cube[1][1][0]} ==  {"White", "Blue"}:
            Cube, Ledger = Back(Cube, Ledger)
            #Ledger.append("Back")
        elif {Cube[1][1][2], Cube[2][1][0]} == {"White","Blue"}:
            Cube, Ledger = FrontPrime(Cube, Ledger)
            #Ledger.append("FrontPrime")
    #Now edge must be in bottom
    while {Cube[2][2][1], Cube[5][0][1]} != {"White","Blue"}:
        Cube, Ledger = Down(Cube, Ledger)
        #Ledger.append("Down")
    if [Cube[2][2][1], Cube[5][0][1]] == ["Blue", "White"]:
        return Cube, Ledger
    Cube, Ledger = Down(*Left(*Front(Cube, Ledger)))
    #Ledger.append("Front")
    #Ledger.append("Left")
    #Ledger.append("Down")
    return Cube, Ledger

def InsertWhiteRed(Cube,Ledger):
    MiddleEdges = [{Cube[2][1][2], Cube[3][1][0]}, {Cube[3][1][2], Cube[4][1][2]}, {Cube[4][1][0], Cube[1][1][0]},{Cube[1][1][2], Cube[2][1][0]}] #BlueRed, RedGreen, GreenOrange, OrangeBlue
    TopEdges = [{Cube[0][0][1], Cube[4][2][1]}, {Cube[0][1][0], Cube[1][0][1]}, {Cube[0][2][1], Cube[2][0][1]},{Cube[0][1][2], Cube[3][0][1]}]
    if {"White", "Red"} not in TopEdges and {"White", "Red"} not in MiddleEdges:
        if [Cube[3][2][1], Cube[5][1][2]] == ["Red", "White"]:
            return Cube, Ledger
        while {Cube[3][2][1], Cube[5][1][2]} != {"Red", "White"}:
            Cube, Ledger = Down(Cube, Ledger)
            #Ledger.append("Down")
        Cube, Ledger = Right(*Right(Cube, Ledger))
        #Ledger.append("Right")
        #Ledger.append("Right")
        while [Cube[2][2][1], Cube[5][0][1]] != ["Blue", "White"]:
            Cube, Ledger = DownPrime(Cube, Ledger)
            #Ledger.append("DownPrime")
        #Then do top
    if {"White", "Red"} in MiddleEdges:
        if {Cube[2][1][2], Cube[3][1][0]} == {"White", "Red"}:
            Cube, Ledger = Right(Cube, Ledger)
            #Ledger.append("Right")
        elif {Cube[3][1][2], Cube[4][1][2]} == {"White", "Red"}:
            Cube, Ledger = RightPrime(Cube, Ledger)
            #Ledger.append("RightPrime")
        elif {Cube[4][1][0], Cube[1][1][0]} ==  {"White", "Red"}:
            Cube, Ledger = Left(Cube, Ledger)
            #Ledger.append("Left")
        elif {Cube[1][1][2], Cube[2][1][0]} == {"White","Red"}:
            Cube, Ledger = LeftPrime(Cube, Ledger)
            #Ledger.append("LeftPrime")
    while {Cube[0][1][2], Cube[3][0][1]} != {"White","Red"}:
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if [Cube[0][1][2], Cube[3][0][1]] == ["White","Red"]:
        Cube, Ledger = Right(*Right(Cube, Ledger))
        #Ledger.append("Right")
        #Ledger.append("Right")
        return Cube, Ledger
    Cube, Ledger = Right(*BackPrime(*UpPrime(Cube, Ledger)))
    #Ledger.append("UpPrime")
    #Ledger.append("BackPrime")
    #Ledger.append("Right")
    return Cube, Ledger

def InsertWhiteGreen(Cube,Ledger):
    MiddleEdges = [{Cube[2][1][2], Cube[3][1][0]}, {Cube[3][1][2], Cube[4][1][2]}, {Cube[4][1][0], Cube[1][1][0]},{Cube[1][1][2], Cube[2][1][0]}] #BlueRed, RedGreen, GreenOrange, OrangeBlue
    TopEdges = [{Cube[0][0][1], Cube[4][2][1]}, {Cube[0][1][0], Cube[1][0][1]}, {Cube[0][2][1], Cube[2][0][1]},{Cube[0][1][2], Cube[3][0][1]}]
    if {"White", "Green"} not in TopEdges and {"White", "Green"} not in MiddleEdges:
        if [Cube[4][0][1], Cube[5][2][1]] == ["Green", "White"]:
            return Cube, Ledger
        while {Cube[4][0][1], Cube[5][2][1]} != {"White", "Green"}:
            Cube, Ledger = DownPrime(Cube, Ledger)
            #Ledger.append("DownPrime")
        Cube, Ledger = Back(*Back(Cube, Ledger))
        #Ledger.append("Back")
        #Ledger.append("Back")
        while [Cube[0][2][1], Cube[2][0][1]] != ["White", "Blue"]:
            Cube, Ledger = Down(Cube, Ledger)
            #Ledger.append("Down")
        #Then do top
    if {"White", "Green"} in MiddleEdges:
        if {Cube[2][1][2], Cube[3][1][0]} == {"White", "Green"}:
            Cube, Ledger = RightPrime(*UpPrime(*Right(Cube, Ledger)))
            #Ledger.append("Right")
            #Ledger.append("UpPrime")
            #Ledger.append("RightPrime")
        elif {Cube[3][1][2], Cube[4][1][2]} == {"White", "Green"}:
            Cube, Ledger = Back(Cube, Ledger)
            #Ledger.append("Back")
        elif {Cube[4][1][0], Cube[1][1][0]} ==  {"White", "Green"}:
            Cube, Ledger = BackPrime(Cube, Ledger)
            #Ledger.append("BackPrime")
        elif {Cube[1][1][2], Cube[2][1][0]} == {"White","Green"}:
            Cube, Ledger = LeftPrime(Cube, Ledger)
            #Ledger.append("LeftPrime")
    while {Cube[0][0][1], Cube[4][2][1]} != {"White","Green"}:
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if [Cube[0][0][1], Cube[4][2][1]] == ["White","Green"]:
        Cube, Ledger = Back(*Back(Cube, Ledger))
        #Ledger.append("Back")
        #Ledger.append("Back")
        return Cube, Ledger
    Cube, Ledger = Back(*LeftPrime(*UpPrime(Cube, Ledger)))
    #Ledger.append("UpPrime")
    #Ledger.append("LeftPrime")
    #Ledger.append("Back")
    return Cube, Ledger

def InsertWhiteOrange(Cube, Ledger):
    MiddleEdges = [{Cube[2][1][2], Cube[3][1][0]}, {Cube[3][1][2], Cube[4][1][2]}, {Cube[4][1][0], Cube[1][1][0]},{Cube[1][1][2], Cube[2][1][0]}] #BlueRed, RedGreen, GreenOrange, OrangeBlue
    TopEdges = [{Cube[0][0][1], Cube[4][2][1]}, {Cube[0][1][0], Cube[1][0][1]}, {Cube[0][2][1], Cube[2][0][1]},{Cube[0][1][2], Cube[3][0][1]}]
    if {Cube[5][1][0], Cube[1][2][1]} == {"White", "Orange"}:
        if (Cube[5][1][0], Cube[1][2][1]) == ("White", "Orange"):
            return Cube, Ledger
        Cube, Ledger = Left(*Left(Cube, Ledger))
        #Ledger.append("Left")
        #Ledger.append("Left")

    if {"White", "Orange"} in MiddleEdges:
        if {Cube[2][1][2], Cube[3][1][0]} == {"White", "Orange"}:
            Cube, Ledger = Front(*Up(*FrontPrime(Cube, Ledger)))
            #Ledger.append("FrontPrime")
            #Ledger.append("Up")
            #Ledger.append("Front")
        elif {Cube[3][1][2], Cube[4][1][2]} == {"White", "Orange"}:
            Cube, Ledger = BackPrime(*UpPrime(*Back(Cube, Ledger)))
            #Ledger.append("Back")
            #Ledger.append("UpPrime")
            #Ledger.append("BackPrime")
        elif {Cube[4][1][0], Cube[1][1][0]} ==  {"White", "Orange"}:
            Cube, Ledger = Left(Cube, Ledger)
            #Ledger.append("Left")
        elif {Cube[1][1][2], Cube[2][1][0]} == {"White","Orange"}:
            Cube, Ledger = LeftPrime(Cube, Ledger)
            #Ledger.append("LeftPrime")
    while {Cube[0][1][0], Cube[1][0][1]} != {"White","Orange"}:
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if [Cube[0][1][0], Cube[1][0][1]] == ["White","Orange"]:
        Cube, Ledger = Left(*Left(Cube, Ledger))
        #Ledger.append("Left")
        #Ledger.append("Left")
        return Cube, Ledger
    Cube, Ledger = Front(*Left(*FrontPrime(*UpPrime(Cube, Ledger))))
    #Ledger.append("UpPrime")
    #Ledger.append("FrontPrime")
    #Ledger.append("Left")
    #Ledger.append("Front")
    return Cube, Ledger


def InsertWhiteBlueRedCorner(Cube,Ledger):
    BottomLayerCorners = [[Cube[2][2][2],Cube[3][2][0],Cube[5][0][2]], [Cube[3][2][2],Cube[4][0][2],Cube[5][2][2]], [Cube[4][0][0],Cube[1][2][0],Cube[5][2][0]], [Cube[1][2][2],Cube[2][2][0],Cube[5][0][0]]] 
    #BlueRedWhite, RedGreenWhite, GreenOrangeWhite, OrangeBlueWhite
    #TopLayerCorners =
    #Four cases: Corner in right spot; corner on white but in wrong spot; corner on top with white facing up, corner on top with white not facing up
    if (Cube[5][0][2]=="White") and (Cube[2][2][2]=="Blue") and (Cube[3][2][0]=="Red"):
        return Cube, Ledger
    for Corner in range(len(BottomLayerCorners)):
        if ("White" in BottomLayerCorners[Corner]) and ("Blue" in BottomLayerCorners[Corner]) and ("Red" in BottomLayerCorners[Corner]):
            if Corner == 0:
                Cube, Ledger = RightPrime(*Up(*Right(Cube, Ledger)))
                #Ledger.append("R U R'")
                break
            if Corner == 1:
                Cube, Ledger = Down(*RightPrime(*Up(*Right(*DownPrime(Cube, Ledger)))))
                #Ledger.append("D'")
                #Ledger.append("R U R'")
                #Ledger.append("D")
                break
            if Corner == 2:
                Cube, Ledger = Down(*Down(*RightPrime(*Up(*Right(*Down(*Down(Cube, Ledger)))))))
                #Ledger.append("D")
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D")
                #Ledger.append("D")
                break
            if Corner == 3:
                Cube, Ledger = DownPrime(*RightPrime(*Up(*Right(*Down(Cube, Ledger)))))
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D'")
                break
    #Now the corner should be on the top layer. move it to front side and insert
    
    while ({Cube[0][2][2],Cube[2][0][2],Cube[3][0][0]} != {"Red","Blue","White"}):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if Cube[0][2][2] == "White":  
        Cube, Ledger = UpPrime(*RightPrime(*Up(*Up(*Right(Cube, Ledger)))))
        #Ledger.append("R U U R' U'")
    if Cube[3][0][0] == "White":
        Cube, Ledger = RightPrime(*Up(*Right(Cube, Ledger)))
        #Ledger.append("R U R'")
        return Cube, Ledger
    Cube, Ledger = Front(*UpPrime(*FrontPrime(Cube, Ledger)))
    #Ledger.append("F' U' F")

    return Cube, Ledger

def InsertWhiteRedGreenCorner(Cube, Ledger):
    BottomLayerCorners = [[Cube[3][2][2],Cube[4][0][2],Cube[5][2][2]], [Cube[4][0][0],Cube[1][2][0],Cube[5][2][0]], [Cube[1][2][2],Cube[2][2][0],Cube[5][0][0]]] 
    # RedGreenWhite, GreenOrangeWhite, OrangeBlueWhite
    #TopLayerCorners =
    #Four cases: Corner in right spot; corner on white but in wrong spot; corner on top with white facing up, corner on top with white not facing up
    if (Cube[5][2][2]=="White") and (Cube[4][0][2]=="Green") and (Cube[3][2][2]=="Red"):
        return Cube, Ledger
    for Corner in range(len(BottomLayerCorners)):
        if ("White" in BottomLayerCorners[Corner]) and ("Green" in BottomLayerCorners[Corner]) and ("Red" in BottomLayerCorners[Corner]):
            if Corner == 0:
                Cube, Ledger = Down(*RightPrime(*Up(*Right(*DownPrime(Cube, Ledger)))))
                #Ledger.append("D'")
                #Ledger.append("R U R'")
                #Ledger.append("D")
                break
            if Corner == 1:
                Cube, Ledger = Down(*Down(*RightPrime(*Up(*Right(*Down(*Down(Cube, Ledger)))))))
                #Ledger.append("D")
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D")
                #Ledger.append("D")
                break
            if Corner == 2:
                Cube, Ledger = DownPrime(*RightPrime(*Up(*Right(*Down(Cube, Ledger)))))
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D'")
                break
    #Now the corner should be on the top layer. move it to front side and insert
    
    while ({Cube[0][2][2],Cube[2][0][2],Cube[3][0][0]} != {"Red","Green","White"}):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if Cube[0][2][2] == "White":  
        Cube, Ledger = Down(*UpPrime(*RightPrime(*Up(*Up(*Right(*DownPrime(Cube, Ledger)))))))
        #Ledger.append("D' R U U R' U' D")
    if Cube[3][0][0] == "White":
        Cube, Ledger = Down(*RightPrime(*Up(*Right(*DownPrime(Cube, Ledger)))))
        #Ledger.append("D' R U R' D")
        return Cube, Ledger
    Cube, Ledger = Down(*Front(*UpPrime(*FrontPrime(*DownPrime(Cube, Ledger)))))
    #Ledger.append("D' F' U' F D")
    return Cube, Ledger

def InsertWhiteGreenOrangeCorner(Cube,Ledger):
    BottomLayerCorners = [[Cube[4][0][0],Cube[1][2][0],Cube[5][2][0]], [Cube[1][2][2],Cube[2][2][0],Cube[5][0][0]]] 
    # GreenOrangeWhite, OrangeBlueWhite
    #TopLayerCorners =
    #Four cases: Corner in right spot; corner on white but in wrong spot; corner on top with white facing up, corner on top with white not facing up
    if (Cube[5][2][0]=="White") and (Cube[4][0][0]=="Green") and (Cube[1][2][0]=="Orange"):
        return Cube, Ledger
    for Corner in range(len(BottomLayerCorners)):
        if ("White" in BottomLayerCorners[Corner]) and ("Green" in BottomLayerCorners[Corner]) and ("Orange" in BottomLayerCorners[Corner]):
            if Corner == 0:
                Cube, Ledger = Down(*Down(*RightPrime(*Up(*Right(*Down(*Down(Cube, Ledger)))))))
                #Ledger.append("D")
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D")
                #Ledger.append("D")
                break
            if Corner == 1:
                Cube, Ledger = DownPrime(*RightPrime(*Up(*Right(*Down(Cube, Ledger)))))
                #Ledger.append("D")
                #Ledger.append("R U R'")
                #Ledger.append("D'")
                break
    #Now the corner should be on the top layer. move it to front side and insert
    
    while ({Cube[0][2][2],Cube[2][0][2],Cube[3][0][0]} != {"Orange","Green","White"}):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if Cube[0][2][2] == "White":  
        Cube, Ledger = Down(*Down(*UpPrime(*RightPrime(*Up(*Up(*Right(*DownPrime(*DownPrime(Cube, Ledger)))))))))
        #Ledger.append("D' D' R U U R' U' D D")
    if Cube[3][0][0] == "White":
        Cube, Ledger = Down(*Down(*RightPrime(*Up(*Right(*DownPrime(*DownPrime(Cube, Ledger)))))))
        #Ledger.append("D' D' R U R' D D")
        return Cube, Ledger
    Cube, Ledger = Down(*Down(*Front(*UpPrime(*FrontPrime(*DownPrime(*DownPrime(Cube, Ledger)))))))
    #Ledger.append("D' D' F' U' F D D")
    return Cube, Ledger

def InsertWhiteOrangeBlueCorner(Cube,Ledger):
    BottomLayerCorners = {Cube[1][2][2],Cube[2][2][0],Cube[5][0][0]} 
    # OrangeBlueWhite
    #TopLayerCorners =
    #Four cases: Corner in right spot; corner on white but in wrong spot; corner on top with white facing up, corner on top with white not facing up
    if (Cube[5][0][0]=="White") and (Cube[2][2][0]=="Blue") and (Cube[1][2][2]=="Orange"):
        return Cube, Ledger
    if BottomLayerCorners == {"Blue", "Orange", "White"}:
        Cube, Ledger = DownPrime(*RightPrime(*Up(*Right(*Down(Cube, Ledger)))))
        #Ledger.append("D")
        #Ledger.append("R U R'")
        #Ledger.append("D'")

    #print(Cube, Ledger)
    #print(Ledger)
    #Now the corner should be on the top layer. move it to front side and insert
    
    while ({Cube[0][2][2],Cube[2][0][2],Cube[3][0][0]} != {"Orange","Blue","White"}):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if Cube[0][2][2] == "White":  
        Cube, Ledger = DownPrime(*UpPrime(*RightPrime(*Up(*Up(*Right(*Down(Cube, Ledger)))))))
        #Ledger.append("D R U U R' U' D'")
    if Cube[3][0][0] == "White":
        Cube, Ledger = DownPrime(*RightPrime(*Up(*Right(*Down(Cube, Ledger)))))
        #Ledger.append("D R U R' D'")
        return Cube, Ledger
    Cube, Ledger = Down(*Front(*UpPrime(*FrontPrime(*DownPrime(Cube, Ledger)))))
    #Ledger.append("D F' U' F D'")
    return Cube, Ledger

def InsertBlueRedEdge(Cube, Ledger):
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]] #YellowGreen, YellowOrange, YellowBlue, YellowRed
    MiddleEdges = [[Cube[2][1][2], Cube[3][1][0]], [Cube[3][1][2], Cube[4][1][2]], [Cube[4][1][0], Cube[1][1][0]],[Cube[1][1][2], Cube[2][1][0]]] #BlueRed, RedGreen, GreenOrange, OrangeBlue
    #Check if BlueRed edge is in the right spot:
    if (Cube[2][1][2]=="Blue") and (Cube[3][1][0]=="Red"):
        return Cube, Ledger
    #Now check if the BlueRed piece is in the middle layer
    for Edge in range(len(MiddleEdges)):
        if MiddleEdges[Edge] == (["Blue", "Red"]) or MiddleEdges[Edge] ==(["Red", "Blue"]):
            #Do the insertion alg corresponding to the Edge #
            if Edge == 0:
                Cube, Ledger = BlueF2LRight(Cube, Ledger)
                #Ledger.append("BlueF2LRight")
                break
            if Edge == 3:
                Cube, Ledger = BlueF2LLeft(Cube, Ledger)
                #Ledger.append("BlueF2LLeft")
                break
            if Edge == 1:
                Cube, Ledger = RedF2LRight(Cube, Ledger)
                #Ledger.append("RedF2LRight")
                break
            if Edge == 2:
                Cube, Ledger = OrangeF2LLeft(Cube, Ledger)
                #Ledger.append("OrangeF2LLeft")
                break
    #Now the Edge must be in top layer, just need to update top layer:    
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]]
    #Lets rotate top layer until Edge is in correct position (of the two possibilities)
    #[Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]
    while ([Cube[0][2][1], Cube[2][0][1]] != ["Red", "Blue"]) and ([Cube[0][1][2], Cube[3][0][1]] != ["Blue", "Red"]):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if ([Cube[0][2][1], Cube[2][0][1]] == ["Red", "Blue"]):
        Cube, Ledger = BlueF2LRight(Cube, Ledger)
        #Ledger.append("BlueF2LRight")
        return Cube, Ledger
    Cube, Ledger = RedF2LLeft(Cube, Ledger)
    #Ledger.append("RedF2LLeft")
    return Cube, Ledger

def InsertRedGreenEdge(Cube, Ledger):
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]] #YellowGreen, YellowOrange, YellowBlue, YellowRed
    MiddleEdges = [[Cube[3][1][2], Cube[4][1][2]], [Cube[4][1][0], Cube[1][1][0]],[Cube[1][1][2], Cube[2][1][0]]] #RedGreen, GreenOrange, OrangeBlue
    #Check if RedGreen edge is in the right spot:
    if (Cube[3][1][2]=="Red") and (Cube[4][1][2]=="Green"):
        return Cube, Ledger
    #Now check if the RedGreen piece is in the middle layer
    for Edge in range(len(MiddleEdges)):
        if MiddleEdges[Edge] == (["Red", "Green"]) or MiddleEdges[Edge] ==(["Green", "Red"]):
            #Do the insertion alg corresponding to the Edge #
            if Edge == 2:
                Cube, Ledger = BlueF2LLeft(Cube, Ledger)
                #Ledger.append("BlueF2LLeft")
                break
            if Edge == 0:
                Cube, Ledger = RedF2LRight(Cube, Ledger)
                #Ledger.append("RedF2LRight")
                break
            if Edge == 1:
                Cube, Ledger = OrangeF2LLeft(Cube, Ledger)
                #Ledger.append("OrangeF2LLeft")
                break
    #Now the Edge must be in top layer, just need to update top layer:    
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]]
    #Lets rotate top layer until Edge is in correct position (of the two possibilities)
    #[Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]
    while ([Cube[0][1][2], Cube[3][0][1]] != ["Green", "Red"]) and ([Cube[0][0][1], Cube[4][2][1]] != ["Red", "Green"]):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if ([Cube[0][1][2], Cube[3][0][1]] == ["Green", "Red"]):
        Cube, Ledger = RedF2LRight(Cube, Ledger)
        #Ledger.append("RedF2LRight")
        return Cube, Ledger
    Cube, Ledger = GreenF2LLeft(Cube, Ledger)
    #Ledger.append("GreenF2LLeft")
    return Cube, Ledger

def InsertGreenOrangeEdge(Cube,Ledger):
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]] #YellowGreen, YellowOrange, YellowBlue, YellowRed
    MiddleEdges = [[Cube[4][1][0], Cube[1][1][0]],[Cube[1][1][2], Cube[2][1][0]]] # GreenOrange, OrangeBlue
    #Check if GreenOrange edge is in the right spot:
    if (Cube[4][1][0]=="Green") and (Cube[1][1][0]=="Orange"):
        return Cube, Ledger
    #Now check if the GreenOrange piece is in the middle layer
    for Edge in range(len(MiddleEdges)):
        if MiddleEdges[Edge] == (["Green", "Orange"]) or MiddleEdges[Edge] ==(["Orange", "Green"]):
            #Do the insertion alg corresponding to the Edge #
            if Edge == 1:
                Cube, Ledger = BlueF2LLeft(Cube, Ledger)
                #Ledger.append("BlueF2LLeft")
                break
            if Edge == 0:
                Cube, Ledger = OrangeF2LLeft(Cube, Ledger)
                #Ledger.append("OrangeF2LLeft")
                break
    #Now the Edge must be in top layer, just need to update top layer:    
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]]
    #Lets rotate top layer until Edge is in correct position (of the two possibilities)
    #[Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]
    while ([Cube[0][1][0], Cube[1][0][1]] != ["Green", "Orange"]) and ([Cube[0][0][1], Cube[4][2][1]] != ["Orange", "Green"]):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if ([Cube[0][1][0], Cube[1][0][1]] == ["Green", "Orange"]):
        Cube, Ledger = OrangeF2LLeft(Cube, Ledger)
        #Ledger.append("OrangeF2LLeft")
        return Cube, Ledger
    Cube, Ledger = GreenF2LRight(Cube, Ledger)
    #Ledger.append("GreenF2LRight")
    return Cube, Ledger

def InsertOrangeBlueEdge(Cube, Ledger):
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]] #YellowGreen, YellowOrange, YellowBlue, YellowRed
    MiddleEdges = [[Cube[1][1][2], Cube[2][1][0]]] #  OrangeBlue
    #Check if OrangeBlue edge is in the right spot:
    if (Cube[1][1][2]=="Orange") and (Cube[2][1][0]=="Blue"):
        return Cube, Ledger
    #Now check if the OrangeBlue piece is in the middle layer (only one possible slot now):
    if (Cube[1][1][2]=="Blue") and (Cube[2][1][0]=="Orange"):
        Cube, Ledger = BlueF2LLeft(Cube, Ledger)
        #Ledger.append("BlueF2LLeft")

    #Now the Edge must be in top layer, just need to update top layer:    
    #TopEdges = [[Cube[0][0][1], Cube[4][2][1]], [Cube[0][1][0], Cube[1][0][1]], [Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]]
    #Lets rotate top layer until Edge is in correct position (of the two possibilities)
    #[Cube[0][2][1], Cube[2][0][1]],[Cube[0][1][2], Cube[3][0][1]]
    while ([Cube[0][1][0], Cube[1][0][1]] != ["Blue", "Orange"]) and ([Cube[0][2][1], Cube[2][0][1]] != ["Orange", "Blue"]):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if ([Cube[0][1][0], Cube[1][0][1]] == ["Blue", "Orange"]):
        Cube, Ledger = OrangeF2LRight(Cube, Ledger)
        #Ledger.append("OrangeF2LRight")
        return Cube, Ledger
    Cube, Ledger = BlueF2LLeft(Cube, Ledger)
    #Ledger.append("BlueF2LLeft")
    return Cube, Ledger

def IdentifyYellowLayer(Cube, Ledger):
    EdgeYellowCount = 0
    YellowEdges = [Cube[0][0][1], Cube[0][1][0], Cube[0][1][2], Cube[0][2][1]]
    for Edge in YellowEdges: #Cube[0] is Yellow face
        if Edge == "Yellow":
            EdgeYellowCount += 1
    if EdgeYellowCount == 0:
        return "Dot"
    if EdgeYellowCount == 4:
        return "Cross"
    if (Cube[0][0][1] == "Yellow") and (Cube[0][2][1] == "Yellow") and (Cube[0][1][0] != "Yellow"):
        return "Blue to Green Bar"
    if (Cube[0][1][0] == "Yellow") and (Cube[0][1][2] == "Yellow") and (Cube[0][0][1] != "Yellow"):
        return "Bar"
    return "Hook"
    

#def IsItBar(Cube, Ledger): 
    if (Cube[0][0][1] == "Yellow") and (Cube[0][2][1] == "Yellow") and (Cube[0][1][0] != "Yellow"):
        return True
    if (Cube[0][1][0] == "Yellow") and (Cube[0][1][2] == "Yellow") and (Cube[0][0][1] != "Yellow"):
        return True
    return False

#def IsItHook(Cube, Ledger):
    YellowEdges = [Cube[0][0][1], Cube[0][1][0], Cube[0][1][2], Cube[0][2][1]]
    for Edge in YellowEdges: #Cube[0] is Yellow face
        if Edge == "Yellow":
            EdgeYellowCount += 1
    if (EdgeYellowCount == 2) and not IsItBar(Cube, Ledger):
        return True
    return False

#def IsItDot(Cube, Ledger):
    EdgeYellowCount = 0
    YellowEdges = [Cube[0][0][1], Cube[0][1][0], Cube[0][1][2], Cube[0][2][1]]
    for Edge in YellowEdges: #Cube[0] is Yellow face
        if Edge == "Yellow":
            EdgeYellowCount += 1
        if EdgeYellowCount !=0:
            return False
    return True

def SolveYellowCross(Cube, Ledger):
    YellowLayer = IdentifyYellowLayer(Cube, Ledger)
    if YellowLayer == "Cross":
        return Cube, Ledger
    if YellowLayer == "Dot":
        Cube, Ledger = Hook(*Bar(Cube, Ledger))
        #Ledger.append("Bar")
        #Ledger.append("Hook")
        return Cube, Ledger
    if YellowLayer == "Bar":
        Cube, Ledger = Bar(Cube, Ledger)
        #Ledger.append("Bar")
        return Cube, Ledger
    if YellowLayer == "Blue to Green Bar":
        Cube, Ledger = Bar(*Up(Cube, Ledger))
        #Ledger.append("Up")
        #Ledger.append("Bar")
        return Cube, Ledger
    #elsewise Yellow layer = Hook. Now just need to turn last layer so that hook is oriented:
    if Cube[0][2][1] == "Yellow":
        if Cube[0][1][2] == "Yellow":
            Cube, Ledger = Hook(Cube, Ledger)
            #Ledger.append("Hook")
            return Cube, Ledger
        Cube, Ledger = Hook(*UpPrime(Cube, Ledger))
        #Ledger.append("UpPrime")
        #Ledger.append("Hook")
        return Cube, Ledger
    if Cube[0][1][0] == "Yellow":
        Cube, Ledger = Hook(*Up(*Up(Cube, Ledger)))
        #Ledger.append("Up")
        #Ledger.append("Up")
        #Ledger.append("Hook")
        return Cube, Ledger
    Cube, Ledger = Hook(*Up(Cube, Ledger))
    #Ledger.append("Up")
    #Ledger.append("Hook")
    return Cube, Ledger

def TwoYellowCornersSolver(Cube, YellowCorners, Ledger): #YlwCorners = Signs;[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,1,0,1], Infinities:  [1,0,0,1], [0,1,1,0]
    if (YellowCorners == [1,0,0,1]) or (YellowCorners == [0,1,1,0]):
        #Infinity; Now just rotate until Blue Top left corner is yellow
        while Cube[2][0][0] != "Yellow":
            Cube, Ledger = Up(Cube, Ledger)
            #Ledger.append("Up")
        Cube, Ledger = ReverseFish(*Up(*Up(*Fish(Cube, Ledger))))
        #Ledger.append("Fish")
        #Ledger.append("Up")
        #Ledger.append("Up")
        #Ledger.append("ReverseFish")
        return Cube, Ledger
    #elsewise we have sign
    while (Cube[0][0][0] == "Yellow") or (Cube[0][2][0] == "Yellow"): 
        Cube, Ledger = Up(Cube, Ledger) #Orienting the sign
        #Ledger.append("Up")
    if Cube[2][0][0] != "Yellow": 
        Cube, Ledger = ReverseFish(*Up(*Fish(*UpPrime(Cube, Ledger))))
        #Ledger.append("UpPrime")
        #Ledger.append("Fish")
        #Ledger.append("Up")
        #Ledger.append("ReverseFish")
        return Cube, Ledger
    Cube, Ledger = ReverseFish(*UpPrime(*Fish(Cube, Ledger)))
    #Ledger.append("Fish")
    #Ledger.append("UpPrime")
    #Ledger.append("ReverseFish")
    return Cube, Ledger

def SolveYellowSide(Cube, Ledger):
    TopCorners = [Cube[0][0][0], Cube[0][0][2], Cube[0][2][0], Cube[0][2][2]]
    YellowCorners = []
    YellowCornerCount = 0
    for Corner in TopCorners:
        if Corner == "Yellow":
            YellowCorners.append(1)
            YellowCornerCount += 1
        else:
            YellowCorners.append(0)
    #print(Cube, Ledger)
    #print(Ledger)
    
    if YellowCornerCount == 4: #Yellow solved!
        return Cube, Ledger
    if YellowCornerCount == 3: #Not possible!
        print("Error: Impossible yellow side.")
        print(Cube, Ledger)
        exit()
        return
    if YellowCornerCount == 2: #4 cases to determine from; lets make function to solve this
        Cube, Ledger = TwoYellowCornersSolver(Cube, YellowCorners, Ledger)
        return Cube, Ledger
    if YellowCornerCount ==1: #Fish - just have to figure out what type:
        while Cube[0][2][0] != "Yellow":
            Cube, Ledger = Up(Cube, Ledger)
            #Ledger.append("Up")
        if Cube[2][0][2] == "Yellow": #Case 7
            Cube, Ledger = Fish(Cube, Ledger)
            #Ledger.append("Fish")
            return Cube, Ledger
        Cube, Ledger = ReverseFish(*Up(*Up(Cube, Ledger))) #Case 8
        #Ledger.append("Up")
        #Ledger.append("Up")
        #Ledger.append("ReverseFish")
        return Cube, Ledger
    #elsewise YellowCornerCount == 0: 
    #print(Cube, Ledger)
    #print(Ledger)
    while (Cube[2][0][0] != "Yellow") or (Cube[2][0][2] != "Yellow"):
        Cube, Ledger = Up(Cube, Ledger)
        #Ledger.append("Up")
    if Cube[4][2][0] == "Yellow": #Then we have Case 1
        Cube, Ledger = Fish(*Fish(*Up(Cube, Ledger)))
        #Ledger.append("Up")
        #Ledger.append("Fish")
        #Ledger.append("Fish")
        return Cube, Ledger
    #Else case 2:
    Cube, Ledger = ReverseFish(*UpPrime(*ReverseFish(*Up(Cube, Ledger))))
    #Ledger.append("Up")
    #Ledger.append("ReverseFish")
    #Ledger.append("UpPrime")
    #Ledger.append("ReverseFish")
    return Cube, Ledger

def SolveLastLayer(Cube, Ledger):
    SolvedCube = [[["Yellow", "Yellow","Yellow"],["Yellow", "Yellow","Yellow"], ["Yellow", "Yellow","Yellow"]],[["Orange","Orange","Orange"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Blue","Blue"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Red","Red","Red"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Green","Green"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
    while Cube != SolvedCube:
        LastLayer = [[Cube[1][0][0],Cube[1][0][1], Cube[1][0][2]], [Cube[2][0][0], Cube[2][0][1], Cube[2][0][2]], [Cube[3][0][0],Cube[3][0][1],Cube[3][0][2]], [Cube[4][2][2],Cube[4][2][1], Cube[4][2][0]]]
        MatchingCorners = 0
        for Side in LastLayer: #Count number of sides with matching corners
            if Side[0] == Side[2]:
                MatchingCorners +=1
        if MatchingCorners == 0:
            Cube, Ledger = LastLayerAlg(Cube, Ledger)
            #Ledger.append("LastLayerAlg")
            continue
        if MatchingCorners == 1:
            while Cube[4][2][2] != Cube[4][2][0]: #orient so that matching corners are on green side, then LL alg
                Cube, Ledger = Up(Cube, Ledger)
                #Ledger.append("Up")
            Cube, Ledger = LastLayerAlg(Cube, Ledger)
            #Ledger.append("LastLayerAlg")  
            continue
    
        if MatchingCorners == 4: #Uperm time; now just need to count # of sides where top corners match top middle, and also find which direction to uperm
            MatchingCornersAndEdges = 0
            for Side in LastLayer:
                if Side[0] == Side[1]:
                    MatchingCornersAndEdges += 1
            if MatchingCornersAndEdges == 4: #Solved last layer!
                safetycounter = 0
                while Cube != SolvedCube:
                    Cube, Ledger = Up(Cube, Ledger)
                    #Ledger.append("Up")
                    safetycounter += 1
                    if safetycounter ==6:
                        print("Something is wrong here...")
                        exit()
            if MatchingCornersAndEdges == 0: #shouldn't matter which direction you Uperm
                Cube, Ledger = UPermUp(Cube, Ledger)
                #Ledger.append("UPermUp")
                continue
            if MatchingCornersAndEdges == 1: #Turn upper layer until green side has matching pair
                while Cube[4][2][2] != Cube[4][2][1]:
                    Cube, Ledger = Up(Cube, Ledger)
                    #Ledger.append("Up") 
                #Now cube is oriented right, but we still should figure out which way to uperm:
                #compare Blue top middle edge to red top left corner: if same color, UPrime uperm, otherwise Uperm
                if Cube[2][0][1] == Cube[3][0][0]:
                    Cube, Ledger = UPermUpPrime(Cube, Ledger)
                    #Ledger.append("UPermUpPrime")
                    continue
                Cube, Ledger = UPermUp(Cube, Ledger)
                #Ledger.append("UPermUp")
                continue
            
    return Cube, Ledger


#SolvedCube = [[["Yellow", "Yellow","Yellow"],["Yellow", "Yellow","Yellow"], ["Yellow", "Yellow","Yellow"]],[["Orange","Orange","Orange"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Blue","Blue"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Red","Red","Red"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Green","Green"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]

# SolvedCubeTest = [[["Yellow", "Yellow","Yellow"],["Yellow", "Yellow","Yellow"], ["Yellow", "Yellow","Yellow"]],[["Orange","Orange","Orange"],["Orange","Orange","Orange"],["Orange1","Orange2","Orange3"]],[["Blue","Blue","Blue"],["Blue","Blue","Blue"],["Blue1","Blue2","Blue3"]],[["Red","Red","Red"],["Red","Red","Red"],["Red1","Red2","Red3"]],[["Green3","Green2","Green1"],["Green","Green","Green"],["Green","Green","Green"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]

# print(*Down(SolvedCubeTest))

#print(*UpermUpPrime(SolvedCube))

#print(*Up(*Up(*Back(*Left(*Left(*Down(*Front(*Front(*RightPrime(*Left(*Back(*Up(*Right(SolvedCube))))))))))))))
#print(*Down(*Front(*Front(*RightPrime(*Left(*Back(*Up(*Right(SolvedCube)))))))))


#print(*Up(*Right(*Right(*Left(*BackPrime(*Down(*Front(*Front(*Down(*UpPrime(*LeftPrime(*Up(*Right(*FrontPrime(*Down(*Left(*RightPrime(*Down(*Front(*Front(*LeftPrime(*Up(*Up(*Front(*Front(*Down(*Left(*Up(*Up(*Back(*Down(*Down(SolvedCube)))))))))))))))))))))))))))))))))


