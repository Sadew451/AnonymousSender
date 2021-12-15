import logging
from pyrogram import Client
from vars import var

logging.basicconfig(level=logging.INFO)

SD = Client('Anonymous-Sender',
        api_id=var.API_ID,
        api_hash=var.API_HASH,
        bot_token=var.BOT_TOKEN,
        SDBot=dict(root="helper"))

SD.run()
