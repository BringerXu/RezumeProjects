#Shawn Li 88405009 Zhengyi Xu 68996560 Lab 7 assignment 6

#RESTAURANT COLLECTION PROGRAM

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
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
 sa: search for all the restaurants serve a specified cuisine with average price of that cuisine
 wp: search for all the restaurants with dish including a word or phrase
 q:  Quit
->"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='e':
            C = Collection_remove_all(C)
        elif response=='c':
            n = float(input("Please enter the amount of percentage you want to change in price: "))
            C = Collection_change_prices(C,n)
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='sa':
            n = input("Please enter the name of the cuisine to search for:  ")
            print(Collection_search_by_cuisine(C, n))
            print(Average_price(C,n))
        elif response=='wp':
            n = input("Please enter the word of the dish to search for:  ")
            print(Collection_search_by_dish(C,n))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish', 'name price cal')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Average_price(C:list,n:str)->str:
    '''return a string of that Cuisine'''
    x=0
    y=0
    for i in range(len(C)):
        if C[i].cuisine==n:
            for n in range(len(C[i].menu)):
                y=y+1
                x=x+C[i].menu[n][1]
    return x/y
                
                
    return("Average price:  ${:5.2f}.".format(x))

def Restaurant_str(self: Restaurant) -> str:
    '''Return a string of that Restaurant'''
    return (
        "\n"+"Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        str(self.menu)+"\n"+
        "Average price:  ${:5.2f}.  Average calories:  {:5.1f}".format(average_price(self.menu),average_cal(self.menu)))

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter([]))


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C:list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_cuisine(C:list,n:str)->list:
    """Return list of Restaurants in input list whose cuisine matches input string.
    """
    result=[]
    for i in range(len(C)):
        if C[i].cuisine==n:
            result.append(C[i].name)
    return result

def Collection_search_by_dish(C:list,n:str)->list:
    result=[]
    for i in range(len(C)):
        for r in range(len(C[i].menu)):
            if n in C[i].menu[r].name:
                result.append(C[i])
    return result
            
def Collection_search_by_name(C:list, n: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == n:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C:list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C:list, n: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != n:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]
def Collection_remove_all(C:list)->list:
    '''Return list'''
    result=[]
    return result
def Collection_change_prices(C:list,n:float)->list:
    '''Return list with its new price'''
    result = []
    for i in range(len(C)):
        C[i]=Restaurant(C[i].name,C[i].cuisine,C[i].phone,change_one_price(C[i].menu,n))
        result.append(C[i])
    return result

def change_one_price(m:list,n:float) -> list:
    '''Return new price of that dish'''
    result_=[]
    for w in range(len(m)):
        result_.append(m[w]._replace(price=m[w].price*(1+n/100)))
    return result
####Dish
def average_price(D:list)->float:
    a=0
    for i in range(len(D)):
        a=a+D[i].price
    return a/len(D)
def average_cal(D:list)->float:
    b=0
    for i in range(len(D)):
        b=b+D[i].cal
    return b/len(D)
def Dish_str(x: Dish ) -> str:
    '''Takes a Dish and returns a string'''
    return (
        "Name:     " + x.name + "\n" +
        "Price:    ${:2.2f}".format(x.price)+"\n"+
        "Calories:   {:6.1f}".format(x.cal))

def Dish_get_info() -> Dish:
    ''' Prompt user for fields of Dish; create and return.
    '''
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter the calories of that dish: ")))

####Menus
def Menu_enter(D:Dish)->list:
    '''Create a list of a Restaurant by adding dishes'''
    while True:
        x=input('Do you want to add a Dish?')
        if x=='Yes':
            l = Dish_get_info()
            D = Collection_adddish(D, l)
        elif x=='No':
            return D
        else:
            invalid_command(x)

def invalid_command(x):
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + x + "' isn't a valid command.  Please try again.")

def Collection_adddish(D: list, l:Dish) -> list:
    """ Return list of dish with input Dish added at end.
    """
    D.append(l)
    return D

def Collection_strdish(D:Dish) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for l in D:
        s = s + Dish_str(l)
    return s


restaurants()
