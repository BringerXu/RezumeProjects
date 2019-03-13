# Zhengyi xu 68996560
import json
import urllib.parse
import urllib.request
API_key='49xaGKWAXWNQGG3SGiHc1G59Ey45rLBt'
RouteQuest='http://open.mapquestapi.com/directions/v2'
ElevationQuest='http://open.mapquestapi.com/elevation/v1'

'''
This module is for send request to web api and return data in json formation
'''

#locations example
#http://open.mapquestapi.com/directions/v2/route?key=49xaGKWAXWNQGG3SGiHc1G59Ey45rLBt&from=Irvine%2CCA&to=4533%20Campus%20Dr%2C%20Irvine%2C%20CA&to=Los+Angeles%2CCA&to=4533%20Campus%20Dr%2C%20Irvine%2C%20CA&to=Los+Angeles%2CCA
#Irvine,CA
#Los Angeles,CA
#4533 Campus Dr, Irvine, CA

#object function:
#:MapQuest
#STEP
#TOTALDISTANCE
#TOTALTIME
#LATLONG

#ELEVATION:ElevationQuest

class MAPQUESTERROR(Exception): # cannot request data from mapquest api, raise this Exception
    pass

def _formmat_locations(LOCATIONS:list):
    '''
    transfer input location into url formation
    '''
    result=[('key',API_key),('from',LOCATIONS[0])]
    for item in LOCATIONS[1:]:
        result.append(('to',item))
    elements=urllib.parse.urlencode(result)
    return elements

def search_ROUTE(LOCATIONS:list):
    '''
    request route json data given location list
    '''
    try:                                            # check request data process
        request=_formmat_locations(LOCATIONS)

        full_request=RouteQuest+'/route?'+request
        
        response=urllib.request.urlopen(full_request)

    except:                                     #  raise, if request data fail
        raise MAPQUESTERROR

    else:                                        # chenge data into dict formation using json module and return it
        json_text=response.read().decode(encoding='utf-8')
    
        content=json.loads(json_text)

        return content

#profile?key=49xaGKWAXWNQGG3SGiHc1G59Ey45rLBt&latLngCollection=39.74012,-104.9849,39.7995,-105.7237,39.6404,-106.3736
def search_ELEV(LATLONG:dict):
    '''
    request elevation json data given single point latlong dict
    '''
    try:                                                                                         # check request data process
        format_LATLONG=str(LATLONG['lat'])+','+str(LATLONG['lng'])

        format_request='key=49xaGKWAXWNQGG3SGiHc1G59Ey45rLBt&latLngCollection='+format_LATLONG

        full_request=ElevationQuest+'/profile?'+format_request

        response=urllib.request.urlopen(full_request)

    except:                                                                                  # raise, if request data fail
            raise MAPQUESTERROR

    else:                                                                                     # chenge data into dict formation using json module and return it

        json_text=response.read().decode(encoding='utf-8')

        content=json.loads(json_text)

        return content