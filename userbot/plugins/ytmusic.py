from youtubesearchpython import SearchVideos
from pytube import YouTube
import os
from userbot.uniborgConfig import Config
from userbot.utils import sudo_cmd, friday_on_cmd
@friday.on(friday_on_cmd(pattern="ytsong ?(.*)"))
@friday.on(sudo_cmd(pattern="ytsong ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    await event.edit("Fecthing Song....")
    search = SearchVideos(f"{urlissed}", offset = 1, mode = "dict", max_results = 1)
    mi = search.result()
    mio = mi['search_result']
    mo = mio[0]['link']
    thum = mio[0]['title']
    thumb_nail = mio[0]['thumbnails']
    kek = thumb_nail[0]
    do = await borg.download(kek, Config.TMP_DOWNLOAD_DIRECTORY)
    youtube_video_url = f"{mo}"
    yt_obj = YouTube(youtube_video_url)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    path = Config.TMP_DOWNLOAD_DIRECTORY
    keks = yt_obj.streams.get_audio_only().download(output_path=path, filename=f'{thum}')
    await borg.send_file(file=keks, thumb=kek, caption=f"{thum}")
    
