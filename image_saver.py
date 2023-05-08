import urllib.parse
import requests
import pathlib
import os

def file_format(image_link):
    name_ext = os.path.splitext(os.path.split(urllib.parse.urlsplit(image_link).path)[1])
    image = {
      "name": urllib.parse.unquote(name_ext[0]),
      "format": name_ext[1]
    }
    return image

def save_to(url_request, path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url_request)
    response.raise_for_status()
    image =  file_format(response.url)
    filename = f"images/{path}/{image['name']}{image['format']}"
    with open(filename, "wb") as file:
        file.write(response.content)
