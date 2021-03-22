import requests
import vk_api
import random
import re
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def GetMark(a,b):
    result = ''
    counter = 0

    USERNAME = a
    PASSWORD = b
    # Задаем необходимые адреса сайтов
    LOGINURL = 'https://login.school.mosreg.ru/login'
    DATAURL = 'https://school.mosreg.ru/feed/'

    req_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    formdata = {
        'Login': USERNAME,
        'Password': PASSWORD,
        'LoginButton': 'Submit'
    }

    session = requests.session()
    # Открываем файл, в который сохраним html код сайта
    file = open("pudge.txt", "w", encoding="utf-8")
    # Аутентификация
    r = session.post(LOGINURL, data=formdata, headers=req_headers)
    r2 = session.get(DATAURL)
    r2 = str(r2.text)
    # Записываем код сайта в файл
    file.write(r2)
    # Ищем часть сайта, где содержатся элементы ленты новостей
    word = '"work"'
    inp = open("pudge.txt", encoding="utf-8").readlines()
    for i in iter(inp):
        if word in i:
            break
    # Для более удобного поиска разделим исходную часть сайта (1 очень длинная строка) на строки
    newLine = i.split('{')
    file = open("pudge.txt", "w")
    for k in range(1, len(newLine)):
        file.write(newLine[k] + '\n')
    # Алгоритм поиска и вывода оценок
    word = 'Mark5'
    ass = '"subject"'
    inp = open("pudge.txt").readlines()
    for i in range(1, len(inp) - 4):
        counter += 1
        if word in inp[i] and ass in inp[i]:
            for k in range(counter, counter + 3):
                line = inp[k].split('"')
                if len(line) > 3:
                    text = line[3] + ' '
                    # print(text,' ', end='')
                    result += text + ' '
                    if k == counter + 2:
                        # print('\n')
                        result += '\n'
                        i += 4
    file.close()
    return result

def get_random_id():
    return random.randint(1,100000)
log = ['blank','blank']
i=0
vk_session = vk_api.VkApi(token='1a915719e4cf8146cc9a8ed2cd9cc46507994c9868dbd5dd4b96af5235e4cbd3d98892c514cfef37ef3af')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Начать': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message='Нужно будет ввести ваш логин и пароль от ШП, логин:'
		)
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and i==0:
             log[i] = event.text
             print(log[i])
             i+=1
             vk.messages.send(  # Отправляем сообщение
              random_id=get_random_id(),
              user_id=event.user_id,
              message='Логин принят. Пароль:'
             )
        elif  event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and i==1:
             log[i] = event.text
             print(log[i])
	     i = 0
             vk.messages.send(  # Отправляем сообщение
              random_id=get_random_id(),
              user_id=event.user_id,
              message='Данные приняты'
             )
             vk.messages.send(  # Отправляем сообщение
                 random_id=get_random_id(),
                 user_id=event.user_id,
                 message=GetMark(log[0],log[1])
             )





