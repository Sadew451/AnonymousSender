import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

SD = Client('Anonymous-Sender',
                  api_id=var.API_ID,
                  api_hash=var.API_HASH,
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="helper"))

SD.run()
