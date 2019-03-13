# Submitter: zhengyix(Xu, Zhengyi)
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    nodes = defaultdict(set)
    for line in file.readlines():
        nodes[line[0]].add(line[2])
    return nodes

def graph_as_str(graph : {str:{str}}) -> str:
    return ''.join(sorted(['  '+k+' -> '+str(sorted(v))+'\n' for k,v in graph.items()], key = lambda ob:ob[2]))
        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    result = set()
    exploring = [start]
    while exploring != []:
        object = exploring.pop(0)
        result.add(object)
        for item in graph.get(object,[]):
            exploring.append(item)
    return result
        




if __name__ == '__main__':
    # Write script here
    graph_file = goody.safe_open('  Enter some graph file name','r','error')
    graph = read_graph(graph_file)
    print('  Graph: source node -> [destination nodes]')
    print(graph_as_str(graph))
    print()
    print()
    while True:
        start = prompt.for_string('  Enter some starting node name (else quit)')
        if start == 'quit':
            break
        print('  From',start,'the reachable nodes are',reachable(graph,start))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
