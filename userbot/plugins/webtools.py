from userbot.utils import sudo_cmd, friday_on_cmd, edit_or_reply
from selenium import webdriver
import requests
from iplookup import iplookup


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
    
    
@friday.on(friday_on_cmd(pattern="lp ?(.*)"))
async def _(event):
    if event.fwd_from:
            return
    try:
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain="+gone
        await event.edit("Fecthing Website Info ! Stay Tuned. This may take some time ;)")
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (f'Domain Name => {sed["domain"]} \nCreated On => {sed["create_date"]} \nDomain ID => {sed["domain_id"]} \nHosted ON => {kek["url"]}'
         f'\nLast updated => {sed["update_date"]} \nExpiry Date => {sed["expire_date"]} \nDomain Age => {sed["domain_age"]}'
         f'\nOwner => {km["name"]} \nCountry => {km["country"]} \nState => {km["region"]}'
         f'\nPhone Number => {km["phone"]} \nDomain Ip => {okthen}')
        await event.edit(sedlyf)
    except Exception as e:
        await event.edit(f'Something went wrong \nERROR => {e}')
