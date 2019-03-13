# Define a special exception for use with the Graph class methods
# Use like any exception: e.g., raise GraphError('Graph.method...error indication...')
 
class GraphError(Exception):
    pass # Inherit all methods, including __init
 
 
class Graph:
    # HELPER METHODS: useful for checking legal arguments to methods below
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
        self.is_legal_edge_value = legal_edge_value_predicate
        self.edges = {}
        for odv in edges:
            if type(odv) is str:
                if odv in self.edges:
                    raise GraphError('__init__: illegal node: already in Graph('+str(odv)+')')
                else:
                    self.edges[odv] = {}
 
            elif self.legal_tuple3(odv):
                o,d,v = odv
                if o in self.edges and d in self[o]:
                    raise  GraphError('__init__: illegal edge: already in Graph('+str(odv)+')')
                self[o,d] = v
            else:
                raise GraphError('__init__: illegal node/edge specification('+str(odv)+')')

 
    def __str__(self):
        return '\nGraph:\n  '+'\n  '.join(str(o)+':' + ','.join(' '+str(d)+'('+str(v)+')' for d,v in sorted(dv.items())) for o,dv in sorted(self.edges.items()))
 
 
    def __getitem__(self,item):
        if type(item) is str and item in self.edges:
            return self.edges[item]
        elif self.legal_tuple2(item) and item[0] in self.edges and item[1] in self.edges[item[0]]:
            o,d = item
            return self.edges[o][d]
        else:
            raise GraphError('Graph.__getitem__: argument('+str(item)+') illegal: not string, 2-tuple of string, or not a node/edge in the Graph')
   
     
    # item must be a legal 2-tuple - (origin node, destination node), and
    # value must satisfy the predicate passed to __init__         
    def __setitem__(self,item,value):
        if self.legal_tuple2(item) and self.is_legal_edge_value(value):
            o,d = item
            if o not in self.edges:
                self.edges[o] = {}
            if d not in self.edges:
                self.edges[d] = {}
            self.edges[o][d] = value
        else:
            raise GraphError('Graph.__setitem__: item('+str(item)+') illegal or value('+str(value)+') not satisfy __init__\'s predicate')
 
 
    def node_count(self):
        return len(self.edges)
 
     
    # len returns the number of edges in the Graph (NOT the number of nodes; see above)
    def __len__(self):
        return sum(len(o) for o in self.edges.values())
 
 
    def out_degree(self,node):
        if type(node) is not str or node not in self:
            raise GraphError('Graph.out_degree: argument('+str(node)+') illegal: not a string that is a node in the Graph')
        return len(self[node])
     
     
    def in_degree(self,node):
        if type(node) is not str or node not in self:
            raise GraphError('Graph.in_degree: argument('+str(node)+') illegal: not a string that is a node in the Graph')
        return sum(1 if node in d else 0 for d in self.edges.values())
     
     
    # item can be either
    # a str - node,
    # a legal 2-tuple - (origin node, destination node),
    # a legal 3-tuple - (origin node, destination node, edge value)         
    def __contains__(self,item):
        if type(item) is str:
            return item in self.edges
        elif self.legal_tuple2(item):
            o,d = item[0],item[1]
            return o in self.edges and d in self.edges[o]
        elif self.legal_tuple3(item):
            o,d,v = item[0], item[1], item[2]
            return o in self.edges and d in self.edges[o] and v == self[o,d]
        else:
            raise GraphError('Graph.__contains__: item('+str(item)+') illegal: not string, 2-tuple of strings, or 3-tuple of two strings and a value satisfying __init__\'s predicate')
     
     
    # item can be either a str - node, or a legal 2-tuple - (origin node, destination node)        
    def __delitem__(self,item):
        if type(item) is str:
            o = item
            if o not in self.edges:
                return
            del self.edges[o]
            for ao in self.edges:
                if o in self.edges[ao]:
                    del self.edges[ao][o]
        elif self.legal_tuple2(item):
            o,d = item
            if o in self.edges and d in self.edges[o]:
                del self.edges[o][d]        
        else: 
            raise GraphError('Graph.__delitem__: argument('+str(item)+') illegal: not string or 2-tuple of strings')
 
 
    # d must be a str, destination node     
    def __call__(self,d):
        if type(d) is str and d in self.edges:
            return {o:v for o,_dv in self.edges.items() for pd,v in self.edges[o].items() if d == pd}
        else:
            raise GraphError('Graph.__call__: argument('+str(d)+') must be node in Graph')
 
  
    def clear(self):
        self.edges.clear()
        

    # file is a file open for writing
    # sep is the separation string to use when writing the file
    # edge_to_str converts an edge value into a string that can appear in the file
    def dump(self,file, sep=':', edge_to_str = str):
        with file:
            for o, dv in sorted(self.edges.items()):
                file.write(o + ''.join(sep+d+sep+edge_to_str(v) for d,v in sorted(dv.items())) +'\n')

            
    # file is a file open for reading
    # sep is the separation string to use when reading the file
    # edge_from_str converts a string read from the file into an edge value
    def load(self,file ,sep=':', edge_from_str = int):
        with file:
            self.edges.clear()
            for l in file:
                l = l.rstrip().split(sep)
                o = l[0]
                if o not in self.edges:
                    self.edges[o] = {}
                if len(l) > 1:
                    for d,v in zip(l[1::2],l[2::2]):
                        self[l[0],d] = edge_from_str(v)
        

    # contains all the nodes and edges in self, but with the origin/destination nodes reversed
    def reverse(self):
        g = Graph(self.is_legal_edge_value)
        for o in self.edges:
            g.edges[o] = {}
        for o,dv in self.edges.items():
            for d,v in dv.items():
                g[d,o] = v
        return g            
  
             
    # contains all the nodes in self and all the edges in self, such that the nodes are in the nodes_allowable
    def natural_subgraph(self,*nodes_allowable):
        if not all(type(n) is str for n in nodes_allowable):
            raise GraphError('Graph.natural_subgraph: argument('+str(nodes_allowable)+') must contain only strings')

        g = Graph(self.is_legal_edge_value)
        # Bypass using __setattr__ to avoid triggering error for changing edges
        g.__dict__['edges'] = {o: {d:v for d,v in dv.items() if d in nodes_allowable} for o,dv in self.edges.items() if o in nodes_allowable}
        return g
 
                          
    # Produces str, nodes with no edges to/from them,
    #   or 3-tuple, (origin node, destination node, edge value),
    #   in alphabetic order by str/origin node 
    #      and by destination node for all edge values with the same origin node        
    def __iter__(self):
        for o in sorted(self.edges):
            if self.edges[o] == {} and not any(o in d for d in self.edges.values()):
                yield o
            else:
                for d in sorted(self[o]):
                    yield (o,d,self[o,d]) 

                                
    def __eq__(self,right):
        return self.edges == right.edges
    

    def __ne__(self,right):
        return self.edges != right.edges
    
    
    # self <= right if every node in self is in right, and every edge in self is also in right (with the same value)                
    def __le__(self,right):
        for n in self.edges:
            if n not in right.edges:
                return False
        for o,d,v in self:
            if (o,d) not in right or v != right[o,d]:
                return False
        return True
         
 
    # right can be 
    #   another Graph or                 
    #   a str - node,
    #   a legal 3-tuple - (origin node, destination node, edge value)         
    def __add__(self,right):
        g = Graph(self.is_legal_edge_value)
        for o,dv in self.edges.items():
            if o not in g:
                g.edges[o] = {}
            for d,v in dv.items():
                g[o,d] = v
             
        if type(right) is Graph:    
            #favor first node
            for o,dv in right.edges.items():
                if o not in g:
                    g.edges[o] = {}
                for d,v in dv.items():
                    if (o,d) not in g:
                        g[o,d] = v
        elif type(right) is str:
            if right not in g:
                g.edges[right] = {}
        elif self.legal_tuple3(right):
            o,d,v = right
            g[o,d] = v
        else:
            raise GraphError('Graph.__add__: argument('+str(right)+') must be Graph or 3-tuple:(origin,destination,value)')
 
        return g
 
 
    def __radd__(self,left):
        # Commutative
        return self + left
        

    # right can be 
    #   another Graph or                 
    #   a str - node,
    #   a legal 3-tuple - (origin node, destination node, edge value)         
    def __iadd__(self,right):
        if type(right) is Graph:    
            #favor first node
            for o,dv in right.edges.items():
                if o not in self:
                    self.edges[o] = {}
                for d,v in dv.items():
                    if (o,d) not in self:
                        self[o,d] = v
        elif type(right) is str:
            if right not in self:
                self.edges[right] = {}
        elif self.legal_tuple3(right):
            o,d,v = right
            self[o,d] = v
        else:
            raise GraphError('Graph.__iadd__: argument('+str(right)+') must be Graph or 3-tuple:(origin,destination,value)')
 
        return self
    
    
    def __setattr__(self,name,value):
        assert 'edges' not in self.__dict__, 'Graph.__setattr__ attempted to set/reset attribute:'+name
        self.__dict__[name] = value
        
 
 
if __name__ == '__main__':
    #Put code here to test Graph before doing bsc test; for example
    g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
    print(repr(g))
    print(g)
    print(g['a'])
    print(g['a','b'])
    print(g.node_count())
    print(len(g))
    print(g.out_degree('c'))
    print(g.in_degree('a'))
    print('c' in g)
    print(('a','b') in g)
    print(('a','b',1) in g)
    print(g('c'))
    #print(g.reverse())
    print(g.natural_subgraph('a','b','c'))
    print()    
     
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
