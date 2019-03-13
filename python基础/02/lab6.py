#Shawn Li 88405009 Zhengyi Xu 68996560 Lab 7 assignment 6
def c(a):
	print('---------------c',a,'---------------\n')
def d(a):
	print('---------------d',a,'---------------\n')
#c.1
c(1)
def contains(a:str,b:str)->bool:
	'''
reutrn true or false for whether the a include b'''
	return b in a
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')

#c.2
c(2)
def sentence_states(a:str)->None:
	'''
print Characters, Words, Average word length from given string'''
	no_punct_table = str.maketrans('.,:;?!"* ',
		                           '         ')
	b = a.translate(no_punct_table)
	c = b.count(' ')
	print('Characters:',len(b))
	print('Words:',len(b.split()))
	print('Average word length:',(len(b)-c)/len(b.split()))
sentence_states('I love UCI')
sentence_states('***The ?! quick brown fox:  jumps over the lazy dog.')

#c.3
c(3)
def our_upper(s: str) -> str:
	'''
change every character in given string to upper characters
'''
	table = str.maketrans('abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	s = s.translate(table)
	return s
def initials(a:str)->str:
	'''
return initials from given name
'''
	b = our_upper(a)
	c = b.split()
	d = ""
	for i in c:
		d = d + i[0]
	return d
print(initials('Bill Cospy'))
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

#d.1
d(1)
from random import randrange
print('\n\t50 times producing random numbers from 0-10')
for i in range(50):
	print('\n\t'+str(randrange(0,11)))

print('\n\t50 times rolling standard six-sided dice')
for i in range(4):
	print("\n\t"+str(randrange(1,7)))

#d.2
d(2)
def roll2dice():
	'''
return result of rolling two dice at the same time
'''
	return(randrange(1,7)+randrange(1,7))
for i in range(50):
	roll2dice()
	
#d.3
d(3)
def distribution_of_rolls(times:int)->None:
	print('Distribtion of dice rolls')
	a=[]
	c=[]
	for l in range(times):
        a.append(roll2dice())
    for b in range(2,13):
        d=a.count(b)/times*100
        e='*'*a.count(b)
        print('{:2}:{:6}({:4.1f}%)  {}'.format(b,a.count(b),d,e))
    print('--------------------------\n\t',times,' rolls')
distribution_of_rolls(200)

#e
print('---------------e---------------\n')
def rotate(b:int)->str:
	'''
rotate the decipher/cipher code list
'''
	ALPHABET='abcdefghijklmnopqrstuvwxyz'
	c=ALPHABET[:b]
	ALPHABET=ALPHABET.strip(c)
	ALPHABET+=c
	return ALPHABET
def Caesar_encrypt(a:str,b:int)->str:
	'''
cipher the str from given key number
'''
	ALPHABET='abcdefghijklmnopqrstuvwxyz'
	if b%26==26:
		c=b
	else:
		c=b%26
	table=str.maketrans(ALPHABET,rotate(c))
	a = a.translate(table)
	return a
def Caesar_decrypt(a:str,b:int)->str:
	'''
decipher the str from given key number
'''
	ALPHABET='abcdefghijklmnopqrstuvwxyz'
	if b%26==26:
		c=b
	else:
		c=b%26
	table=str.maketrans(rotate(c),ALPHABET)
	a = a.translate(table)
	return a
assert Caesar_encrypt('cat',1)=='dbu'
assert Caesar_decrypt(Caesar_encrypt('cat',1),1)=='cat'
assert (Caesar_encrypt('cat',28))=='ecv'
assert Caesar_encrypt('cat',197)==Caesar_encrypt('cat',171)
#f
def f(a):
	print('---------------f',a,'---------------\n')
[ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]
#f.1
f(1)
def print_line_numbers(a:list)->None:
	'''
print list indexing number and elements of list
'''
	for i in range(len(a)):
		print("{:2}:  {}".format(i+1,a[i]))
print_line_numbers([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ])

#f.2
f(2)
def outformat(a:float,b:str)->None:
	'''
set up print format to print
'''
	print ('{:7.1f} {}'.format(a,b))
def outformat2(a:float,b:str)->None:
	'''
set up print format to print
'''
	print ('{:7} {}'.format(a,b))
def stats(a:list)->None:
	'''
do statistics of given list
'''
	b=len(a)
	c=len(a)-a.count('')
	d=0
	outformat2(b,'lines in the list')
	outformat2(a.count(''),'empty lines')
	table=str.maketrans(',.','  ')
	for i in a:
		i=i.translate(table)
		i=i.split()
		for l in i:
			d+=len(l)
	outformat(d/b,'average characters per line')
	outformat(d/c,'average characters per non-empty line')

stats([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ])
	
#f.3
f(3)
def list_of_words(a:list)->list:
	'''
return a list including elements which only show charcters without whitespace
'''
	table=str.maketrans(',.?!*','     ')
	b=''
	c=[]
	for l in a:
		l=l.translate(table)
		l=l.split()
		l=b.join(l)
		c.append(l)
	return c

assert list_of_words([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ])==[ "Fourscoreandsevenyearsagoourfathersbroughtforthon",
  "thiscontinentanewnationconceivedinlibertyanddedicated",
  "tothepropositionthatallmenarecreatedequalNowweare",
  "engagedinagreatcivilwartestingwhetherthatnationorany",
  "nationsoconceivedandsodedicatedcanlongendure" ]


                




