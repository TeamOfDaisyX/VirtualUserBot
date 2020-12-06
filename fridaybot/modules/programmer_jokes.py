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


import pyjokes
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern=r"pjoke"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit(pyjokes.get_joke(category="all"))


CMD_HELP.update(
    {
        "programmer_jokes": "**Programmer Jokes**\
\n\n**Syntax : **`.pjoke`\
\n**Usage :** Get programmer jokes."
    }
)
