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
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 c:  Change prices the dishes served
 1: Search for (and display) all the restaurants that serve
     a specified cuisine along with the average price of (all
     the menus of the restaurants that serve) that cuisine
 2: Search for (and display) all the restaurants that serve
     a dish whose name contains a given word or phrase
 q:  Quit
"""

def handle_commands(C: list) -> list:
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
            print("Average prices:  $"+str(average_price(C))+".  "+"Average calories:  "+str(average_calories(C)))
        elif response=='c':
            n=float(input('Please enter an amount representing a percentage change:  '))
            C=Collection_change_prices(C,n)
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='1':
            n=input("Please enter the cuisine of the restaurant to search for:  ")
            for r in Collection_search_by_cuisine(C, n):
                print(Restaurant_str(r))
            print(average_price(Collection_search_by_cuisine(C, n)))
        elif response=='2':
            n=input("Please enter the dish of the restaurant to search for:  ")
            for r in Collection_search_by_dish(C, n):
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
   
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
        "Menu:     " + Menu_str(self.menu) +"\n\n")
    

def Restaurant_get_info() -> Restaurant:
    
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())

def Restaurant_change_prices(r:Restaurant,n:float)->Restaurant:
    r=r._replace(menu=Menu_change_prices(r.menu,n))
    return r

    


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
    r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])
    r3=Restaurant('Pascal','French','940-752-0107',[Dish('escargots',12.95,250),
                                                Dish('poached salmon',18.50,550),
                                                Dish('rack of lamb',24.00,850),
                                                Dish('marjolaine',8.50,950)])




    return [r1,r2,r3]

def Collection_str(C: list) -> str:
    
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
   
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]


def Collection_search_by_cuisine(C: list, cuisine: str) -> list:
    
    result = [ ]
    for r in C:
        if r.cuisine == cuisine:
            result.append(r)
    return result
def Collection_search_by_dish(C: list, dish: str) -> list:
    
    result = [ ]
    for r in C:
        for m in r.menu:
            if dish in m.name:
                result.append(r)
                break
    return result
def Collection_add(C: list, R: Restaurant) -> list:
    
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

def Collection_change_prices(l:list,n:float)->list:
    for i in range(len(l)):
        l[i]=Restaurant_change_prices(l[i],n)
    return l




#Dish
Dish=namedtuple('Dish','name price calories')
def Dish_str(d:Dish)->str:
    return d.name+' ($'+str(d.price)+'): '+str(d.calories)+' cal'+'\n'    

def Dish_get_info() -> Dish:
    
    return Dish(
        input("Please enter the Dish's name:  "),
        float(input("Please enter the Dish's price:  ")),
        float(input("Please enter the Dish's calories:  ")))

def Dish_change_price(r:Dish,n:float)->Dish:
    r=r._replace(price=r.price+r.price*n*0.01)
    return r




#Menu
def Menu_enter()->list:
    l=[]
    while True:
        response=input('Do you want to add a Dish? ')
        
        if response=='yes':
            
            l.append(Dish_get_info())
            
        elif response=='no':
            return l

def Menu_str(m: list) -> str:
    
    s = ""
    for r in m:
        s = s + Dish_str(r)
    return s            
            
def Menu_change_prices(m:list,n:float)->list:
    for i in range(len(m)):
        m[i]=Dish_change_price(m[i],n)
    return m    

#average
def average_price(l:list)->float:
    sum=0
    n=0
    for i in l:
        for m in i.menu:
            sum+=m.price
            n=n+1
    return sum/n


def average_calories(l:list)->float:
    sum=0
    n=0
    for i in l:
        for m in i.menu:
            sum+=m.calories
            n=n+1
    return sum/n

        
    








































restaurants()




