from fridaybot.utils import friday_on_cmd
import asyncio
import os
import time
from datetime import datetime
from fridaybot.Configs import Config
import subprocess
import os
import re
import html
import shlex
import asyncio
from os.path import basename
from typing import Tuple, List, Optional
from telegraph import Telegraph, exceptions, upload_file
telegraph = Telegraph()
tgnoob = telegraph.create_account(short_name="Friday 🇮🇳")

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)

@friday.on(friday_on_cmd(pattern="spotdl (.*)"))
async def kek(event):
    app_name = event.pattern_match.group(1)
    out, err, ret, pid = await runcmd(f'spotdl "{app_name}"')
    await friday.send_file(event.chat_id, file=out, caption="=+  MUSIC +=")
    os.remove(out)
