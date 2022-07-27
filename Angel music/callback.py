## ©copyright infringement on team comrade

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from modules.clientbot.queues import queues, clear          
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from modules.clientbot.clientbot import client
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from modules.clientbot import clientbot
from modules.config import GROUP, NETWORK, BOT_USERNAME

## don't change any value in this repo if you change the value bot will crash your heroku accounts. 

menu_keyboard = InlineKeyboardMarkup(
    [
        [
            
            InlineKeyboardButton("▷", callback_data="resume_vc"),
            InlineKeyboardButton("II", callback_data="pausevc"),
            ],[
            InlineKeyboardButton("‣‣I", callback_data="skip_vc"),
            InlineKeyboardButton("▢", callback_data="stop_vc"),
            ],[
            InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close"), 
        ], 
     ]
 ) 
    


@Client.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ {query.message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ.. 

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade) !**
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📚ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("✨ғᴜᴄᴋᴇʀ✨", url="https://t.me/about_bobby"), 
            ],[
            InlineKeyboardButton("🐾sᴜᴘᴘᴏʀᴛ🐾", url=f"https://t.me/comrade_botz"), 
            InlineKeyboardButton("🐾ᴄʜᴀɴɴᴇʟ🐾", url=f"https://t.me/comrade_robots"), 
            ],[
            InlineKeyboardButton("🔺 ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔺", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
   

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("opening command list", show_alert=True) 
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ ʜᴇʟʟᴏ ɴᴀᴍsᴛʜᴇ ᴀɴɴᴀ ᴛʜɪs ɪs ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ɢᴜɪᴅᴇ ᴡʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ɴᴇᴅᴅ sᴇʟᴇᴄᴛ ʜᴇʀᴇ.. 

➠ ᴛʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴀᴍɪʟ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/comrade_robotz) 
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📚ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="general_list"), 
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
            InlineKeyboardButton("◁", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
async def general_list(_, query: CallbackQuery):
    await query.answer("opening general commands", show_alert=True)
    await query.edit_message_text(
        f"""🥳 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ\n
➠ /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ\n
➠ /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ\n
➠ /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs\n
➠ /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs\n
➠ /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)\n
➠ /help - ᴛᴏ sʜᴏᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ (ғᴜʟʟ ʙᴏᴛ ɢᴜɪᴅᴇ)\n
➠ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
async def skip_list(_, query: CallbackQuery): 
    await query.answer("skiped current song")
    await query.edit_message_text(
        f"""🚩 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/skip ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ sᴋɪᴘ ᴛᴏ ɴᴇxᴛ sᴏɴɢ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(_, query: CallbackQuery):
    await query.answer("pause current playing song")
    await query.edit_message_text(
        f"""💘 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/pause ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ɪɴ ɢʀᴏᴜᴘ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/comrade_botz)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(_, query: CallbackQuery): 
    await query.answer("resume current playing song")
    await query.edit_message_text(
        f"""❤ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/resume ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/comrade_robotz)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(_, query: CallbackQuery):
    await query.answer("stopping current playing song")
    await query.edit_message_text(
        f"""💓 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/end ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴇɴᴅ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/comrade_botz)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(_, query: CallbackQuery):
    await query.answer("playing song in vc")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/play ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴘʟᴀʏ ᴀ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("source"))
async def source(_, query: CallbackQuery): 
    await query.answer("team shadow source code")
    await query.edit_message_text(
        f"""❣️ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠  **ᴀɴɢᴇʟ ᴍᴜsɪᴄ sᴏᴜʀᴄᴇ ɪs ᴄᴏᴍᴘʟᴇᴛᴇ ᴄʟᴏsᴇᴅ sᴏᴜʀᴄᴇ ʀᴇᴘᴏʀᴛɪɴɢ ᴀɴʏ ʙᴜɢs ᴏʀ ʀᴇᴘᴏʀᴛs ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade)!**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 ʙɪɴ", callback_data="close_panel")]]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

💘 ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ ɪs ᴀ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ɪɴ sᴏ ᴍᴀɴʏ sᴇʀᴠᴇʀ's, ɪᴛ's ᴏɴʟɪɴᴇ sɪɴᴄᴇ 𝟷sᴛ ᴊᴜɴᴇ 𝟸𝟶𝟸𝟸 ᴀɴᴅ ɪᴛ's ᴄᴏɴsᴛᴀɴᴛʟʏ ᴜᴘᴅᴀᴛᴇᴅ \n
💝 ᴛʜɪs ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ](https://t.me/tamil_comrade) \n 
❣️ © ᴏɴ ᴏғ [ʙᴏʙʙʏ](https://t.me/about_bobby)
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 ʙɪɴ", callback_data="close_panel")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("pausevc"))
async def pausevc(_, query: CallbackQuery, message: Message):
    if query.message.sender_chat:
        return await query.answer("ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💞 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    chat_id = query.message.chat.id
    if queues.Queue(chat_id):
        try:
            await clientbot.pytgcalls.pause_stream(message.chat.id)
            await query.edit_message_text(
                "ɪɪ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ ʜᴀs ᴘᴀᴜsᴇᴅ", 
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await query.answer("🚫 ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ ɴᴏᴡ", show_alert=True)


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("menu")) 
async def menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.edit_message_text(
        text=f"""ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴛᴇᴀᴍ ᴄᴏᴍʀᴀᴅᴇ""",
        disable_web_page_preview=True, 
        reply_markup=menu_keyboard
    ) 



