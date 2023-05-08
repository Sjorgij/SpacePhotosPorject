from dotenv import load_dotenv
import argparse
import requests
import os
from image_saver import save_to

def main():
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
        image_info = {
            "url": "https://api.nasa.gov/EPIC/archive/natural",
            "date": image["date"].split()[0].replace("-", "/"),
            "name": f"{image['image']}.png"
        }
        url = f"{image_info['url']}/{image_info['date']}/png/{image_info['name']}"
        url = requests.get(url, params = params).url
        save_to(url, args.path)

if __name__ == "__main__":
    load_dotenv()
    main()