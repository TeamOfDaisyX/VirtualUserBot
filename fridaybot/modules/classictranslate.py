""" Google Translate
Available Commands:
.tl LanguageCode as reply to a message
.tl LangaugeCode | text to translate"""

import emoji
from googletrans import Translator

from fridaybot import CMD_HELP

from ..utils import admin_cmd


@borg.on(admin_cmd("tl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit(".tl LanguageCode as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated Successfully** from {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))


CMD_HELP.update(
    {
        "Classic translate": ".tl <language code> <reply to text>"
        "\nUsage: reply any msg with .tr (language code) example .tr en / .tr hi\n\n"
        ".tl <language code> | <msg> "
        "\nUsage: translate text example .tr en|msg (note:- this | mark is important.\n\n"
    }
)
