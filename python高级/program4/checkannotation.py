from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set the name below to True for checking to occur
    checking_on  = True
    
    # self._checking_on must also be true for checking to occur
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value, annot)
        elif type(annot) == list:
            assert isinstance(value, list)
            if len(annot) == 1:
                assert all([type(v) in annot for v in value])
            elif len(annot) > 1:
                assert set([type(v) for v in value]) == set(annot)
        elif type(annot) == tuple:
            assert isinstance(value, tuple)
            assert all([type(v) in annot for v in value])
            assert set([type(v) for v in value]) == set(annot)
        elif type(annot) == dict:
            assert isinstance(value, dict)
        elif type(annot) == set:
            assert isinstance(value, set)
        # Decode your annotation here; then check against argument
        
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict: the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if not self._checking_on:
            return self._f(*args, **kargs)   
        try:
            # Check the annotation for every parameter (if there is one)
            for arg in param_arg_bindings():
                self.check(arg,self._f.__annotations__[arg],param_arg_bindings()[arg])
            # Compute/remember the value of the decorated function
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                assert type(self._f(*args,**kargs)) == self._f.__annotations__['return']
            # Return the decorated answer
            return self._f(*args, **kargs)
            # remove after adding real code in try/except
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #    print(l.rstrip())
            #print(80*'-')
            raise


  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    '''
    def f(x:int): pass
    f = Check_Annotation(f)
    f(3)
    f('a')
    '''
           
    import driver
    driver.driver()
