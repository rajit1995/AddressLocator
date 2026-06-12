import urllib.request, urllib.parse, urllib.error
import json
import codecs
import ssl
import app
import shutil, os
from models import *

def geocode(address) : 
        api_key = False
        # If you have a Google Places API key, enter it here
        # api_key = 'AIzaSy___IDByT70'
        # https://developers.google.com/maps/documentation/geocoding/intro

        if api_key is False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/json?'
        else :
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        address= address
            
        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
                js = None

        
        
        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            
        else :
            print(json.dumps(js, indent=4))
            print("\nThe Details Are as Follows : \n")
            lat = js['results'][0]['geometry']['location']['lat']
            lng = js['results'][0]['geometry']['location']['lng']
            print('Lattitude : ', lat, '\nLongitude : ', lng)
            location = js['results'][0]['formatted_address']
            print("Address: ",location)
            placeid = js['results'][0]['place_id']
            print("Place id: ",placeid)
            print("\n")
            tlist = [address,lat ,lng ,location,placeid]            
            print(tlist)

            
            fhand = codecs.open('where.js', 'w', "utf-8")
            fhand.write("myData = [\n")
            output = "["+str(lat)+","+str(lng)+", '"+location+"']"
            fhand.write(output)
            fhand.write("\n];\n")
            fhand.close()
            
            source = os.getcwd()
            source.replace('\\','/')
            destination = source + '/' + 'templates'
            shutil.copy('where.js',destination)
            print(source)
            print(destination)
            
            return (tlist)


        
            
            


        




