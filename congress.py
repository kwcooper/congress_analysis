
# this is limited by its need to have the session info etc. 

import json
import requests

def proAPI():
	key = 'JzeVIAj87jLigjawkeddvpbxi1yDZmnIGHjBsMuV'
	#url = "https://api.propublica.org/congress/v1/115/senate/members.json"
	# get recent bills
	url = "https://api.propublica.org/congress/v1/115/house/bills/introduced.json"
	r = requests.get(url,headers={"X-API-KEY":key})
	return r.content
	#return r.content

def grabRollVotes():
	key = 'JzeVIAj87jLigjawkeddvpbxi1yDZmnIGHjBsMuV'
	# https://api.propublica.org/congress/v1/{congress}/{chamber}/sessions/{session-number}/votes/{roll-call-number}.json
	# congress = 102-115 for House, 80-115 for Senate
	# Chamber = house or senate
	# session-number = 1 or 2, depending on year (1 is odd-numbered years, 2 is even-numbered years)
	# roll-call-number	integer
	congress = '115'
	chamber = 'senate'
	session_number = '1'
	roll_call_number = '17'
	url = "https://api.propublica.org/congress/v1/" + congress + "/" + chamber + "/sessions/" + session_number + "/votes/" + roll_call_number + ".json"
	r = requests.get(url,headers={"X-API-KEY":key})
	return r.content
	#return r.content

def print_data(data):
	r = json.loads(data)
	bills = r['results'][0]['bills']
	for i in range(len(bills)):
		print(bills[i]['number'])
		print(bills[i]['introduced_date'])
		print(bills[i]['title'])
		print(bills[i]['latest_major_action'])
		print(bills[i]['latest_major_action_date'])
		print("")

if __name__ == '__main__':
	data = proAPI()
	#print_data(data)
	data = grabRollVotes()
	print(json.loads(data))