
import requests
import json
import os.path

if os.path.exists("key.txt") == 0:
	APIKey = open("key.txt","w+")
	print("API key not found. Please enter your osu! API key (found at osu.ppy.sh/p/api)")
	APIKey.write(input())
	APIKey.close()

APIKey = open("key.txt","r")

key = APIKey.read()
APIKey.close()

print("Enter file name")
poolName = input()

file = open(poolName + ".txt", "r+")

mapList = file.readlines()

originalList = mapList.copy()


for x in range(0, len(originalList) - 1):
	originalList[x] = originalList[x][:-1]


bIDS = originalList.copy()
if bIDS[0][0] == "h":
	for x in range(0,len(bIDS)):
		y = 0
		while y < 5:
			if bIDS[x][0] != "/":
				bIDS[x] = bIDS[x][1:]
			else:
				bIDS[x] = bIDS[x][1:]
				y += 1



file.close()
file = open(poolName + ".txt", "w+")


for x in range(0,len(bIDS)):
	weblink = 'https://osu.ppy.sh/api/get_beatmaps?k=' + key + '&b=' + bIDS[x]
	formatted = json.loads(requests.get(weblink).text)
	if formatted[0]["download_unavailable"] == "0" and formatted[0]["audio_unavailable"] == "0":
		fullString = "=HYPERLINK(\"" + "https://osu.ppy.sh/b/" + bIDS[x] + "\",\"" + formatted[0]["artist"] + " - " + formatted[0]["title"] + " [" + formatted[0]["version"] + "]\")\n"
	else:
		fullString = "=HYPERLINK(\"https://bloodcat.com/osu/s/" + formatted[0]["beatmapset_id"] + "\",\"" + formatted[0]["artist"] + " - " + formatted[0]["title"] + " [" + formatted[0]["version"] + "]\")\n"
	print("Converting " + formatted[0]["artist"] + " - " + formatted[0]["title"] + " [" + formatted[0]["version"] + "]...\n")
	file.write(fullString)
	

file.close()


