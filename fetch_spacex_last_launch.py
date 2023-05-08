import argparse
import requests
from image_saver import save_to

def main():
    parser = argparse.ArgumentParser(description="Программа загружает фотографии с запуска ракет")
    parser.add_argument("path", help="Путь к папке, куда сохранить изображения")
    parser.add_argument("--id", help="ID желаемого запуска. Оставьте пустым, что бы загрузить фото с последнего запуска", default="latest")
    args = parser.parse_args()
    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    response = requests.get(url)
    for image in response.json()["links"]["flickr"]["original"]:
        save_to(image, args.path)

if __name__ == "__main__":
    main()