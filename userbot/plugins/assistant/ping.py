# Copyright (C) Midhun KM 
# 
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot 
# x0x

from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
from googletrans import Translator
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from userbot import Lastupdate, bot

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    start = datetime.now()
    vent = event.chat_id
    starttext = ("Hi! This Bot is Part of @FridayOT \nThis Bot is Used For "
                 "Some Features That Can Be Used Via Bot. \nIf you want your"
                 "Own Assistant Bot Then Deploy From Button Bellow")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    if event.from_id == bot.uid:
        await tgbot.send_message(event.chat_id, f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n ➲ `{ms}` \n ➲ `{uptime}`")
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
      ]
     )
