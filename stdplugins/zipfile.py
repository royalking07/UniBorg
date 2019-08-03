"""Plugin Made By SnapDragon
Use: .zip <file_directory> <file_name>"""
import zipfile
from telethon import events
from uniborg.util import admin_cmd


@borg.on(admin_cmd("earth ?(.*) ?(.*)"))
async def _(event):
	if event.fwd_from:
		return
  file_dir = event.pattern_match.group(1)
  input_str = event.pattern_match.group(2)
  if not file_dir is None:
      if not input_str is None:
          zip_file = zipfile.ZipFile(file_dir, "w")
          zip_file.write(input_str + ".zip", compress_type=zipfile.ZIP_DEFLATED)
          zip_file.close()
          await event.edit("File Succesfully Zipped To `{}`".format(input_str + ".zip")
      else:
          await event.edit("Please Enter A Zip Name")
  else:
      await event.edit("Please Enter A File Directory")
      
      
