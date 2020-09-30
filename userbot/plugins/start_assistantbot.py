from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events

@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    vent = event.chat_id
    starttext = ("Hi! This Bot is Part of @FridayOT \nThis Bot is Used For "
                 "Some Features That Can Be Used Via Bot. \nIf you want your"
                 "Own Assistant Bot Then Deploy From Button Bellow")
    if vent == bot.uid:
        await tgbot.send_message(
           vent,
           message="Hi Master, It's Me Your Assistant.",
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
            ]
           )
    else:
        await tgbot.send_message(
           vent,
           message=starttext,
           link_preview=False,
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
       ]
      )
