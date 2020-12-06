import antispaminc
from fridaybot import sclient
from telethon.events import ChatAction

from fridaybot.Configs import Config


@borg.on(ChatAction)
async def ok(event):
    if Config.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined or event.user_added:
        juser = await event.get_user()
        user = sclient.is_banned(juser.id)
        if user.banned == True:
                try:
                    await borg.edit_permissions(
                        event.chat_id, juser.id, view_messages=False
                    )
                    await event.reply(
                        f"**#FRIDAY-ANTISPAM** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{sed.reason}`"
                    )
                except:
                    pass
        else:
            pass
