import discord
from discord import client
from discord.ext import commands
import os
from dotenv import load_dotenv
import music

bot = commands.Bot(command_prefix='.', description="L's very own Jukebot", intents=discord.Intents.all())


def setup(client):
    client.add_cog(music)





@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("-----")


load_dotenv('development.env')

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
