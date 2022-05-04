import discord
from discord import client
from discord.ext import commands
import os
from dotenv import load_dotenv
import music

bot = commands.Bot(command_prefix='.', description="L's very own Jukebot", intents=discord.Intents.all())


def setup(client):
    client.add_cog(music)


@bot.command("join")
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You're currently not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("-----")


load_dotenv('development.env')

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
