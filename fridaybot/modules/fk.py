from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="fk$"))
@bot.on(sudo_cmd(pattern="fk$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "**පල හුත්තෝ යන්න 😂\n තෝ සමාජයට විහිළුවක් ඕයි 😒**",
    )
