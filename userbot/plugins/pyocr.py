try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
from userbot.utils import friday_on_cmd, sudo_cmd
from userbot.uniborgConfig import Config

@friday.on(friday_on_cmd(pattern="readit$"))
async def _(event):
    global images
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        imagez = await borg.download_media(
            await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
        )
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
    results = (pytesseract.image_to_string(Image.open(imagez)))
    await event.edit("READ :" + results)
    if os.path.exists(results):
        os.remove(results)
