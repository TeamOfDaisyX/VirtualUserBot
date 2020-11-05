<p align="center"><a href="https://t.me/fridayot"><img src="https://telegra.ph/file/22535f8051a58af113586.jpg" width="5000"></a></p> 
<h1 align="center"><b>FRIDAY-USERBOT 🇮🇳 </b></h1>
<h4 align="center">A Powerful, Smart And Simple Userbot In Telethon.</h4>

<h1 align="center"><b>For any query or want to know how it works join Group And Channel</b></h1>

<p align="center"><a href="https://t.me/FridaySupportOfficial"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a></p>
<p align="center"><a href="https://t.me/fridayOT"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a></p>

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/FridaySupportOfficial"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>

<a href="https://t.me/fridayOT"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

## HOW TO DEPLOY 

<a href="https://youtu.be/xfHcm_e92eQ"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>


### Host Friday In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/StarkGang/FridayUserbot)

## Telegram-String

[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://friday.midhunkm1294.repl.run)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/starkGang/Fridayfridaybot
cd FridayUserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m fridaybot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `fridaybot/Configs.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars
```
[+] Only two of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    
[+] The fridaybot will not work without setting the mandatory vars.
```
## Credits 
`[+] Check Contribution At https://github.com/StarkGang/FridayUserbot/graphs/contributors`

  
## Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

FridayUserbot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 
