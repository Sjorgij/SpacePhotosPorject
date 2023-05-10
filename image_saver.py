import urllib.parse
import requests
import pathlib
import os

def get_file_name_format(image_link):
    image_path = urllib.parse.urlsplit(image_link).path
    image = os.path.split(image_path)[1]
    name_ext = os.path.splitext(image)
    image = {
      "name": urllib.parse.unquote(name_ext[0]),
      "format": name_ext[1]
    }
    return image

def save_to(url_request, path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url_request)
    response.raise_for_status()
    name, ext =  get_file_name_format(response.url).values()
    filename = f"images/{path}/{name}{ext}"
    with open(filename, "wb") as file:
        file.write(response.content)
