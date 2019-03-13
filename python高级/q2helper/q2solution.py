# Submitter: zhengyix(Xu, Zhengyi)
import re

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1.txt, repattern2a.txt, and
#   repattern2b.txt (or comment out those tests). The patterns must be on the
#   first line.


def multi_compare(pat_file : open, text_file1 : open, text_file2 : open) -> [(int,str,str)]:
    result = []
    for num,line in enumerate(zip(text_file1,text_file2), 1):
        for p in pat_file:
            matcher = re.compile(p.rstrip())
            if (matcher.match(line[0].rstrip()) and not matcher.match(line[1].rstrip())) or (not matcher.match(line[0].rstrip()) and matcher.match(line[1].rstrip())):
                result.append((num, line[0].rstrip(), line[1].rstrip()))
                break
        pat_file.seek(0)
    return result
        
            
    
def expand_re(pat_dict:{str:str}):
    for k in pat_dict.keys():
        for k2,v in pat_dict.items():
            if k!=k2: 
                pat_dict[k2] = re.sub('#'+k+'#','('+pat_dict[k]+')',v)




if __name__ == '__main__':
    p1 = open('repattern1.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1: ',p1)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p2a = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2a: ',p2a)
    for text in open('bm2.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p2a = open('repattern2b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2b: ',p2a)
    for text in open('bm2.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2a,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    
    print('\nTesting multi_search')
    print('  first  result  =',multi_compare(open('pats1.txt'),open('texts1a.txt'),open('texts1b.txt')))
    print('  second result  =',multi_compare(open('pats2.txt'),open('texts2a.txt'),open('texts2b.txt')))
    
    print('\nTesting expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
    
    pd = dict(integer       =r'[+-]?\d+',
              integer_range =r'#integer#(..#integer#)?',
              integer_list  =r'#integer_range#(?,#integer_range#)*',
              integer_set   =r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer'      : '[+-]?\\d+',
    #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
    #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
    #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'d': '(((correct)))',
    #  'c': '((correct))',
    #  'b': '(correct)',
    #  'a': 'correct',
    #  'g': '((((((correct))))))',
    #  'f': '(((((correct)))))',
    #  'e': '((((correct))))'
    # }
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
