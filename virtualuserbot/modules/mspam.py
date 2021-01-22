# Written By Inuka Asith for VirtualUserbot

from virtualuserbot import pro

from ..utils import admin_cmd

if pro == "True":

    @bot.on(admin_cmd(pattern="mspam (.*)"))
    async def tiny_pic_spam(e):

        sender = await e.get_sender()
        me = await e.client.get_me()

        if not sender.id == me.id and not FULL_SUDO:

            return await e.reply("`Sorry sudo users cant access this command..`")

        try:

            await e.delete()

        except:

            pass

        try:

            counter = int(e.pattern_match.group(1).split(" ", 1)[0])

            reply_message = await e.get_reply_message()

            if (
                not reply_message
                or not e.reply_to_msg_id
                or not reply_message.media
                or not reply_message.media
            ):

                return await e.edit("```Reply to a pic/sticker/gif/video message```")

            message = reply_message.media

            for i in range(1, counter):

                await e.client.send_file(e.chat_id, message)

        except:

            return await e.reply(
                f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
            )
