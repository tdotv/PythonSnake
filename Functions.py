def multiply(number):
    print(number * 2)

multiply(2)

def max(x, y):
    '''Описание функции'''
    if x > y:
        return x
    else:
        return y

x = float(input("Введите значение x = "))
y = float(input("Введите значение y = "))

my_var = max # Функция = переменная

print (max.__doc__)
print (my_var(x, y))
