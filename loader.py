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
            print("Количество изображений для загрузки (число): ")
        else:
            break
    return a


def SavePhotos(url, i, path):
    print("начало сохранения изображения #" + str(i))
    if path == "":
        filename = "wallpaper" + str(i) + ".jpg"
    elif path != "":
        filename = path + "\wallpaper" + str(i) + ".jpg"
    else:
        print("При сохранении файла что то пошло не так! (Возможно вы указали не верный или не существующий путь.)")

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as imgfile:
            imgfile.write(response.content)
    print("изображение #" + str(i) + " было успешно сохранено по пути: " + path)


def GetUrl(i, a, path):
    print("Начало загрузки изображений...")
    while i < a:
        i = i + 1
        print("Текущий прогресс: " + "[" + str(i) + "/" + str(a) + "]\n")
        r = requests.get('https://nekos.life/api/v2/img/wallpaper')
        html = BS4(r.content, 'html.parser')
        data = json.loads(str(html))
        url = data['url']
        print("Получено изображение: " + url)
        SavePhotos(url, i, path)
        t.sleep(1)
        os.system('cls||clear')
    print("Загрузка изображений закончена")


def GetPath():
    getPath = str(input(
        r'Введите путь для сохранения изображений, ничего не вводите для того что бы оставить путь по умолчанию: '))
    return getPath


a = NumOfPhotos()
path = GetPath()

if a == 0:
    quit()
elif a >= 1:
    GetUrl(i, a, path)
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
