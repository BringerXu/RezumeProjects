# Zhengyi xu 68996560
import location_class
import url_request

'''
I make input must valid because when I test this program, I will make mistake sometimes 
so I can input as any times as I can until I enter correct number and valid input  
'''

CONTENT=['STEPS','TOTALTIME','TOTALDISTANCE','LATLONG','ELEVATION']

class InvalidInputError(Exception):
    pass

def locationNUM_input():
    '''
    limit valid input location number
    '''
    while True:
        try:
            STEP=int(input('Please enter your positions number: '))
            if STEP<2:
                raise InvalidInputError
        except ValueError:
            print('Your input STEP is not a integer')
        except InvalidInputError:
            print('Your input STEP is invalid')
        except:
            print('Unexpected Error')
        else:
            return STEP

def LOCATION_input(step:int):
    '''
    valid location input
    limited location number given integer
    '''
    ALL_LOCATION=[]
    for times in range(step):
        while True:
            try:
                LOCATION=input('Please enter your locations: ').strip()
            except:
                print('Unexpected Error')
            else:
                ALL_LOCATION.append(LOCATION)
                break
    return ALL_LOCATION

def _REPRESENT_number():
    '''
    valid represent num input
    '''
    try:
        command=int(input('How many kinds of information you want to see, 1-5: '))
        if command>5 or command<1:
            raise InvalidInputError
    except ValueError:
        print('Your must enter a integer')
    except InvalidInputError:
        print('Input integer must range from 1 to 5')
    except:
        print('Unexpected Error')
    else:
        return command

def _checkvalid(element:str):
    '''
    check whether input represent element input is valid(in the CONTENT)
    '''
    for valid_element in CONTENT:
        if element==valid_element:
            return True
    return False

def REPRESENT_element():
    '''
    valid REPRESENT_elements input
    '''
    elements_list=[]
    element_num=_REPRESENT_number()
    for num in range(element_num):
        while True:
            try:
                element=input()
                if _checkvalid(element)==False:
                    raise InvalidInputError
            except InvalidInputError:
                print('Your input represent element is invalid')
            except:
                print('Unexpected Error')
            else:
                elements_list.append(element)
                break
    return elements_list

def main():
    '''
    input valid location num
    input valid locations
    request json data
    input valid represent parameters(basing on CONTENT)
    build up parent class(check routeError automatically)

    basing on represent parameter call some classes
    show solutions
    '''
    while True:
        try:
            step=locationNUM_input() # input location num
            locations=LOCATION_input(step) # input location num
        except:
            print('Unexpected Error')
        else: 
            present_list=REPRESENT_element() # input represent parameters

            try: # check request json data
                ROUTE_json=url_request.search_ROUTE(locations) # store json data
            except url_request.MAPQUESTERROR: # if request fail print M.*?R
                print('MAPQUEST ERROR')
            else:

                try:
                    search_object=location_class.Route(step,ROUTE_json) # check ROUTE exist
                except location_class.NOROUTEFOUND:
                    print('NO ROUTE FOUND')
                else: # call classes basing on represent parameters 
                    for item in present_list:
                        print('') # line for formation

                        if item=='STEPS':
                            location_class.STEP(step,ROUTE_json).show()

                        elif item=='TOTALTIME':
                            location_class.TOTALTIME(step,ROUTE_json).show()

                        elif item=='TOTALDISTANCE':
                            location_class.TOTALDISTANCE(step,ROUTE_json).show()

                        elif item=='LATLONG':
                            location_class.LATLONGS(step,ROUTE_json).show()

                        elif item=='ELEVATION': 
                            print(item+'S') # line for formation
                            elev=location_class.LATLONGS(step,ROUTE_json).latlong() # using LATLONGS method return a list of dicts
                            for item in elev: # using single point latlng to request elevation because if those points are far away with each other we cannot get elevation
                                try: # check in case of some unexpected error
                                    ELEV_json=url_request.search_ELEV(item)
                                except url_request.MAPQUESTERROR:
                                    print('MAPQUEST ERROR')
                                except:
                                    print('Unexpected Error')
                                else:
                                    location_class.ELEVATION(ELEV_json).show()

                    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors') # line for formation

if __name__ == '__main__':
    main()
    
