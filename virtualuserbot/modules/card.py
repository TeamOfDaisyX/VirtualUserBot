# Original By
# @THE_B_LACK_HAT
# @danish_00
# For #Cobra
#
# Card Generator
##############################
from faker import Faker as dc

from virtualuserbot import bot as cobra

from ..utils import admin_cmd as hehe


@cobra.on(hehe("card"))
async def _cobra(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    danish = cyber.credit_card_full()
    await dark.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{danish}`")
