import requests
import pprint
import json
#from geopy.geocoders import Nominatim

base_url = "https://api.skydio.com/api"
get_flights = base_url + "/v0/flights"
#BNSF: c7cf702d2e7375e75b61738d3406429fee95df21f5b25263f23ee243627f7755
#Mo: 54a610a1cd9cedb4f157ee22e1e9b79c80a64ce9ee61dcba6da1a7133b2b186a
payload={}
headers={
    'accept': 'application/json',
    'Authorization' : 'c7cf702d2e7375e75b61738d3406429fee95df21f5b25263f23ee243627f7755'
}

#########Function to run the API######

def get_flights_API (url):
    flights_holder = requests.request('GET', url, headers=headers, data=payload)
    data = flights_holder.text
    parse_data = json.loads(data)
    flights_dict=(parse_data['data'])
    flights_list = flights_dict['flights']
    current = flights_dict['pagination']['current_page']
    total = flights_dict['pagination']['total_pages']
    global flights
    flights += flights_list
    return current, total

def flights_with_telemetry_fun(flights):
    i = 0
    for flight_id in range(len(flights)):
        if flights[i]['has_telemetry'] == True:
            global  flights_with_telemetry
            flights_with_telemetry += [flights[i]['flight_id']]
        i += 1

def get_telemetry(flights):
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'c7cf702d2e7375e75b61738d3406429fee95df21f5b25263f23ee243627f7755'
    }
    id = 0
    for flight in flights:
        url = base_url + "/v0/flight/" + f"{flight}" + "/telemetry"
        pprint.pprint(url)
        telemetry = requests.request('GET', url=url, headers=headers, data=payload)
        pprint.pprint(telemetry.text)

flights = []
flights_with_telemetry = []
current, total = get_flights_API(get_flights);
print(current)
print(total)
next = current
while next < total:
    next += 1
    get_flights_url = get_flights + "?page_number=" + f"{next}" + "&per_page=25"
    get_flights_API(get_flights_url);


flights_with_telemetry_fun(flights)
get_telemetry(flights_with_telemetry);
pprint.pprint(flights_with_telemetry)
