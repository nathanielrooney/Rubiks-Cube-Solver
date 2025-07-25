from InputtingCube import *
from Moves import *

SolvedCube = [[["Yellow", "Yellow","Yellow"],["Yellow", "Yellow","Yellow"], ["Yellow", "Yellow","Yellow"]],[["Orange","Orange","Orange"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Blue","Blue"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Red","Red","Red"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Green","Green"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
Scramble = []

#Given scrambled cube, locate White edge piees, 
#Scrambled F2L Solved:
# One = [[["Yellow", "Green","Blue"],["Yellow", "Yellow","Red"], ["Orange", "Yellow","Red"]],[["Orange","Blue","Blue"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Yellow","Orange","Green"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Yellow","Yellow","Red"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Yellow","Yellow"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Two = [[["Red", "Yellow","Yellow"],["Orange", "Yellow","Red"], ["Orange", "Yellow","Green"]],[["Yellow","Yellow","Blue"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Yellow","Blue","Orange"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Yellow","Yellow","Blue"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Green","Red"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Three = [[["Green", "Red","Yellow"],["Blue", "Yellow","Orange"], ["Yellow", "Green","Green"]],[["Yellow","Yellow","Orange"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Yellow","Yellow"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Red","Yellow","Blue"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Orange","Yellow","Red"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Four = [[["Green", "Yellow","Red"],["Yellow", "Yellow","Yellow"], ["Blue", "Yellow","Red"]],[["Yellow","Orange","Yellow"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Orange","Blue","Green"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Yellow","Green","Yellow"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Orange","Red","Blue"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Five = [[["Blue", "Yellow","Red"],["Orange", "Yellow","Yellow"], ["Yellow", "Red","Orange"]],[["Orange","Yellow","Red"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Green","Yellow","Yellow"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Green","Blue","Yellow"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Yellow","Green","Blue"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]


# Six = [[["Yellow", "Yellow","Yellow"],["Red", "Yellow","Green"], ["Yellow", "Yellow","Yellow"]],[["Orange","Yellow","Orange"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Orange","Red"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Green","Yellow","Blue"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Green","Blue","Red"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Seven = [[["Green", "Yellow","Yellow"],["Red", "Yellow","Green"], ["Red", "Yellow","Yellow"]],[["Yellow","Yellow","Yellow"],["Orange","Orange","Orange"],["Orange","Orange","Orange"]],[["Blue","Blue","Red"],["Blue","Blue","Blue"],["Blue","Blue","Blue"]],[["Green","Yellow","Orange"],["Red","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Green","Green","Green"],["Orange","Orange","Blue"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
# Eight =[[["Green", "Green","Yellow"],["Blue", "Yellow","Yellow"], ["Blue", "Yellow","Orange"]],[["Yellow","Orange","Red"],["Green","Orange","Green"],["Orange","Orange","Orange"]],[["Yellow","Red","Blue"],["Red","Blue","Yellow"],["Blue","Blue","Blue"]],[["Yellow","Blue","Red"],["Orange","Red","Blue"],["Red","Red","Red"]],[["Green","Green","Green"],["Yellow","Green","Red"],["Orange","Orange","Green"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
#Nine = [[["Orange", "Green","Orange"],["Green", "Yellow","Yellow"], ["Yellow", "Yellow","Yellow"]],[["Green","Red","Blue"],["Green","Orange","Blue"],["Orange","Orange","Orange"]],[["Red","Blue","Red"],["Orange","Blue","Red"],["Blue","Blue","Blue"]],[["Green","Orange","Blue"],["Yellow","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Yellow","Green","Blue"],["Yellow","Orange","Yellow"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]
#Ten = [[["Orange", "Green","Red"],["Orange", "Yellow","Blue"], ["Orange", "Orange","Red"]],[["Green","Yellow","Blue"],["Green","Orange","Yellow"],["Orange","Orange","Orange"]],[["Yellow","Blue","Yellow"],["Blue","Blue","Red"],["Blue","Blue","Blue"]],[["Blue","Red","Green"],["Green","Red","Red"],["Red","Red","Red"]],[["Green","Green","Green"],["Yellow","Green","Yellow"],["Yellow","Orange","Yellow"]],[["White","White","White"],["White","White","White"],["White","White","White"]]]

#Eleven = DownPrime(*RightPrime(*Up(*Right(*UpPrime(*RightPrime(*Up(*Right(*Down(SolvedCube)))))))))
#Twelve = [[["Blue", "Yellow","Yellow"],["Orange", "Yellow","Yellow"], ["Orange", "Green","Red"]],[["Orange","Yellow","White"],["Orange","Orange","Orange"],["Blue","Orange","Orange"]],[["Blue","Yellow","White"],["Green","Blue","Red"],["White","Blue","Orange"]],[["Green","Blue","Red"],["Green","Red","Blue"],["Green","Red","White"]],[["Red","Green","Blue"],["Blue","Green","Red"],["Yellow","Red","Green"]],[["Green","White","Yellow"],["White","White","White"],["Yellow","White","Red"]]]
#Thirteen = [[["Orange", "Orange","Green"],["Yellow", "Yellow","Blue"], ["Orange", "Orange","Yellow"]],[["Blue","Green","Green"],["Red","Orange","Red"],["Blue","Orange","Yellow"]],[["White","Yellow","Orange"],["Blue","Blue","Green"],["Green","Blue","Blue"]],[["Blue","Yellow","Orange"],["Orange","Red","Yellow"],["Yellow","Red","White"]],[["White","Green","Red"],["Green","Green","Red"],["White","Blue","Yellow"]],[["Red","White","Red"],["White","White","White"],["Red","White","Green"]]]
#Fourteen = Right(*Front(*DownPrime(*Back(*Right(*Right(*Left(*FrontPrime((*RightPrime(*Down(*Front(*Right(*Back(*Up(*Up(*LeftPrime(*Down(*Up(SolvedCube)))))))))))))))))))
#Fifteen = Left(*Left(*UpPrime(*Back(*Back(*UpPrime(*Front(*Down(*Left(*UpPrime(*Left(*Front(*Front(*Up(*BackPrime(*Down(*Down(*Front(*Right(*Right(SolvedCube))))))))))))))))))))
#Sixteen = Right(*UpPrime(*Left(*Back(*Back(*Down(*Front(*Left(*Front(*Up(*Up(*Back(*Right(*Down(*Right(SolvedCube)))))))))))))))

#Seventeen, Scramble = Up(*Up(*Back(*Back(*Up(*Back(*DownPrime(*FrontPrime(*Up(*Up(*RightPrime(*Front(*Down(*Down(*Front(*Up(*Up(*BackPrime(*Left(*Left(*Front(*Front(*Up(*Up(*FrontPrime(*Down(*Down(*Left(*Left(*Back(*Back(*Down(SolvedCube, Scramble))))))))))))))))))))))))))))))))

#Cube = Down(*Front(*UpPrime(*FrontPrime(*DownPrime(*RightPrime(*Up(*Right(*Up(*Up(*Up(*Down(*RightPrime(*Up(*Right(*DownPrime(SolvedCube))))))))))))))))


#print(IdentifyYellowLayer(Four))
Ledger = []

#Solving White Cross
Ledger.append("Solving White Cross:")
Cube, Ledger = InsertWhiteBlue(Cube,Ledger)
Cube, Ledger = InsertWhiteRed(Cube,Ledger)
Cube, Ledger = InsertWhiteGreen(Cube,Ledger)
Cube, Ledger = InsertWhiteOrange(Cube,Ledger)

#Solving White Face
Ledger.append("Solving White Face:")
Cube, Ledger = InsertWhiteBlueRedCorner(Cube,Ledger)
Cube, Ledger = InsertWhiteRedGreenCorner(Cube, Ledger)
Cube, Ledger = InsertWhiteGreenOrangeCorner(Cube, Ledger)
Cube, Ledger = InsertWhiteOrangeBlueCorner(Cube, Ledger)

#Solving F2L
# print(Cube):
# print(Ledger)
Ledger.append("Solving First Two Layers:")
Ledger.append("Inserting Blue and Red Edge:")
Cube, Ledger = InsertBlueRedEdge(Cube, Ledger)
Ledger.append("Inserting Red and Green Edge:")
Cube, Ledger = InsertRedGreenEdge(Cube, Ledger)
Ledger.append("Inserting Green and Orange Edge:")
Cube, Ledger = InsertGreenOrangeEdge(Cube,Ledger)
Ledger.append("Inserting Orange and Blue Edge:")
Cube, Ledger = InsertOrangeBlueEdge(Cube,Ledger)

#Solving Yellow Cross
Ledger.append("Solving Yellow Cross:")
Cube, Ledger = SolveYellowCross(Cube,Ledger)

#Solving Yellow Face
Ledger.append("Solving Yellow Face:")
Cube, Ledger = SolveYellowSide(Cube,Ledger)

#Solving Last Layer
Ledger.append("Solving Last Layer:")
Cube, Ledger = SolveLastLayer(Cube,Ledger)

print("Results:")
if Cube != SolvedCube:
    print(Cube)
print("Moves:")
for move in Ledger:
    print(move, end= " ")
