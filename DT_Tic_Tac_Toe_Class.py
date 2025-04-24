'''
Pseudcode:
1. Initialize an empty board every time a new game starts
2. print the empty board to the user
3. iterate the plays for 9 times since we know there can be no more plays for a particular game
4. first is player X and once an iteration completed swap between player between O and X
5. Get the input from the user for each play and validate the input.
    If value<0 or >2 print error message
6. If values are correct check if the spot is open to play by checking if the row and column in the board is empty
7. Place X or O in the selected spot and check for winning
8. We check only 3 parts
    a. the row in which the insert happened (not necessary to check other rows)
    6. the column in which the insert happened
    c. If both the row and column values are equal check the first diagonal
    b. if adding both row and column gives 2(n-1) check the opposite diagonal
7. If none of the above check results in full 3 count for X or O return False. Else return the winner and jump to step-10
8. Print the winner if the returned value is true else continue by repeating steps (5-7)
9. If all the 9 plays are done, Print Draw match
10. Ask for a new game if yes repeat from step(1-10)
'''
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
        self.board = Board()
        self.turn = 'X'
        self.possiblewins = [[0,1,2],[10,11,12],[20,21,22],[0,10,20]
                             ,[1,11,21],[2,12,22],[0,11,22],[2,11,20]]
    
    def switchPlayer(self):
        if(self.turn == 'X'):
            self.turn = 'O'
        else:
            self.turn = 'X'
    

    def validateEntry(self):
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
        self.board.c[r][c] = self.turn
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
        print(checkwin)
        if(checkwin):
            return self.turn+' is the Winner!!!'
        checkfull = self.checkFull()
        if(checkfull):
            return 'Draw! NOBODY WINS!'
        else:
            return 
        

    def playGame(self):
        print('New Game: X goes first.')
        self.board.print_board()
        for i in range(9):
            print(self.turn+"'s turn.")
            print('Where do you want your '+self.turn+' placed?')
            r,c = self.validateEntry()
            print('Thank you for your selection.')
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