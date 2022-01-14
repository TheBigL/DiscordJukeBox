import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import music

cogs = [music]
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

def setup(client):
    client.add_cog(music(client))


for i in range(len(cogs)):
    cogs[i].setup(client)

load_dotenv()
# Run the Bot
client.run(os.getenv('TOKEN'))
