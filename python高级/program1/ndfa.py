# Submitter: zhengyix(Xu, Zhengyi)
import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    result = dict()
    for line in file:
        list_line = line.rstrip().split(';')
        result.setdefault(list_line[0],dict())
        for k,v  in zip(list_line[1::2],list_line[2::2]):
            result[list_line[0]].setdefault(k,set())
            result[list_line[0]][k].add(v)
    return result

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
   return ''.join(sorted(['  ' + k +' transitions: ' + str(sorted((x, sorted(y)) for x,y in ndfa[k].items())) + '\n' for k in ndfa]))

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    exploring = [state]
    for i in inputs:
        con = set()
        for object in exploring:
            if i in ndfa[object]:
                con = con | {item for item in ndfa[object][i]}
        result.append((i,con))
        if con == set():
            break
        exploring = [item for item in con]
    return result

def interpret(result : [None]) -> str:
   return 'Start state = ' + result[0] + '\n' + ''.join(['  Input = ' + n + '; new possible states = ' + str(sorted(t)) + '\n' for n,t in result[1:]]) + 'Stop state(s) = ' + str(sorted(result[-1][-1])) + '\n'





if __name__ == '__main__':
    # Write script here
    object_file = goody.safe_open('Enter some non-deterministic finite automaton file name', 'r', 'error')
    ndfa = read_ndfa(object_file)
    print('The Non-Deterministic Finite Automaton Description\n'+ndfa_as_str(ndfa))
    trace_ndfa = goody.safe_open('Enter some file name with start-state and inputs','r','error')
    for line in trace_ndfa:
        print('Starting up a new simulation\n' + interpret(process(ndfa,line.rstrip().split(';')[0],line.rstrip().split(';')[1:])))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
