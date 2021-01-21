import os

from pdf2docx import parse

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


@friday.on(friday_on_cmd(pattern=r"pdf2docx"))
@friday.on(sudo_cmd(pattern=r"pdf2docx", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Pdf File.")
        return
    await event.reply("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)

    await event.reply("hmm... Please Wait...🚶")

    pdf_file = starky
    docx_file = "./fridaybot/DOWNLOADS/FRIDAYOT.docx"

    parse(pdf_file, docx_file, start=0, end=None)

    await borg.send_file(
        event.chat_id,
        docx_file,
        caption=f"*PDF Converted Into Docx by VirtualUserbot. Special thanks to @FRIDAYOT.",
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()


CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx."
    }
)
