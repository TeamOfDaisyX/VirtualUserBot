"""Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .karb //as a reply to any text message

Thanks to dev for THIS PLUGIN"""

import os
import random
from time import sleep
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fridaybot import CMD_HELP

from ..utils import admin_cmd


# @borg.on(events.NewMessage(pattern=r"\.karb ", outgoing=True))
@borg.on(admin_cmd(pattern="karb"))
async def carbon_api(e):
    RED = random.randint(0, 256)
    GREEN = random.randint(0, 256)
    BLUE = random.randint(0, 256)
    THEME = [
        "3024-night",
        "a11y-dark",
        "blackboard",
        "base16-dark",
        "base16-light",
        "cobalt",
        "dracula",
        "duotone-dark",
        "hopscotch",
        "lucario",
        "material",
        "monokai",
        "night-owl",
        "nord",
        "oceanic-next",
        "one-light",
        "one-dark",
        "panda-syntax",
        "paraiso-dark",
        "seti",
        "shades-of-purple",
        "solarized",
        "solarized%20light",
        "synthwave-84",
        "twilight",
        "verminal",
        "vscode",
        "yeti",
        "zenburn",
    ]

    CUNTHE = random.randint(0, len(THEME) - 1)
    The = THEME[CUNTHE]

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """A Wrapper for carbon.now.sh"""
        await e.edit("⬜⬜⬜⬜⬜")
        CARBON = "https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C.{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}"
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[6:]:
            pcode = str(pcode[6:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, T=The, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        prefs = {"download.default_directory": "./"}
        chrome_options.add_experimental_option("prefs", prefs)
        await e.edit("⬛⬛⬜⬜⬜")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options
        )
        driver.get(url)
        download_path = "./"
        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )
        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {"behavior": "allow", "downloadPath": download_path},
        }
        driver.execute("send_command", params)

        driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
        # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
        # sleep(5)
        await e.edit("⬛⬛⬛⬜⬜")
        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        # sleep(5) #Waiting for downloading

        await e.edit("⬛⬛⬛⬛⬛")
        file = "./carbon.png"
        await e.edit("✅RGB Karbon Completed, Uploading...........")
        await e.client.send_file(
            e.chat_id,
            file,
            caption="Carbonised by [VirtualUserbot](https://github.com/inukaasih/virtualuserbot)",
            force_document=False,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove("./carbon.png")
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


CMD_HELP.update(
    {
        "carbonRBG": ".karb <reply to text> "
        "\nCreate a cool random colorful carbon image for that text 😂😂(not work in media)"
    }
)
