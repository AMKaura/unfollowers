import json

#file path goes where the json files go
followersPath = input("Enter the path for your 'followers_1.json' file: ")
followingPath = input("Enter the path for your 'following.json' file: ")

with open(followersPath, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open(followingPath, "r", encoding="utf-8") as f:
    following_data = json.load(f)

#print(following_data)

# Extract usernames into Python lists
followers  = dict()
following = []

#O(n)
for person in following_data["relationships_following"]:
    following.append(person["title"])
    
#O(m)
for person in followers_data:
    followers[person["string_list_data"][0]["value"]] = 0

#print(myFollowers)
unfollowers = []

#O(n)
for person in following:
    if person not in followers:
        link = "https://www.instagram.com/" + person
        unfollowers.append([person,link])
        
print(unfollowers)



