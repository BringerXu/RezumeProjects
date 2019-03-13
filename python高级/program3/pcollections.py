import re, traceback, keyword
from xml.dom import SyntaxErr
import copy

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'), 1):
            print('{line: >4} {text}'.format(line = i, text = l.rstrip()))
    # put your code here
    def unique(iterable):
        iterated = set()
        for i in iterable:
            if i not in iterated:
                iterated.add(i)
                yield i
    str_fn = []
    matcher = re.compile('^[a-zA-Z]\w*$')
    if type(type_name) != str or not matcher.match(type_name) or type_name in keyword.kwlist:
        raise SyntaxError
    else:
        if type(field_names) == list:
            for field_name in unique(field_names):
                if not matcher.match(field_name) or field_name in keyword.kwlist:
                    raise SyntaxError
                else:
                    str_fn.append(field_name)
        elif type(field_names) == str:
            fns = field_names.replace(',','').split(' ')
            fns = [fn for fn in fns if fn!='']
            for fn in unique(fns):
                if not matcher.match(fn) or fn in keyword.kwlist:
                    raise SyntaxError
                else:
                    str_fn.append(fn)
        else:
            raise SyntaxError
    # bind class_definition (used below) to the string constructed for the class
    class_definition = \
'''
class {}:\n\tdef __init__(self,'''.format(type_name)
    # init
    class_definition += ','.join(str_fn)
    class_definition += '):'
    for fn in str_fn:
        class_definition += ('\n\t\t'+'self.'+fn+' = '+fn)
    class_definition += ('\n\t\t'+'self._fields'+' = '+str(str_fn))
    class_definition += ('\n\t\t'+'self._mutable'+' = '+str(mutable))
    # repr
    class_definition += '\n\tdef __repr__(self):'
    con  = '('+','.join([fn+'='+'{'+fn+'}' for fn in str_fn])+')'
    recon = ','.join([fn+'='+'self.'+fn for fn in str_fn])
    formation = '\''+type_name+con+'\''
    class_definition += '\n\t\treturn '+formation+'.format('+recon+')'
    # get
    for fn in str_fn:
        class_definition += '\n\tdef get_'+fn+'(self):\n\t\treturn self.'+fn
    # getitem
    class_definition += '\n\tdef __getitem__(self,value):\n\t\tif type(value) == int:\n\t\t\tkey = self._fields[value]\n\t\t\treturn self.__dict__[key]\n\t\telif type(value) == str and value in self._fields:\n\t\t\treturn self.__dict__[value]\n\t\telse:\n\t\t\traise IndexError'
    # ==
    class_definition += '\n\tdef __eq__(self,right):\n\t\tif type(self) == type(right) and all([self[f] == right[f] for f in self._fields]):\n\t\t\treturn True\n\t\telse:\n\t\t\treturn False'
    #_replace
    class_definition += '\n\tdef _replace(self,**kargs):\n\t\tfor k in kargs:\n\t\t\tif k not in self._fields:\n\t\t\t\traise TypeError\n\t\tif self._mutable:\n\t\t\tfor k,v in kargs.items():\n\t\t\t\tself.__dict__[k] = v\n\t\telse:\n\t\t\tnew = copy.deepcopy(self)\n\t\t\tfor k,v in kargs.items():\n\t\t\t\tnew.__dict__[k] = v\n\t\t\treturn new'
    
    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace; next bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__='pnamedtuple_{type}'.format(type=type_name))
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]
Triple1 = pnamedtuple('Triple1', 'a b c')
t1 = Triple1(1,2,3)
t1._replace(a=2)
if __name__ == '__main__':
    # Test pnamedtuple in this script: e.g., Point = pnamedtuple('Point', 'x y')

    import driver
    driver.driver()
