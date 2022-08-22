from colorama import init
from colorama import Fore, Back, Style

# use colorama to make Termcolor work on Windows too
init()

# int
number = 5
# float
fnumber = 5.7
# str
name = "Oleh"
# bool
status = True

#Экранирование
print(name, "Он \"хороший\" человек")

#Перевод строки
print ('Привет \n\tмир')

#Конкатенация
print("Привет меня зовут ", name)
print("Привет меня зовут", name)
print("Привет меня зовут " + name)
print("Привет меня зовут" + name)

#f-строки
print(f"Привет, {name}!")

print("Мне " + str(number) + " годиков")

# age = input("Введите свой возраст: ")
# print (age)

#Дебильный калькулятор
print(Back.GREEN)
what = input("Что делаем (+, -): ")
print(Back.CYAN)
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))

if what == '+':
    c = a + b
    print("Результат: " + str(c))
elif what == '-':
    c = a - b
    print("Результат: ", c)
else: print("Выбрана неверная операция!")
