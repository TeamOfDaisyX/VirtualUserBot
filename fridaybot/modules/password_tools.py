#    Copyright (C) @chsaiujwal 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import string
from random import *

from password_strength import PasswordStats
from telethon import events
from uniborg.util import friday_on_cmd
from fridaybot.utils import admin_cmd
from fridaybot import CMD_HELP


@friday.on(admin_cmd(pattern="passcheck (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stats = PasswordStats(input_str)
    sedbruh = stats.strength()
    if stats.strength() >= 0.6:
        await event.edit(f"<b><u>Password Checked</b></u> \n<b>Password :</b> <code>{input_str}</code> \n<b>Strength :</b> <code>{sedbruh}</code> \n<b>Result :</b> <code>Good Password</code>", parse_mode='HTML')
    else:
        await event.edit(f"<b><u>Password Checked</b></u> \n<b>Password :</b> <code>{input_str}</code> \n<b>Strength :</b> <code>{sedbruh}</code> \n<b>Result :</b> <code>Bad Password</code>", parse_mode='HTML')


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
