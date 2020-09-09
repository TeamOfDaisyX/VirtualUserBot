# Base Credits @MrConfused And Help Inline 
import io
import re
import json
import random
import asyncio
from math import ceil
from .. import CMD_LIST , LOGS
from telethon import events, errors, custom, Button

statstext = "Yes , Me Iz Alive"

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery) 
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("__**Test"):
            buttons = [(custom.Button.inline("Stats", data="statstext"),
                        Button.url("License" , "https://github.com/StarkGang/FridayUserbot/blob/master/LICENSE"),
                        Button.url("Deploy Friday" , "github.com/Starkgang/FridayUserbot"))]
            results = builder.article(
                         title = "",
                         text = query,
                         buttons = buttons
                         )
            await event.answer([results] if result else None)
        
