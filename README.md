# brutyry

Сгенерирует цифровой пароль для любого кол-ва символов.
Использование:
python -OO -u brutyry.py
# Флаги и параметры:

## -fn (file_name.txt)
Имя файла, в который запишется результат.
Default: Wordlist.txt
Example: ```python -OO -u brutyry.py -fn (file_name.txt)```

## -len (length)
Кол-во символов в коде.
default: 4
Example: ```python -OO -u brutyry.py -len 4```

## -A
Если присудствует, файл будет открыт на **дозапись**, иначе, на **перезапись**
Example: ```python -OO -u brutyry.py -A```

## -T
Если присудствует, в конце генерации будет выведено время, в секундах.
Которое было затрачено на генерацию
Example: ```python -OO -u brutyry.py -T```

## -out
Будет отображать все значения, которые генерирует.
Значительно влияет на скорость работы.
Example: ```python -OO -u brutyry.py -out```
