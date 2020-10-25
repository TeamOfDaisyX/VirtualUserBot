from youtubesearchpython import SearchVideos
from pytube import YouTube
import os
import wget
from userbot.uniborgConfig import Config
import asyncio
from userbot.utils import sudo_cmd, friday_on_cmd, edit_or_reply
from downloader_cli.download import Download

@friday.on(friday_on_cmd(pattern="ytmusic ?(.*)"))
@friday.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`")
    search = SearchVideos(f"{urlissed}", offset = 1, mode = "dict", max_results = 1)
    mi = search.result()
    mio = mi['search_result']
    mo = mio[0]['link']
    thum = mio[0]['title']
    fridayz = mio[0]['id']
    thums = mio[0]['channel']
    kekme = f"http://img.youtube.com/vi/" + fridayz + "/maxresdefault.jpg"
    youtube_video_url = f"{mo}"
    yt_obj = YouTube(youtube_video_url)
    await asyncio.sleep(0.6)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = Download(kekme).download()
    keks = yt_obj.streams.get_audio_only().download(output_path=path, filename=f'{thum}')
    await myself_stark.edit("`Song Downloaded Sucessfully. Let Me Upload it Here.`")
    renamee = keks
    pre, ext = os.path.splitext(renamee)
    new_extension = ".mp3"
    hmm = os.rename(renamee, pre + new_extension)
    km = pre + new_extension
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`" 
    await borg.send_file(event.chat_id,
                km,
                force_document=False,
                allow_cache=False,
                caption=capy,
                performer=thums,
                thumb = sedlyf,
                supports_streaming=True) 
    await myself_stark.edit("`Song Uploaded. By (C) @FridayOT`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)
