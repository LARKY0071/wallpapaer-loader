# импортируем модули
import requests
import json
import os
from bs4 import BeautifulSoup as BS4
import time as t
# необходимые переменные
i = 0
a = 0

banner = """
 ____________________________________________________
|                                                    |
| [<0>] Name: WallpapaerLoader                       |
|                                                    |
| [<0>] Site: https://nekos.life                     |
|                                                    |
| [<0>] Created by: Larky#0891                       |
|                                                    |
| [<0>] Discord server: http://discord.gg/Usqvnju    |
|                                                    |
| [<0>] YouTube Guide:                               |
|____________________________________________________|
"""

print(banner)


def NumOfPhotos():
    while True:
        try:
            a = int(input("Количество изображений для загрузки: "))
        except ValueError:
            print("Количество изображений для загрузки: ")
        else:
            break
    return a


def SavePhotos(url, i, path, chose):
    print("начало сохранения изображения #" + str(i))
    format = chose
    if format == "https://nekos.life/api/kiss":
        format = ".gif"
    elif format == "https://nekos.life/api/v2/img/ngif":
        format = ".gif"
    else:
        format = ".jpg"

    if path == "":
        filename = "image" + str(i) + format
    elif path != "":
        filename = path + "\image" + str(i) + format
    else:
        print("При сохранении файла что то пошло не так! (Возможно вы указали не верный или не существующий путь.)")

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as imgfile:
            imgfile.write(response.content)
    print("изображение #" + str(i) + " было успешно сохранено по пути: " + path)


def GetUrl(i, a, path, chose):
    print("Начало загрузки изображений...")
    while i < a:
        i = i + 1
        print("Текущий прогресс: " + "[" + str(i) + "/" + str(a) + "]\n")
        r = requests.get(str(chose))
        html = BS4(r.content, 'html.parser')
        data = json.loads(str(html))
        url = data['url']
        print("Получено изображение: " + url)
        SavePhotos(url, i, path, str(chose))
        t.sleep(1)
        os.system('cls||clear')
    print("Загрузка изображений закончена")


def GetPath():
    getPath = str(input(
        r'Введите путь для сохранения изображений, ничего не вводите для того что бы оставить путь по умолчанию: '))
    return getPath


ChoseBanner = """
 ___________________________________________________
|                                                   |
|               Укажите один вариант:               |
|                                                   |
|                1 - > wallpaper                    |
|                                                   |
|                2 - > hentai                       |
|                                                   |
|                3 - > neko                         |
|                                                   |
|                4 - > kiss                         |
|                                                   |
|                5 - > ngif                         |
|___________________________________________________|
"""


def GetValue():
    print(ChoseBanner)
    cho = str(input("Вариант: "))
    if cho == "wallpaper":
        return "https://nekos.life/api/v2/img/wallpaper"
    elif cho == "hentai":
        return "https://nekos.life/api/v2/img/hentai"
    elif cho == "neko":
        return "https://nekos.life/api/v2/img/neko"
    elif cho == "kiss":
        return "https://nekos.life/api/kiss"
    elif cho == "ngif":
        return "https://nekos.life/api/v2/img/ngif"
    else:
        print("Неверный вариант!")
        quit()


a = NumOfPhotos()
path = GetPath()
chose = GetValue()

if a == 0:
    quit()
elif a >= 1:
    print("lol : " + chose)
    GetUrl(i, a, path, chose)
else:
    print("Что-то пошло не так!")

Endbanner = """
 ___________________________________________________
|                                                   |
|             Спасибо за использование!             |
|                                                   |
| [<0>] Site: https://nekos.life                    |
|                                                   |
| [<0>] Created by: Larky#0891                      |
|                                                   |
| [<0>] Discord server: http://discord.gg/Usqvnju   |
|                                                   |
| [<0>] My GitHub: LARKY0071                        |
|                                                   |
| [<0>] YouTube Guide:                              |
|___________________________________________________|
"""

print(Endbanner)
