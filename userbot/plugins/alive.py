"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
import time
from userbot.plugins.timefunc import uptimebot, get_readable_time
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

uptime = get_readable_time((time.time() - uptimebot))
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
currentversion = "3.0"

if issudousing:
    amiusingsudo = 'Active ✅'
else:
    amiusingsudo = 'Inactive ❌'

if islogokay:
    logchat = 'Connected ✅'
else:
    logchat = 'Dis-Connected ❌'

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/22535f8051a58af113586.jpg"
pm_caption = "➥ **FRIDAY IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0`\n**Python:** `3.7.4`\n"
pm_caption += f"➥ **Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **OS** : `Slim Buster` \n"
pm_caption += "➥ **Current Branch** : `Master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **Sudo** : `{amiusingsudo}`\n"                                                                      
pm_caption += f"➥ **Log Connections** : `{logchat}` \n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [StarkGang@Github](GitHub.com/StarkGang)\n"
pm_caption += "🎀 [Deploy FridayUserbot](https://telegra.ph/FRIDAY-06-15) 🎀"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
