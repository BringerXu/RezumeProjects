from _collections import defaultdict
import copy
 
class GraphError(Exception):
    pass # Inherit all methods, including __init__
 
 
class Graph:
    # HELPER METHODS: used for checking legal arguments to methods below
    def legal_tuple2(self,t):
        return type(t) is tuple and len(t) == 2 and\
               type(t[0]) is str and type(t[1]) is str

    def legal_tuple3(self,t):
        return type(t) is tuple and len(t) == 3 and\
               type(t[0]) is str and type(t[1]) is str and self.is_legal_edge_value(t[2])
        
 
    # __str__ and many bsc tests use the name self.edges for the outer/inner-dict.
    # So __init__ should use self.edges for the name for this dictionary
    # self should store NO other attributes: compute all results from self.edges ONLY
    # Each value in the edges tuple can be either a 
    #   (a) str = origin node
    #   (b) 3-tuple = (origin node, destination node, edge value) 
    def __init__(self,legal_edge_value_predicate,*edges):
        self.edges = defaultdict(dict)
        self.is_legal_edge_value = legal_edge_value_predicate
        for e in edges:
            if type(e) == tuple and self.legal_tuple3(e) and e[1] not in self.edges[e[0]]:
                self.edges[e[0]].update({e[1]:e[2]})
                self.edges[e[1]].update({})
            elif type(e) == str and e not in self.edges:
                self.edges[e] = {}
            else:
                raise GraphError
            
    # Put all other methods here
    def __str__(self):
        return '\nGraph:' + ''.join(['\n  {}:{}'.format(o,','.join([' {}({})'.format(d,v)  for d,v in dv.items()])) for o,dv in self.edges.items()])
    
    def __getitem__(self, item):
        if type(item) == str and item in self.edges:
            return self.edges[item]
        elif type(item) == tuple and self.legal_tuple2(item) and item[0] in self.edges and item[1] in self.edges[item[0]]:
            return self.edges[item[0]][item[1]]
        else:
            raise GraphError
        
    def __setitem__(self, item, value):
        if type(item) == tuple and self.legal_tuple2(item) and self.is_legal_edge_value(value):
            self.edges[item[0]][item[1]] = value
            self.edges[item[1]].update({})
        else:
            raise GraphError
        
    def node_count(self):
        return len(self.edges.keys())
    
    def __len__(self):
        result = []
        for o,dv in self.edges.items():
            for d,v in dv.items():
                result.append(v)
        return len(result)
    
    def out_degree(self, node):
        if type(node) == str and node in self.edges:
            return len(self.edges[node])
        else:
            raise GraphError
    
    def in_degree(self, node):
        if type(node) == str and node in self.edges:
            return len([dv for dv in self.edges.values() if node in dv])
        else:
            raise GraphError
        
    def __contains__(self, item):
        if type(item) == str:
            if item in self.edges:
                return True
            else:
                return False
        elif type(item) == tuple:
            if len(item) == 2 and self.legal_tuple2(item):
                if self.edges.get(item[0],None).get(item[1],None) != None:
                    return True
                else:
                    return False
            elif len(item) == 3 and self.legal_tuple3(item):
                if self.edges.get(item[0],None).get(item[1],None) == item[2]:
                    return True
                else:
                    return False
            else:
                raise GraphError
        else:
            raise GraphError
        
    def __delitem__(self, item):
        if type(item) == str: 
            if item in self.edges:
                self.edges.pop(item,None)
                for v in self.edges.values():
                    v.pop(item,None)
        elif type(item) == tuple and self.legal_tuple2(item):
            if item in self:
                self.edges[item[0]].pop(item[1],None)
        else:
            raise GraphError
        
    def __call__(self, d):
        if type(d) == str and d in self:
            result = {}
            for o in self.edges:
                for de in self.edges[o]:
                    if d == de:
                        result.update({o:self.edges[o][de]})
            return result
        else:
            raise GraphError
        
    def clear(self):
        self.edges = {}
        
    def dump(self, file_w, sep = ':', fun = str):
        for o in sorted(self.edges.keys()):
            result = [o]
            for d in sorted(self.edges[o].keys()):
                result.extend([d,fun(self.edges[o][d])])
            file_w.write(sep.join(result)+'\n')
        file_w.close()
        
    def load(self, file_r, sep = ':', fun = int):
        result = defaultdict(dict)
        for line in file_r:
            linelist = line.rstrip().split(sep)
            if len(linelist) > 1:
                for dv in zip(linelist[1::2],linelist[2::2]):
                    result[linelist[0]][dv[0]] = fun(dv[1])
            else:
                result[linelist[0]] == {}
        self.edges = result
        
    def reverse(self):
        result = defaultdict(dict)
        for o in self.edges:
            if self.edges[o] == {}:
                result.setdefault(o,{})
            else:
                for d in self.edges[o]:
                    result[d].update({o:self.edges[o][d]})
                    result.setdefault(o, {})
        g = Graph(self.is_legal_edge_value)
        g.edges = result
        return g
    
    def natural_subgraph(self, *nodes):
        result = defaultdict(dict)
        for n in nodes:
            if type(n) == str:
                if n in self.edges:
                    result[n] = {d:v for d,v in self.edges[n].items() if d in nodes}
            else:
                raise GraphError
        g = Graph(self.is_legal_edge_value)
        g.edges = result
        return g
    
    def __iter__(self):
        for o in sorted(self.edges.keys()):
            if self.edges[o] == {} and not self.in_degree(o):
                yield o
            else:
                for d in sorted(self.edges[o].keys()):
                    yield (o, d, self.edges[o][d])
                    
    def __eq__(self, right):
        return self.edges == right.edges
    
    def __nq__(self, right):
        return self.edges != right.edges
    
    def __le__(self, right):
        for o in self.edges:
            if o not in right.edges:
                return False
            for dv in self.edges[o].items():
                if dv not in right.edges[o].items():
                    return False
        return True
         
    def __add__(self, right):
        result = copy.deepcopy(self)
        if type(right) == Graph:
            for o,dv in right.edges.items():
                for d,v in dv.items():
                    if o in result.edges:
                        if d not in result.edges:
                            result.edges[o].update({d:v})
                    else:
                        result.edges[o] = {} 
        elif type(right) == str:
            if right not in result.edges:
                result.edges.update({right:{}}) 
            return result
        elif type(right) == tuple and result.legal_tuple3(right):
            result.edges.setdefault(right[0],{}).update({right[1]:right[2]})
            result.edges.setdefault(right[1],{})
            return result
        else:
            raise GraphError
        
    def __radd__(self, left):
        return self+left
    
    def __iadd__(self, right):
        return self+right
    
g1 = Graph( (lambda x : type(x) is int), ('a','b',1),('b','a',2) )
g2 = Graph( (lambda x : type(x) is int), ('d','b',2),('d','c',1),'e')
(g1+g2).edges