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

g1 = {'e': {'d'}, 'a': {'b', 'c'}, 'd': {'g'}, 'b': {'d'}, 'c': {'f', 'e'}, 'f': {'g', 'd'}}
reachable.reachable(g1,'a')
reachable.reachable(g1,'c')