import pyqrcode
import png
from pyqrcode import QRCode

print ("Copyright (c) 2023 //// Faouzi HAMRI //// All rights reserved.")
Link = input("please put the link : ")
url = pyqrcode.create(Link)
url.png (input("put the name : ")+".png", scale=input("put the scale (integer) : "))