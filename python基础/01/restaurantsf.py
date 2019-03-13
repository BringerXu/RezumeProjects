#Zhengyi Xu 68996560 and Eric Nguyen ICS 31 Lab sec 7.  Lab asst 5.
__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 c:  Change prices for the dishes served
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='c':
            n = float(input("Please enter the percentage of the change in prices:  "))
            C = Collection_change_price(C, n)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:\n" + Menu_str(self.menu) + "\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())

def Restaurant_change_price(r: Restaurant, n: float) -> Restaurant:
    return r._replace(menu = Menu_change_price(r.menu, n))

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

def Collection_change_price(C: list, n: float) -> list:
    result = [ ]
    for r in C:
        result.append(Restaurant_change_price(r, n))
    return result

###Dish
Dish = namedtuple('Dish', 'name price calories')
def Dish_str(self: Dish) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n" +
        "Calories:    {:2.2f}".format(self.calories) +"  cal\n\n")

def Dish_get_info() -> Dish:
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter the calories of that dish:  ")))

def Dish_change_price(d: Dish, n: float) -> Dish:
    return d._replace(price = d.price * (1 + n / 100))

###Menu
def Menu_enter() -> list:
    print("Please enter the menu of the restaurant below:  ")
    M = []
    while True:
        add = input("Do you want to add a new dish to the menu?(Please answer by 'Yes' or 'No')")
        if add == "Yes":
            M.append(Dish_get_info())
        if add == "No":
            print("That is the end of the menu.")
            return M
        
def Menu_str(M: list) -> str:
    result = ''
    for d in M:
        result += Dish_str(d)
    return result

def Menu_change_price(M: list, n: float) -> list:
    result = [ ]
    for r in M:
        result.append(Dish_change_price(r, n))
    return result

restaurants()

