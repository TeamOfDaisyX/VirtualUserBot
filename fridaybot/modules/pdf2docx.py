import asyncio
import os
import time
import time as t
import zipfile
from datetime import datetime
import shutil
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image, crop_vid, runcmd
from fridaybot.utils import friday_on_cmd, sudo_cmd
from pdf2docx import parse
import glob
import string 
import random 
import uuid



if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
  os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
  
@friday.on(friday_on_cmd(pattern=r"pdf2docx"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Pdf File.")
        return
    hmmu = await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    hmmu = await event.edit("hmm... Please Wait..")
    pdf_file = starky
    docx_file = './fridaybot/DOWNLOADS/FRIDAYOT.docx'
    parse(pdf_file, docx_file, start=0, end=None)
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by Friday bot. Get your Friday From @FRIDAYOT."
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()




CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)
