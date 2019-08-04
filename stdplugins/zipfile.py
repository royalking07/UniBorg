"""Plugin Made By SnapDragon
Use: .compress"""
import zipfile
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from uniborg.util import admin_cmd


@borg.on(admin_cmd("compress"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to a file to compress it")
        return
    reply_file = await event.get_reply_message()
    if not reply_file is None:
        directory_name =  await borg.download_media(
                reply_message
        )
        zipf = zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED)
        zipdir(directory_name, zipf)
        zipf.close()
        await borg.send_file(
            event.chat_id,
            directory_name + ".zip",
            caption=file_caption,
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=progress
        )
        try:
            os.remove(directory_name + ".zip")
            os.remove(directory_name)
        except:
            pass
        await event.edit("task Completed")
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit("Invalid Message Type")


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
