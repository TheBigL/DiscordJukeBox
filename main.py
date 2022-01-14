import discord
from discord.ext import commands

import music

bot = commands.Bot(command_prefix='.', description="L's very own Jukebot", intents=discord.Intents.all())


def setup(client):
    client.add_cog(music)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("-----")


bot.add_cog(music)
bot.run('TOKEN')
