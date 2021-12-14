import pyrogram
from pyrogram import Client as pyrogram, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from script import script

helpbutton = [[
        InlineKeyboardButton(f' Channel ', url="https://t.me/SDBOTs_inifinity"),
        InlineKeyboardButton(f'♀️ Support♀️', url="https://t.me/SDBOTz")
        ],[
        InlineKeyboardButton(f' About', callback_data="about")
    ]]

aboutbutton = [[
        InlineKeyboardButton(f' How To Use', callback_data="help"),
        InlineKeyboardButton(f'Close ', callback_data="close_data")
    ]]


@pyrogram.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)

    elif update.data == "help":
        await update.answer()
        keyboard = InlineKeyboardMarkup(helpbutton)
        await update.message.edit_text(
            text=script.HELP_USER,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    elif update.data == "about":
        await update.answer()
        keyboard = InlineKeyboardMarkup(aboutbutton)
        await update.message.edit_text(
            text=script.ABOUT_ME,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    elif update.data == "close_data":
        await update.message.delete()

        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
