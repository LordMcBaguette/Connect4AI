class position:
    def __init__(self):
        self.gamepos = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]
        self.playorder = []
        self.pieces = 42

    def ReadGameState(self,GS):
        for i in GS:
            self.play(int(i)-1)

    def LegalPlay(self,colummn):
        return self.gamepos[colummn][0] == -1
    def TurnOrder(self):
        if self.pieces %2 == 0:return True
        return False
    def play(self,colummn):
        if self.LegalPlay(colummn):
            c = True
            i = 5
            while c == True:
                if self.gamepos[colummn][i] == -1:
                    self.gamepos[colummn][i] = self.TurnOrder()
                    self.pieces -= 1
                    self.playorder.append(colummn)
                    c = False
                i -= 1
    def UndoPlay(self):
        columm = self.playorder[-1]
        i = 0
        c = True
        while c == True:
            if self.gamepos[columm][i] != -1:
                self.gamepos[columm][i] = -1
                self.pieces +=1
                self.playorder.pop()
                c = False
            i += 1
    def Verti(self):
        Wincolumm = []
        no = 0
        colour = self.TurnOrder()
        for columm in self.gamepos:
            LenoWin = 1
            for i in range(4, -1, -1):
                if colour == columm[i] == columm[i + 1] and columm[i + 1] != -1:
                    LenoWin += 1
                    if LenoWin == 3 and columm[i - 1] == -1:
                        Wincolumm.append(no)
                else:
                    LenoWin = 1
            no += 1
        return Wincolumm
    def Horiscan(self):
        LenoWin = 1
        colour = self.TurnOrder()
        Wincolumm = []
        for row in range(5, -1, -1):
            for i in range(1, 7):
                if self.gamepos[i][row] == self.gamepos[i - 1][row] == colour:
                    LenoWin += 1
                    if LenoWin == 2:
                        if i <= 4:
                            if row == 5 and self.gamepos[i+1][row] == -1 and self.gamepos[i+2][row] == colour:
                                Wincolumm.append(i+1)
                            try:
                                if self.gamepos[i+1][row+1] != -1 and self.gamepos[i+1][row] == -1 and self.gamepos[i+2][row] == colour:
                                    Wincolumm.append(i+1)
                            except:pass
                        if i >= 3:
                            if row == 5 and self.gamepos[i-1][row] == -1 and self.gamepos[i-1][row] == colour:
                                Wincolumm.append(i - 1)
                            try:
                                if self.gamepos[i  -2][row + 1] != -1 and self.gamepos[i - 2][row] == -1 and self.gamepos[i-3][row] == colour:
                                    Wincolumm.append(i - 2)
                            except: pass
                    elif LenoWin >= 3:
                        if row == 5:
                            if ((self.gamepos[i - 3][row] == -1 and i - 3 >= 0)):
                                Wincolumm.append(i-3)
                            try:
                                if (self.gamepos[i + 1][row] == -1):
                                    Wincolumm.append(i + 1)
                            except: pass
                        elif ((self.gamepos[i - 3][row] == -1 and i - 3 >= 0)) and self.gamepos[i-3][row+1] != -1:
                            Wincolumm.append(i - 3)
                        try:
                            if (self.gamepos[i+1][row] == -1) and self.gamepos[i+1][row+1] != -1:
                                Wincolumm.append(i+1)
                        except:pass
                else:
                    LenoWin = 1
            LenoWin = 1
        return Wincolumm
    def DownrightScan(self):
        colour = self.TurnOrder()
        Wincolumm = []
        for i in range(0,4):
            for j in range(0,3):
                if self.gamepos[i][j] == self.gamepos[i+1][j+1] == self.gamepos[i+2][j+2] == colour and self.gamepos[i+3][j+3] == -1 and j == 2:
                    if i+3 not in Wincolumm:Wincolumm.append(i+3)
                elif self.gamepos[i][j] == self.gamepos[i+1][j+1] == self.gamepos[i+3][j+3] == colour and self.gamepos[i+2][j+2] == -1 and self.gamepos[i+2][j+3] != -1:
                    if i+2 not in Wincolumm:Wincolumm.append(i+2)
                elif self.gamepos[i][j] == self.gamepos[i + 2][j + 2] == self.gamepos[i + 3][j + 3] == colour and self.gamepos[i+1][j+1] == -1 and self.gamepos[i+1][j+2] != -1:
                    if i+1 not in Wincolumm:Wincolumm.append(i+1)
                elif self.gamepos[i+1][j+1] == self.gamepos[i + 2][j + 2] == self.gamepos[i + 3][j + 3] == colour and self.gamepos[i][j] == -1 and self.gamepos[i][j+1] != -1:
                    if i not in Wincolumm:Wincolumm.append(i)
                try:
                    if self.gamepos[i][j] == self.gamepos[i + 1][j + 1] == self.gamepos[i + 2][j + 2] == colour and self.gamepos[i + 3][j + 3] == -1 and self.gamepos[i + 3][j + 4] != -1:
                        if i + 3 not in Wincolumm: Wincolumm.append(i + 3)
                except:
                    pass
        return Wincolumm
    def UprightScan(self):
        colour = self.TurnOrder()
        Wincolumm = []
        for i in range(0, 4):
            for j in range(5, 2,-1):
                if self.gamepos[i][j] == self.gamepos[i + 1][j - 1] == self.gamepos[i + 2][j - 2] == colour and self.gamepos[i + 3][j - 3] == -1  and self.gamepos[i+3][j-2] != -1:
                    if i + 3 not in Wincolumm: Wincolumm.append(i + 3)
                elif self.gamepos[i][j] == self.gamepos[i + 1][j - 1] == self.gamepos[i + 3][j - 3] == colour and self.gamepos[i + 2][j - 2] == -1 and self.gamepos[i+2][j-1] != -1:
                    if i + 2 not in Wincolumm: Wincolumm.append(i + 2)
                elif self.gamepos[i][j] == self.gamepos[i + 2][j - 2] == self.gamepos[i + 3][j - 3] == colour and self.gamepos[i + 1][j - 1] == -1 and self.gamepos[i+1][j] !=-1:
                    if i + 1 not in Wincolumm: Wincolumm.append(i + 1)
                elif self.gamepos[i + 1][j - 1] == self.gamepos[i + 2][j - 2] == self.gamepos[i + 3][j - 3] == colour and self.gamepos[i][j] == -1 and j == 5:
                    if i not in Wincolumm: Wincolumm.append(i)
                try:
                    if self.gamepos[i+3][j-3] == self.gamepos[i + 1][j - 1] == self.gamepos[i + 2][j - 2] == colour and self.gamepos[i][j] == -1 and self.gamepos[i][j + 1] != -1:
                        if i not in Wincolumm: Wincolumm.append(i)
                except:
                    pass
        return Wincolumm
    def checkPossibleWin(self):
        Win = []
        Win += self.Horiscan()
        Win += self.Verti()
        Win += self.DownrightScan()
        Win += self.UprightScan()
        return Win
    def checkWin(self,column):
        if column in self.checkPossibleWin():
            return True
        return False


