#Shawn Li 88405009 Zhengyi Xu 68996560 Lab 7 assignment 6
def c(b):
    print('\t---------------c.',b,'---------------')
#c1
c(1)
def contains(s:str,s2:str)->bool:
    return s2 in s
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')

#c2
c(2)
def sentence_stats(s:str)->None:
    print(len(s))
    
    table=str.maketrans('*?!.:',
                        '     ')
    b=s.translate(table)
    print(b)
    print(len(b.split()))
    a= b.count(' ')
    print((len(b)-a)/len(b.split()))

sentence_stats('I love UCI')
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
#c3
c(3)
def initials(s:str)->str:
    table=str.maketrans('qwertyuiopasdfghjklzxcvbnm',
                        'QWERTYUIOPASDFGHJKLZXCVBNM')
    a=s.translate(table)
    b=a.split()
    d=""
    for c in b:
        d = d + c[0]
    return d
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'


def d(b):
    print('\t---------------d.',b,'---------------')
#d1
d(1)
from random import randrange
for i in range(50):
    print(randrange(0,11))
print('-----------------------------------')
for i in range(50):
    print(randrange(1,7))

#d2
d(2)
def roll2dice():
    return(randrange(1,7)+randrange(1,7))
for i in range(50):
    print(roll2dice())
    
   
#f1
E =[ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

def print_line_numbers(l:list)->None:
    formatStr='{:0}:  {}'
    for i in range(1,len(l)+1):
        print(formatStr.format(i,l[i-1]))
print_line_numbers(E)


#f2

def stats(l:list)->None:
    result=[]
    e_line=0
    non_line=0
    charatcer=0
    for i in l:
        result.append(i.strip())
    for i in result:
        character+=len(i)
        if i =="":
            e_line+=1
        else:
            non_line+=1
    lines=e_line+non_line
    averagec=character/lines
    averagenc=character/non_line
    formatStr1='{:5}   {}'
    formatStr2='{:7.1f} {}'
    print(formatStr1.format(lines,'lines in the list'))
    print(formatStr1.format(e_line,'empty lines'))
    print(formatStr2.format(averagec,'average characters per line'))
    print(formatStr2.format(averagenc,'average characters per non-empty line'))

#f3

def list_of_word(l:list)->list:
    resulta=[]
    resultb=[]
    for i in l:
        table=str.maketrans(',.!?;:"',
                            '       ')
        np=i.translate(table)
        resulta.append(np)
    for p in resulta:
        q=p.spilt()
        resultb.extend(q)
    return resultb
print(list_of_word(E))    
    
    
    
