""" tiktok downloaded plugin creted by @mrconfused and @sandy1709 


Dont edit credits """
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import CMD_HELP

from ..utils import admin_cmd


@borg.on(admin_cmd("tti ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("downloading your video")

    async with borg.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await borg.send_message(event.chat_id, "sorry . something went wrong")
                return
            await conv.get_response()
            await conv.get_response()
            await borg.send_file(event.chat_id, details, caption=details.text)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


@borg.on(admin_cmd("ttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")

    async with borg.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await borg.send_message(event.chat_id, "sorry . something went wrong")
                return
            await conv.get_response()
            cat3 = await conv.get_response()
            await borg.send_file(event.chat_id, cat3)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


@borg.on(admin_cmd("wttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")

    async with borg.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await borg.send_message(event.chat_id, "sorry . something went wrong")
                return
            cat2 = await conv.get_response()
            await conv.get_response()
            await borg.send_file(event.chat_id, cat2)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


CMD_HELP.update(
    {
        "tiktok": "`.tti` <link> :\
      \nUSAGE: Shows you the information of the given tiktok video link.\
      \n\n `.ttv `<link>\
      \nUSAGE: Sends you the tiktok video of the given link without watermark\
      \n\n `.wttv `<link>\
      \n\nUSAGE: Sends you the tiktok video of the given link with watermark\
      "
    }
)
