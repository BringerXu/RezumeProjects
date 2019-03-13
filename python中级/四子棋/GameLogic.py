# 68996560 Zhengyi Xu 19758650 Lukun Han
'''
This module's goal:
Preparing interface tools for build up connectfour games
Store two global variables about move
So other python program can use them more easily
'''
import connectfour
METHOD=''
COLUMN=0

# method: select pop or drop

class InvalidInput(Exception):
    """Raised when input method or column is invalid"""
    pass

def _check_method()->str:
    '''
    receive input method
    Check method input whether valid
    if it is not raise MethodInputInvalid exception
    '''
    method=input('D(rop) or P(op): ').strip()
    if method=='D':
        return 'DROP'
    elif method=='P':
        return 'POP'
    else:
        raise InvalidInput()

def select_method()->None:
    '''
    Check whether it is valid
    If not, let user pick again
    convert correct selection into full formation
    using global variable METHOD store user's selection 
    '''
    global METHOD
    while True:
        try:
            METHOD=_check_method()
        except InvalidInput:
            print('Your input method is invalid')
        except:
            raise
        else:
            break

# column: select chesspiece position

def _check_column()->int:
    '''
    receive input column
    Check method input whether valid
    if it is not raise MethodInputInvalid exception
    '''
    column=int(input('Enter your chesspiece position from 1 to 7: '))
    if 0<column<8:
        return column
    else:
        raise InvalidInput()

def select_column()->None:
    '''
    Check whether it is valid
    If not, let user pick again
    convert correct selection into full formation
    using global variable COLUMN store user's selection 
    '''
    global COLUMN
    while True:
        try:
            COLUMN=_check_column()-1
        except InvalidInput:
            print('Your input column is invalid')
        except ValueError:
            print('You must enter a integer number')
        except:
            raise
        else:
            break
