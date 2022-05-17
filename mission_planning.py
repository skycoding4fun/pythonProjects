import requests
import pprint
import json

get_missions = "https://api.skydio.com/api/v0/mission/schedules"

payload = {}
headers = {
'Accept': 'application/json',
'Authorization': '54a610a1cd9cedb4f157ee22e1e9b79c80a64ce9ee61dcba6da1a7133b2b186a'
}

missions = requests.request('GET', get_missions, headers=headers, data=payload)
missions_json = missions.json()

pprint.pprint(missions_json)
