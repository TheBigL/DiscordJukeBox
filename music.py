import asyncio

import discord
from discord.ext import commands
import youtube_dl
import YTDLSource






class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot






    @commands.command()
    async def ping(ctx):
        await ctx.send('Ping!')

    @commands.command("join")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're currently not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command("play")
    async def play(self, ctx, *, url):

        if(url == None):
            ctx.send("You need to enter a URL before playing!")

        else:

            ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 '
                                                '-reconnect_delay_max 5', 'options': '-vn'}
            ydl_options = {'format': 'bestaudio'}
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop= self.bot.loop)
                ctx.voice_client.play(player, after=lambda e: print(f'Player Error: {e}') if e else None)










    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ⏸")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()
        await ctx.send("Stopped ⏹")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resuming ▶")


