# 68996560 Zhengyi Xu 19758650 Lukun Han
import connectfour
import GameLogic

game=connectfour.new_game()

def ShowChessTable()->None:
    '''
    print chess table
    '''
    global game
    title=''
    for column_num in range(connectfour.BOARD_COLUMNS):
        title+='{}   '.format(column_num+1)
    print(title)
    for i in range(connectfour.BOARD_ROWS):
        row = ''
        for column in game.board:
            if column[i] == 0:
                row += '.   '
            if column[i] == 1:
                row += 'R   '
            if column[i] == 2:
                row += 'Y   '
        print(row)

def ResponseACT()->'game table':
    '''
    map move(including METHOD and COLUMN) on the table 
    '''
    global game
    try:
        game_copy=game
        if GameLogic.METHOD=='POP':
            game=connectfour.pop(game_copy,GameLogic.COLUMN)
        elif GameLogic.METHOD=='DROP':
            game=connectfour.drop(game_copy,GameLogic.COLUMN)
    except connectfour.InvalidMoveError:
        print('Your move is invalid')
    except:
        raise

def ShowWinner()->'integer 10 or None':
    '''
    judge who is winner
    print winner
    '''
    global game # for use global variable
    if connectfour.winner(game)==connectfour.RED: # judge who is winner
        print('RED WIN') # print correct winner
    elif connectfour.winner(game)==connectfour.YELLOW:
        print('YELLOW WIN')
    else:
        return 10 # set up a default value for more convenient control in Online Version game

def connectfour_console():
    '''
    whole structure of console version connectfour
    '''
    global game # for use global variable
    while connectfour.winner(game)==connectfour.NONE: # if winner still not emerge: keep loop
        try:
            GameLogic.select_method() # request METHOD to user
            GameLogic.select_column() # request COLUMN to user
            ResponseACT() # map previous action in chess table
            ShowChessTable() # print chess table, a simple interface
        except connectfour.GameOverError: # when winner emerge: break loop for printing winner
            break
        except connectfour.InvalidMoveError: # alert user their move is invalid and keep game procedure again
            print('Your move is invalid')
        except:
            raise
    ShowWinner() # printing winner

if __name__ == '__main__':
    connectfour_console()   
