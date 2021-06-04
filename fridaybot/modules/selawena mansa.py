from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="sm$"))
@bot.on(sudo_cmd(pattern="sm$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** එහෙම එවා නෑ එ සෙලවෙන මනස **",
    )
