from goody import type_as_str

class Time:
    def __init__(self,hour:int=0,minute:int=0,second:int=0):
        assert type(hour) is int and 0 <= hour <= 23,   'Time.__init__: hour('+str(hour)+') is not int in range [0,23)'
        assert type(hour) is int and 0 <= minute <= 59, 'Time.__init__: minute('+str(minute)+') is not int in range [0,59)'
        assert type(hour) is int and 0 <= second <= 59, 'Time.__init__: second('+str(second)+') is not int in range [0,59)'
        self.hour   = hour
        self.minute = minute
        self.second = second
        

    def __getitem__(self,index):
        if type(index) is not tuple:
            index =(index,)
        if not all(type(i) is int and 1<=i<=3 for i in index):
            raise IndexError('Time.__getitem__: illegal argument in '+str(index))
        answer = tuple(self.hour if i==1 else self.minute if i==2 else self.second for i in index)
        if len(answer)==1:
            answer = answer[0]
        return answer
        
        
    def __repr__(self):
        return 'Time('+','.join(str(part) for part in self[1,2,3])+')'
    
    
    def __str__(self):
        def two_digit(d): return ('' if d >= 10 else '0' ) + str(d)            
        start = str(12 if self.hour == 0 else self.hour if self.hour <= 12 else self.hour-12)
        return start + ':'+two_digit(self.minute)+':'+two_digit(self.second)+('am' if self.hour<12 else 'pm')


    def __bool__(self):
        return self.hour != 0 or self.minute != 0 or self.second != 0
    
    
    def __len__(self):
        return sum(c*i for c,i in zip((3600,60,1),self[1,2,3]))
    
    
    def __lt__(self,right):
        if type(right) is Time:
            return len(self) < len(right)
        elif type(right) is int:
            return len(self) < right
        else:
            raise TypeError('unorderable types: '+type_as_str(self)+'() < '+type_as_str(right)+')')


    def __eq__(self,right):
        return type(right) is Time and self[1,2,3] == right[1,2,3]
    
    
    def __ne_(self,right):
        return type(right) is not Time or self[1,2,3] != right[1,2,3]
    
    
    def __add__(self,right):
        if type(right) is not int:
            raise TypeError(' unsupported operand type(s) for +: '+type_as_str(self)+' and '+type_as_str(right))
        t = (len(self) + right)%86400
        s = t%60
        m = t//60 % 60
        h = t//3600
        
#         #Alternative calculation
#         h,m,s = self[1,2,3]
#         for _i in range(right%86400):
#             s += 1
#             if s == 60:
#                 m, s = m+1, 0
#                 if m == 60:
#                     h, m = h+1, 0
#                     if h == 24:
#                         h = 0
        return Time(h,m,s)
    
    def __radd__(self,left):
        return self+left
    
    def __call__(self,hour,minute,second):
        self.__init__(hour,minute,second)
        

if __name__ == '__main__':
    # Put in simple tests for Time before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()



        
        
        
        
        