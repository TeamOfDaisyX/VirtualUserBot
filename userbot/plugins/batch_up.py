"""
Files Batch Uploader Plugin for userbot.
usage:- .upb 
Note:- set TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870	

"""
import os 
import asyncio
from uniborg.util import admin_cmd
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply


@borg.on(admin_cmd(pattern=r"upb"))
@borg.on(sudo_cmd(pattern=r"upb", allow_sudo=True))
async def batch_upload(event):
	if event.fwd_from:
		return   
	temp_dir = Config.TEMP_DIR	
	if os.path.exists(temp_dir):    
		files = os.listdir(temp_dir)
		files.sort()
		await edit_or_reply(event, "Uploading Files on Telegram...")
		for file in files:
			required_file_name = temp_dir+"/"+file
			print(required_file_name)
			await borg.send_file(
					event.chat_id,
					required_file_name,
					force_document=True
				)	
	else:
		await edit_or_reply(event, "Directory Not Found.")
		return		
	await edit_or_reply(event, "Successfull.")	
