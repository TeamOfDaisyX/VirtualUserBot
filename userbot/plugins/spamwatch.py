import os
import asyncio
from telethon import events
import spamwatch as starkwatch
from var import Var

spamwatchapi = Var.SPAMWATCH_API 
SPAM_PROTECT = Var.ANTISPAM_SYSTEM
W_CHAT = Var.WHITE_CHAT


if SPAM_PROTECT == "ENABLE":
 @bot.on(events.ChatAction)
 async def spamwatch(event): 
   if event.user_joined or event.user_added and not event.chat_id in W_CHAT and SPAM_PROTECT and spamwatchapi and not event.is_private:
       chat = await event.get_chat()
       admin = chat.admin_rights
       creator = chat.creator   
       if admin or creator:
           return
       sw = starkwatch.Client(spamwatchapi)
       whoistheguy = await event.get_user()      
       try:
           sswatch = sw.get_ban(whoistheguy.id) 
       except: 
           return                   
       if sswatch:                                                                                                
                 try:
                    await borg.edit_permissions(event.chat_id, whoistheguy.id, view_messages=False)    
                    action = "`Banned 😢`" ; return await event.reply(f"**🛡️ SpamWatch Banned User Detected 🛡️** \n"                      
            f"**Banned For :**  : `{sswatch.reason}`\n"
            f"**User ID :** [{guser.id}](tg://user?id={guser.id})\n"                   
            f"**Action Taken :**  : {action}"
            "Kindly Appeal Here => @SpamWatch")                            
                 except:                          
                    return 
  
    	
