"""Emoji
Available Commands:
.nope
Credits to @mariodevs
"""


import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("nope"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "nope":
    await event.edit("nope")
    animation_chars = [
        "No",
        "Problem",
        "Boss",
        "Yeah ! No problem",
        "No Problem Boss.lol",
        "No Problem Boss😇.Lol",
        "No Problem Man😇.Lol",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "np": "**Nope**\
\n\n**Syntax : **`.nope`\
\n**Usage :** Use this plugin the say nope in funny way."
    }
)
