# -*- coding: utf-8 -*-
from datetime import datetime as дата

global КолоСимволов, ИмяФайла, предел

def сгенерировать():
	print('Вы начали', дата.today())
	уже = 0
	файл = open(ИмяФайла, 'a')

	while уже <= предел:
		файл.write(str(уже).rjust(КолВоСимволов, '0'))
		уже += 1
	
	print('Вы закончили', дата.today())

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
