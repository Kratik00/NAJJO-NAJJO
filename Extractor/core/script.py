import config
from config import ADMIN_BOT_USERNAME


# ------------------------------------------------------------ #
IMG = [
"https://graph.org/file/d81baf8451cf1627ae3f6-c819d31887f32db07d.jpg",
"https://graph.org/file/b29c2581eab59309d72cf-86cea750f2e54d6798.jpg",
"https://graph.org/file/37eae141246f30803c113-f2a0774fc851ca0562.jpg",
"https://graph.org/file/4afaa8ad4b2f757bdf9d7-47d5f883ea944a498d.jpg",
"https://graph.org/file/153308ce2d6f968e25965-d310556f3d191bcc62.jpg",
]

START_TXT = """
**ʜᴇʟʟᴏ** {},

**<blockquote>ɪ'ᴍ ᴀᴅᴇᴘᴛ ᴀᴛ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴏɴʟɪɴᴇ ᴄᴏᴜʀsᴇs ᴡɪᴛʜ ᴄᴜᴛᴛɪɴɢ-ᴇᴅɢᴇ ᴛᴇᴄʜɴᴏʟᴏɢʏ. ɪ'ᴠᴇ ᴍᴀɴᴀɢᴇᴅ ᴛᴏ ɢᴀᴛʜᴇʀ ʟɪɴᴋs ғᴏʀ ᴀʟᴍᴏsᴛ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴜʀsᴇs, ᴍᴀᴋɪɴɢ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴇғғᴏʀᴛʟᴇss ᴀɴᴅ ᴇғғɪᴄɪᴇɴᴛ.</blockquote>**

**<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/urs_lucifer">Aᴅᴍɪɴ 🫠</a></blockquote>**
"""

FORCE_MSG = """
**ʜᴇʏ** {}

**<blockquote>ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !</blockquote>**

**<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/urs_lucifer">Aᴅᴍɪɴ 🫠</a></blockquote>**
"""

MODES_TXT = """
**<blockquote>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴍᴏᴅᴇ sᴇᴄᴛɪᴏɴ. ʜᴇʀᴇ, ʏᴏᴜ ᴄᴀɴ ᴄʜᴏᴏsᴇ ʙᴇᴛᴡᴇᴇɴ ᴛᴡᴏ ᴍᴏᴅᴇs: ʟᴏɢɪɴ ᴍᴏᴅᴇ ᴏʀ ᴡɪᴛʜᴏᴜᴛ ʟᴏɢɪɴ ᴍᴏᴅᴇ.</blockquote>**
"""

CUSTOM_TXT = """
⌬ **﹝𝐖 𝐈 𝐓 𝐇 𝐎 𝐔 𝐓 𝐋 𝐎 𝐆 𝐈 𝐍﹞**

**<blockquote>ɪɴ ᴡɪᴛʜᴏᴜᴛ ʟᴏɢɪɴ ᴍᴏᴅᴇ, ʏᴏᴜ ᴄᴀɴ ᴇxᴛʀᴀᴄᴛ ᴀɴʏ ᴄᴏᴜʀsᴇ ғʀᴏᴍ ᴀɴʏ ᴀᴘᴘ's ʟɪɴᴋ, ʙᴜᴛ ʏᴏᴜ'ʟʟ ɴᴇᴇᴅ ᴀɴ ᴘʀᴇᴍɪᴜᴍ ғᴏʀ ᴛʜᴀᴛ.</blockquote>**

"""

MANUAL_TXT = """
⌬ **﹝𝐋 𝐎 𝐆 𝐈 𝐍﹞**

**<blockquote>ɪɴ ʟᴏɢɪɴ ᴍᴏᴅᴇ, ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs. ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴏɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴛʜᴇ ᴄᴏᴜʀsᴇ ʏᴏᴜ ᴡᴀɴᴛ.</blockquote>**
"""


PLANS_TXT = """
⌬ **﹝𝐏 𝐑 𝐄 𝐌 𝐈 𝐔 𝐌﹞**

<b><blockquote>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴇxᴄʟᴜsɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ sᴇᴄᴛɪᴏɴ, ᴡʜᴇʀᴇ ʏᴏᴜ'ʟʟ ғɪɴᴅ ᴄᴜʀᴀᴛᴇᴅ ɪɴsɪɢʜᴛs ᴀɴᴅ ᴇxᴘᴇʀɪᴇɴᴄᴇs ᴛᴀɪʟᴏʀᴇᴅ ᴛᴏ ᴛʜᴏsᴇ sᴇᴇᴋɪɴɢ ᴛᴏᴘ-ᴛɪᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ sᴇʀᴠɪᴄᴇs.</blockquote>

<blockquote>‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</blockquote></b>
**<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Xyzaxv">Aᴅᴍɪɴ 🫠</a></blockquote>**
"""

    
FREE_TXT = """
⌬ **﹝𝐅 𝐑 𝐄 𝐄﹞**
<b>
🏆 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🏆
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ʙʏᴘᴀss ᴀʟʟ ᴄᴏᴜʀsᴇ
○ ғᴀsᴛ ɴᴏᴅᴇ 
</b>"""

BRONZE_TXT = """
⌬ **﹝𝐁 𝐑 𝐎 𝐍 𝐙 𝐄﹞**
<b>
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 7 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 300₹
</b>"""

SILVER_TXT = """
⌬ **﹝𝐒 𝐈 𝐋 𝐕 𝐄 𝐑﹞**
<b> 
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 15 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 500₹
</b>"""

GOLD_TXT = """
⌬ **﹝𝐆 𝐎 𝐋 𝐃﹞**  
<b>
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 800₹
</b>"""


OTHER_TXT = """
⌬ **﹝𝐏 𝐋 𝐀 𝐍 𝐒﹞** 
<b>
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.
</b>"""


PAYMENT_TXT = """<b>
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/2fbd9fda0f646b1422f05-218a2421d48d601d10.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
</b>"""






