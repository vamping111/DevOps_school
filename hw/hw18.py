#!/usr/bin/env python3
from PIL import Image

img = Image.open('./maps.jpg')
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
resized_img = img.resize((width, height), Image.ANTIALIAS)
resized_img.save('./maps_new.jpg')
