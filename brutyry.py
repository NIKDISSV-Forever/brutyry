# -*- coding: utf-8 -*-
from sys import stdout

def generate(number_of_characters, file_name, chapel):
	already = 0
	file = open(file_name, 'a')

	while already <= chapel:
		result = str(already).rjust(number_of_characters, '0')
		file.write(result)
		stdout.write(result+'\n')
		already += 1
while 1:
	try:
		number_of_characters = int(input("Кол-во символов: "))
		chapel = int('9' * number_of_characters)
		break
	except Exception as error:
		stdout.write(error+'\n')

file_name = input("Введите имя файла (любое): ")
if file_name.isspace() or file_name == '':
	file_name = 'wordlist.txt'
generate(number_of_characters, file_name, chapel)
