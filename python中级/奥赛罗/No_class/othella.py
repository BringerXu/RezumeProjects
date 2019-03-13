BLACK=-1 
WHITE=1
NONE=0

Direction=  [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
#build up gametable
def Set_TableSize():
        result=[]
        for num in range(2):
            while True:
                try:
                    size=int(input())
                except ValueError:
                    print('Input again, you do not enter a integer')
                except:
                    raise
                else:
                    result.append(size)
                    break
        return result

def Build(SizeList:list):
    row=SizeList[0]
    column=SizeList[1]
    gametable=[]
    for row in range(row):
        gametable.append([0]*column)
    column=len(gametable[0])
    row=len(gametable)
    gametable[int(row/2)-1][int(column/2)-1]=BLACK
    gametable[int(row/2)][int(column/2)]=BLACK
    gametable[int(row/2)-1][int(column/2)]=WHITE
    gametable[int(row/2)][int(column/2)-1]=WHITE
    return gametable

def Print(gametable:'table'):
    pixel=''
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            if gametable[row][col]==NONE:
                pixel='[   ]  '
            elif gametable[row][col]==WHITE:
                pixel='[W]  '
            elif gametable[row][col]==BLACK:
                pixel='[B ]  '
            print(pixel,sep='',end='')
        print()
    return

#Check+ChangeColor
def InTable(row,column,table_column,table_row):
    if row>table_row-1 or row <0 or column>table_column-1 or column<0:
        return False
    else:
        return True

def Empty(row,column,gametable):
    if gametable[row][column]!=NONE:
        return False
    else:
        return True

def _aroud_chess(table,column:int,row:int,deltacolumn:int,deltarow:int,turn:int):
    try:
        new_column=column+deltacolumn
        new_row=row+deltarow
        if table[new_row][new_column]!=turn and table[new_row][new_column]!=NONE:
            return True
        else:
            return False
    except:
        return False

def JudgeList(table,column:int,row:int,turn):
    JudgeList=[_aroud_chess(table,column,row,-1,-1,turn),
    _aroud_chess(table,column,row,0,-1,turn),
    _aroud_chess(table,column,row,1,-1,turn),
    _aroud_chess(table,column,row,-1,0,turn),
    _aroud_chess(table,column,row,1,0,turn),
    _aroud_chess(table,column,row,-1,1,turn),
    _aroud_chess(table,column,row,0,1,turn),
    _aroud_chess(table,column,row,1,1,turn)]
    return JudgeList

def GetDirectionIndex(JudgeList:list):
    numlist=[]
    for index in range(len(JudgeList)):
        if JudgeList[index]==True:
            numlist.append(index)
    return numlist

def SearchDirection(row,column,table,turn):
    sizerow=len(table)
    sizecolumn=len(table[0])
    List=JudgeList(table,column,row,turn)
    numlist=GetDirectionIndex(List)
    searchrow=row
    searchcolumn=column
    direction=[]
    for num in numlist:
        time=1
        while True:
            try:
                time+=1
                searchrow=row+Direction[num][1]*time
                searchcolumn=column+Direction[num][0]*time
                if table[searchrow][searchcolumn]==turn:
                    break
            except IndexError:
                break
            except:
                raise
        if searchrow>sizerow-1 or searchrow<0 or searchcolumn>sizecolumn-1 or searchcolumn<0:
            pass
        else:
            direction.append(num)
    return direction


def ValidMove1(numlist):
    if numlist==[]:
        return False
    else:
        return True

def ValidMove2(Direction):
    if Direction==[]:
        return False
    else:
        return True

#Move
def ChangeColor(table,direction,row,column,turn):
    for index in direction:
        time=0
        while True:
            try:
                time+=1
                new_row=row+Direction[index][1]*time
                new_column=column+Direction[index][0]*time
                if table[new_row][new_column]!=turn and table[new_row][new_column]!=NONE:
                    table[new_row][new_column]=turn
                else:
                    pass
            except IndexError:
                break
            except:
                raise

def STEPSCheck(gametable,turn):
    table_row=len(gametable)
    table_column=len(gametable[0])
    stepslist=[]
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            stepslist.append((row,col))
    result=[]
    for step in stepslist:
        row=step[0]
        column=step[1]
        
        JList=JudgeList(gametable,column,row,turn)
        numlist=GetDirectionIndex(JList)
        direction=SearchDirection(row,column,gametable,turn)
        if InTable(row,column,table_column,table_row)\
        and Empty(row,column,gametable)\
        and ValidMove1(numlist)\
        and ValidMove2(direction):
            result.append(step)
    return result

def checkPS(row,column,PS):
    pos=(row,column)
    if pos in PS:
        return True
    else:
        return False

#check win
def SumNum(gametable):
    BLACK_num=0
    WHITE_num=0
    for row in range(len(gametable)):
        for col in range(len(gametable[0])):
            if gametable[row][col]==BLACK:
                BLACK_num+=1
            elif gametable[row][col]==WHITE:
                WHITE_num+=1
    print('B: '+str(BLACK_num))
    print('W: '+str(WHITE_num))

    

def main():
    print('FULL')
    tablesize=Set_TableSize()
    gametable=Build(tablesize)
    turn=BLACK
    while True:
        Print(gametable)
        PS=STEPSCheck(gametable,turn)
        print(PS)
        if PS==[]:
            if turn == BLACK:
                turn = WHITE
            elif turn == WHITE:
                turn = BLACK
            PS=STEPSCheck(gametable,turn)
            print(PS)
            row=int(input())
            column=int(input())

            if checkPS(row,column,PS):

                gametable[row][column]=turn

                PD=SearchDirection(row,column,gametable,turn)
                ChangeColor(gametable,PD,row,column,turn)

                SumNum(gametable)

                if turn == BLACK:
                    turn = WHITE
                elif turn == WHITE:
                    turn = BLACK
        else:
            row=int(input())
            column=int(input())

            if checkPS(row,column,PS):

                gametable[row][column]=turn

                PD=SearchDirection(row,column,gametable,turn)
                ChangeColor(gametable,PD,row,column,turn)

                SumNum(gametable)
                if turn == BLACK:
                    turn = WHITE
                elif turn == WHITE:
                    turn = BLACK
           

if __name__ == '__main__':
    main()


