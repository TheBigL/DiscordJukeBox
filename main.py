import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='.', description="L's very own Jukebox", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("-----")
    print(f"Starting to load cogs...")
    for cog in os.listdir("cog"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"cog.{cog.strip('.py')}")
                print({cog} + " cog has been loaded")
            except Exception as e:
                print(e)
                print("{cog} cog can't be loaded.")


load_dotenv('development.env')

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
