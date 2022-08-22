# def test(number):
#     assert number > 0, 'Number should be bigger than 0'
#     print(number)

filename1 = input('Какой файл забэкапить?:')
filename2 = 'backup_' + filename1

file1 = open(filename1, 'r') #rb for images, music and etc
file2 = open(filename2, 'w') #wb

file2.write(file1.read())

file1.close()
file2.close()

# r - Чтение файла
# w - Перезаписи файла
# a - Добавление в файл

# b - Binary mode