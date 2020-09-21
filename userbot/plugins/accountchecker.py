import requests
import os
import requests
import json
from telethon.tl.functions.messages import ImportChatInviteRequest
from friday.utils import sudo_cmd, admin_cmd, edit_or_reply
from userbot.plugins import idgen, findnemo


@borg.on(admin_cmd("zee5 (.*)"))
@borg.on(sudo_cmd("zee5 (.*)"))
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
        await borg(ImportChatInviteRequest('NvhhslSY5CBUwUWWL7ku1w'))
    email = stark[0]
    password = stark[1]
    results = get(f"https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}").json()
    if not results.get("token"):
        await stuber.edit(f"**ZEE5 Account** : \n**Email** : `{email}` \n**Password** : `{password}` \n**Respone** : __Invalid Login__ 💫 \nJoin @ZeltraxRockz For Support And Info About This Module")
    else:
        await stuber.edit(f"ZEE5 Account : \nEmail : {email} \nPassword : {password} \nRespone : Login Sucessful 🇮🇳 \nJoin @ZeltraxRockz For Support And Info About This Module")
