from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup

SD = Client("anymouse sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

START_TEXT = """Hey I am **Anonymous Sner Bot.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!
Made by @SDBotsz"""

REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("👥 Group",
                          url="https://t.me/SDBotz")],
    [InlineKeyboardButton("🔊 Channel",
                          url="https://t.me/SDBOTs_Inifinity")]])

@SD.on_message(filters.command('start') & filters.private)
async def start(client, message):    
    await message.reply_text(START_TEXT,
                             reply_markup=REPLY_MARKUP)

@SD.on_message(filters.caption & filters.private)
async def addorno(client, message):
    msg = message.message._id
    await message.reply_text('start bot go to the option', quote=True,
    reply_markup=InlineKeyboardMarkup([InlineKeyboardButton(text="yes",
    callback_data=f"yes-{msg}"),
    InlineKeyboardButton(text="No",
    callback_data=f"no-{msg}")])
    )

@SD.on_message(filters.private & filters.text | filters.media)
async def SDBot(client, message):
    await message.copy(message.chat.id)

SD.run()
