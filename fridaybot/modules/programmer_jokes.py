""" Plugin By @chsaiujwal on telegram """
""" Plugin By @chsaiujwal on telegram """
""" Plugin By @chsaiujwal on telegram """
""" Plugin By @chsaiujwal on telegram """
""" Plugin By @chsaiujwal on telegram """


import pyjokes
from fridaybot import CMD_HELP
from uniborg.util import friday_on_cmd
from asyncio import wait
from telethon import events

 
 
@friday.on(friday_on_cmd(pattern=r"pjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category='all'))



CMD_HELP.update(
    {
        "programmer_jokes": "**Programmer Jokes**\
\n\n**Syntax : **`.pjoke`\
\n**Usage :** Get programmer jokes."
    }
)