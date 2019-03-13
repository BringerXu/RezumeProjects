
class Vertex():
    ''' This class represents a vertex in a graph '''

    def __init__(self, num:int):
        ''' initialize the vertex '''
        
        self._num = num
        self._edges = []

    #Getters
    def get_num(self) -> int:
        ''' get the ID for the vertex '''
        return self._num

    def get_edges(self) -> ['Edge']:
        ''' get the edges connected to this vertex '''
        return self._edges

    #Setters
    def add_edge(self, inEdge:'Edge') -> None:
        ''' add an edge to this vertex '''
        self._edges.append(inEdge)

    def remove_edge(self, inEdge:'Edge') -> None:
        ''' remove an edge from this vertex '''
        self._edges.remove(inEdge)
    
    #functions for printing
    def __str__(self) -> str:
        return "Vertex({num}, {edges})".format(
            num = self._num, 
            edges = ["Edge({n}, {v})".format(n = x.get_num(), v = x.get_vertices()) for x in self._edges])
