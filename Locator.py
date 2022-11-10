import phonenumbers
from phonenumbers import geocoder
number = input("Enter your number :")
x = phonenumbers.parse(number)

location = geocoder.description_for_number(x,"en")
print(location)

from phonenumbers import carrier

print(carrier.name_for_number(x,"en"))
###################################################

import opencage
from opencage.geocoder import OpenCageGeocode

key = '0a2bb97ed6f5443c8185ff2692bae869'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

#############################################
import folium

myMap = folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=location).add_to((myMap))

##save map in html file

myMap.save("locator.html")