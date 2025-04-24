import pickle as pkl
import numpy as np
import pandas as pd
class Board:
    def __init__(self):
        #initialize an empty board everytime a new game starts
        self.c = [['','',''],['','',''],['','','']]
    def print_board(self):
        #board constants that that doesnt change for each play
        print('-------------------')
        print('| R\\C | 0 | 1 | 2 |')
        print('-------------------')
        #print the values stored in board for each game
        for i in range(3):
            print('| '+str(i).ljust(3),end = ' | ')
            for j in range(3):
                if(self.c[i][j]==''): #if empty spot print empty space
                    print(' ',end = ' | ') 
                else:
                    print(self.c[i][j],end = ' | ')
            print()
            print('-------------------')
        return


class Game:
    def __init__(self) -> None:
        self.model = pkl.load(open('C:/Users/Aishu/Downloads/Programming in python assignments/Mini Project - 1/Mini Project-2/RandomForestTicTac.pickle', 'rb'))
        self.board = Board()
        self.turn = 'X'
        self.possiblewins = [[0,1,2],[10,11,12],[20,21,22],[0,10,20]
                             ,[1,11,21],[2,12,22],[0,11,22],[2,11,20]]
    
    def switchPlayer(self):
        if(self.turn == 'X'):
            self.turn = 'O'
        else:
            self.turn = 'X'
    

    def player_validateEntry(self):
        available = False # Initially availability is false
        valid_inputs = ['1','2','0']
        while(not(available)):
            inputs = input('Please enter row number and column number separately by a comma.')
            while(len(inputs)!=3 or inputs[0] not in valid_inputs or inputs[1]!=',' or inputs[2] not in valid_inputs):
                print('Invalid entry: try again.')
                print('Row & column numbers must be either 0, 1, or 2.')
                inputs = input('Please enter row number and column number separately by a comma.')
                #r,c = map(int,input('Please enter row number and column number separated by a comma.').split(','))
            r,c = map(int,inputs.split(','))
            if(self.board.c[r][c]!=''):
                available = False
            else:
                available = True
            if(not(available)):
                print('That cell is already taken.')
                print('Please make another selection.')
        #if all tests are passed display the inputs
        print('You have entered row #'+str(r))
        print('\t\t and column #'+str(c))
        return (r,c)

        
    def __checkcomplete(self,pointer,flag):
        #if flag is r check the particular row for the count of the player
        if(flag=='r'):
            if(self.board.c[pointer].count(self.turn)==3):
                return True
            return False
        #if flag is 'c' check the particular column for the count of the player
        if(flag=='c'):
            for i in range(3):
                if(self.board.c[i][pointer]!=self.turn):
                    return False
            return True
        #if the flag is 'd' check the diagonals for the count of the player
        if(flag=='d'):
            if(pointer==0):#for 1st diagonal
                for i in range(3):
                    if(self.board.c[i][i]!=self.turn):
                        return False
                return True
            else:#for opposite diagonal
                for i in range(3):
                    if(self.board.c[2-i][i]!=self.turn):
                        return False
                return True
            

    def new_checkWin(self):
        for i in range(len(self.possiblewins)):
            countX=0
            countO = 0
            countEmpty = 0
            for j in range(3):
                r,c = self.possiblewins[i][j]//10,self.possiblewins[i][j]%10
                if(self.board.c[r][c]=='X'):
                    countX+=1
                elif(self.board.c[r][c]==''):
                    countEmpty+=1
                else:
                    countO+=1
            if(countO==3 or countX==3):
                return True
            elif(countO==2 or countX==2):
                return False
            elif(countEmpty<=1):
                self.possiblewins.pop(i)
                print(self.possiblewins)
                break
        return False
    

    def checkwin(self,r,c):
        #self.board[r][c] = player #place the current player in the board
        res = self.__checkcomplete(r,'r') # check for row match
        if(res==True):
            return res
        res = self.__checkcomplete(c,'c') # check for column match
        if(res==True):
            return res
        if(r==c): # check for first diagonal match
            res = self.__checkcomplete(0,'d')
            if(res==True):
                return res
        if((r+c)==(2)): #check for opposite diagonal match
            res = self.__checkcomplete(1,'d')
            if(res==True):
                return res
        return False


    def checkFull(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if(self.board.c[i][j]!=''):
                    count+=1
        if(count==9):
            return True
        else:
            return False
        

    def checkEnd(self,r,c):
        checkwin = self.checkwin(r,c)
        #checkwin = self.new_checkWin()
        #print(checkwin)
        if(checkwin):
            #print('Here!!!')
            return self.turn+' is the Winner!!!'
        checkfull = self.checkFull()
        if(checkfull):
            return 'Draw! NOBODY WINS!'
        else:
            return 

    def computermove(self):
        res=[]
        for i in range(3):
            for j in range(3):
                if(self.board.c[i][j]==''):
                    res.append(0)
                elif(self.board.c[i][j]=='X'):
                    res.append(1)
                else:
                    res.append(-1)
        move_array = np.array(res).reshape(1,-1)
        #print(move_array)
        move_df = pd.DataFrame([res],columns=['x1','x2','x3','x4','x5','x6','x7','x8','x9'])
        #print(move_df)
        move = self.model.predict(move_df)[0]
        #print(move)
        r = move//3
        c = move%3
        #print(r,c)
        return (r,c)
    

    def playGame(self):
        print('New Game: X goes first.')
        self.board.print_board()
        for i in range(9):
            if(self.turn=='X'):
                print('Your turn.')
                print('Where do you want your '+self.turn+' placed?')
                r,c = self.player_validateEntry()
                self.board.c[r][c] = self.turn
                print('Thank you for your selection.')
                result = self.checkEnd(r,c)
                if(result!=None):
                    print(result)
                    self.board.print_board()
                    break
            else:
                print('Systems turn.')
                r,c = self.computermove()
                self.board.c[r][c] = self.turn
                result = self.checkEnd(r,c)
                if(result!=None):
                    print(result)
                    self.board.print_board()
                    break
            self.switchPlayer()
            if(i<8):
                self.board.print_board()
        return


def main():
    
    choice = 'y'
    while(choice.lower() in ('y','yes')):
        new_game = Game() #Initialize a new game
        new_game.playGame()
        #ask the user for a new game
        choice = input('Another game? Enter Y or y for yes.')
    print('Thank you for Playing!')

if __name__ == '__main__':
    main()