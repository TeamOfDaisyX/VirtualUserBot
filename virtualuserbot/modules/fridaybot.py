"""Emoji
Available Commands:
.support
"""


import asyncio

from virtualuserbot import CMD_HELP
from virtualuserbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("virtualuserbot"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Thanks")
    animation_chars = [
        "Click here to Go to our Official Website",
        "[Click Here For Guide](https://techwizardent.com/blog/twe_blog_userbot.php)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "VirtualUserbot": "**VirtualUserbot**\
\n\n** Congragulations **\
\n ` You have Successfully installed the VirtualUserbot`\
\n\n Now you can find all new features in Whats New\
\n\n In this Help menu You can find all the available commands with .help\
\n `If you need more plugins contact @InukaASiTH`\
\n Updates Channel:  @Infinity_Bots\
\n Bot Support: @InfinityJE\
\n Developed By: @InukaASiTH for @Infinity_Bots\
\n Supporters: @Kaveesha_Induwara ,@Zzlll_lllzZ , @ImJanindu, @dasun_pamod \
\n\n ❤️ Project Cloned and Developed based on @FridayOT Project ❤️\
\n `Full Respect to Friday Devs`\
\n\n\n**Try : **`.virtualuserbot`\
\n**For :** full VirtualUserbot's guide."
    }
)
