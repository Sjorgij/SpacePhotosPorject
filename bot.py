from dotenv import load_dotenv
import telegram
import os
from random import choice

load_dotenv()
bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
print(bot.get_me())
#bot.send_message(chat_id=os.environ["CHAT_ID"], text="Посмотрите, как прекрасен космос!")
path = f"images/{choice(os.listdir('images'))}"
bot.send_document(chat_id=os.environ["CHAT_ID"], document=open(f"{path}/{choice(os.listdir(path))}", "rb"))

