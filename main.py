import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

load_dotenv()
client = commands.Bot(command_prefix='.')
intents = discord.Intents.default()
intents.members = True

# Run the Bot
client.run(os.getenv('TOKEN'))
