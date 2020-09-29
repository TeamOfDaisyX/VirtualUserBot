from userbot.utils import admin_cmd, sudo_cmd
import asyncio
import os
from datetime import datetime
from pathlib import Path
fridaythumb = './resources/IMG_20200929_103719_628.jpg'

@borg.on(admin_cmd(pattern="send ?(.*)"))
@borg.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(5)
    await event.delete()
