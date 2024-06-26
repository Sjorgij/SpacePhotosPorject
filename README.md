# Загрузка изображений космоса

Программа может скачивать фотографии сделанные SpaceX и NASA.
К программе прилагается телеграм-бот публикующий эти фото.

### Как установить

Для корректрой работы программы необходимо использовать токен NASA. Получить токен можно в [по ссылке](https://api.nasa.gov).<br>
Токен должен иметь вид sa0m0p000000let0ok0000e00n000a0mp0le000.<br>
Также необходимо зарегистрировать бота используя [ОтцаБотов](https://telegram.me/BotFather).<br>
После регистрации вы получите токен бота, он будет иметь вид 0123456789:SAmpl3T0ken54MP1E7OK3NN.<br>
Токен для управления ботом должен быть сохранен в переменной окружения TG_BOT_TOKEN.<br>
Бота необходимо пригласить в чавт и узнать ID этого чата, можно воспользоваться [Ботом](https://t.me/getmyid_bot).<br>
ID чата тоже надо сохранить в переменной окружения - TG_CHAT_ID.<br>
С помощью переменной окружения PUBLICATION_DELAY можно настроить частоту публикаций фотографий. Необходимо указать целое количество часов.<br>
<br>
Python3 должен быть уже установлен. <br>
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Пример запуска программы:
```
python nasa_epic.py new_earth_photos
```
В выбранную папку скачиваются последние снимки земли из космоса
```
nasa_apod.py 10 new_space_photos
```
В выбранную папку скачивается выбранное кол-вол фотографий
```
fetch_spacex_last_launch.py new --id 5eb87d47ffd86e000604b38a
```
В выбранную папку будут скачаны фотографии с выбранного запуска
```
python bot.py
```
Будет выбрана случайная папка внутри директории images. Из нее в случайном порядке будут опубликованы все фото. После окончания публикации папка будет выбрана заново случайным образом.
```
python bot.py --path ИМЯ_ПАПКИ
```
Из папки ИМЯ_ПАПКИ внутри images будут опубликованы все фото в случайном порядке. Когда будет опубликована последняя фотография, порядок будет изменен случайным образом и публикация продолжится.
### Цель проекта

Код написан в образовательных целях.
