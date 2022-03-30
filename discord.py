import requests
import json

class user:
    def __init__(self, Token):
        self.token = Token
        self.user = self.GetCurrentUser()
        self.id = self.user['id']
        self.Username = self.user['username']

    def GetCurrentUser(self):
        response = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": self.token})
        return json.loads(response.content)

    def GetGuilds(self):
        response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": self.token})
        return json.loads(response.content)

    def GetGuild(self, id):
        response = requests.get("https://discord.com/api/v9/guilds/" + id, headers={"Authorization": self.token})
        return json.loads(response.content)

    def GetGuildChannels(self, id):
        response = requests.get("https://discord.com/api/v9/guilds/" + id + '/channels', headers={"Authorization": self.token})
        return json.loads(response.content)

    def GetChannelMessages(self, id):
        response = requests.get("https://discord.com/api/v9/channels/" + id + '/messages?limit=50', headers={"Authorization": self.token})
        messages = json.loads(response.content)
        if len(messages) == 50:
            while True:
                r = requests.get("https://discord.com/api/v9/channels/" + id + '/messages?limit=50&before=' + messages[len(messages)-1]['id'],  headers={"Authorization": self.token})
                r = json.loads(r.content)
               # print(type(r))
                #print(type(messages))
                messages.extend(r)
                if len(r) < 50:
                    break

        return messages