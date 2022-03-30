import progress
import download
import discord
import time

user = discord.user(input("PLease enter your token: "))
print("Welcome " + user.Username)

guilds = user.GetGuilds()

for index, guild in enumerate(guilds):
    print(f"{index + 1} - {guild['name']}")

Tindex = int(input("Please sellect guild that you want to preform work on: "))

wGuild = guilds[Tindex - 1]

channels = user.GetGuildChannels(wGuild['id'])
Tchannel = []

for channel in channels:
    if channel['type'] == 0:
        Tchannel.append(channel)

channels = Tchannel

for index, channel in enumerate(channels):
    print(f"{index + 1} - {channel['name']}")

Tindex = int(input("Please sellect channel that you want to preform work on: "))

wChannel = channels[Tindex - 1]
progress.clearConsole()
print(f"Getting messages from {wChannel['name']} on {wGuild['name']}")
messages = user.GetChannelMessages(wChannel['id'])

files = []

for msg in messages:
    for atc in msg['attachments']:
        #print(atc.get('content_type'))
        file = {
            "id": atc.get('id'),
            "url": atc.get('url'), 
           "filename": atc.get('filename'), 
            "content_type": atc.get('content_type')
        }

        files.append(file)

path = input('Please enter a path to save: ')
progress.clearConsole()
print(f"Download started for {wChannel['name']} on {wGuild['name']}")

Loader = download.download(files, path)
Loader.Start()
input()