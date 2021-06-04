from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd


@borg.on(admin_cmd("audio ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@AudioTubeBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=507379365)
            )
            await borg.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("🌐"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await borg.send_file(event.chat_id, response.message.message.media)
