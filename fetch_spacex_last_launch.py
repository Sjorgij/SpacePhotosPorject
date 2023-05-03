import argparse
import requests
from image_saver import path_direction

def main():
    parser = argparse.ArgumentParser(description="Программа загружает фотографии с запуска ракет")
    parser.add_argument("path", help="Путь к папке, куда сохранить изображения")
    parser.add_argument("--id", help="ID желаемого запуска. Оставьте пустым, что бы загрузить фото с последнего запуска")
    args = parser.parse_args()
    if not args.id: args.id = "latest"
    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    response = requests.get(url)
    for image in response.json()["links"]["flickr"]["original"]:
        path_direction(image, args.path)

if __name__ == "__main__":
    main()