from dotenv import load_dotenv
import argparse
import requests
import os
from image_saver import save_to

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Программа загружает фотографии Земли из космоса")
    parser.add_argument("path", help="Путь к папке, куда сохранить изображения")
    args = parser.parse_args()
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": os.environ["NASA_TOKEN"]  
    }
    response = requests.get(f"{url}/images", params = params)
    response.raise_for_status()
    for image in response.json():
        img_url: "https://api.nasa.gov/EPIC/archive/natural",
        img_date: image["date"].split()[0].replace("-", "/"),
        img_name: f"{image['image']}.png"
        url = f"{img_url}/{img_date}/png/{img_name}"
        url = requests.get(url, params = params).url
        save_to(url, args.path)

if __name__ == "__main__":
    main()