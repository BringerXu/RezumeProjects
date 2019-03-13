# Submitter zhengyix(Xu, Zhengyi)
from goody import type_as_str

class Time:
    def __init__(self,hour = 0,minute = 0,second = 0):
        assert type(hour) == int and type(minute) == int and type(second) == int ,'hour, minute and second must be a integer'
        assert 0 <= hour <= 23, 'Hour ranges from 0 to 23 inclusively'
        assert 0 <= minute <= 59, 'minute ranges from 0 to 59 inclusively'
        assert 0 <= second <= 59, 'second ranges from 0 to 59 inclusively'
        self.hour = hour
        self.minute = minute
        self.second = second

    def __getitem__(self, index):
        Time = [self.hour,self.minute,self.second]
        if type(index) == tuple:
            result = list()
            for i in index:
                if type(i) == int and 1<=i<=3:
                    result.append(Time[i-1])
                else:
                    raise IndexError
            return tuple(result)
        if type(index) == int and 1<=index<=3:
            return Time[index-1]
        else:
            raise IndexError
        
    def __repr__(self):
        return 'Time({},{},{})'.format(self.hour,self.minute,self.second)
    
    def __str__(self):
        if self.hour == 0:
            return '{}:{:02d}:{:02d}{}'.format(self.hour+12,self.minute,self.second,'am')
        elif 0<self.hour<12:
            return '{}:{:02d}:{:02d}{}'.format(self.hour,self.minute,self.second,'am')
        elif self.hour == 12:
            return '{}:{:02d}:{:02d}{}'.format(self.hour,self.minute,self.second,'pm')
        else:
            return '{}:{:02d}:{:02d}{}'.format(self.hour-12,self.minute,self.second,'pm')
    
    def __bool__(self):
        if self.__repr__() == 'Time(0,0,0)':
            return False
        else:
            return True
    
    def __len__(self):
        return self[1]*60**2 + self[2]*60 + self[3]
    
    def __eq__(self,right):
        return len(self) == len(right) if type(right) == Time else False
    
    def __lt__(self,right):
        if type(right) == Time:
            return len(self) < len(right)
        elif type(right) == int:
            return len(self) < right
        else:
            raise TypeError
        
    def __add__(self,right):
        if type(right) == int:
            return Time((len(self)+right)%86400//3600,\
                        ((len(self)+right)%86400-(len(self)+right)%86400//3600*3600)//60,\
                        (len(self)+right)%86400-(len(self)+right)%86400//3600*3600-((len(self)+right)%86400-(len(self)+right)%86400//3600*3600)//60*60)
        else:
            raise TypeError
    
    def __radd__(self,left):
        return self+left
    
    def __call__(self, hour=0, minute = 0, second = 0):
        self.__init__(hour, minute, second)
        

if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Time before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback =True
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
    driver.driver()



        
        
        
        
        
