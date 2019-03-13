import prompt
from goody import irange
from listlib import remove


def overlaps(upper : str, lower : str, n : int) -> bool:
    return upper[-n:] == lower[0:n]


def max_overlap(upper : str, lower : str):
    max_n = min(len(upper),len(lower))
    answer = 0
    for i in irange(1,max_n+1):
        if overlaps(upper,lower,i):
            answer = i
    return answer


#def test_max_overlap():
#    while True:
#        u = prompt.for_string('\nEnter upper')
#        l = prompt.for_string('Enter lower')
#        mo = max_overlap(u,l)
#        print('overlap='+str(mo), u, (len(u)-mo)*' '+l, sep='\n')
#test_max_overlap()    


def read_fragments(file):
    return [l.rstrip() for l in open(file)]

 
def choose(fragments,min_overlap):
    for upper in fragments:
        for lower in fragments:
            if upper != lower:
                mo = max_overlap(upper,lower)
                if mo >= min_overlap:
                    return upper,lower,mo
    return ('','',0)


#print(choose(['aacc','ccgg','ggtt'],2))
#print(choose(['aacc','ggtt','ccgg'],2))
#print(choose(['ccgg','aacc','ggtt'],2))
#print(choose(['aacc','ccgg','ggtt'],3))


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

    
file_name = prompt.for_string('Enter file to process')
fragments = read_fragments(file_name)
min_overlap = prompt.for_int('Enter minimum overlap')
tracing     = prompt.for_bool('Tracing on?',default=True)
assemble(fragments,min_overlap,tracing)
fragments.sort(key = lambda x : len(x),reverse=True)
remove(fragments,lambda x : len(x) < len(fragments[0]) and x in fragments[0])
print('\nAssembled with '+str(len(fragments))+' strand(s) remaining')
print(fragments[0])
print(fragments[0],file=open('assembled-'+file_name,'w'))
print('Answer written into file: assembled-'+file_name)


#def print_strand(strand,max):
#    while len(strand) > max:
#        print(strand[:max])
#        strand = strand[max:]
#    print(strand)
#
#    def choose_2():   
#        mo_max = 0
#        for u in range(len(fragments)):
#            if mo_max > min_overlap: break
#            for l in range(len(fragments)):
#                if u != l:
#                    mo = max_overlap(fragments[u],fragments[l])
#                    if mo > mo_max:
#                        mo_u,mo_l,mo_max = u,l,mo
#        return mo_u,mo_l              
