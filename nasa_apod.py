from dotenv import load_dotenv
import argparse
import requests
import os
from image_saver import save_to

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Программа загружает фотографии космоса")
    parser.add_argument("count", help="Количество фотографий", type=int)
    parser.add_argument("path", help="Путь к папке, куда сохранить изображения")
    args = parser.parse_args()
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": os.environ["NASA_TOKEN"],
        "count": args.count
    }
    response = requests.get(url, params = params)
    response.raise_for_status()
    for image_url in response.json():
        save_to(image_url["url"], args.path)

if __name__ == "__main__":
    main()