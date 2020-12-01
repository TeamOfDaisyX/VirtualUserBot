""".cowsay, .tuxsay, .milksay, .kisssay, .wwwsay, .defaultsay, .bunnysay,
.moosesay, .sheepsay, .rensay, .cheesesay, .ghostbusterssay, .skeletonsay,
and may cmd would be added soon."""


from cowpy import cow
from telethon import events

from fridaybot import CMD_HELP


@friday.on(events.NewMessage(pattern=r"^.(\w+)say (.*)", outgoing=True))
async def univsaye(cowmsg):
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


CMD_HELP.update(
    {
        "cow": "**Cow**\
        \n\n**Syntax : **`.cowsay`\
        \n\n**Syntax : **`.tuxsay`\
        \n\n**Syntax : **`.milksay`\
        \n\n**Syntax : **`.kisssay`\
        \n\n**Syntax : **`.wwwsay`\
        \n\n**Syntax : **`.defaultsay`\
        \n\n**Syntax : **`.bunnysay`\
        \n\n**Syntax : **`.moosesay`\
        \n\n**Syntax : **`.sheepsay`\
        \n\n**Syntax : **`.rensay`\
        \n\n**Syntax : **`.cheesesay`\
        \n\n**Syntax : **`.ghostbusterssay`\
        \n\n**Syntax : **`.skeletonsay`\
        \n\n**Usage :** A fun plugin to get ur texts look like its being said by different characters"
    }
)
