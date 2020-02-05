import instaloader
import os
from getpass import getpass

print("\n Unfollower Tracker, written by Addie Abukasis \n")
username = input("Enter Username: ")
password = getpass()

L = instaloader.Instaloader()
L.login(username, password) 
profile = instaloader.Profile.from_username(L.context, username)


followers = []
print("Gathering Followers..")
counter = 0
for follower in profile.get_followers():
	followers.append(follower.username)
	counter = counter + 1
	if(counter % 50 == 0):
		print("Read " + str(counter) + " followers.. ")
print("Finished collecting " + str(counter) + " followers")

myFile = open('followers.txt', 'a+')
myFile.seek(0)
oldFollowersList = myFile.readlines()
myFile.close()

followersFromTextFile = []

for username in oldFollowersList:
	followersFromTextFile.append(username.rstrip())

if(len(followersFromTextFile) == 0):
	print("First Time Log in!")
	print("In your next login, we can check who has unfollowed you")
	myFile = open('followers.txt', 'w+')
	for user in followers:
		myFile.write(user + "\n")
else:
	print("\nchecking who has unfollowed you.. \n")
	dictionaryOfFollowers = {}
	for user in followers:
		dictionaryOfFollowers[user] = 1
	
	unfollowersTextFile = open('unfollowers.txt', 'a+')
	
	unfollowersList = []
	for oldFollower in followersFromTextFile:
		if oldFollower in dictionaryOfFollowers:
			c = 2 + 2
		else:
			print(oldFollower + " has unfollowed you\n\n")
			unfollowersTextFile.write(oldFollower + "\n")
			unfollowersList.append(oldFollower)
	if(len(unfollowersList) == 0):
		print("No one has unfollowed you since last login \n")
	
	unfollowersTextFile.close()
	os.remove("followers.txt")
	myFile = open('followers.txt', 'a+')
	myFile.seek(0)
	for usr in followers:
		myFile.write(usr + "\n")
	myFile.close()
	print("You can see full list of unfollowers in unfollowers.txt file")
	print("Thanks for using Unfollower Tracker!\n")