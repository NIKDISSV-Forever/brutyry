# -*- coding: utf-8 -*-
from datetime import datetime as дата
from sys import stdout
global КолоСимволов, ИмяФайла, предел

def сгенерировать():
	началв = дата.today()
	уже = 0
	файл = open(ИмяФайла, 'a')

	while уже <= предел:
		результат = str(уже).rjust(КолВоСимволов, '0')
		файл.write(результат)
		stdout.write(результат+'\n')
		уже += 1
	всёв = дата.today()
	
	print('Начало: %s \nКонец: %s' %(началв, всёв))

while 1:
	try:
		КолВоСимволов = int(input('Кол-во символов: '))
		предел = int('9' * КолВоСимволов)
		break
	except Exception as ошибку:
		print(ошибку)

ИмяФайла = input('Введите имя файла (любое): ')
if ИмяФайла.isspace() or ИмяФайла == '':
	ИмяФайла = 'wordlist.txt'
сгенерировать()
