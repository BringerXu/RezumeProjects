import re
def expand_re(pat_dict:{str:str}):
    for k in pat_dict:
        repl = pat_dict[k]
        for v in pat_dict.values():
            re.sub('#'+k+'#',repl,v)
pd = {'dig': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
expand_re(pd)
print(pd)
#{'dig': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}