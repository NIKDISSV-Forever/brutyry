# -*- coding: utf-8 -*-
from sys import stdout, argv

number_of_characters, file_name = None, None
if "-nc" in argv:
    if argv.index("-nc") != argv[-1]:
        tmp = argv[argv.index("-nc")+1]
        number_of_characters = round(int(tmp)) if tmp.isnumeric() else None
        del tmp
if "-fn" in argv:
    if argv.index("-fn") != argv[-1]:
        number_of_characters = argv[argv.index("-fn")+1]

def generate(
    number_of_characters,
    file_name,
    chapel,
):

    file = open(file_name, 'a')
    for i in range(chapel): file.write(str(i).rjust(number_of_characters, '0')+'\n')
    
    file.close()


while 1:

    try:
        if not number_of_characters:
            number_of_characters = int(input("??????? ???-?? ????????: "))
        chapel = int('9' * number_of_characters) + 1
        break
    except Exception as error:
        stdout.write(str(error)+'\n')

if not file_name:
    file_name = input("??? ????? (wordlist.txt): ")


if (file_name.isspace() or file_name == ''):
    file_name = 'wordlist.txt'


generate(
    number_of_characters,
    file_name,
    chapel,
)
