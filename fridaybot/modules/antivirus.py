# Lots of lub to @r4v4n4 for gibing the base <3
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="scan ?(.*)"))
@bot.on(sudo_cmd(pattern="scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    x = await edit_or_reply(event, "scanning...")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await x.edit("```reply to a media message```")
        return
    chat = "@DrWebBot"
    reply_message.sender
    if reply_message.sender.bot:
        await x.edit("```Reply to actual users message.```")
        return
    await x.edit(" `Sliding my tip, of fingers over it`")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await x.edit(
                "```can you kindly disable your forward privacy settings for good?```",
            )
        else:
            if response.text.startswith("Select"):
                await x.edit("`Please go to` @DrWebBot `and select your language.`")
            else:
                await x.edit(
                    f"**Antivirus scan was completed. I got dem final results.**\n {response.message.message}",
                )


CMD_HELP.update(
    {"antivirus": "➟ `.scan <reply to pic/doc>`\nUse - Scan the pic/doc for viruses."}
)
