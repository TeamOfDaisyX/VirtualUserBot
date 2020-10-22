from userbot import CMD_LIST
from userbot.utils import sudo_cmd, edit_or_reply

@friday.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    help_string = ""
    for i in CMD_LIST[plugin_name]:
        help_string += i
        help_string += "\n"
    await event.reply(help_string)
