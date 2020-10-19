from userbot.utils import sudo_cmd, friday_on_cmd, edit_or_reply
from selenium import webdriver

@friday.on(friday_on_cmd(pattern="wshot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    sedlyfstarky = await event.edit("Capturing Webshot, Stay Tuned.")
    driver = webdriver.Chrome()
    driver.get(urlissed)
    stark_img = driver.get_screenshot_as_file('Webshot-@fridayot.png')
    imgpath = "Webshot-@fridayot.png"
    await sedlyfstarky.edit("Completed. Uploading in Telegram..")
    await borg.send_file(event.chat_id, file=imgpath, caption=f"**WEBSHOT OF** `{urlissed}` \n**Powered By @Fridayot**")

