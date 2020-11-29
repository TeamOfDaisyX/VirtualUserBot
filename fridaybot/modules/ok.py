"""Emoji

Available Commands:

.ok"""


import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.00001
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "ok":
        await event.edit(input_str)
        animation_chars = [
            "F",
            "U",
            "C",
            "K",
            "Y",
            "O",
            "U",
            "B",
            "C",
            "FK",
            "UU",
            "FCUK",
            "UOY",
            "C",
            "F",
            "Y",
            "F",
            "Ok Sar 😇",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "ok": "**OK**\
\n\n**Syntax : **`.ok`\
\n**Usage :** Funny plugin to say 'ok sar'."
    }
)
