"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events
from userbot.utils import sudo_cmd, edit_or_reply

import asyncio





@borg.on(events.NewMessage(pattern=r"hack$", outgoing=True))
@borg.on(sudo_cmd(pattern=r"hack$", allow_sudo=True))
async def _(event):
    sed = await edit_or_reply(event ,"`Hacking.....`")
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
        await sed.edit("Me Bhill Hack You")
        animation_chars = [
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Hacking... Sucessfull Imported Data To Userbot/Downloads`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await sed.edit(animation_chars[i % 11])
