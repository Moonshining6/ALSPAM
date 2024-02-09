from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ ™°‌ 🫧 ☆𝐕ᴀᴘᴏʀᴇᴏɴ☆ 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽 𝙵𝙾𝚁 𝙷𝙴𝙻𝙿**\n» **𝐃ᴇᴠᴇʟᴏᴘᴇʀ: @queen_huu**"

HELP_BUTTON = [
    [
      Button.inline("⛈◄⏤ 𝐒ᴘᴀᴍ ◄⏤⛈", data="spam"),
      Button.inline("⛈◄⏤ 𝐑ᴀɪᴅ ◄⏤⛈", data="raid")
    ],
    [
      Button.inline("⛈◄⏤ 𝐂ᴏᴍᴍᴀɴᴅꜱ ◄⏤⛈", data="extra")
    ],
    [
      Button.url("⛈◄⏤ 𝐃ᴇᴠᴇʟᴏᴘᴇʀ ◄⏤⛈", "https://t.me/queen_huu"),
      Button.url("⛈◄⏤ 𝐆ᴀʟᴀxʏ ◄⏤⛈", "https://t.me/MILKYYYYY_WAYYY")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/0edf1bf66c01b464e67c3.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**»💘 𝐄𝐗𝐓𝐑𝐀 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐔𝐒𝐄𝐑 𝐁𝐎𝐓💘: **💘𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐂𝐌𝐃𝐒💘**
  1) {hl}𝐏𝐈𝐍𝐆
  2) {hl}𝐑𝐄𝐁𝐎𝐎𝐓
  3) {hl}𝐒𝐔𝐃𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑>  --> 𝐎𝐖𝐍𝐄𝐑 𝐂𝐌𝐃
  4) {hl}𝐋𝐎𝐆𝐒--> 𝐎𝐖𝐍𝐄𝐑 𝐂𝐌𝐃

💘 𝐄𝐂𝐇𝐎: **💘𝐓𝐎 𝐀𝐂𝐓𝐈𝐕𝐄 𝐄𝐂𝐇𝐎 𝐎𝐍 𝐀𝐍𝐘 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐄𝐂𝐇𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐑𝐌𝐄𝐂𝐇𝐎 <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐋𝐄𝐀𝐕𝐄: **💘𝐓𝐎 𝐋𝐄𝐀𝐕𝐄 𝐆𝐑𝐎𝐔𝐏 / 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 💘**
  1) {hl}𝐋𝐄𝐀𝐕𝐄 <𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐓 𝐈𝐃>
  2) {hl} 𝐋𝐄𝐀𝐕𝐄 : 𝐓𝐘𝐏𝐄 𝐈𝐍 𝐓𝐇𝐄𝐈𝐑 𝐆𝐑𝐎𝐔𝐏 𝐁𝐎𝐓 𝐖𝐈𝐋𝐋 𝐀𝐔𝐓𝐎 𝐋𝐄𝐀𝐕𝐄 𝐓𝐇𝐀𝐓 𝐆𝐑𝐎𝐔𝐏 


**© @Moonshining6**
"""

                 
raid_msg = f"""
**» 💘𝐑𝐀𝐈𝐃 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐑𝐀𝐈𝐃: **💘𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐀𝐍𝐘 𝐈𝐍𝐃𝐈𝐕𝐈𝐃𝐔𝐀𝐋 𝐔𝐒𝐄𝐑 𝐅𝐎𝐑 𝐆𝐈𝐕𝐄𝐍 𝐑𝐀𝐍𝐆𝐄 💘**
  1) {hl}𝐑𝐀𝐈𝐃 <𝐂𝐎𝐔𝐍𝐓> <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl}𝐑𝐀𝐈𝐃 <𝐂𝐎𝐔𝐍𝐓> <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐑𝐄𝐏𝐋𝐘𝐑𝐀𝐈𝐃: **💘𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐄𝐏𝐋𝐘 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐑𝐑𝐀𝐈𝐃 <𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐓𝐎 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐑𝐑𝐀𝐈𝐃 <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄>

💘𝐃𝐑𝐄𝐏𝐋𝐘𝐑𝐀𝐈𝐃: **💘𝐃𝐄𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐒 𝐑𝐄𝐏𝐋𝐘 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl}𝐃𝐑𝐑𝐀𝐈𝐃 <𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐓𝐎 𝐔𝐒𝐄𝐑 >
  2) {hl}𝐃𝐑𝐑𝐑𝐀𝐈𝐃 <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄

💘 𝐌𝐑𝐀𝐈𝐃: **💘𝐋𝐎𝐕𝐄 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐌𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄>
  2) {hl} 𝐌𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐒𝐑𝐀𝐈𝐃: **💘𝐒𝐇𝐀𝐘𝐀𝐑𝐈 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐒𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl} 𝐒𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

💘 𝐂𝐑𝐀𝐈𝐃: **💘𝐀𝐁𝐂𝐃 𝐑𝐀𝐈𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑 💘**
  1) {hl} 𝐂𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 >
  2) {hl} 𝐂𝐑𝐀𝐈𝐃 < 𝐂𝐎𝐔𝐍𝐓 > <𝐑𝐄𝐏𝐋𝐘 𝐓𝐎 𝐀 𝐔𝐒𝐄𝐑 >

**© @Moonshining6**💘
"""

spam_msg = f"""
**» 💘𝐒𝐏𝐀𝐌 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 💘:**

💘 𝐒𝐏𝐀𝐌: **💘𝐒𝐏𝐀𝐌𝐒 𝐀 𝐌𝐄𝐒𝐒𝐆𝐀𝐄 💘**
  1) {hl}𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 >  < 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐓𝐎 𝐒𝐏𝐀𝐌 >  (𝐘𝐎𝐔 𝐂𝐀𝐍 𝐑𝐄𝐏𝐋𝐘 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐈𝐅 𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐑𝐄𝐏𝐋𝐘 𝐓𝐇𝐀𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐀𝐍𝐃 𝐃𝐎 𝐒𝐏𝐀𝐌𝐌𝐈𝐍𝐆 )
  2) {hl}𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 > < 𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 > 

💘 𝐏𝐎𝐑𝐍𝐒𝐏𝐀𝐌: **💘𝐏𝐎𝐑𝐍𝐎𝐆𝐑𝐀𝐏𝐇𝐘 𝐒𝐏𝐀𝐌 💘**
  1) {hl}𝐏𝐒𝐏𝐀𝐌 < 𝐂𝐎𝐔𝐍𝐓 > 

💘 𝐇𝐀𝐍𝐆: **💘𝐒𝐏𝐀𝐌𝐒 𝐇𝐀𝐍𝐆 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐅𝐎𝐑 𝐆𝐈𝐕𝐄𝐍 𝐂𝐎𝐔𝐍𝐓𝐄𝐑𝐒 💘**
  1) {hl}𝐇𝐀𝐍𝐆 < 𝐂𝐎𝐔𝐍𝐓𝐄𝐑 >


** © @Moonshining6**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("⛈◄⏤ 𝐒ᴘᴀᴍ ◄⏤⛈", data="spam"),
                Button.inline("⛈◄⏤ 𝐑ᴀɪᴅ ◄⏤⛈", data="raid")
              ],
              [
                Button.inline("⛈◄⏤ 𝐂ᴏᴍᴍᴀɴᴅꜱ ◄⏤⛈", data="extra")
              ],
              [
                Button.url("⛈◄⏤ 𝐇ᴇʟʟ 𝐐ᴜᴇᴇɴ ◄⏤⛈", "https://t.me/queen_huu"),
                Button.url("⛈◄⏤ 𝐆ᴀʟᴀxʏ ◄⏤⛈", "https://t.me/MILKYYYYY_WAYYY")
              ]
            ]
          )
    else:
        await event.answer("★𝐌𝐎𝐎𝐍 𝐊𝐎 𝐃𝐌 𝐊𝐑𝐎 𝐒𝐔𝐃𝐎 𝐊𝐄 𝐋𝐈𝐘𝐄 @MOON_M_6★" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("★𝐌𝐎𝐎𝐍 𝐊𝐎 𝐃𝐌 𝐊𝐑𝐎 𝐒𝐔𝐃𝐎 𝐊𝐄 𝐋𝐈𝐘𝐄 @MOON_M_6★", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("★𝐌𝐎𝐎𝐍 𝐊𝐎 𝐃𝐌 𝐊𝐑𝐎 𝐒𝐔𝐃𝐎 𝐊𝐄 𝐋𝐈𝐘𝐄 @MOON_M_6★", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("★𝐌𝐎𝐎𝐍 𝐊𝐎 𝐃𝐌 𝐊𝐑𝐎 𝐒𝐔𝐃𝐎 𝐊𝐄 𝐋𝐈𝐘𝐄 @MOON_M_6★", cache_time=0, alert=True)
