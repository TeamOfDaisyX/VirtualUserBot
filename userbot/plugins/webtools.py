from userbot.utils import sudo_cmd, friday_on_cmd, edit_or_reply
from selenium import webdriver
import requests
import html
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


@friday.on(friday_on_cmd(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    try:
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
           f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
           f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
           f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
           f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n")
        await event.edit(data_is, parse_mode="HTML")
    except:
        await event.edit("Not a Valid Bin Or Don't Have Enough Info.")

                   
@friday.on(friday_on_cmd(pattern="iban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        banks = lol["bankData"]
        kek = (f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
           f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
           f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
           f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
           f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
           f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
           f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n")
        await event.edit(kek, parse_mode="HTML")
    except:
        await event.edit(f"Invalid IBAN Or Doesn't Have Enough Info")
