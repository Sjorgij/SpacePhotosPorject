from dotenv import load_dotenv
import telegram
import os
import argparse
import random
import time

FILE_MAX_SIZE_IN_BYTES = 20 * 1024**2

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Программа загружает фотографии в телеграм")
    parser.add_argument("--path", help = "Путь к папке, откуда брать изображения. Оставьте пустым, чтобы изображения выбирались случайно", default = f"{random.choice(os.listdir('images'))}")
    args = parser.parse_args()
    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])
    delay = int(os.environ["PUBLICATION_DELAY"]) * 3600
    chat_id = os.environ["TG_CHAT_ID"]
    while True:
        path = f"images/{args.path}"
        images = os.listdir(path)
        random.shuffle(images)
        for image in images:
            image = f"{path}/{image}"
            if os.stat(image).st_size >= FILE_MAX_SIZE_IN_BYTES:
                continue
            bot.send_message(chat_id=chat_id, text="Посмотрите, как прекрасен космос!")
            with open(image, "rb") as document:
                bot.send_document(chat_id=chat_id, document=document)
            time.sleep(delay)

if __name__ == "__main__":
    main()

