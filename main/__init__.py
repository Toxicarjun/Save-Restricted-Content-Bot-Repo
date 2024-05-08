#Join me at telegram @Privatearjun

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("13892075", default=None, cast=int)
API_HASH = config("e3b8632e5034801fbeaea7aa3283f442", default=None)
BOT_TOKEN = config("6877763529:AAHHqDbHnSu2_I8h_ktcYQT6TrUjAkZicMM", default=None)
SESSION = config("BADT-esAop9llYIB6jXDFmEBHZyA73YU7ha7B1jauPD-csQw_pbkpra5J6V2hrepyOzcNzSmsvMiLXpjVO0drx5_-bycKblIXN9xasjILW9ND-kpywmGomeymPfH99Yenle0DkRclBRhgOFoOQT50dT4RRdraYBKDYL2jt5d6dO-oBDVlTfQZKXR6E_Vn08B1hxJstloRMKn7cRWas2-UwtfcrJCgFnAqCU36pKd8rvHE2TRedP4kZVDdYrKcEbeHVK7g4moQu5JncI2Z8xXxw0awhTaKKLl46dtTXlSyjO3OR8rfE8cyb7Oj7Cpvn9ISEd2ym42VJNCt2hY4ZOE7ItbhfNUsgAAAAGBTrCyAA", default=None)
FORCESUB = config("privatearjun", default=None)
AUTH = config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
