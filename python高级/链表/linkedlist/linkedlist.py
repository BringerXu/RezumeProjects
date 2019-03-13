class LN:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        current = self
        while current != None:
            yield current.value
            current = self.next

# Query/accessor functions

def len_ll(ll):
    count = 0
    while ll != None:
        count += 1
        ll = ll.next
    return count

def len_ll_r(ll):
    if ll == None:
        return 0
    else:
        return 1 + len_ll_r(ll.next)

 
def sum_ll(ll):
    total = 0
    while ll != None:
        total += ll.value
        ll = ll.next
    return sum

def sum_ll_r(ll):
    if ll == None:
        return 0
    else:
        return ll.value + sum_ll_r(ll.next)


def str_ll(ll):
    answer = ''
    while ll != None:
        answer += str(ll.value)+'->'
        ll = ll.next
    return answer + 'None'
    
def str_ll_r(ll):
    if ll == None:
        return 'None'
    else:
        return str(ll.value)+'->'+str_ll_r(ll.next)

    
 
def list_to_ll(l):
    if l == []:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front

def list_to_ll_r(l):
    if l == []:
        return None
    else:
        return LN(l[0], list_to_ll_r(l[1:]))


def find_ll(ll, avalue):
    while ll != None:
        if ll.value == avalue:
            return ll
        ll = ll.next
    return None

def find_ll_r(ll, avalue):
    if ll == None:
        return None
    else:
        if ll.value == avalue:
            return ll
        else:
            return find_ll_r(ll.next,avalue)

def find_ll_r2(ll, avalue):
    if ll == None or ll.value == avalue: # short-circuit or is critical
        return None
    else:
        return find_ll_r(ll.next,avalue)


def copy_ll(ll): 
    if ll == None:
        return None
    front = rear = LN(ll.value)
    while ll.next != None:
        ll = ll.next
        rear.next = LN(ll.value)
        rear = rear.next
    return front
        
def copy_ll_r(ll):
    if ll == None:
        return None
    else:
        return LN(ll.value,copy_ll_r(ll.next))

def iterator(ll):
    while ll != None:
        yield ll.value
        ll = ll.next



# Command/mutator functions

def append_ll(ll,value):
    if ll == None:
        return LN(value)
    front = ll
    while ll.next != None:  # while ll does not refer to the last node...
        ll = ll.next        # terminates when ll.next == None
    ll.next = LN(value)     # append value at end
    return front            # return reference to original front of ll
    
def append_ll_r(ll,value):
    if ll == None:
        return LN(value)
    else:
        ll.next = append_ll_r(ll.next,value)
        return ll

    
def add_after_ll(ll,value):
    # raises an exception of ll is None
    ll.next = LN(value,ll.next)

def remove_after_ll(ll):
    # raises an exception of ll is None or ll.next is None
    ll.next = ll.next.next




# Driver
if __name__ == '__main__':
    test = list_to_ll(['a','b','c','d','e'])  
