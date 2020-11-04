# EXAMPLE CODE FOR ASSISTANT MODULE/PLUGIN

## is_args can be false if your command has no args else set it to true.

```python3
from fridaybot.Configs import Config
from userbot import bot
@assistant_cmd("commandhere", is_args=True)
async def shit(event):
    await event.reply(f"My master is [Pro](tg://user?id={bot.uid}")
```
## Some Wrappers To Help You
```
[+] - @is_admin
[+] - @god_only
[+] - @only_groups
[+] - @only_pro
[+] - @only_group
[+] - @is_bot_admin
[+] - @peru_only
[+] - @only_pvt
```
