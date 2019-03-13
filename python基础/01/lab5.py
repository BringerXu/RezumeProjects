#Zhengyi Xu 68996560 and Eric Nguyen ICS 31 Lab sec 7.  Lab asst 5.
def s(a):
	print("---------------c.",a,"---------------")
def e(a):
	print("---------------e.",a,"---------------")
#c
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

#c1
s(1)
d1 = Dish('John',4.5,250)
d2 = Dish('Jack',6.0,260)
d3 = Dish('InAndOut',8.5,350)
d4 = Dish('InAndOut',24.5,350)

#c2
s(2)
def Dish_str(Dish:namedtuple)->str:
	'''
    return d.name + '($' + str(d.price) + '):' + str(d.calories) + 'cal'
    '''
	return "{} (${}): {} cal".format(Dish.name, Dish.price, Dish.calories)
assert Dish_str(d1)=='John ($4.5): 250 cal'
assert Dish_str(d2)=='Jack ($6.0): 260 cal'
assert Dish_str(d3)=='InAndOut ($8.5): 350 cal'

#c3
s(3)
def Dish_same(d1: Dish, d2: Dish) -> bool:
	'''
	given 2 dishes and return bool of their 
	'''
	return d1.name == d2.name and d1.calories == d2.calories
assert not Dish_same(d1,d2)
assert Dish_same(d3,d4)

#c4
s(4)
def Dish_change_price(d: namedtuple, n: int) -> namedtuple:
	'''
	given a namedtuple and int, return a namedtuple whose price have changed n percentage
	'''
	d=d._replace(price = d.price * (1 + (n / 100)))
	return d
assert Dish_change_price(d1,50)==Dish('John',6.75,250)

#c5
s(5)
def Dish_is_cheap(Dish:namedtuple,N:float)->bool:
	'''
	return whether the Dish.price <N
	'''
	if Dish.price < N:
		return True
assert Dish_is_cheap(d1,4.0)==None
assert Dish_is_cheap(d1,6.0)==True

#c6
DL=[Dish('John',4.5,250),
Dish('Jack',6.0,260),
Dish('InAndOut',8.5,350),
Dish('Which wich',12.5,400),
Dish('IntheBox',3.5,180)]

DL2=[Dish('Jesse',15,800),
Dish('Gogi',17.5,430),
Dish('Xuan',24,380),
Dish('Cate',14,260)]
DL3=[]
DL3.extend(DL)
DL3.extend(DL2)
s(6)
def Dishlist_display(D:list)->None:
	'''
	Display List every line
	'''
	for d in D:
		print (str(d)+"\n")
#c.7
s(7)
def Dishlist_all_cheap(D:list,N:float)->bool:
	'''
	compare every price in the big namedtuples and return bool
	'''
	for d in D:
		return Dish_is_cheap(d,N)
assert Dishlist_all_cheap(DL,4.0)==None
assert Dishlist_all_cheap(DL,12.6)==True
#c.8
s(8)
def Dishlist_change_price(D:list,N:float)->list:
	'''
	return new list which have been changed prices
	'''
	result=[]
	for d in D:
		d = d._replace(price=d.price*N/100)
		result.append(d)
	return result
assert Dishlist_change_price(DL,50)==[Dish('John',2.25,250),
Dish('Jack',3.0,260),
Dish('InAndOut',4.25,350),
Dish('Which wich',6.25,400),
Dish('IntheBox',1.75,180)]
#c.9
s(9)	
def Dishlist_price(D:list)->list:
	'''
	return new list including price from namedtuple in the old list
	'''
	ND=[]
	for d in D:
		ND.append(d.price)
	return ND
assert Dishlist_price(DL)==[4.5,6.0,8.5,12.5,3.5]
#c.10	
s(10)	
def Dishlist_average(D:list)->float:
	'''
	sum all price in the new list geting from last function and then calculate their average price
	'''
	a = 0
	for p in Dishlist_price(D):
		a=a+p
	return a/len(D)
assert Dishlist_average(DL)==(4.5+6.0+8.5+12.5+3.5)/5
#c.11
s(11)
def Dishlist_keep_cheap(D:list,N:float)->list:
	'''
	if the average price of list < N keep them in the new list
	'''
	ND=[]
	for d in D:
		if d.price<N:
			ND.append(d)
	return ND
assert Dishlist_keep_cheap(DL,13.0)==[Dish('John',4.5,250),
Dish('Jack',6.0,260),
Dish('InAndOut',8.5,350),
Dish('Which wich',12.5,400),
Dish('IntheBox',3.5,180)]
assert Dishlist_keep_cheap(DL,5)==[Dish('John',4.5,250),Dish('IntheBox',3.5,180)]
#c.12
s(12)
DL4=[Dish('John',4.5,250),
Dish('Jack',6.0,260),
Dish('InAndOut',8.5,350),
Dish('Which wich',12.5,400),
Dish('IntheBox',3.5,180),
Dish('Jesse',15,800),
Dish('Gogi',17.5,430),
Dish('Xuan',24,380),
Dish('Cate',14,260),
Dish('Craft',48,239),
Dish('Chipotle',16.99,248),
Dish('Johnny',8.99,130),
Dish('Jane',6.9,530),
Dish('HamburgerKing',13.5,550),
Dish('Which',11.99,220),
Dish('BoxChicken',7.9,290),
Dish('Jessie',15.9,770),
Dish('Geoge',33.5,980),
Dish('Guotie',29.99,390),
Dish('CatKing',7.98,99),
Dish('Starfish',27.9,749),
Dish('Slapfish',21.99,339),
Dish('Creepy',2.59,59),
Dish('Yougurt',13.69,419),
Dish('FishPan',29.99,990)]
def before_and_after()->None:
	'''
	first show the previous list and then changed price in that list and the show this new list
	'''
	print('Percentage change', end=' ')
	a=float(input())
	print(Dishlist_display(DL4))
	Dishlist_change_price(DL4,a)
	print(Dishlist_display(Dishlist_change_price(DL4,a)))
before_and_after()

#e
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

#e1
e(1)
r3 = Restaurant('Pascal', 'French', '940-752-0107', [
    Dish('escargots', 12.95, 250),
    Dish('poached salmon', 18.50, 550),
    Dish('marjolaine cake', 8.50, 950)])

#e2
e(2)
def Restaurant_first_dish_name(r: Restaurant) -> str:
	'''
	return Restaurant first dish name
	'''
	return r.menu[0].name
assert Restaurant_first_dish_name(r1) == 'Mee Krob'

#e3
e(3)
def Restaurant_is_cheap(r: Restaurant, n: float) -> bool:
	'''
	if average price of this namedtuple < N return True If not return False
	'''
	return Dishlist_average(r.menu) <= n
assert Restaurant_is_cheap(r1, 11.75) == True

#e4
e(4)
RC = [r1, r2, r3]
def Collection_raise_price(C: list, p: float) -> list:
	'''
	return new list including namedtuple which have raised prices
	'''
	result = []
	for r in C:
		result.append(Restaurant_raise_price(r, p))
	return result

def Restaurant_raise_price(r: Restaurant, p: float) -> Restaurant:
	'''
	return a namedtuple including raised prices
	'''
	return Menu_raise_price(r.menu, p)

def Menu_raise_price(m: list, p: float) -> list:
	'''
	return a list incluindg menu namedtuple which have raised prices
	'''
	result = []
	for d in m:
		result.append(Dish_raise_price(d, p))
	return result

def Dish_raise_price(d: Dish, p: float) -> Dish:
	'''
	return raised price in Dish namedtuple
	'''
	return d._replace(price = d.price + p)

def Collection_change_price(C: list, p: int) -> list:
	'''
	return new list including restaurant namedtuples which have raised prices 
	'''
	result = []
	for r in C:
		result.append(Restaurant_change_price(r, p))
	return result

def Restaurant_change_price(r: Restaurant, p: int) -> Restaurant:
	'''
	return Restaurant namedtuples which raised price in the menu in the Dish
	'''
	return Menu_change_price(r.menu, p)

def Menu_change_price(m: list, p: int) -> list:
	'''
	return list incluindg changed price in the menu
	'''
	result = [ ]
	for d in m:
		result.append(Dish_change_price(d, p))
	return result

#e5
e(5)
def Collection_select_cheap(C: list, p: float) -> list:
	'''
	return new list including those restaurant whose average price is cheaper than p
	'''
	result = []
	for r in C:
		if Restaurant_is_cheap(r, p):
			result.append(r)
	return result
assert Collection_select_cheap(RC, 10.0) == []
assert Collection_select_cheap(RC, 20.0) == [r1, r3]

#g
print('---------------g---------------')
Count=namedtuple('Count','letter number')
def countl(Ob:str,i:str)->namedtuple:
	'''
	return Count namedtuple showing how many specific n in the Ob
	'''
	Ob.count(i)
	return Count(i,Ob.count(i))
def letter_count(Ob:str,letter:str)->list:
	'''
	return new list including all seperated part in letter using countl
	'''
	list=[]
	for i in letter:
		list.append(countl(Ob,i))
	return list
assert letter_count('The cabbage has baggage', 'abcd')==[Count(letter='a',number=5), Count(letter='b',number=3), Count(letter='c',number=1), Count(letter='d',number=0)]