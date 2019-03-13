# Zhengyi Xu 68996560
'''
Othello Game Tools
'''
BLACK=-1 
WHITE=1
NONE=0

Direction =  [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)] # set up 8 direction around a chess

class InvalidMove(Exception):
    '''
    Your move do not fit in Rule
    '''
    pass

class NoValidMove(Exception):
    '''
    if no existing valid move for this turn, raise this Exception 
    '''
    pass

class Table(object):
    def __init__(self,tablerow,tablecolumn,LeftTop):
        self.tablerow = tablerow
        self.tablecolumn = tablecolumn
        self.LeftTop = LeftTop

    def Build(self):
        '''
        initial table base on tablerow and tablecolumn
        initial 4 chesspieces in the middle base LeftTop
        '''
        gametable=[]
        for row in range(self.tablerow):
            gametable.append([0]*self.tablecolumn)

        row=len(gametable)
        column=len(gametable[0])
        if self.LeftTop == BLACK:
            gametable[int(row/2)-1][int(column/2)-1] = BLACK
            gametable[int(row/2)][int(column/2)] = BLACK
            gametable[int(row/2)-1][int(column/2)] = WHITE
            gametable[int(row/2)][int(column/2)-1] = WHITE
        elif self.LeftTop == WHITE:
            gametable[int(row/2)-1][int(column/2)-1] = WHITE
            gametable[int(row/2)][int(column/2)] = WHITE
            gametable[int(row/2)-1][int(column/2)] = BLACK
            gametable[int(row/2)][int(column/2)-1] = BLACK      
        return gametable

class Check(object):
    def __init__(self,gametable,turn):
#inital all of paramters
        self.turn = turn
        self.gametable = gametable
        self.tablerow = len(self.gametable)
        self.tablecolumn = len(self.gametable[0])
        self.AllEmptyMove = self._AllEmptyMove()
        self.ValidMove=[]
        self.PureValidMove=[] 

# Check all possible move for this turn and store them in two list
        for move in self.AllEmptyMove:
            self.row = move[0]
            self.column = move[1]

            self.JudgeList = [self._aroud_chess(-1,-1),
        self._aroud_chess(0,-1),
        self._aroud_chess(1,-1),
        self._aroud_chess(-1,0),
        self._aroud_chess(1,0),
        self._aroud_chess(-1,1),
        self._aroud_chess(0,1),
        self._aroud_chess(1,1)]

            self.numlist = self._GetDirectionIndex()
            self.direction = self._SearchDirection()
            if self.direction != []:
                self.PureValidMove.append(move)
                self.ValidMove.append([move,self.direction])

    def _AllEmptyMove(self):
        AllMove=[]
        for row in range(self.tablerow):
            for col in range(self.tablecolumn):
                if self.gametable[row][col] == NONE:
                    AllMove.append((row,col))
        return AllMove


    def _aroud_chess(self,deltacolumn,deltarow):
        '''
        check 8 chesspiece aroud object chess:
        if any of them are reverse turn chess, return True
        else return False
        '''
        try:
            new_column=self.column+deltacolumn
            new_row=self.row+deltarow
            if self.gametable[new_row][new_column]!=self.turn and self.gametable[new_row][new_column]!=NONE:
                return True
            else:
                return False
        except:
            return False

    def _GetDirectionIndex(self):
        numlist=[]
        for index in range(len(self.JudgeList)):
            if self.JudgeList[index] == True:
                numlist.append(index)
        return numlist

    def _SearchDirection(self):
        searchrow=self.row
        searchcolumn=self.column
        direction=[]
        for num in self.numlist:
            time=1
            while True:
                try:
                    time+=1
                    searchrow=self.row+Direction[num][1]*time
                    searchcolumn=self.column+Direction[num][0]*time
                    if self.gametable[searchrow][searchcolumn] == NONE:
                        break
                    elif self.gametable[searchrow][searchcolumn]==self.turn:
                        break
                except IndexError:
                    break
                except:
                    raise
            if searchrow>self.tablerow-1 or searchrow<0 or searchcolumn>self.tablecolumn-1 or searchcolumn<0:
                pass
            elif self.gametable[searchrow][searchcolumn] == NONE:
                pass
            else:
                direction.append(num)
        return direction

    def CheckValid(self,row,column):
        if (row,column) in self.PureValidMove:
            pass
        else:
            raise InvalidMove

    def _Pointer(self,row,column):
        for index in range(len(self.PureValidMove)):
            if self.PureValidMove[index]==(row,column):
                return index
            else:
                pass

    def Full(self):
        '''
        Check Whether gametable have been full
        '''
        i=0
        for row in range(self.tablerow):
            for col in range(self.tablecolumn):
                if self.gametable[row][col]!=NONE:
                    i+=1
        if i == self.tablerow * self.tablecolumn:
            return True

    def Almost_Full(self):
        '''
        Check Whether gametable have been full
        '''
        i=0
        for row in range(self.tablerow):
            for col in range(self.tablecolumn):
                if self.gametable[row][col]!=NONE:
                    i+=1
        if i == self.tablerow * self.tablecolumn-1:
            return True

    def Map(self,row,column):
        '''
        Map chesspiece on gametable
        Change chesspieces color base on rule
        '''
        self.gametable[row][column] = self.turn
        pointer = self._Pointer(row,column)
        for index in self.ValidMove[pointer][1]:
            time=0
            while True:
                try:
                    time+=1
                    new_row=row+Direction[index][1]*time
                    new_column=column+Direction[index][0]*time
                    if self.gametable[new_row][new_column]==self.turn:
                        break
                    elif self.gametable[new_row][new_column]!=self.turn and self.gametable[new_row][new_column]!=NONE:
                        self.gametable[new_row][new_column]=self.turn
                    else:
                        pass
                except IndexError:
                    break
                except:
                    raise

def SumNum(gametable:'table'):
    '''
    Sum gametable black chess number and white chess number
    print them
    '''
    BLACK_num=0
    WHITE_num=0
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            if gametable[row][col]==BLACK:
                BLACK_num+=1
            elif gametable[row][col]==WHITE:
                WHITE_num+=1
    return [BLACK_num,WHITE_num]

def ChangeTurn(turn:int):
    '''
    receive turn number
    return another turn number
    '''
    if turn == BLACK:
        return WHITE
    elif turn == WHITE:
        return BLACK

def CheckWin(WinRule:str,gametable:'gametable'):
    NUM = SumNum(gametable)
    BLACK_num = NUM[0]
    WHITE_num = NUM[1]
    if WinRule=='<':
        if BLACK_num < WHITE_num:
            return 'BLACK'
        elif WHITE_num < BLACK_num:
            return 'WHITE'
        elif BLACK_num == WHITE_num:
            return 'NONE'
    elif WinRule=='>':
        if BLACK_num > WHITE_num:
            return 'BLACK'
        elif WHITE_num > BLACK_num:
            return 'WHITE'
        elif BLACK_num == WHITE_num:
            return 'NONE'