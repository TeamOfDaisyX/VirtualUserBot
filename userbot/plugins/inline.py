from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var





@borg.on(admin_cmd(pattern="showstats$"))
async def stats(event):
    if event.fwd_from:
        return
    botusername = Var.TG_BOT_USER_NAME_BF_HER
    noob = "noob"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob) 
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(admin_cmd(pattern="xogame$"))
async def stats(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob) 
    await tap[0].click(event.chat_id)
    await event.delete()
