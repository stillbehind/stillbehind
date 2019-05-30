import os
import json
import urllib2
os.system("reset")

print " ===== IP TRACK ==== "
print "\r"


while True:

		ip1=raw_input("Masukkan IP atau web, jika web tanpa https : ")
		url = "http://ip-api.com/json/"
		response = urllib2.urlopen(url + ip1)
		data = response.read()
		values = json.loads(data)
		os.system("reset")

		print " ------------- IP TRACK  ------------- "
		print " ------------------------------------- "
		print "\r"

		print ("IP 		: " + values ['query'])
		print ("NEGARA 		: " + values ['country'])
		print ("ISP 		: " + values ['isp'])
		print ("KOTA 		: " + values ['regionName'])
		print ("ZONA WAKTU 	: " + values ['timezone'])
		print ("LATITUDE 	: " + str (values['lat']))
		print ("LONGITUDE 	: " + str (values['lon']))
		print ("NAMA PERUSAHAAN : " + values ['as'])
		print "\n"

		break

