import asyncio
import discord
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''

ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 '
                                    '-reconnect_delay_max 5', 'options': '-vn'}
ydl_options = {'format': 'best-audio'}

ytdl = youtube_dl.YoutubeDL(ydl_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.url('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegOpusAudio(filename, **ffmpeg_options), data=data)
