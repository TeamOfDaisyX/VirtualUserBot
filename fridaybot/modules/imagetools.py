import os
import requests
from fridaybot.utils import friday_on_cmd, sudo_cmd
from telethon.tl.types import MessageMediaPhoto
sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
 
@friday.on(friday_on_cmd(pattern=r"cit"))
@friday.on(sudo_cmd(pattern=r"cit", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {
    "api-key": life
    }
    hmm = await event.edit("Colourzing..")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in response.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
    "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/colorizer"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedimg = r['output_url']
    await borg.send_file(event.chat_id, sedimg)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)
    
