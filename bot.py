from dotenv import load_dotenv
import telegram
import os
import argparse
import random
import time

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Программа загружает фотографии в телеграм")
    parser.add_argument("--path", help="Путь к папке, откуда брать изображения. Оставьте пустым, чтобы изображения выбирались случайно", default=f"{random.choice(os.listdir('images'))}")
    args = parser.parse_args()
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    delay = int(os.environ["PUBLICATION_DELAY"]) * 3600
    while True:
        path = f"images/{args.path}"
        images = os.listdir(path)
        random.shuffle(images)
        for image in images:
            image = f"{path}/{image}"
            if os.stat(image).st_size >= 20 * 1024**2:
                continue
            bot.send_message(chat_id=os.environ["CHAT_ID"], text="Посмотрите, как прекрасен космос!")
            bot.send_document(chat_id=os.environ["CHAT_ID"], document=open(image, "rb"))
            time.sleep(delay)

if __name__ == "__main__":
    main()

