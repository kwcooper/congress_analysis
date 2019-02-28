
# Script to grab data from www.senate.gov

import requests
import time


# def download(url, file_name):
# 	# open in binary mode
# 	with open(file_name, "wb") as file:
# 		# get request
# 		response = requests.get(url)
# 		if not response.status_code == 404:
# 			# write to file
# 			file.write(response.content)
# 			print("Wrote to file")
# 		else:
# 			print("404")

# url = "https://www.govtrack.us/data/congress/112/votes/2012/h100/data.json"
# file_name = "tst.json"
# #download(url, file_name)


# #                        votes/{session}/{chamber}{vote-number}/data.json
# # ex. /data/congress/113/votes/2014/h108/data.json
# for congress_num = range(100,115):
# 	for session_i = range(0,1):
# 		session = 1987 
# 		for vote_num = range(1,500):
# 			url = "https://www.govtrack.us/data/congress/" + str(congress_num) + "/votes/" + str(session + session_i) + "/s" + str(vote_num) + "/data.json"
# 		session += 2


def download2():
	session = 1987 
	for congress_num in range(100,115):
		for session_i in range(0,2):

			
			vote_num = 1
			print(session + session_i)
			start_time = time.time()
			while True:
				url = "https://www.govtrack.us/data/congress/" + str(congress_num) + "/votes/" + str(session + session_i) + "/s" + str(vote_num) + "/data.json"
				response = requests.get(url)

				if response.status_code == 404:
					print("404 on",vote_num)
					break
				else:
					file_name = "/home/wade/congressVoting/vote_" + str(congress_num) + "_" + str(session + session_i) + "_" + str(vote_num) + ".json"
					with open(file_name, "wb") as file:
						file.write(response.content)
						#print("Wrote", file_name)
				vote_num += 1
			print(vote_num, "votes for session", session + session_i)
			print("--- in %s seconds ---" %(time.time() - start_time))
			session += 1


def download3(): # Try to grab a bunch of them
			
			for congress_num in range(110,112):
				
			#congress_num = 111
				
				for session in [1,2]:
					print()
					print("Parsing congress", congress_num,"Session", session)
				#session = 1
					
					start_time = time.time()
					voteTick = 0
					for voteNum in range(1,1000):
					#voteNum = 555

						time.sleep(1)

						vote = f'{voteNum:05}'
						
						url = "https://www.senate.gov/legislative/LIS/roll_call_votes/vote" + str(congress_num) + str(session) + "/vote_" + str(congress_num) + "_" + str(session) + "_" + str(vote) + ".xml"
						response = requests.get(url)

						print('STATUS', response.status_code)
						# check if it exists
						if response.status_code == 503: # or 404
							response = requests.get(url) # try it again
							
							if response.status_code == 503:
								print("503 on",voteNum)
								print(url)
								break

						
						file_name = "/home/wade/Documents/Datasets/senateRecordsScraped/" + str(congress_num) + str(session) + "_" + str(vote) + ".xml"
						#file_name = "/home/wade/codingCoop/congress/scrapeData/" + str(congress_num) + str(session) + "_" + str(vote) + ".xml"
						with open(file_name, "wb") as file:
							file.write(response.content)
							#print("Wrote", file_name)
						
						voteTick += 1

					print("Grabed and saved some data:", voteTick, "votes")
					print("--- in %s seconds ---" %(time.time() - start_time))


def download4(): # test to download one file
			
			congress_num = 111
			session = 2
			voteNum = 2
			vote = f'{voteNum:05}'

			start_time = time.time()

			url = "https://www.senate.gov/legislative/LIS/roll_call_votes/vote" + str(congress_num) + str(session) + "/vote_" + str(congress_num) + "_" + str(session) + "_" + str(vote) + ".xml"
			response = requests.get(url)

			# check if it exists
			if response.status_code == 503: # or 404
				print(response.status_code, "on",voteNum)
				print(url)
				
			else:
				#file_name = "/home/wade/codingCoop/congress/scrapeData/" + str(congress_num) + str(session) + "_" + str(vote) + ".xml"
				file_name = "/home/wade/codingCoop/congress/scrapeData/" + str(congress_num) + str(session) + "_" + str(vote) + ".xml"
				with open(file_name, "wb") as file:
					file.write(response.content)
					#print("Wrote", file_name)
						
				print("Grabed and saved some data:", voteNum)
			
			print("--- in %s seconds ---" %(time.time() - start_time))


download3()

# https://www.senate.gov/legislative/LIS/roll_call_votes/vote1112/vote_111_2_00001.xml
# https://www.senate.gov/legislative/LIS/roll_call_votes/vote1112/vote_111_2_0001.xml

# https://www.senate.gov/legislative/LIS/roll_call_votes/vote1102/vote_110_2_00003.xml
# https://www.senate.gov/legislative/LIS/roll_call_votes/vote1102/vote_110_2_00003.xml

#https://www.senate.gov/legislative/LIS/roll_call_votes/vote1111/vote_111_1_00006.xml
#https://www.senate.gov/legislative/LIS/roll_call_votes/vote1111/vote_111_1_00006.xml


'''
so this works, but the webmaster has a strict setting in place. I suppose that this makes 
sense, but even my 1 second block didn't seem to do anything. Maybe randomize the queries 
to prevent any mech's of incrementing through the XML's? The 503 or html tags wouldn't get
around this
'''


 