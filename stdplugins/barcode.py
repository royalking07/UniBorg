#Modded from dagd.py
"""
BarCode Generator
Command .bar (your text)
By @snappy101
"""

from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd


@borg.on(admin_cmd("bar (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://www.scandit.com/wp-content/themes/bridge-child/wbq_barcode_gen.php?symbology=code128&value={}&size=100&ec=L".format(input_str.replace(" ","-"))
    response_api = requests.get(sample_url).text
    if response_api:
        link = response_api.rstrip()
        await event.edit("Barcode {} Was Successfully Generated\n\n[BARCODE]({})".format(input_str, link))
    else:
        await event.edit("Error Occured. Please Try Again Later.")
