import urllib.request
import json


# Getting the number of subscribers (ChannelID = UCopVMAEcdblYjF1-4Z7rcvw)
name = "Boas Novas"
channelId = "UCopVMAEcdblYjF1-4Z7rcvw"
key = "AIzaSyCnTiw1I-7NZIxJ3l6xh7nqN2Zob8wQKu0"

data = urllib.request.urlopen("https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelId + '+&key=' + key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!")
