from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup

API_ID = ("4165223")
API_HASH = ("972c118766f5e4a76847c1ffdb7d9a04")
BOT_TOKEN = ("2100965681:AAH_09Shvy-kaHyioHnPJlUa2Y5z88zUbNY")

SD = Client("anymouse sender", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

STICKER = "CAACAgEAAxkBAAEByPxhuFGJrPxtyuVHqhUDlwLBFyx3uAACrAIAArx2eUS2Q-OWqN3gZyME"

START_TEXT = """👋 Hey I am **Anonymous Sender Bot.** 

Just Forward me Some messages or media and I will **Anonymouse** that !!

- Server : [Heroku](Heroku.com)
- Library : [Pyrogram](https://github.com/pyrogram/pyrogram)

Made by @SDBotsz."""

REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="👩‍💻 Creater", url="https://t.me/Itz_Sadew"),
        InlineKeyboardButton(
            text="👥 Support Group", url=f"https://t.me/SDBotz")],
    [InlineKeyboardButton(text="🙋‍♀️ Update Channel", url=f"https://t.me/SDBOTs_Inifinity"),
        InlineKeyboardButton(
            text="💾 Scource Code", url=f"https://github.com/Sadew451")]])

@SD.on_message(filters.command('start') & filters.private)
async def start(client, message):    
    await message.reply_sticker(STICKER)
    await message.reply_text(START_TEXT,
                             reply_markup=REPLY_MARKUP)
                             disable_web_page_preview=True,
    
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

print("Bot is Started")
print("Join @SDBotsz.")
SD.run()
