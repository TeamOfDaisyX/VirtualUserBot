import time
from datetime import datetime

from fridaybot import CMD_HELP, Lastupdate
from fridaybot.utils import edit_or_reply, friday_on_cmd


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


@friday.on(friday_on_cmd(pattern="ping$"))
async def _(event):
    starkislub = await edit_or_reply(event, "`Pong !`")
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await starkislub.edit(
        f"**🙈වැඩ වැඩ මහතයෝ⚙🔧** \n **ᵐʸ ᶜᵘʳʳᵉⁿᵗ ᵖᶦⁿᵍʳᵃᵗᵉ**👇 \n \n ⚡️ `{ms}` \n ⚡️ `{uptime}`"
    )


CMD_HELP.update(
    {
        "ping": "**Ping**\
\n\n**Syntax : **`.pin`\
\n**Usage :** Get uptime and speed of your bot."
    }
)
