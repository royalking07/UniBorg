from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(util.admin_cmd(r"^\.xd$"))
async def payf(event):
    if event.fwd_from:
        return   
    paytext=event.text[6:]
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.edit(pay)