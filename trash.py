# -*- coding: utf-8 -*-
import requests
#функция для очищения файла
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

result = ''
counter = 0

USERNAME = str(input('Введите ваш логин'))
PASSWORD = str(input('Введите ваш пароль'))
# Задаем необходимые адреса сайтов
LOGINURL = 'https://login.school.mosreg.ru/login/?ReturnUrl=https%3a%2f%2fschool.mosreg.ru%2ffeed%2f'
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
        print(i)
        break
# Для более удобного поиска разделим исходную часть сайта (1 очень длинная строка) на строки
newLine = i.split('{')
file = open("pudge.txt","w")
for k in range(1, len(newLine)):
    file.write(newLine[k] + '\n')
# Алгоритм поиска и вывода оценок
word = 'Mark5'
ass = '"subject"'
inp = open("pudge.txt").readlines()
for i in range(1,len(inp)-4):
    counter+=1
    if word in inp[i] and ass in inp[i]:
        for k in range(counter,counter+3):
            line = inp[k].split('"')
            if len(line) > 3:
               text = line[3]+' '
               #print(text,' ', end='')
               result += text + ' '
               if k == counter+2:
                   #print('\n')
                   result+='\n'
                   i += 4
print(result)
file.close()

