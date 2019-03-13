class Triple1:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self._fields = ['a', 'b', 'c']
        self._mutable = False
    def __repr__(self):
        return 'Triple1(a={a},b={b},c={c})'.format(a=self.a,b=self.b,c=self.c)
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def __getitem__(self,value):
        if type(value) == int:
            key = self._fields[value]
            return self.__dict__[key]
        elif type(value) == str and value in self._fields:
            return self.__dict__[value]
        else:
            raise IndexError
    def __eq__(self,right):
        if type(self) == type(right) and all([self[f] == right[f] for f in self._fields]):
            return True
        else:
            return False
    def _replace(self,**kargs):
        for k in kargs:
            if k not in self._fields:
                raise TypeError
        if self._mutable:
            for k,v in kargs.items():
                self.__dict__[k] = v
        else:
            new = copy.deepcopy(self)
            for k,v in kargs.items():
                new.__dict__[k] = v
            return new
     
        

