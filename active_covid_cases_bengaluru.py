import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')

data = response_API.text
parse_json = json.loads(data)

jsonString = json.dumps(parse_json)
jsonFile = open("covid_data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

#print("printing json: ",parse_json)
active_case = parse_json['Karnataka']['districtData']['Bengaluru Urban']['active']
print("Active cases in Bengaluru: ",active_case)
