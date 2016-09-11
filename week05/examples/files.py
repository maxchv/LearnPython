## [file attributes]

f = open(r"e:\tmp\some.txt", "w", encoding="utf-8")
print("Имя файла: ", f.name)
print("Файл закрыт: ", f.closed)
print("В каком режиме файл открыт: ", f.mode)
print("Кодировка файла: ", f.encoding)

## [method close()]

f = open(r"e:\tmp\some.txt")
print("Имя файла: ", f.name)
print("Файл закрыт: ", f.closed)
f.close()
print("А теперь закрыт: ", f.closed)

## [method write()]

f = open(r"e:\tmp\some.txt", "w", encoding='utf-8')
print('Файл открыт на запись:', f.writable())  
f.write("Мне нравится Python!\nЭто классный язык!")
f.close()

## [method read()]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
print('Файл открыт на чтение:', f.readable())  
text = f.read()
print('Из файла:', text)
f.close()

## [method read(count)]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
print('Файл открыт на чтение:', f.readable())  
text = f.read(10)
print('Из файла:', text)
f.close()

## [method readline()]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
print('Файл открыт на чтение:', f.readable())
print('Файл открыт на запись:', f.writable())
line = f.readline()
print('Из файла:', line)
f.close()

## [method readlines()]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
print('Файл открыт на чтение:', f.readable())
print('Файл открыт на запись:', f.writable())
lines = f.readlines()
print('Из файла:', lines)
print("type(lines)", type(lines))
f.close()

## [for]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
for line in f:
    print(line, end='')
f.close()

## [tell() and seek()]

f = open(r"e:\tmp\some.txt",  encoding='utf-8')
print(f.read(10))
print("Мы находимся на позиции: ", f.tell())
f.seek(0) # Возвращаемся в начало
print(f.read(10))
f.close()

## [with]

with open(r"e:\tmp\some.txt",  encoding='utf-8') as f:
    for line in f:
        print(line, end='')
print("\nФайл закрыт:", f.closed)

## [scandir]

for entry in os.scandir(r'e:\tmp'):
    print(entry.name)

