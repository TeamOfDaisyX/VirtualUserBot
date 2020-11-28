# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal
# plugin by @chsaiujwal


from password_strength import PasswordStats
from telethon import events

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


CMD_HELP.update(
    {
        "passcheck": "**Password Checker**\
\n\n**Syntax : **`.passcheck <your password>`\
\n**Usage :** This plugin checks the strength of your password."
    }
)
