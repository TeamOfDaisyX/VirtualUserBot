# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal


import string
from random import *

from password_strength import PasswordStats
from telethon import events
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(events.NewMessage(pattern=r"\.passcheck(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stats = PasswordStats(input_str)
    stats.strength()

    if stats.strength() >= 0.6:
        await event.edit("Good Password. 😎")
    else:
        await event.edit("bad password, change it.😔")


@friday.on(friday_on_cmd(pattern=r"passgen"))
async def hi(event):
    if event.fwd_from:
        return
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(14, 16)))
    await event.edit(password)


CMD_HELP.update(
    {
        "password_tools": "**Password Tools**\
\n\n**Syntax : **`.passgen`\
\n**Usage :** This plugin generates good strong password for you.\
\n\n**Syntax : **`.passcheck <your password>`\
\n**Usage :** This plugin checks the strength of your password."
    }
)
