## ©copyright infringement on team comrade


import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import GROUP, NETWORK, BOT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

    
   ## don't change any value in this repo if you change the value bot will crash your heroku accounts. 


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bb2448b6c4a377de2e32a.jpg",
        caption=f"""**👋🏻 ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴡɪᴛʜ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade)**
""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📚ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("✨ᴏᴡɴᴇʀ✨", url="https://t.me/about_Bobby"), 
            ],[
            InlineKeyboardButton("🐾sᴜᴘᴘᴏʀᴛ🐾", url=f"https://t.me/{GROUP}"), 
            InlineKeyboardButton("🐾ᴄʜᴀɴɴᴇʟ🐾", url=f"https://t.me/{UPADATE}"), 
            ],[
            InlineKeyboardButton("🔺 ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔺", url=f"https://t.me/Angelmusicrobot?startgroup=true")
            ]]
            ) 
        ) 
     
    
@Client.on_message(commandpro(["/alive"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/468a7a0bf377925dbf0fa.jpg",
        caption=f"""ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀʟɪᴠᴇ ɴᴏᴡ 👻""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="info")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["/repo", "#repo"]) & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/880a44ce9606f7ecec06f.jpg",
        caption=f"""ᴄʜᴇᴄᴋ ɴᴏᴡ😃""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄʜᴇᴄᴋ ɴᴏᴡ☺", url="https://t.me/comrade_botz")
                ]
            ]
        ),
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/80b75c16eac2ad6df5ac3.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command("ghelp") & filters.group & ~filters.edited)
async def gelp(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/59ab3595d5c4e60e0a76f.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("sᴋɪᴘ", callback_data="skip_list"), 
            InlineKeyboardButton("ᴘᴀᴜsᴇ", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("ʀᴇsᴜᴍᴇ", callback_data="resume_list"), 
            InlineKeyboardButton("sᴛᴏᴘ", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="play_list"), 
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="source"), 
            ],[
            InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close"), 
            ]]
            ) 
        ) 


@Client.on_message(command("uptime") & filters.group & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9b70bb1c866ce97de94dc.jpg", 
        caption=f""" 💞 **ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ʙᴏᴛ ᴜᴘᴛɪᴍᴇ**:\n
➠ **ᴜᴘᴛɪᴍᴇ:** **{uptime}**\n
➠ **ᴜsᴇʀ:** **{message.from_user.mention()}**\n
➠ **sᴛᴀʀᴛ ᴛɪᴍᴇ:** **{START_TIME_ISO}**\n
➠ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** **[ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗑 ʙɪɴ", callback_data="set_close")
                ]
            ]
        ),
    )
                 

@Client.on_message(command("ping") & filters.group & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**ᴘɪɴɢɪɴɢ...**")
    delta_ping = time() - start
    await m_reply.edit_text("💝 **ᴘᴏɴɢ!!**\n" f"💖 **{delta_ping * 1000:.3f} ms**")

