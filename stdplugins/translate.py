""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
import goslate
from uniborg.util import admin_cmd


@borg.on(admin_cmd("tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        lan, text = input_str.split("|")
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    gs = goslate.Goslate()
    try:
        await asyncio.sleep(2)
        translated = gs.translate(text, input_str)
        after_tr_text = translated
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**TRANSLATED** to {}
{}""".format(
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
