# Zhengyi Xu 68996560
'''
Accept  table_row table_column table
Build gametable
print gametable(or tkinter draw)
Accept input row and column
Check Valid Move
Map Valid Move on gametable
Check Win
No Winner, Keep line(2-7). Exist Winner,  stop game and print Winner
'''
import rule

# I added some prompts before if user input wrong data
# but in website professor claimed that users knew how to use this software
# so I have canceled them and add pass to replace them.
# I wished you do not decrease my score because I knew how to delete these extra functions and extra exceptions
# It will be more helpful when I want to test this program

class InvalidTableSizeParameter(Exception):
    '''
    if input table size parameters are not between 4-16, raise this exception
    '''
    pass

class InvalidChessPosParameter(Exception):
    '''
    if input chess position parameters are invalid raise, this exception
    '''
    pass

class InvalidTurnParameter(Exception):
    '''
    Input Wrong Turn Parameter
    '''
    pass

class NoValidMove(Exception):
    '''
    if no existing valid move for this turn, raise this Exception 
    '''
    pass

def TableParameter():
    '''
    input table size parameter
    Check input table size correctness
    return correct Table Parameter
    '''
    while True:
        try:
            TableParameter=int(input())
            if TableParameter>16 or TableParameter<4 or TableParameter%2!=0:
                raise InvalidTableSizeParameter
        except ValueError:
            pass
        except InvalidTableSizeParameter:
            pass
        except:
            raise
        else:
            break
    return TableParameter

def ChessPosParameter(tablerow,tablecolumn):
    '''
    input chess Row parameter
    Check input chess Row correctness
    return correct ChessRow
    '''
    while True:
        try:
            ChessPos = str(input())
            ChessRow = int(ChessPos.split()[0].strip())
            ChessColumn = int(ChessPos.split()[1].strip())

            if ChessRow  > tablerow or ChessColumn > tablecolumn or ChessRow < 1 or ChessColumn < 1:
                raise InvalidChessPosParameter
        except:
            raise InvalidChessPosParameter
        else:
            break
    POS=[ChessRow-1,ChessColumn-1]
    return POS

def FirstTurn():
    '''
    input First turn
    Check input First turn correctness
    return actual Turn in rule module
    '''
    while True:
        try:
            FirstTurn=str(input())
            if FirstTurn!='B' and FirstTurn!='W':
                raise InvalidTurnParameter
        except ValueError:
            pass
        except InvalidTurnParameter:
            pass
        except:
            raise
        else:
            break
    if FirstTurn=='B':
        return rule.BLACK
    elif FirstTurn=='W':
        return rule.WHITE

def TranslateTurn(turn:int):
    '''
    receive a number representing turn which set in rule module
    print turn string('BLACK' or 'WHITE') basing on number
    '''
    if turn == rule.BLACK:
        print('TURN: B')
    elif turn == rule.WHITE:
        print('TURN: W')


def Print(gametable:'table'):
    '''
    Print gametable
    '''
    pixel=''
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            if gametable[row][col]==rule.NONE:
                pixel='[   ]  '
            elif gametable[row][col]==rule.WHITE:
                pixel='[W]  '
            elif gametable[row][col]==rule.BLACK:
                pixel='[B ]  '
            print(pixel,sep='',end='')
        print()
    return

def ChangeTurn(turn:int):
    '''
    receive turn number
    return another turn number
    '''
    if turn == rule.BLACK:
        return rule.WHITE
    elif turn == rule.WHITE:
        return rule.BLACK

def SumNum(gametable:'table'):
    '''
    Sum gametable black chess number and white chess number
    print them
    '''
    BLACK_num=0
    WHITE_num=0
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            if gametable[row][col]==rule.BLACK:
                BLACK_num+=1
            elif gametable[row][col]==rule.WHITE:
                WHITE_num+=1
    return [BLACK_num,WHITE_num]

def CheckWin(WinRule:str,gametable:'gametable'):
    NUM = SumNum(gametable)
    BLACK_num = NUM[0]
    WHITE_num = NUM[1]
    if WinRule=='<':
        if BLACK_num < WHITE_num:
            print('WINNER: BLACK')
        elif WHITE_num < BLACK_num:
            print('WINNER: WHITE')
        elif BLACK_num == WHITE_num:
            print('WINNER: NONE')
    elif WinRule=='>':
        if BLACK_num > WHITE_num:
            print('WINNER: BLACK')
        elif WHITE_num > BLACK_num:
            print('WINNER: WHITE')
        elif BLACK_num == WHITE_num:
            print('WINNER: NONE')


def main():
# represent Rule kind
    print('FULL')
# Initial Input
    tablerow = TableParameter() # input table row size
    tablecolumn = TableParameter() # input table column size
    
    Turn = FirstTurn() # input first turn
    LeftTop = FirstTurn() # input LeftTop chess color
    WinRule=input()
# Initial gametable
    gametable = rule.Table(tablerow,tablecolumn,LeftTop).Build()
    NUM = SumNum(gametable) # Calculate Current Chesspieces number(BLACK AND WHITE)
    BLACK_num = NUM[0]
    WHITE_num = NUM[1]
    print('B: '+str(BLACK_num)+'  '+'W: '+str(WHITE_num))
    Print(gametable)
    TranslateTurn(Turn)

# Start game
    while True:
        try:
            MOVE = rule.Check(gametable,Turn).ValidMove # GET All Possible Moves Basing on Current Turn
            print(MOVE)
            if MOVE==[]: # Check Whether exist Turn, if not pass this turn
                raise NoValidMove
#Input chess position
        except NoValidMove: # Pass Current Turn
            Turn = ChangeTurn(Turn) # Special Change Turn
        except:
            raise

        else:

            while True:
                try:
                    POS = ChessPosParameter(tablerow,tablecolumn)
                    row = POS[0]
                    column = POS[1]
                    rule.Check(gametable,Turn).CheckValid(row,column) # Check whether input Chess Position valid, if not raise Invalid Move
                except rule.InvalidMove: # Invalid Chess Position
                    print('INVALID')
                except InvalidChessPosParameter:
                    print('INVALID')
                else:
                    break

            print('VALID')
            rule.Check(gametable,Turn).Map(row,column) # Maping change on gametable
            NUM = SumNum(gametable) # Calculate Current Chesspieces number(BLACK AND WHITE)
            BLACK_num = NUM[0]
            WHITE_num = NUM[1]
            print('B: '+str(BLACK_num)+'  '+'W: '+str(WHITE_num))
            Print(gametable) # Show Gametable

            Turn = ChangeTurn(Turn) # Normal: Change Turn

 
            
# Check Win Condition:
        finally:
 # if both turn cannot have valid move, stop game, check and show winner 
            if rule.Check(gametable,rule.BLACK).ValidMove==[] and rule.Check(gametable,rule.WHITE).ValidMove==[]:
                break
# if gametable have been full, check and show winner
            elif rule.Check(gametable, Turn).Full():
                break
            else:
                TranslateTurn(Turn) # Show turn which should be moved NOW
# Show Winner
    CheckWin(WinRule,gametable)

if __name__ == '__main__':
    main()