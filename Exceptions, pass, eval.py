try:
    eval('print(7 / 4)a')
except ZeroDivisionError: # Если убрать ZeroDivisionError, то будет ловить все ошибки
    print('Поймано исключение ДелениеПоНулю')
    #pass
except SyntaxError: # Проблематично засечь без eval, да и вообще сам программист должен исправить
    print('Поймано исключение СинтаксическаяОшибка')
except:
    print('Поймано какое-то там исключение...')
finally:
    print('Конец поимки')

try:
    pogoda = 'Хорошая'
    if pogoda == 'Плохая':
        raise NameError('Test')
except NameError:
    print('Поймано исключение NameError')

try:
    print(7 / 0)
except:
    print('Test')
    raise

print('Программа завершена')