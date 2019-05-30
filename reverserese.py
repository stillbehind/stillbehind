import requests
import os

os.system("reset")


print " R E V E R S E R E S E   I P "
print "--------------------------------"
print"\r" 
domain=raw_input("Masukkan domain :")
req=requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(domain))
os.system("reset")
print(req.text)
