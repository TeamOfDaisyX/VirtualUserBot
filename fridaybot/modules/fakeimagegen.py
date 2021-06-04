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


import os

import requests

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd


# hmm
@friday.on(friday_on_cmd(pattern="picgen"))
@friday.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    if response.status_code == 200:
        with open("FRIDAYOT.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By VirtualUserbot.\nGet Your Own Superpowers From [VirtualUserbot](github.com/inukaasith/virtualuserbot)."
    fole = "FRIDAYOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/fridaybot/FRIDAYOT.jpg ")


CMD_HELP.update(
    {
        "picgen": "**Fake Picture Gen**\
\n\n**Syntax : **`.picgen`\
\n**Usage :** Genetates Fake Image.\
\n\n**Note : **The Person In Picture Really Doesn't Exist."
    }
)
