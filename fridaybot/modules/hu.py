from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="hu$"))
@bot.on(sudo_cmd(pattern="hu$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
       "** කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි! **",
    )

