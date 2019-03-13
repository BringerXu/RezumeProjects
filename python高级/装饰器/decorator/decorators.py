# Tracking (counting) function calls as decorator class/function

class Track_Calls:
    def __init__(self,f):
        self.f = f
        self.calls = 0
    
    def __call__(self,*args,**kargs):  # bundle arbitrary arguments
        self.calls += 1
        return self.f(*args,**kargs)   # unbundle arbitrary arguments

    def called(self):
        return self.calls
    
    def reset_calls(self):
        self.calls = 0

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)
    

# Memoizing function calls as decorator class/function

class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}
        
    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer

    def reset_cache(self):
        self.cache = {}
        
    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)


# Illustrating the recursive structure (calls/returns) of recursive functions

class Illustrate_Recursive:
    def __init__(self,f):
        self.f = f
        self.trace = False
        
    def illustrate(self,*args,**kargs):
        self.indent = 0
        self.trace = True
        answer = self.__call__(*args,**kargs)
        self.trace = False
        return answer
    
    def __call__(self,*args,**kargs):
        if self.trace:
            if self.indent == 0:
                print('Starting recursive illustration'+30*'-')
            print (self.indent*"."+"calling", self.f.__name__+str(args)+str(kargs))
            self.indent += 2
        answer = self.f(*args,**kargs)
        if self.trace:
            self.indent -= 2
            print (self.indent*"."+self.f.__name__+str(args)+str(kargs)+" returns", answer)
            if self.indent == 0:
                print('Ending recursive illustration'+30*'-')
        return answer

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)





if __name__ == '__main__':
    from goody import irange
    
    @Illustrate_Recursive
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    
    print('Illustrating recursive factorial')    
    factorial.illustrate(5)     # For Illustrate_Recursive
    

    # Use any combination (in any order) of Decorators (why __getattr__ is needed)
    #@Memoize
    @Illustrate_Recursive
    @Track_Calls
    def fib(n):
        if    n == 0: return 1
        elif  n == 1: return 1
        else:         return fib(n-1) + fib(n-2)
    
    print('\nIllustrating recursive fib(onacci)')    
    fib.illustrate(5)           # For Illustrate_Recursive
    print('\nTracking calls for recursive fib(onacci)')    
    for i in irange(0,30): 
            fib.reset_calls()  # if Track_Calls decorator
            #fib.reset_cache()  # if Memoize decorator
            print('  Fib('+str(i)+') =', fib(i), 'and # calls for fib('+str(i)+') =', fib.called())

    
    
    # Examining/manipulating recursion depth
    
    import sys 
    print('\nShowing manipulation of sys. get/set recursion limit')
    print('Current recursion limit =',sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    print('Current recursion limit =',sys.getrecursionlimit())
