from random import randrange
#c
print('\n---------------c---------------')
s=open('surnames.txt','r')
f=open('femalenames.txt','r')
m=open('malenames.txt','r')
contain=[]
contain2=[]
def grab_name(n)->str:
    for line in n:
        contain.append(line)
    for i in contain:
        i=i.split('\t')
        contain2.append(i[0])
    return(contain2[randrange(0,1001)])
def Sex_random(b,c):
    if randrange(0,1)==0:
        return grab_name(b)
    elif randrange(0,1)==1:
        return grab_name(c)
def random_names(a:int)->list:
    c=[]
    for b in range(a):
        c.append(grab_name(s)+','+Sex_random(f,m))
    print(c)
random_names(6)
#d
def rotate(b:int)->str:
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
wordlist=open('wordlist.txt')
word=wordlist.read()
table=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'abcdefghijklmnopqrstuvwxyz')
word2=word.translate(table)
word3=word2.split('\n')
def container(a:int):
    return str(a)=[]
def classi(a:int):
    for i in word3:
        if len(i)=a:
            return container(a)

def Caesar_break(ciper:str)->str:
    result=[]
    for i in range(26):
        if Caesar_encrypt(ciper,i) in word3:
            result.append(Caesar_encrypt(ciper,i))

#f
def copy_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

  

