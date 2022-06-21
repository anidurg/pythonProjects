import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')

data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Karnataka']['districtData']['Bengaluru Urban']['active']
print("Active cases in Bengaluru: ",active_case)
