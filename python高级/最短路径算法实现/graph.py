from vertex import Vertex
from edge import Edge
from edge import DirectedEdge

class Graph():
    ''' This is a graph. '''
    
    _graph_counter = 0
    
    def __init__(self):
        Graph._graph_counter += 1
        self._num = Graph._graph_counter

class SimpleGraph(Graph):
    ''' This is a "simple" graph.
    A "simple" graph is defined as:  a graph in which an edge cannot be duplicated, 
        i.e., only one edge can connect vertex v1 and vertex v2  '''
    
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        ''' initialize the graph '''
        
        Graph.__init__(self)
        
        self._vertices = []
        self._edges = []
        self._edge_counter = 0
        
        for item in vertex_nums:
            v = Vertex(item)
            self._vertices.append(v)
        
        for item1 in edges_to_add:
            for item2 in self._vertices:
                if item2.get_num() == item1[0]:
                    v1 = item2
                if item2.get_num() == item1[1]:
                    v2 = item2
        
            self.add_edge(v1, v2)
    
    def get_num(self) -> int:
        ''' get the ID for the graph '''
        return self._num
    
    def get_vertices(self) -> ['Vertex']:
        ''' get the vertices in this graph '''
        return self._vertices
    
    def get_vertex(self, vertexID:int) -> 'Vertex':
        ''' returns the vertex object with the given ID '''
        
        vertex_to_return = None
        for item in self._vertices:
            if item.get_num() == vertexID:
                vertex_to_return = item
        
        return vertex_to_return 
    
    def get_edge_by_id(self, edgeID:int) -> 'Edge':
        ''' returns the edge object with the given ID '''
        
        edge_to_return = None
        for item in self._edges:
            if item.get_num() == edgeID:
                edge_to_return = item
        
        return edge_to_return   
    
    def get_edge_by_vertexID(self, vertexID1:int, vertexID2:int) -> 'Edge':
        ''' returns the edge object that connects the given vertices '''
        
        edge_to_return = None
        for item in self._edges:
            if (item.get_vertices()[0].get_num() == vertexID1):
                if (item.get_vertices()[1].get_num() == vertexID2):      
                    edge_to_return = item
            if (item.get_vertices()[1].get_num() == vertexID1):
                if (item.get_vertices()[0].get_num() == vertexID2):      
                    edge_to_return = item
        
        return edge_to_return       
        
    def add_vertex(self, vertex_num:int, edges_to_add:[int] = []) -> None:
        ''' add a vertex to the graph '''
        
        v = Vertex(vertex_num)
        self._vertices.append(v)
        
        for item1 in edges_to_add:
            for item2 in self._vertices:
                if item2.get_num() == item1:
                    v_to_add = item2
            
            self.add_edge(v, v_to_add)
            
    def remove_vertex(self, inVertex:'Vertex') -> None:
        ''' remove a vertex from the graph '''
        
        vertexToDelete = None
        for item in self._vertices:
            if item.get_num() == inVertex.get_num():
                vertexToDelete = item
        
        edgeList = list(vertexToDelete.get_edges())
        for item in edgeList:
            item.get_vertices()[0].remove_edge(item)
            item.get_vertices()[1].remove_edge(item)    
            self._edges.remove(item)
        
        for item in self._vertices:
            if item.get_num() == vertexToDelete.get_num():        
                self._vertices.remove(item)

    def get_edges(self) -> ['Edge']:
        ''' returns the edges in this graph '''
        return self._edges

    def add_edge(self, inVertex1:'Vertex', inVertex2:'Vertex') -> None:
        ''' add an edge to the graph ''' 
        
        self._edge_counter += 1
        
        e = Edge(self._edge_counter, inVertex1, inVertex2)
        self._edges.append(e)
        inVertex1.add_edge(e)
        inVertex2.add_edge(e)
        
    def remove_edge(self, inEdge:'Edge') -> None:
        ''' remove an edge from the graph '''
        
        edgeToDelete = None
        for item in self._edges:
            if item.get_num() == inEdge.get_num():
                edgeToDelete = item
                
        for item in edgeToDelete.get_vertices():
            item.remove_edge(edgeToDelete)
        
        for item in self._edges:
            if item.get_num() == edgeToDelete.get_num():
                self._edges.remove(item)
    
    def __str__(self) -> str:
        return "SimpleGraph({num}, {vertices}, {edges})".format(
            num = self._num, 
            vertices = ["Vertex({n})".format(n = x.get_num()) for x in self._vertices],
            edges = ["Edge({n}, {v1} - {v2})".format(n = y.get_num(), v1 = y.get_vertices()[0].get_num(), v2 = y.get_vertices()[1].get_num()) for y in self._edges])

class SimpleColorableGraph(SimpleGraph):
    ''' This is a "simple", "colorable" graph.
    A "simple" graph is defined as:  a graph in which an edge cannot be duplicated, 
        i.e., only one edge can connect vertex v1 and vertex v2  
    A "colorable" graph is defined as:  a graph in which a vertex can be colored,
        e.g., no color, red, blue, etc. '''
    
    UNCOLORED = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        ''' initialize the graph '''
        
        SimpleGraph.__init__(self, vertex_nums, edges_to_add)
        
        self._vertex_colors = []
        for item in self._vertices:
            t = (item.get_num(), SimpleColorableGraph.UNCOLORED)
            self._vertex_colors.append(t)
    
    def get_color_by_vertex(self, inVertex:'Vertex') -> int:
        ''' get the color for the provided vertex object '''
        
        color_to_return = SimpleColorableGraph.UNCOLORED
        for item in self._vertex_colors:
            if item[0] == inVertex.get_num():
                color_to_return = item[1]
        
        return color_to_return
    
    def set_color_by_vertex(self, inVertex:'Vertex', inColor:int) -> None:
        ''' set the color for the provided vertex object '''
        
        for item in self._vertex_colors:
            if item[0] == inVertex.get_num():
                self._vertex_colors.remove(item)
                t = (inVertex.get_num(), inColor)
                self._vertex_colors.append(t)
                
    def add_vertex(self, vertex_num:int, edges_to_add:[int] = [], inColor:int = UNCOLORED) -> None:
        ''' add a vertex to the graph '''
        
        SimpleGraph.add_vertex(self, vertex_num, edges_to_add)
        t = (vertex_num, inColor)
        self._vertex_colors.append(t)       
            
    def remove_vertex(self, inVertex:'Vertex') -> None:
        ''' remove a vertex from the graph '''
        
        SimpleGraph.remove_vertex(self, inVertex)
        for item in self._vertex_colors:
            if item[0] == inVertex.get_num():
                self._vertex_colors.remove(item)
    
    def __str__(self) -> str:
        return "SimpleColorableGraph({num}, {vertices}, {edges})".format(
            num = self._num, 
            vertices = ["Vertex({n}, {c})".format(n = x.get_num(), c = self.get_color_by_vertex(x)) for x in self._vertices],
            edges = ["Edge({n}, {v1} - {v2})".format(n = y.get_num(), v1 = y.get_vertices()[0].get_num(), v2 = y.get_vertices()[1].get_num()) for y in self._edges])

class DirectedGraph(Graph):
    ''' This is a "directed" graph.
    A "directed" graph is defined as:  a graph in which each edge has a direction, 
        i.e., an edge flows from vertex v1 (the source) to vertex v2 (the destination)  '''
    
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        ''' initialize the graph
        In the list of edges to add, the tuples should be ordered as (source, destination). '''
        
        Graph.__init__(self)
        
        self._vertices = []
        self._edges = []
        self._edge_counter = 0
        
        for item in vertex_nums:
            v = Vertex(item)
            self._vertices.append(v)
        
        for item1 in edges_to_add:
            for item2 in self._vertices:
                if item2.get_num() == item1[0]:
                    v1 = item2
                if item2.get_num() == item1[1]:
                    v2 = item2
        
            self.add_edge(v1, v2)
    
    def get_num(self) -> int:
        ''' get the ID for the graph '''
        return self._num
    
    def get_vertices(self) -> ['Vertex']:
        ''' get the vertices in this graph '''
        return self._vertices
    
    def get_vertex(self, vertexID:int) -> 'Vertex':
        ''' returns the vertex object with the given ID '''
        
        vertex_to_return = None
        for item in self._vertices:
            if item.get_num() == vertexID:
                vertex_to_return = item
        
        return vertex_to_return 
    
    def get_edges(self) -> ['Edge']:
        ''' returns the edges in this graph '''
        return self._edges
    
    def get_edge_by_id(self, edgeID:int) -> 'DirectedEdge':
        ''' returns the edge object with the given ID '''
        
        edge_to_return = None
        for item in self._edges:
            if item.get_num() == edgeID:
                edge_to_return = item
        
        return edge_to_return   
    
    def get_edge_by_vertexID(self, sourceID:int, destinationID:int) -> 'DirectedEdge':
        ''' returns the edge object that connects the given vertices '''
        
        edge_to_return = None
        for item in self._edges:
            if (item.get_source().get_num() == sourceID):
                if (item.get_destination().get_num() == destinationID):      
                    edge_to_return = item
        
        return edge_to_return       
        
    def add_vertex(self, vertex_num:int, edges_to_add:[int] = []) -> None:
        ''' add a vertex to the graph 
        Here the edges to add will flow from the new vertex to the indicated vertices. '''
        
        v = Vertex(vertex_num)
        self._vertices.append(v)
        
        for item1 in edges_to_add:
            for item2 in self._vertices:
                if item2.get_num() == item1:
                    v_to_add = item2
            
            self.add_edge(v, v_to_add)
            
    def remove_vertex(self, inVertex:'Vertex') -> None:
        ''' remove a vertex from the graph '''
        
        vertexToDelete = None
        for item in self._vertices:
            if item.get_num() == inVertex.get_num():
                vertexToDelete = item
        
        edgeList = list(vertexToDelete.get_edges())
        for item in edgeList:
            item.get_vertices()[0].remove_edge(item)
            item.get_vertices()[1].remove_edge(item)    
            self._edges.remove(item)
        
        for item in self._vertices:
            if item.get_num() == vertexToDelete.get_num():        
                self._vertices.remove(item)

    def add_edge(self, source:'Vertex', destination:'Vertex') -> None:
        ''' add an edge to the graph ''' 
        
        self._edge_counter += 1
        
        e = DirectedEdge(self._edge_counter, source, destination)
        self._edges.append(e)
        source.add_edge(e)
        destination.add_edge(e)
        
    def remove_edge(self, inEdge:'Edge') -> None:
        ''' remove an edge from the graph '''
        
        edgeToDelete = None
        for item in self._edges:
            if item.get_num() == inEdge.get_num():
                edgeToDelete = item
                
        for item in edgeToDelete.get_vertices():
            item.remove_edge(edgeToDelete)
        
        for item in self._edges:
            if item.get_num() == edgeToDelete.get_num():
                self._edges.remove(item)
    
    def __str__(self) -> str:
        return "DirectedGraph({num}, {vertices}, {edges})".format(
            num = self._num, 
            vertices = ["Vertex({n})".format(n = x.get_num()) for x in self._vertices],
            edges = ["DirectedEdge({n}, {v1} -> {v2})".format(n = y.get_num(), v1 = y.get_vertices()[0].get_num(), v2 = y.get_vertices()[1].get_num()) for y in self._edges])          
        
class SimpleColorableDirectedGraph(DirectedGraph, SimpleColorableGraph):
    ''' This is a "simple", "colorable", "directed" graph.
    A "simple" graph is defined as:  a graph in which an edge cannot be duplicated, 
        i.e., only one edge can connect vertex v1 and vertex v2
    A "colorable" graph is defined as:  a graph in which a vertex can be colored,
        e.g., no color, red, blue, etc.
    A "directed" graph is defined as:  a graph in which each edge has a direction, 
        i.e., an edge flows from vertex v1 (the source) to vertex v2 (the destination)  
    Combined together, this means that one edge can go v1 -> v2,
        and another edge can go v2 -> v1,
        but you cannot have two edges going v1 -> v2 or v2 -> v1.'''
    
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        ''' initialize the graph
        In the list of edges to add, the tuples should be ordered as (source, destination). '''
        
        SimpleColorableGraph.__init__(self, vertex_nums, edges_to_add)
        DirectedGraph.__init__(self, vertex_nums, edges_to_add)    
        
    def add_vertex(self, vertex_num:int, edges_to_add:[int] = [], inColor:int = SimpleColorableGraph.UNCOLORED) -> None:
        ''' add a vertex to the graph 
        Here the edges to add will flow from the new vertex to the indicated vertices. '''
        
        DirectedGraph.add_vertex(self, vertex_num, edges_to_add)
        t = (vertex_num, inColor)
        self._vertex_colors.append(t)
            
    def remove_vertex(self, inVertex:'Vertex') -> None:
        ''' remove a vertex from the graph '''
        
        DirectedGraph.remove_vertex(self, inVertex)
        for item in self._vertex_colors:
            if item[0] == inVertex.get_num():
                self._vertex_colors.remove(item)
    
    def __str__(self) -> str:
        return "SimpleColorableDirectedGraph({num}, {vertices}, {edges})".format(
            num = self._num, 
            vertices = ["Vertex({n}, {c})".format(n = x.get_num(), c = self.get_color_by_vertex(x)) for x in self._vertices],
            edges = ["SimpleColorableDirectedEdge({n}, {v1} -> {v2})".format(n = y.get_num(), v1 = y.get_vertices()[0].get_num(), v2 = y.get_vertices()[1].get_num()) for y in self._edges])          

if __name__ == '__main__':
    
    print("######## simple graph test ########")
    
    sg = SimpleGraph([0, 1, 2], [(0,1), (1,2)])
    print(sg)
    
    sg.add_vertex(3, (0,1))
    print(sg)
    
    v1 = sg.get_vertex(2)
    v2 = sg.get_vertex(3)
    
    sg.add_edge(v1, v2)
    print(sg)
    
    e1 = sg.get_edge_by_vertexID(1, 2)
    sg.remove_edge(e1)
    print(sg)
    
    v1 = sg.get_vertex(0)
    sg.remove_vertex(v1)
    print(sg)
    
    print("######## simple, colorable graph test ########")
    
    scg = SimpleColorableGraph([0, 1, 2], [(0,1), (1,2)])
    print(scg)
    
    scg.add_vertex(3, (0,1))
    print(scg)
    
    v1 = scg.get_vertex(2)
    v2 = scg.get_vertex(3)
    
    scg.set_color_by_vertex(v1, SimpleColorableGraph.BLUE)
    scg.set_color_by_vertex(v2, SimpleColorableGraph.RED)
    scg.add_edge(v1, v2)
    print(scg)
    
    e1 = scg.get_edge_by_vertexID(1, 2)
    scg.remove_edge(e1)
    print(scg)
    
    v1 = scg.get_vertex(0)
    scg.remove_vertex(v1)
    print(scg)
    
    print("######## directed graph test ########")
    dg = DirectedGraph([0, 1, 2], [(0,1), (1,2)])
    print(dg)
    
    dg.add_vertex(3, (0,1))
    print(dg)
    
    v1 = dg.get_vertex(2)
    v2 = dg.get_vertex(3)
    
    dg.add_edge(v1, v2)
    print(dg)
    
    e1 = dg.get_edge_by_vertexID(1, 2)
    dg.remove_edge(e1)
    print(dg)
    
    v1 = dg.get_vertex(0)
    dg.remove_vertex(v1)
    print(dg)
   
    print("######## simple, colorable, directed graph test ########")
    
    scdg = SimpleColorableDirectedGraph([0, 1, 2], [(0,1), (1,2)])
    print(scdg)
    
    scdg.add_vertex(3, (0,1))
    print(scdg)
    
    v1 = scdg.get_vertex(2)
    v2 = scdg.get_vertex(3)
    
    scdg.set_color_by_vertex(v1, SimpleColorableGraph.BLUE)
    scdg.set_color_by_vertex(v2, SimpleColorableGraph.RED)
    scdg.add_edge(v1, v2)
    print(scdg)
    
    e1 = scdg.get_edge_by_vertexID(1, 2)
    scdg.remove_edge(e1)
    print(scdg)
    
    v1 = scdg.get_vertex(0)
    scdg.remove_vertex(v1)
    print(scdg)
    

