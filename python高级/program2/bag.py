# Submitter zhengyix(Xu, Zhengyi)
from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self,items = None):
        self.bag = defaultdict(int)
        if items != None:
            for item in items:
                self.bag[item] += 1
                
    def __repr__(self):
        return 'Bag({})'.format([k for k in self.bag for t in range(self.bag[k])])
    
    def __str__(self):
        return 'Bag({})'.format(','.join('{}[{}]'.format(k,v) for k,v in self.bag.items()))
    
    def __len__(self):
        return sum(self.bag.values())
    
    def unique(self):
        return len(self.bag.keys())
    
    def __contains__(self, item):
        return item in self.bag.keys()
    
    def count(self, item):
        return self.bag[item] if item in self.bag.keys() else 0
    
    def add(self, item):
        self.bag[item] = self.bag.get(item,0) + 1
    
    def __add__(self,right):
        if type(right) != Bag:
            raise TypeError
        return Bag(eval(repr(self)[4:-1])+eval(repr(right)[4:-1]))
    
    def remove(self, item):
        if item in self.bag.keys():
            self.bag[item] -= 1
            if self.bag[item] == 0:
                self.bag.pop(item)
        else:
            raise ValueError
    
    def __eq__(self,right):
        return self.bag == right.bag if type(right) == Bag else False
    
    def __iter__(self):
        return iter([k for k,v in self.bag.items() for t in range(v)])
'''
        c = self.bag.copy() # cannot work because of mutated self.bag.copy(), it will run every time iterator call next
        for k in c:
            for t in range(c[k]):
                yield k
'''
    
if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
