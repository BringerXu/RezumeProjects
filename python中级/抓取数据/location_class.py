# Zhengyi xu 68996560
'''
This module created for building up a Route class(son class: STEP,TOTALDISTANCE,TOTALTIME,LATLONGS) and a ELEVATION class
because they use different api, I seperate them into two parts
'''
#import re

class NOROUTEFOUND(Exception): # Api return wrong route(from api errorCode in json file), raise
    pass

class Route: # parent class, inherit step, json to son class
    def __init__(self,step,json):
        self._step = step
        self._json = json
        self.errorCode() # check whether whether route is correct before son class run

    def errorCode(self):
        if self._json['route']['routeError']['errorCode']==-400:
            pass
        else:
            raise NOROUTEFOUND # raise exception, when get error code
        
        
class STEP(Route): # son class STEP
    def show(self): # show method in STEP class
        print('STEP')
        for leg in range(self._step-1):
            for num in range(len(self._json['route']['legs'][leg]['maneuvers'])):
                print(self._json['route']['legs'][leg]['maneuvers'][num]['narrative'])



class TOTALDISTANCE(Route): # son class TOTALDISTANCE
    def show(self): # show method in TOTALDISTANCE class
        print('TOTAL DISTANCE')
        print(str(int(round(self._json['route']['distance'])))+' miles')

class TOTALTIME(Route): # son class TOTALTIME
    def show(self): # show method in TOTALTIME class
        minute=(int(round(self._json['route']['time']/60)))
        print('TOTAL TIME: {} minutes'.format(minute))


class LATLONGS(Route): # son class LATLONGS
    def latlong(self): #store list of dicts(latlng) for elevation call 
        latlong=[]
        for location in range(self._step):
            latlong.append(self._json['route']['locations'][location]['latLng'])
        return latlong

    def show(self): # show method in LATLONGS class
        print('LATLONGS')
        for location in range(self._step):
            if self._json['route']['locations'][location]['latLng']['lat']>=0:
                print('{:.2f}N'.format(self._json['route']['locations'][location]['latLng']['lat']), end=' ')

                if self._json['route']['locations'][location]['latLng']['lng']>=0:
                    print('{:.2f}E'.format(self._json['route']['locations'][location]['latLng']['lng']))
                elif self._json['route']['locations'][location]['latLng']['lng']<0:
                    print('{:.2f}W'.format(abs(self._json['route']['locations'][location]['latLng']['lng'])))

            elif self._json['route']['locations'][location]['latLng']['lat']<0:
                print('{:.2f}S'.format(abs(self._json['route']['locations'][location]['latLng']['lat'])), end=' ')

                if self._json['route']['locations'][location]['latLng']['lng']>=0:
                    print('{:.2f}E'.format(self._json['route']['locations'][location]['latLng']['lng']))
                elif self._json['route']['locations'][location]['latLng']['lng']<0:
                    print('{:.2f}W'.format(abs(self._json['route']['locations'][location]['latLng']['lng'])))

class ELEVATION: # parent class ELEVATION
    def __init__(self,json): # build up attribute needed
        self._json = json

    def show(self): # use attribute print elevation data
        for item in self._json['elevationProfile']:
            print(int(round(item['height']*3.2808399)))

