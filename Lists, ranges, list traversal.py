numbers = list(range(0, 101, 2)) # Первый аргумент - начало, второй - конец, третий - интервал

print(numbers)

onenumbers = [1, 2, 3, 4, 5]

#-------------------1-------------------
# i = 0
# length = len(numbers) - 1

# while i<= length:
#     print (str(onenumbers[i]) + '!')
#     i += 1

#-------------------2-------------------
for element in onenumbers: #создаем переменную элемент, для получения доступа в цикле
    print (str(element) + '!')

for test in range(10):
        print("Hello")