import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from cog import music

bot = commands.Bot(command_prefix='.', description="L's very own Jukebot", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("-----")


@bot.command()
async def load(extension):
    bot.load_extension(f'cog.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cog.{extension}')

load(music)
load_dotenv('development.env')

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
