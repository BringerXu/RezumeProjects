
from vertex import Vertex

class Edge():
    ''' This class represents an edge in a graph '''

    def __init__(self, num:int, vertex1:'Vertex', vertex2:'Vertex'):
        ''' initialize the edge '''
        
        self._num = num
        self._vertices = [vertex1, vertex2]

    #Getters
    def get_num(self) -> int:
        ''' get the ID for the edge '''
        return self._num

    def get_vertices(self) -> ['Vertex']:
        ''' get the source and destination vertices for the edge '''
        return self._vertices

    #Setters
    
    #functions for printing
    def __str__(self) -> str:
        return "Edge({num}, {vertices})".format(
            num = self._num,
            vertices = self._vertices)

class DirectedEdge(Edge):
    ''' This class represents an edge in a graph '''

    def __init__(self, num:int, source:'Vertex', destination:'Vertex'):
        ''' initialize the edge '''

        Edge.__init__(self, num, source, destination)

    #Getters
    def get_num(self) -> int:
        ''' get the ID for the edge '''
        return self._num
    
    def get_source(self) -> 'Vertex':
        ''' get the source vertex for the edge '''
        return self._vertices[0]
    
    def get_destination(self) -> 'Vertex':
        ''' get the destination vertex for the edge '''
        return self._vertices[1]
    
    #functions for printing
    def __str__(self) -> str:
        return "DirectedEdge({num}, {source} -> {destination})".format(
            num = self._num,
            source = self._vertices[0],
            destination = self.vertices[1])
