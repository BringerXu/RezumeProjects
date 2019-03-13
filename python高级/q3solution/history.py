from collections import defaultdict


class History:
    def __init__(self):
        self._history = defaultdict(list)
    
    def __getattr__(self,name):
        num = name.count('_prev') 
        name = name.replace('_prev', "")
        if name not in self.__dict__:
            raise NameError("Invalid: Name is not in dictionary")
        if num > (len(self._history[name])-1):
            return None
        return (self._history[name])[-(num+1)]


    def __getitem__(self,index):
        if index > 0:
            raise IndexError('Invalid: index should not be positive')
        for key in self._history.keys():
            if abs(index) + 1 > len(self._history[key]):
                self._history[key].insert(0, None)
        return {key: value[index-1] for (key, value) in self._history.items()}

    
    def __setattr__(self,name,value):
        if name.find('_prev') != -1:
            raise NameError('Invalid: Attribute contains _prev in name')
        if '_history' in self.__dict__: 
            self._history[name].append(value)
        self.__dict__[name] = value





if __name__ == '__main__':
    # Put in simple tests for History before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
