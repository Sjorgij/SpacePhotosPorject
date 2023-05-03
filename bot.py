from dotenv import load_dotenv
import argparse
import telegram
import os

load_dotenv()
bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
print(bot.get_me())
bot.send_message(chat_id=os.environ["CHAT_ID"], text="I'm sorry Dave I'm afraid I can't do that.")