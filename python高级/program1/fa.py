# Submitter: zhengyix(Xu, Zhengyi)
import goody

def read_fa(file : open) -> {str:{str:str}}:
    result = dict()
    for line in file:
        s_line = line.rstrip().split(';')
        result[s_line[0]] = dict(zip(s_line[1::2],s_line[2::2]))
    return result
        
        
def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join(sorted(['  ' + k + ' transitions: '+str(sorted([(n,tran) for n,tran in v.items()])) + '\n' for k,v in fa.items()]))
        

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    current = state
    for t in inputs:
        if t in fa[current]:
            result.append((t,fa[current][t]))
            current = fa[current][t]
        else:
            result.append((t,None))
            break
    return result


def interpret(fa_result : [None]) -> str:
    if fa_result[-1][-1] == None:
        return 'Start state = ' + fa_result[0] + '\n' + ''.join(['  Input = ' + i[0] + '; new state = ' + i[1] + '\n' for i in fa_result[1:-1]]) + '  Input = ' + fa_result[-1][0] + '; illegal input: simulation terminated\n' + 'Stop state = None\n'
    else:
        return 'Start state = ' + fa_result[0] + '\n' + ''.join(['  Input = ' + i[0] + '; new state = ' + i[1] + '\n' for i in fa_result[1:]]) + 'Stop state = ' + fa_result[-1][-1] + '\n'   
        




if __name__ == '__main__':
    # Write script here
    object_file = goody.safe_open('Enter some finite automaton file name', 'r', 'error')
    automaton = read_fa(object_file)
    print('The Finite Automaton Description\n' + fa_as_str(automaton))
    operate = goody.safe_open('Enter some file name with start-state and inputs', 'r', 'error')
    for line in operate:
        print('Starting up a new simulation\n' + interpret(process(automaton,line.split(';')[0],line.split(';')[1:])))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
