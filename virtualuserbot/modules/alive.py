"""Check if virtualuserbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from uniborg.util import friday_on_cmd, sudo_cmd

from virtualuserbot import ALIVE_NAME, CMD_HELP, Lastupdate
from virtualuserbot.Configs import Config
from virtualuserbot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "VirtualUserbot"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = f" **\n   \n🔥 {DEFAULTUSER} VIRTUALUSERBOT IS AT YOUR SERVICE 🔥** \n\n"
pm_caption += "➣ **SYS**                        `នƴន ʀᴜɴɴɪɢ⋆ 🏃`\n"
pm_caption += "➣ **Telethon**                `₁.₁₅.₀ ` \n"
pm_caption += "➣ **Python**                   `₃.₇.₄ ` \n"
pm_caption += f"➣ **Uptime**                  `{uptime}` \n"
pm_caption += "➣ **Realised By**            @Infinity_Bots\n"
pm_caption += "➣ **Branch**                  `master`\n"
pm_caption += f"➣ **Version**                  `{currentversion}`\n"
pm_caption += f"➣ **My Boss**                {DEFAULTUSER} \n"
pm_caption += "➣ **RDP**                        `Azureˢˢˡ`\n"
pm_caption += "➣ **License**                  [GNU GPLv3.0](github.com/inukaasith/virtualuserbot/blob/master/LICENSE)\n"
pm_caption += "➣ **Copyright**             [@virtualuserbot](https://github.com/inukaasith/virtualuserbot)\n"
pm_caption += "➣ **Check **                   `.stat`.\n"
pm_caption += "➣ **Contact Dev**             [Dev](https://t.me/InukaASiTH)\n"
pm_caption += "➣ **Contact Mod**             [Mod](https://t.me/Zzlll_lllzZ)\n"


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
