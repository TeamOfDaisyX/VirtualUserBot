


<h1 align="center"><b> Virtual-USERBOT 🇱🇰  </b></h1>
<h4 align="center">A Powerful, Smart And Simple Userbot with 300+ Plugins <br> ... Remodied Friday for Sri Lanka ...</h4>

<p align="center">
    <a href="https://github.com/Infinity-bots/virtualuserbot/commits/master"><img src="https://img.shields.io/github/last-commit/infinity-bots/virtualuserbot/master?label=Last%20Commit&style=flat-square&logo=github&color=F10070" alt="Commit" /></a>
    <a href="https://github.com/Infinity-bots/virtualuserbot/stargazers"><img src="https://img.shields.io/github/stars/infinity-bots/virtualuserbot?label=Stars&style=flat-square&logo=github&color=F10070" alt="Stars" /></a>
    <a href="https://github.com/Infinity-bots/virtualuserbot/network/members"><img src="https://img.shields.io/github/forks/infinity-bots/virtualuserbot?label=Fork&style=flat-square&logo=github&color=F10070" alt="Fork" /></a>
</p>

<p align="center"><a href="https://techwizardent.com/blog/twe_blog_userbot.php"><img src="https://telegra.ph/file/4e1364fb18f899ad47dec.png" width="400"></a></p> 


### BASED ON FRIDAY v7. 

### BTW FRIDAY USERBOT v8 AVAILABLE BY NOW. A POWERFUL AND SECURE USERBOT BUILD FROM SCRATCH
### https://github.com/devsexpo/fridayuserbot

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Inukaasith/virtualuserbot)

## HEROKU ERROR FIXED. BTW USE FRIDAY INSTEAD

# 😍 Credits
### Cloned from [Friday Userbot](github.com/starkgang/fridayuserbot) on 28/01/2021.. Full credits to Friday Developers 
#### Special thanks To Friday Bot And Dark Cobra Bot a lot
##### ♡ Friday is the best userbot ♡ ~ This is just a remodification.. Original work was done by them

 
● Most of the plugins in this are developed FridayUserbot and many others..
So, all respect and credits goes to them

● Also original owners of modules mentioned at the top of every module.

``` Full credits mentioned at the bottom```

◇ It is recommend you to use the [Friday Userbot](github.com/starkgang/fridayuserbot). It is more better than other userbots

# 

# 🧙‍♀️ Deploy Guide
Complete guide on deploying VirtualUserbot to Heroku.

<p align="left"><ba href="https://youtu.be/hMhcKxNi-vw"><img src="https://telegra.ph/file/35c283a78116be8499da0.png" width="300"></a></p> 
<a href="https://youtu.be/hMhcKxNi-vw"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>

☆ Video by [TWE](http://techwizardent.com/) ☆

# ❤️ Support

<a href="https://t.me/Infinity_Bots"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>

<a href="https://t.me/infinityje"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

### Please Star this repo If you are deploying this Userbot

<p align="left">
  
  <a href="https://github.com/inukaasith/virtualuserbot">
    <img src="https://img.shields.io/github/stars/inukaasith/virtualuserbot?style=social">
  </a>
</p>

### Also show some support to the base project [Friday Userbot](github.com/starkgang/fridayuserbot)

# 🕵️‍♀️ Before You Go 



## 1)   AppID and API HASH

Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Turn on Inline mode for the bot

## 2)   String Session (Need before deploying)
This is the way thar your userbot connects with you. Need an AppID ApiHash and a username to go..

[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://repl.it/@InukaAsith/VirtualUserbot#main.py)



## 3)   Heroku API

Create a account on [Heroku](dashboad.heroku.com) first. Then goto settings scroll to bottom. Reaveal API and get api

## 4)   Plugin Channel and Private Group ID

Create a private group on Telegram.
Add [MissRoseBot](t.me/missrosebot) to you group and give Admin permissions.
Turn Chat history for members in Manage group
send ```/id``` and get the group's ID

## 5)  Bot Language  (Si or En)

### VirtualUserbot Support Multiple languages..
#### Currently Available Languages are
- Sinhala (si)
- English (en)

Enter ```si``` or ```en``` in lang section while deploying to deploy bot in desired Language

#### You can always change Languages by sending

To Sinhala =>
```.set var lang si```
To English =>
``` .set var lang en```


# 




# 🏃‍♂️ Deploying To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Inukaasith/virtualuserbot)

``` Always try to  Deploy this source. If not you will miss the future updates```

# 
 
 

#  🤴 After Deploying Steps

## 1) Turn Heroku Dynos ON
Dynos are used on heroku. On free accounts You will get 600 free dyno hours. When you link your CC you will get aditional 400 dyno for free.

Ater Building app is completed.. Goto [Heroku](dashboad.heroku.com), Select your app and goto *Resources Tab*.
Then turn  * worker bash start.sh * to ON

## 2) Check you logs
Chack Heroku logs then.. If you done any mistakes they will shown there.

## 3) Goto telegram and check your Superpowers
Goto telegram and send .help to see the help of your Userbot

#


# 🦹‍♀️ What is the message sending to users who message you

### Virtual Userbot has a PM Protection service ( It was just copied from Friday Project)

Send ```.a``` to approove users to PM you 
and, ```.da``` to disapproove 

If you Dont like this send ```.set var PM_DATA DISABLE```


# 
<details>
<summary>-MORE INFO HERE -</summary>

# String Session (Hard Way)

## [Using the Bot](https://t.me/stringsessionbot) (Not Recommended)
[![Use Our Bot](https://img.shields.io/badge/StringSessionGenerator-Use%20Bot-brightgreen)](https://t.me/stringsessionbot)
Simply clone the repository and run the main file:
```sh
# Install Git First.
git clone https://github.com/Inukaasith/VirtualUserbot
# Open Git Cloned File
cd FridayUserbot
# Config Virtual Env
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
# Install All Requirements 
pip install -r requirements.txt
# Create local_config.py with variables as given below
# Start Bot 
python3 -m virtualuserbot
```







# Mandatory Vars
```
[+] Only two of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    
[+] The virtualUserbot will not work without setting the mandatory vars.
```






# Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

VirtualUserbot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 
</details>

# 
 
# 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/inukaasith/virtualuserbot/graphs/commit-activity)

# Full Credits

- FridayUserBot ❤️ - 
Most of the Plugins Taken from this Project.. Made possible by this. Full Credits. Full Respect
Best userbot ever

- DarkCobra 😍 - 
Image Tools Plugins Copied from DC Project.. Credits to DC Team

- CatUserbot - 
Internal Core Plugins taken.. Helped a lot to fix bugs in source.. Full respect

- Uniborg - 
Userbots Made possible. Credits

- TeleBot - 
Speed Boosted by the help of this source code.. Credits

- Black Lightning - 
Got Fun tools from this.. Respect


# 🧐 Disclaimer 

### Use at your Own Risk 😇
Virtualuserbot don't have any torrent leeching plugins.. So risk of bans in TG is low
But somehow if you get banned or anything happened WE ARE NOT RESPONSIBLE FOR THEM

### Report Errors only to virtualuserbot developers

There are various plugins in virtualuserbot owned by Friday and other userbots.. 
All the plugins are reconfigured for for virtualuserbot. So if you have any errors please report only to the virtualuserbot developers

### If you are using adult content in the bot or if you harm someone with fun plugins of the bot you might get banned from Telegram. We are not responsible for that 😅

## ❤️ Made possible by [Friday Project](https://github.com/StarkGang/FridayUserbot) and many other opensource projects.. ❤️

### 😍 Project by [Infinity_Bots](https://t.me/Infinity_Bots)  😍
