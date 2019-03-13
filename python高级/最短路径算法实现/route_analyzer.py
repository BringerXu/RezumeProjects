
from graph import SimpleColorableDirectedGraph
from copy import deepcopy

class RouteAnalyzer():
    ''' This is a class that helps find routes between cities.
    The basic contstructs are:
    an airport:  an airport has a name and a code, and represents an airport somewhere on Earth
            - there should only be one airport with the same airport code, though there can be multiple airports per city
    a flight:  a flight has a departure airport, an arrival airport, and a cost (i.e. the montary value for the flight)
            - there should only be one flight from airport A to airport B
    a route:  a route is a sequence of flights (e.g., Washington D.C. to Chicago, then Chicago to Los Angeles) 
    a flight map:  a flight map is a data structure holding the airports and flights '''
    
    def __init__(self):
        ''' initializes the route analyzer '''
        self._flight_map = None
        self._airport_counter = 0
        self._airports = []
        self._flights = []
    
    def get_airports(self) -> list:
        ''' get the list of airports '''
        return self._airports
    
    def get_flights(self) -> list:
        ''' get the list of flights '''
        return self._flights
    
    def get_flight_map(self) -> SimpleColorableDirectedGraph:
        return self._flight_map
    
    def add_airport(self, name:str, code:str, city:str, dirty:bool = False) -> None:
        ''' Adds an airport to the flight map.
            The name of the aiport is the official name (e.g., Los Angeles International Airport).
            The code is the airport code (e.g., LAX, SDO).
            The city is the closest major city to the airport (e.g., Los Angeles, San Diego) '''
        
        if (self._flight_map == None):
            self._flight_map = SimpleColorableDirectedGraph([self._airport_counter])
        else:
            self._flight_map.add_vertex(self._airport_counter)

        self._airports.append((name, code, city, self._airport_counter))
        self._airport_counter += 1

    def add_flight(self, departureAirportCode:str, arrivalAirportCode:str, cost:float) -> None:
        ''' Adds a flight betewen departure airport and arrival airport for the specified cost.
            Here the airports are identified by airport codes (e.g., LAX, SDO). ''' 
        
        source_vertexID = None
        destination_vertexID = None
        
        for item in self._airports:
            if item[1] == departureAirportCode:
                source_vertexID = item[3]
            if item[1] == arrivalAirportCode:
                destination_vertexID = item[3]
                
        source_vertex = self._flight_map.get_vertex(source_vertexID)
        destination_vertex = self._flight_map.get_vertex(destination_vertexID)
        
        self._flight_map.add_edge(source_vertex, destination_vertex)
        new_flight = self._flight_map.get_edge_by_vertexID(source_vertexID, destination_vertexID)
        
        self._flights.append((departureAirportCode, arrivalAirportCode, cost, new_flight.get_num()))
        
    def can_I_fly_there(self, departureAirportCode:str, arrivalAirportCode:str) -> bool:
        ''' Answers whether it is possible to fly from the departure airport to the arrival airport.
            Connections are allowed.
            Returns True if a flight is possible, False if not. '''
        
        start_vertex = None
        end_vertex = None
        return_val = False
  
        for item in self._airports:
            if item[1] == departureAirportCode:
                start_vertex = self._flight_map.get_vertex(item[3])
            if item[1] == arrivalAirportCode:
                end_vertex = self._flight_map.get_vertex(item[3])    
        
        visited_tracker = []        
        vertices_to_examine = [start_vertex]
        
        while len(vertices_to_examine) > 0:
            current_vertex = vertices_to_examine.pop(0)
            visited_tracker.append(current_vertex.get_num())
            
            for item in current_vertex.get_edges():
                if item.get_source() == current_vertex:
                    if item.get_destination().get_num() == current_vertex.get_num():
                        the_vertex = item.get_source()
                    else:
                        the_vertex = item.get_destination()                  
                    if the_vertex.get_num() == end_vertex.get_num():
                        return_val = True
                    else:
                        if the_vertex not in vertices_to_examine and the_vertex.get_num() not in visited_tracker:
                                vertices_to_examine.append(the_vertex)
            if len(vertices_to_examine) > len(self._airports)**2:
                print([i.get_num() for i in vertices_to_examine])
                raise Exception

        return return_val
    
    def what_is_the_cheapest_route(self, departureAirportCode:str, arrivalAirportCode:str) -> ([(str, str)], float):
        ''' Answers what the cheapest route is to fly from the departure airport to the arrival airport. 
            Returns the chepaest route and its cost like this:  ([(SNA, LAX), (LAX, DCA), (DCA, LAX)], 1643)
            If no route is possible, returns the following ([None, None], 999999) '''
        
        start_vertex = None
        end_vertex = None
  
        for item in self._airports:
            if item[1] == departureAirportCode:
                start_vertex = self._flight_map.get_vertex(item[3])
            if item[1] == arrivalAirportCode:
                end_vertex = self._flight_map.get_vertex(item[3])  
                
        route_tracker = []
        
        for item in self._airports:
            if item[1] == departureAirportCode:
                route_tracker.append([item[3], departureAirportCode, departureAirportCode, 0])
            else:
                route_tracker.append([item[3], item[1], 'XXXXXX', 999999]) 
            
        vertices_to_examine = [start_vertex]
        
        while len(vertices_to_examine) > 0:
            current_vertex = vertices_to_examine.pop(0)
            for r_track_entry in route_tracker:
                if r_track_entry[0] == current_vertex.get_num():
                    current_vertex_airport_code = r_track_entry[1]
                    current_vertex_previous_node = r_track_entry[2]
                    current_vertex_cumulative_cost = r_track_entry[3]
            
            for item in current_vertex.get_edges():
                if item.get_destination().get_num() == current_vertex.get_num():
                    pass
                if item.get_source().get_num() == current_vertex.get_num():
                    for r_track_entry in route_tracker:
                        if r_track_entry[0] != item.get_destination().get_num():
                            pass
                        if r_track_entry[0] == item.get_destination().get_num():
                            for f in self._flights:
                                if f[3] == item.get_num():
                                    current_edge_cost = f[2]
                            if r_track_entry[3] != 999999:
                                pass
                            if r_track_entry[3] != current_edge_cost:
                                r_track_entry[2] = current_vertex_airport_code
                                r_track_entry[3] = current_vertex_cumulative_cost + current_edge_cost
                                vertices_to_examine.append(item.get_destination())
        
        reachable = False                    
        for item in route_tracker:
            if item[1] == arrivalAirportCode:
                if item[2] == 'XXXXXX':
                    return_val = ([None, None], 999999)                  
                else:
                    reachable = True
                    total_cost = item[3]
                    total_route = self._get_route_list(route_tracker, [], item[1], departureAirportCode)  
                               
        
        if reachable:
            return_val = (total_route, total_cost)
                                   
        return return_val   
    
    def _get_route_list(self, route_tracker, route_list, airport_code, departure_airport) -> list:
        ''' reassembles route list from completed route_tracker table '''
        
        if airport_code == departure_airport:
            return route_list
        for item in route_tracker:
            if item[1] == airport_code:
                route_list = self._get_route_list(route_tracker, [(item[2], item[1])] + route_list, item[2], departure_airport)
                return route_list
        
    def terminate_flight(self, departureAirportCode:str, arrivalAirportCode:str) -> None:
        ''' terminates a flight, i.e., the flight can no longer be used. '''
        
        start_vertex = None
        end_vertex = None
  
        for item in self._airports:
            if item[1] == departureAirportCode:
                start_vertex = self._flight_map.get_vertex(item[3])
            if item[1] == arrivalAirportCode:
                end_vertex = self._flight_map.get_vertex(item[3]) 
                
        e = self._flight_map.get_edge_by_vertexID(start_vertex.get_num(), end_vertex.get_num())
        if e == None:
            return
        
        self._flight_map.remove_edge(e)
        
        for item in self._flights:
            if item[3] == e.get_num():
                self._flights.remove(item)
                break
        
    def shutdown_airport(self, airportCode:str) -> None:
        ''' shutdowns an airport, i.e., the airport can no longer be used. '''
        
        start_vertex = None

        for item in self._airports:
            if item[1] == airportCode:
                start_vertex = self._flight_map.get_vertex(item[3])


        for ed in start_vertex.get_edges():
            e = self._flight_map.get_edge_by_vertexID(ed.get_source().get_num(), ed.get_destination().get_num())
            
            for item in self._flights:
                if item[3] == e.get_num():
                    self._flights.remove(item)
            self._flight_map.remove_edge(ed)

        self._flight_map.remove_vertex(start_vertex)

        
        
        for item in self._airports:
            if item[1] == airportCode:
                self._airports.remove(item)
                break      
                
    def what_is_the_cheapest_route_with_no_dirty_airport_layovers(self, departureAirportCode:str, arrivalAirportCode:str) -> ([(str, str)], float):
        ''' Answers what the cheapest route is to fly from the departure airport to the arrival airport.
            There can be no layovers at an airport that is identified as a "dirty" airport.
            A layover is any airport visited along the route, excluding the deparature and arrival airports.
            Returns the chepaest route (excluding dirty layovers) and its cost like this:  ([(SNA, LAX), (LAX, DCA), (DCA, LAX)], 1643).
            If no route is possible, returns the following ([None, None], 999999) '''
        pass
    
    def what_is_the_route_with_the_fewest_layovers(self, departureAirportCode:str, arrivalAirportCode:str) -> ([(str, str)], float):
        ''' Answers what the route with the fewest layovers is to fly from the departure airport to the arrival airport.
            A layover is any airport visited along the route, excluding the deparature and arrival airports.
            Returns the route with the fewest layovers and its cost like this:  ([(SNA, LAX), (LAX, DCA), (DCA, LAX)], 1643).
            If no route is possible, returns the following ([None, None], 999999).
            If multiple routes satisfy these conditions (e.g., two routes share the same, minimal number of layovers), then the following criteria must be used:
                - return the route with the fewest dirty layovers, and if multiple routes satisfy that condition, then
                - return the route with the lowest cost. '''
        pass
        
        
    def __iter__(self):
        ''' iterates over the flights for the flight map '''
        
        class Flight_Map_Iterator():
            def __init__(self, f_m, f):
                self.local_f_m = deepcopy(f_m)
                self.local_f = deepcopy(f)
                self.index = 0
            
            def __next__(self):
                self.index += 1
                if (self.index >= len(self.local_f_m.get_edges())):
                    raise StopIteration
                else:
                    return self.local_f[self.index]
        
        return Flight_Map_Iterator(self._flight_map, self._flights)
        
        
    def printState(self):
        print (self._airports)
        print (self._flights)
        print (self._flight_map)
        
    def __eq__(self, in_r_a:'RouteAnalyzer') -> bool:
        ''' determines if two input route analyzers have the same set of flight and the same set of airports
            returns true if so, false otherwise '''
        
        l_airports = self.get_airports()
        l_flights = self.get_flights()
        r_airports = in_r_a.get_airports()
        r_flights = in_r_a.get_flights()
        
        same_airports = True
        for item1 in l_airports:
            airport_found = False
            for item2 in r_airports:
                if item1 == item2:
                    airport_found = True
            if not airport_found:
                same_airports = False
                
        same_flights = True
        for item1 in l_flights:
            flight_found = False
            for item2 in r_flights:
                if item1 == item2:
                    flight_found = True
            if not flight_found:
                same_flights = False
        
        if same_airports and same_flights:
            return_val = True
        else:
            return_val = False
            
        return return_val
    

if __name__ == '__main__':
    
    ra = RouteAnalyzer()
    #ra.printState()
    
    ra.add_airport("John Wayne Airport", "SNA", "Santa Ana")
    ra.add_airport("Los Angeles International Airport", "LAX", "Los Angeles")
    ra.add_airport("San Diego International Airport", "SDO", "San Diego")
    ra.add_airport("Washington Reagan National Airport", "DCA", "Washington D.C.")
    ra.add_airport("O'Hare International Airport", "ORD", "Chicago")
    ra.add_airport("Kennedy International Airport", "JFK", "New York City")
    ra.add_flight('SNA', 'LAX', 230)
    ra.add_flight('LAX', 'DCA', 1099)
    ra.add_flight('SDO', 'ORD', 950)
    ra.add_flight('DCA', 'JFK', 314)
    ra.add_flight('LAX', 'JFK', 2019)

    ca=RouteAnalyzer()
    ca.add_airport("John Wayne Airport", "SNA", "Santa Ana")
    ca.add_airport("Los Angeles International Airport", "LAX", "Los Angeles")
    ca.add_airport("San Diego International Airport", "SDO", "San Diego")
    ca.add_airport("Washington Reagan National Airport", "DCA", "Washington D.C.")
    ca.add_airport("O'Hare International Airport", "ORD", "Chicago")
    ca.add_airport("Kennedy International Airport", "JFK", "New York City")
    ca.add_flight('SNA', 'LAX', 230)
    ca.add_flight('LAX', 'DCA', 1099)
    ca.add_flight('SDO', 'ORD', 950)
    ca.add_flight('DCA', 'JFK', 314)
    ca.add_flight('LAX', 'JFK', 2019)
    #ra.printState()
    print(ra.get_airports())
    print(ra.get_flights())

    print(ra==ca)



    


