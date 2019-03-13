# Submitter zhengyix(Xu, Zhengyi)
from collections import defaultdict


class History:
    def __init__(self):
        self._dict = defaultdict(list)
        
    def __getattr__(self, name):
        i = -1-name.count('_prev')
        s = name.replace('_prev','')
        if s not in self._dict.keys() or i > -2:
            raise NameError
        return self._dict[s][i] if -1-i < len(self._dict[s]) else None 
    
    def __getitem__(self, index):
        if index > 0:
            raise IndexError('Index must be a integer less than 1')
        return {name:(self._dict[name][index-1] if -index+1<=len(self._dict[name]) else None) for name in self._dict.keys()}    
        
    def __setattr__(self,name,value):
        if '_dict' in self.__dict__:
            if '_prev' not in name:
                self._dict[name].append(value)
            else:
                raise NameError
        self.__dict__[name] = value

if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test History before doing bsc tests

    print('Start simple testing')

    
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback =True
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
    driver.driver()
