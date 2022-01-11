import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import  get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

load_dotenv()
client = commands.Bot(command_prefix='.')
intents = discord.Intents.default()
intents.members = True


@client.event
async def on_ready():
    print('Jukebot has been booted up!')

@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('The Jukebot is current playing')

    else:
        await ctx.send('The Jukebot is already playing a song!')
        return


@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Jukebot has been paused')


@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await  ctx.send('The Jukebot is stopping...')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send('The messages have been cleared!')

client.run(os.getenv('TOKEN'))