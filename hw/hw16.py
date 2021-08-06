#!/usr/bin/env python3

from geopy import GoogleV3

point=open("./hw16.txt","r")
location = GoogleV3(api_key="AIzaSyAOVTj38NidnPmLrnDU3bVzOd6FPenRATM", domain="maps.google.ru").reverse(point)

print(location.address)
print(location.latitude, location.longitude)
print("Google Maps URL: https://maps.google.com?saddr=Current+Location&daddr="+str(location.latitude)+","+str(location.longitude))
