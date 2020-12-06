from telethon.events import ChatAction

from fridaybot import sclient
from fridaybot.Configs import Config
from fridaybot.utils import admin_cmd


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


@friday.on(admin_cmd(pattern="aban (.*)"))
async def ok(event):
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        userz = args[0]
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.edit("Provide User-ID Not Username.")
            return
        if len(args) == 2:
            extra = args[1]
        if extra == None:
            await event.edit("Reason Can't Be None")
            return
        elif extra == "":
            await event.edit("Reason Can't Be None")
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
        try:
            gensys = sclient.ban(user, extra)
            if gensys["error"] == True:
                await event.edit("Error : " + gensys["full"])
            else:
                await borg.send_message("antispamincfed", f"/fban {user} {extra}")
                event.edit(
                    f"**User :** `{user}` \n**Reason :** `{extra}` \n**Banned Sucessfully !**"
                )
        except Exception as e:
            event.edit(e)


@friday.on(admin_cmd(pattern="aunban (.*)"))
async def ok(event):
    args = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
    elif args:
        userz = args
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.reply("Fuck, Gib ID")
            return
        if not user:
            await event.reply("Reply To User Or Mention a User.")
            return
        try:
            gensys2 = sclient.unban(user, extra)
            if gensys2["error"] == True:
                await event.edit("Error : " + gensys2["full"])
            else:
                await borg.send_message("antispamincfed", f"/unfban {user} {extra}")
                event.edit(
                    f"**User :** `{user}` \n**Reason :** `{extra}` \n**Banned Sucessfully !**"
                )
        except Exception as e:
            event.edit(e)


@friday.on(admin_cmd(pattern="anewtoken"))
async def tokens(event):
    okbabe = secrets.token_urlsafe(16)
    try:
        skynet = sclient.new_token(sed_put)
        if skynet["error"] == True:
            await event.edit("Error : " + gensys2["full"])
        else:
            await event.edit(f"**New Token** \n**Token** : `{okbabe}`")
    except Exception as e:
        event.edit(e)
