#!/usr/bin/env python3
from GPSPhoto import gpsphoto
data=gpsphoto.getGPSData('/home/linar/DevOps_school/hw/maps.jpg')
total=(str(data['Latitude'])+','+str(data['Longitude']))
with open('./hw17_prop_photo.txt','w') as of:
	of.write(total)
