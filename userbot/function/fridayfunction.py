# Copyright (C) By @StarkGang And @ZeltraxRockz
# Powered By @Nemo_Projects
import random
import string
import os
import re
import shlex
import asyncio
from typing import Tuple, List, Optional

# String Finder
def stark_finder(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# Id Generator
def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

# https://docs.python.org/3/library/asyncio-subprocess.html 
# https://github.com/code-rgb/USERGE-X/blob/master/userge/utils/tools.py#L79
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

