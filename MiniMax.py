import PositionClass
import json
def minimax(Match, Depth=0, IsMaxPlayer=True,StartPlayer=None):
    # In this case, human is maximising player and AI is minimising one
    if Depth == 0:
        StartPlayer = Match.TurnOrder()
    if Depth == 12:
        return 0
    GameEnd = False
    for i in range(0,7):
        if Match.checkWin(i):
            GameEnd = True
    if GameEnd:
        Winner = Match.TurnOrder()
        if Winner == StartPlayer:
            return Match.pieces//2 + Match.pieces%2
        else:
            return -(Match.pieces//2 + Match.pieces%2)
    elif Match.pieces == 0:
        return 0


    if IsMaxPlayer:
        bestScore = -1000
        Pmove = []
        for i in range(0,7):
            if Match.LegalPlay(i):
                Pmove.append(i)
        for move in Pmove:
            Match.play(move)
            score = minimax(Match,Depth+1,not IsMaxPlayer,StartPlayer)
            Match.UndoPlay()
            bestScore = max(bestScore,score)
        return bestScore

    elif not IsMaxPlayer:
        bestScore = 1000
        Pmove = []
        for i in range(0,7):
            if Match.LegalPlay(i):
                Pmove.append(i)
        for move in Pmove:
            Match.play(move)
            score = minimax(Match,Depth+1,not IsMaxPlayer,StartPlayer)
            Match.UndoPlay()
            bestScore = min(bestScore,score)
        return bestScore

def BestMove(Match):
    PotentScore = []
    Pmove = []
    BestScore = -1000
    Bmove = -1
    WinCon = Match.checkPossibleWin()
    for i in range(0, 7):
        if Match.LegalPlay(i):
            Pmove.append(i)
    for move in Pmove:
        if move in WinCon:
            score = minimax(Match)
        else:
            Match.play(move)
            score = -(minimax(Match))
            Match.UndoPlay()
        PotentScore.append(score)
        if score > BestScore:
            BestScore = score
            Bmove = move
    return Bmove