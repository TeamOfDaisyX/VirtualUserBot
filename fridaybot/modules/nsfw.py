#    Copyright (C) Midhun KM 2020
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
import requests
from telethon.tl.types import MessageMediaPhoto

from fridaybot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern=r"nsfw"))
@friday.on(sudo_cmd(pattern=r"nsfw", allow_sudo=True))
async def nsfw(event):
    url = "https://nsfw-categorize.it/api/upload"
    await event.edit("`Processing..`")
    replymsg = await event.get_reply_message()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await borg.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await borg.download_file(replymsg.media.document)
        else:
            await event.edit("`Reply To Image.`")
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        else:
            await event.edit("Response UnsucessFull. Try Again.")
