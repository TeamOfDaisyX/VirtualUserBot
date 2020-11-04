# EXAMPLE CODE FOR ASSISTANT MODULE/PLUGIN

```python3
from fridaybot.Configs import Config
from userbot import bot
@assistant_cmd("commandhere", is_args=True)
async def shit(event):
    await event.reply(f"My master is [Pro](tg://user?id={bot.uid}")
```
## Note - is_args can be set to `False` if your command has no args else set it to `True`.
## Some Wrappers To Help You ! 
```
[+] - @is_admin ~ This Checks If Sender Is Admin.
[+] - @god_only ~ This Makes Sure Only God (owner) Only Uses it.
[+] - @only_groups ~ This Makes Sure Command is Only Used in Groups. [Silent]
[+] - @only_pro ~ Only Sudo users And Owner Can Use it.
[+] - @only_group ~ This Makes Sure Command is Only Used in Groups.
[+] - @is_bot_admin ~ Checks If Bot is Admin.
[+] - @peru_only ~ Only Sudo users And Owner Can Use it. [Silent]
[+] - @only_pvt ~ This Makes Sure Command Can't Be Used in Groups.
```
