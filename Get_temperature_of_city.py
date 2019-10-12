import socket
import requests
try:
	city = input("Enter city name: ")
	socket.create_connection(("www.google.com", 80))
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	print(res1)
	
	j1 = res1.json()
	print(j1)

	d1 = j1['main']
	print(d1)
	temp = d1['temp']
	print("Temp : ", temp)
except OSError:
	print("Check network")
