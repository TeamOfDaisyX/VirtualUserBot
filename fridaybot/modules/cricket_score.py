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


romm bs4 import BeautifulSoup
import urllib.request
from uniborg.util import friday_on_cmd

from asyncio import wait
from fridaybot import CMD_HELP
from telethon import events


@friday.on(events.NewMessage(pattern=r"\.cricket(.*)", outgoing=True))
async def _(event):
        score_page = 'http://static.cricinfo.com/rss/livescores.xml'
        page = urllib.request.urlopen(score_page)
        soup = BeautifulSoup(page, 'html.parser')
        result = soup.find_all('description')
        Sed = ''
        for match in result:
          Sed +=match.get_text() + "\n\n"
        await event.edit(
        f"<b><u>Match information gathered successful</b></u>\n\n\n<code>{Sed}</code>", parse_mode="HTML",)
          




CMD_HELP.update(
    {
        "cricket_score": "**Cricket Score**\
\n\n**Syntax : **`.cricket`\
\n**Usage :** Gets Live cricket score automatically."
    }
)
