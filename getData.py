
# Script to grab data from govtrack

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

download2()

# timed out after ~ 541 requests


