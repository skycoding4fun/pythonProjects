import json
import requests
import pprint

base_url = "https://api.skydio.com/api"
url_flight = base_url + "/v0/flights"

#BNSF_token = '47d490f64e343f5c5e476969fc2cd2df2d8bb4d17ea43e326159a9ff2ecce00c'
#Mo_token = '83cf16c6f59af79b04b0fae2ad79bc1e02d1712e920bcc06b1c1ec2261f7c0c9'

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': '47d490f64e343f5c5e476969fc2cd2df2d8bb4d17ea43e326159a9ff2ecce00c'
}
print(url_flight)
flights_response = requests.request("GET", url_flight, headers=headers, data=payload)

flights_dict = json.loads(flights_response.text)

flights_data = flights_dict["data"]
print(flights_data)
flights = flights_data["flights"]
print(flights)
print(flights[0]['flight_id'])
flights_id_list=[]
flight_current_page = flights_data["pagination"]["current_page"]
flight_
# Getting Flight IDs in a list #
id = 0
for flight in flights:
  flights_id_list += [flights[id]['flight_id']]
  id+=1

print(flights_id_list)

# Building URLs for the Telemetry #

x = 0
flight_tel_url_list = []
flight_tel_url = []
for flight in flights_id_list:
  flight_tel_url = base_url + "/v0/flight/" f"{flights_id_list[x]}" + "/telemetry"
  flight_tel_url_list += [flight_tel_url]

print (flight_tel_url_list)
print(len(flight_tel_url_list))
# Building URLs for the Telemetry #
