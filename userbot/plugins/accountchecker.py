import requests
import os
import requests
import json
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from friday.util import sudo_cmd, admin_cmd, edit_or_reply
from userbot.plugins import idgen, findnemo
from telethon.tl.functions.account import UpdateProfileRequest

@borg.on(admin_cmd("zee5 (.*)"))
@borg.on(sudo_cmd("zee5 (.*)", allow_sudo=True))
async def zee5(event):
    chat_id = event.chat_id
    text = event.pattern_match.group(1)
    input_str = event.pattern_match.group(1)
    stuber = await edit_or_reply(event, "Checking This Fucking Regex")
    if text:
        if ":" in text:
            stark = input_str.split(":",1)
    else:
        await stuber.edit("You Are Using Invalid Syntax ! Make Sure To Use email:pass Regex")
        return
    if (len(stark) != 2):
        await stuber.edit("You Are Using Invalid Syntax ! Make Sure To Use email:pass Regex")
        return
    email = stark[0]
    password = stark[1]
    results = requests.get(f"https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}").json()
    if not results.get("token"):
        await stuber.edit(f"**ZEE5 Account** : \n**Email** : `{email}` \n**Password** : `{password}` \n**Respone** : __Invalid Login__ 💫 \n**Checked Using Friday Userbot**")
    else:
        await stuber.edit(f"**ZEE5 Account** : \n**Email** : `{email}` \n**Password : `{password}` \n**Respone** : __Login Sucessful 🇮🇳__ \n**Checked Using Friday Userbot**")
