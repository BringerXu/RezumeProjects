from predicate import is_prime

# primes is used to test code you write below
def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1
         
# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v



def running_count(iterable,p):
    answer = 0
    for i in iterable:
        if p(i):
            answer += 1
        yield answer
        
            
def stop_when(iterable,p):
    for i in iterable:
        if p(i):
            return
        yield i

def yield_and_skip(iterable):
    it = iter(iterable)
    while True:
        n = next(it)
        yield n
        if type(n) is int:
            for _i in range(n):
                n = next(it)


def windows(iterable,n,m=1):
    i = iter(iterable)
    answer = [next(i) for _x in range(n)]
    while True:
        yield answer
        answer = answer[m:] + [next(i) for _x in range(m)]


def alternate(*iterables):
    args = [iter(a) for a in iterables]
    while True:
        for a in args:
            yield next(a)


def myzip(*iterables):
    its = [iter(a) for a in iterables]
    while True:
        answer = ()
        stopped = 0
        for i in its:
            try:
                answer += (next(i),)
            except StopIteration:
                answer += (None,)
                stopped += 1
        if stopped != len(iterables):
            yield answer
        else:
            return


class Ordered:
    def __init__(self,aset):
        self.aset = aset

    def __iter__(self):
        if not self.aset:
            return
        min_value = min(self.aset)
        yield min_value
        while True:
            bigger_values = [v for v in self.aset if v>min_value]
            if not bigger_values:
                return
            else:
                min_value = min(bigger_values)
                yield min_value




if __name__ == '__main__':
    
    # Test running_count; you can add your own test cases
    print('\nTesting running_count')
    for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    
    for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    
    
    # Test stop_when; you can add your own test cases
    print('\nTesting stop_when')
    for c in stop_when('abcdefghijk', lambda x : x >='d'):
        print(c,end='')
    print()

    for c in stop_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print('\n')

    # Test group_when; you can add your own test cases
    print('\nTesting yield_and_skip')
    for i in yield_and_skip([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2]):
        print(i,end=' ')
    print()
    
    for i in yield_and_skip(hide([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2])):
        print(i,end=' ')
    print()


    # Test windows; you can add your own test cases
    print('\nTesting windows')
    for i in windows('abcdefghijk',4,2):
        print(i,end=' ')
    print()
    
    print('\nTesting windows on hidden')
    for i in windows(hide('abcdefghijk'),4,2):
        print(i,end=' ')
    print()


    # Test alternate; add your own test cases
    print('\nTesting alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end='')
    print()
       
    for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in alternate(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print()


    # Test myzip; add your own test cases
    print('\nTesting myzip')
    for i in myzip('abcde','fg','hijk'):
        print(i,end='')
    print()
       
    for i in myzip(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in myzip(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print('\n')
       
    
       
    
    # Test Ordered; add your own test cases
    print('\nTesting Ordered')
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print(next(i))
    print(next(i))
    s.remove(8)
    print(next(i))
    print(next(i))
    s.add(32)
    print(next(i))
    print()
   
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print([next(i), next(i), s.remove(8), next(i), next(i), s.add(32), next(i)])
    
    s = {1, 2, 4, 8}
    for v in Ordered(s):
        s.discard(8)
        s.add(10)
        print(v) 
    print('\n')
         
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
