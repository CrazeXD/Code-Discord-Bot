import discord
import os
import config

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def make_event(self): #Make an event
        pass
    

client = Bot()

client.run(config.client_secret)