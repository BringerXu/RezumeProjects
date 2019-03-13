from goody import irange

# The count_predicate function appears in the notes
def count_predicate(alist,p):
    count = 0
    for v in alist:
        if p(v):
            count += 1
    return count

# The rank function appears in the notes
def rank(value,alist):
    return count_predicate(alist, lambda x : x > value)+1


def remove(alist,p):
    i = 0
    while i < len(alist):
        if p(alist[i]):
            del alist[i]
        else:
            i += 1
        

def find_index(alist,arange,p):
    for i in arange:
        if p(alist[i]):
            return i
    return -1


def print_histogram(title,bins):
    print(title)
    min_non0 = find_index(bins,irange(0,len(bins)-1,1), lambda x : x != 0)
    max_non0 = find_index(bins,irange(len(bins)-1,0,-1),lambda x : x != 0)

    count = sum(bins)
    max_for_scale = max(bins)
        
    for i in irange(min_non0,max_non0):
        pc = int(bins[i]/max_for_scale*50)
        print('{bin:4}[{count: 5.1f}%]|{stars}'.format(bin=i,count=bins[i]/count*100,stars='*'*pc))


if __name__ == '__main__':
    print('Testing remove')
    l = ['a','b','c','d','e','f','g','h','i']
    print(l)
    remove(l,(lambda x : x in 'aeiou'))
    print(l)
    remove(l,(lambda x :False))
    print(l)
    remove(l,(lambda x : True))
    print(l)

    print('\nTesting find_index')
    from predicate import is_prime
    l = [4,8,10, 11, 12, 13, 17, 20, 25]
    print(find_index(l,irange(0,len(l)-1),is_prime))
    print(find_index(l,irange(len(l)-1,0,-1),is_prime))
    
    print('\nTesting print_histogram')
    print_histogram(' Bin  Count',[0, 0, 4, 0, 9, 15, 18,8, 7, 0])
   