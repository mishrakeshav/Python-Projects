import socket
import requests

try:
	socket.create_connection(("www.google.com", 80))
	print("Connected")
	res = requests.get("https://ipinfo.io")
	print(res)
	j1 = res.json()
	print(j1)
	city = j1['city']
	print(city)

	la, lo = j1['loc'].split(',')
	print("Latitude: ",la)
	print("Longitude: ",lo)
except OSError as e:
	print("Issue: ", e)
