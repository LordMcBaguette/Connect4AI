import PositionClass
import AlphaBetaPruning as AI

Tests = open("TestFiles/Test_L3_R1.txt","r")

total = 0
Success = 0
answers = []
for line in Tests:
    total += 1
    cut = line.find(" ")
    Game = PositionClass.position()
    Game.ReadGameState(line[0:cut])
    FoundScore = AI.minimax(Game)
    TrueScore = int(line[cut+1:len(line)])
    if FoundScore == TrueScore:
        Success += 1
    else:
        print(str(total) + "   " + str(FoundScore) +  "   " + str(TrueScore))
print(str(Success)+" / "+str(total))

