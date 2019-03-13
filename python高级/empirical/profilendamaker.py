import cProfile
import prompt
from goody import irange
from listlib import remove


def overlaps(upper : str, lower : str, n : int) -> bool:
    return upper[-n:] == lower[0:n]


def exceeds_overlap(upper : str, lower : str, mino):
    max_n = min(len(upper),len(lower))
    answer = 0
    for i in irange(mino,max_n+1,1):
        if overlaps(upper,lower,i):
            return i
    return answer


def read_fragments(file):
    return [l.rstrip() for l in open(file)]

 
def choose(fragments,min_overlap):
    for upper in fragments:
        for lower in fragments:
            if upper != lower:
                mo = exceeds_overlap(upper,lower,min_overlap)
                if mo >= min_overlap:
                    return upper,lower,mo
    return ('','',0)


def assemble(fragments,min_overlap,tracing=True):
    while True:
        if tracing:
            print('\nassembling with',len(fragments),'fragments')
            print(fragments)
        upper,lower,mo = choose(fragments,min_overlap)
        if  mo < min_overlap:
            return None
        else:
            remove(fragments,lambda x : x == upper)
            remove(fragments,lambda x : x == lower)
            fragments.append(upper+lower[mo:])
            if tracing:
                print('Removing upper =',repr(upper),'and lower =',repr(lower),'\nAdding',repr(upper+lower[mo:]))
    return None          

def perform_task():    
    file_name = 'hugedna.txt'#prompt.for_string('Enter file to process')
    fragments = read_fragments(file_name)
    min_overlap = 10         #prompt.for_int('Enter minimum overlap')
    tracing     = False# prompt.for_bool('Tracing on?',default=True)
    assemble(fragments,min_overlap,tracing)
    fragments.sort(key = lambda x : len(x),reverse=True)
    remove(fragments,lambda x : len(x) < len(fragments[0]) and x in fragments[0])
    print('\nAssembled with '+str(len(fragments))+' strand(s) remaining')
    print(fragments[0])
    print(fragments[0],file=open('assembled-'+file_name,'w'))
    print('Answer written into file: assembled-'+file_name)


cProfile.run('perform_task()','profile')