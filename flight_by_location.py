import requests
import pprint
import json
from geopy.geocoders import Nominatim

base_url = "https://api.skydio.com/api"
get_flights = base_url + "/v0/flights"
#BNSF: 634c7cc9ff49f2081494190ab83669c738eaea792106972f0ef51b66a3302ebc
#Mo: 54a610a1cd9cedb4f157ee22e1e9b79c80a64ce9ee61dcba6da1a7133b2b186a
payload={}
headers={
    'accept': 'application/json',
    'Authorization' : '634c7cc9ff49f2081494190ab83669c738eaea792106972f0ef51b66a3302ebc'
}
################### Getting flights in a dict  ####
flights = requests.request('GET', get_flights, headers=headers, data=payload)
print(flights.text)
data = flights.text
parse_data = json.loads(data)
flights_dict=(parse_data['data'])
print(flights_dict)
flights_list = flights_dict['flights']
print(flights_list)

################### Getting flights with telemetry data in a list  ####
flight_id_list = []

i = 0
for flight_id in range(len(flights_list)):
    if flights_list[i]['has_telemetry'] == True:
        flight_id_list += [flights_list[i]['flight_id']]
    i+=1

print(flight_id_list)

################### Building URLs for flight telemetry  #####

flight_tel_url_list = []

id = 0
for id in range(len(flight_id_list)):
    flight_tel_url_list += [base_url + "/v0/flight/" + f"{flight_id_list[id]}" + "/telemetry"]
    id += 1

print(flight_tel_url_list)
print(len(flight_tel_url_list))

################### Iterating through URLs that have flight telemetry  #####

#url = 0
#for url in range(len(flight_tel_url_list)):
    #flight_tel = requests.request('GET', flight_tel_url_list[url], headers=headers, data=payload)
    #url += 1

################### Getting GPS coordinates  #####
print(flight_tel_url_list[2])
#flight_tel_test = requests.request('GET', flight_tel_url_list[0], headers=headers, data=payload)
#print(flight_tel_test.text)


#flight_telemetry = requests.request('GET', flight_telemetry_url, headers=headers, data=payload)
#pprint.pprint(flight_telemetry.text)
#print(flights_list)
#pprint.pprint(flights_json)

#json_object = json.loads(flights_json)
#print(json_object)


#geolocator = Nominatim(user_agent="location_tracker")
#location = geolocator.reverse("1.2130000591278076,1.2130000591278076")
#print(location.address)