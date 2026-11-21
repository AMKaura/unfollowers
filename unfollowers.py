import json
from pyscript import document
from pyodide.http import pyfetch

# TEMPORARY: Browser-based file loading using HTTP
# pyfetch requests the files from our local HTTP server.
# await waits for each asynchronous operation to complete.
# response.json() parses the JSON into Python objects.

response = await pyfetch("followers_1.json")
followers_data = await response.json()

response = await pyfetch("following.json")
following_data = await response.json()


# ORIGINAL: Terminal-based file loading
# Restore this section when running with regular Python.
# Remember to comment out the temporary PyScript loading above.

#file path goes where the json files go
# followersPath = input("Enter the path for your 'followers_1.json' file: ")
# followingPath = input("Enter the path for your 'following.json' file: ")

# with open(followersPath, "r", encoding="utf-8") as f:
#     followers_data = json.load(f)

# with open(followingPath, "r", encoding="utf-8") as f:
#     following_data = json.load(f)

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
output_div = document.querySelector("#textarea")
output_div.innerText = unfollowers



