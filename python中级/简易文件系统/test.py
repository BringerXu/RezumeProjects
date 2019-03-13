#C:\Users\ZhengyiXu\Desktop\ICS32 file system
#C:\Users\Bringer\Desktop\ICS32 file system
#C:\Users\ZhengyiXu\Desktop\testfolder
'''
import os
import stat
import time

dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir)
def ReadFileNames(rootDir):
     FileList = []
     for (parent,dirnames,filenames) in os.walk(rootDir):
         if fileNames:
             for fileName in fileNames:
                 FileList.append(os.path.join(parent,fileName))
     return FileList
for item in ReadFileNames(dir):
	print(item+"\n")

x=input()
for parent in os.walk(x):
	print('parent')

def ReadFileNames(rootDir):
     FileList = []
     for parent,dirNames,fileNames in os.walk(rootDir):
         if fileNames:
             for fileName in fileNames:
                 FileList.append(os.path.join(parent,fileName))
     return FileList

def main():
	start=True
	print(os.getcwd())
	while start:
		print("Please enter your depository root ")
		x=str(input())
		File=ReadFileNames(x)
		main()
'''
'''We start this work before first course and so we have to search modules in google and python documentation. we find shutile which is a high-level copying module and time format of computer(from 1970.1.1). 
we do not know pathlib and recursion at that time so we write this version. It runs well but it is not so efficiently and conveniently programed.'''
#version1.0
'''
import os
import stat
import time
import shutil

def name(root:str,container:list)->list:
    ''''''
    return list including path of the file searching by name input
    ''''''
    result=[]
    print(os.getcwd())
    name=input()
    namepath=os.path.join(root,name)
    if os.path.isfile(namepath):
        for item in container:
            if name==item:
                result.append(namepath)
                return result
    else:
        fline(root,container)

def exten(root:str, container:list)->list:
    ''''''
    return list including path of the files searching by extension input
    ''''''
    result=[]
    print(os.getcwd())
    ext=str(input())
    for item in container:
        itempath=os.path.join(root,item)
        if os.path.splitext(itempath)[1]==ext:
            result.append(itempath)
    return result

def Size(root:str,container:list)->list:
    ''''''
    return list including path of the files searching by size input (> Size)
    ''''''
    result=[]
    print(os.getcwd())
    size=int(input())
    for item in container:
        itempath=os.path.join(root,item)
        if os.path.isfile(itempath):
            if os.path.getsize(itempath)>=size:
                result.append(itempath)
    return result

def fline(root,container)->list:
    ''''''
    first operator control
    ''''''
    operator=str(input())
    if operator=='N':
        return name(root,container)
    elif operator=="E":
        return exten(root,container)
    elif operator=="S":
        return Size(root,container)
    else:
        fline(root,container)

def main()->None:
    ''''''
    Control simple quit and main structure of project
    ''''''
    while 1:
        root=str(input())
        if os.path.exists(root):
            os.chdir(root)
            container=os.listdir(root)
            path=fline(root,container)
            while 1:
                operator=input()
                if operator=="P":
                    print(os.getcwd())
                    for item in path:
                        print(item)
                elif operator=="F":
                    print(os.getcwd())
                    for item in path:
                        con=open(item,'r')
                        print(con.readline())
                        con.close()
                elif operator=="D":
                    print(os.getcwd())
                    for item in path:
                        con=os.path.split(item)[1]
                        shutil.copyfile(con,con+"dup")
                elif operator=="T":
                    print(os.getcwd())
                    for item in path:
                        os.stat(item).st_mtime=time.time()
                elif operator=="Q":
                    break
                else:
                    continue
        else:
            continue
if __name__ == '__main__':
    main()
'''
def transfer(board):
    result=[]
    result2=[]
    i=5
    while i>=0:
        for x in board:
            result.append(x[i])
        i=i-1
    result2.append(result[35:42])
    result2.append(result[28:35])
    result2.append(result[21:28])
    result2.append(result[14:21])
    result2.append(result[7:14])
    result2.append(result[0:7])
    return result2

def printtable(con:'table'):
    List=transfer(con)
    print('1  2 3  4  5  6 7')
    for row in range(len(List)):         
        for col in range(len(List[0])): 
            if List[row][col] == 0:
                pixel = '.   '
            elif List[row][col] == 1:
                pixel = 'R  '
            elif List[row][col] == 2:
                pixel = 'Y  '
            print(pixel,sep= '',end='')
        print()
    return

import ConnectFour
table=ConnectFour.new_game()
def console(s: 'GameState') -> str:
    for i in range(ConnectFour.BOARD_ROWS):
        row = ''
        for column in s.board:
            if column[i] == 0:
                row += '.  '
            if column[i] == 1:
                row += 'R  '
            if column[i] == 2:
                row += 'Y  '
        print(row)
console(table)