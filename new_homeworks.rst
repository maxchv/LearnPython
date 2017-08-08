
Задание 1
---------

Преобразовать строку original_string в ее зеркальное отражение (реверсировать). 
Написать кусок Python кода, который печатает измененную строку

Пишите свой код в следующем окне, предполагая, что original_string уже определена. Описываете логику преобразования 
original_string в reverse_string и не забываем печатать результат print(reverse_string)

Пример
original_string = "ambulance"
reverse_string = "ecnalubma"

Решение
reverse_string = original_string[::-1]
print(reverse_string)

Задание 2
---------

Дана строка original_string. Реализовать функционал который возвращает прореженную строку change_string, оставляя только каждый третий символ.

Пишите свой код в следующем окне, предполагая, что original_string уже определена. 
Описываете логику преобразования original_string в change_string и не забываем печатать результат print(change_string)

Пример
original_string = '123456 7 890 abc'
change_string = '36 0b'

Решение
change_string = original_string[2::3]
print(change_string)

Задание 3
---------

Подсчет гласных букв в строке var_string.

Примечание:

    для простоты строка var_string состоит из букв латинского алфавита;
    набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
    программа должна быть нечувствительна к регистру.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику подсчета гласных букв и не забываем печатать результат print(counting_vowels)

Пример
var_string = "hApPyHalLOweEn!"
counting_vowels = 5

Решение
counting_vowels = 0
for char in var_string:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        counting_vowels += 1
print(counting_vowels)

Задание 4
---------

Реализовать подсчет количества вхождений подстроки "wow" в строке var_string.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику и не забываем печатать результат print(count)

Пример
var_string = "wowhatamanwowowpalehche"
count = 3

Решение
count = 0
for i in range(len(var_string)):
    if var_string[i:i+3] == 'wow':
        count += 1
print(count)

Задание 5
---------

Написать фрагмент python кода, который будет находить в строке text слова палиндромы (слова, читающиеся одинаково в обоих направлениях) 
и выводить на печать количество найденых слов.

Примечание
в строке могут быть знаки припинания , . : ; ! ? которые не должны влиять на результат
регистр в слове не имеет значения слово "sos" и "Sos" считается палиндромом.

Пишите свой код в следующем окне, предполагая, что text уже определена. Описываете логику выполнения и не забывайте печатать результат print(palindromes)

Пример
text = "Swedish pop group ABBA, single SOS unique occo both palindromes."
palindromes = 4

Решение
palindromes = 0
for word in text.split():
    word = word.lower().rstrip(',.:;!?')
    if word == word[::-1]:
        palindromes += 1
print(palindromes)

Задание 6
---------

Написать фрагмент python кода, который модифицирует строку чисел var_string следующим образом:
- в начале строки идут нечетные числа в порядке возрастания
- далее идут четные числа в порядке убывания
и выводит на печать измененную строку var_string.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику выполнения и не забывайте печатать результат print(change_string)

Пример
var_string = '1486371'
change_string = '1137864'

Решение
odds = filter(lambda x: int(x) % 2 == 1, list(var_string))
evens = filter(lambda x: int(x) % 2 == 0, list(var_string))
change_string = ''.join(sorted(odds) + sorted(evens, reverse=True))
print (change_string)

p.s. В этом примере используются анонимная функция lambda, которую мы будем проходить на второй неделе. 
Но мы можете ознакомиться с ними заранее, как пример решения нашей контрольной работы.

Задание 7
---------

Написать фрагмент python кода, который будет находить в строке var_string подстроку, упорядоченною в алфавитном порядке, максимальной длины. Если длины строк совпадают печатаем первую найденную.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику и не забываем печатать результат print(longest)

Пример
var_string = "sabrrtuwacaddabra"
longest = "abrrtuw"

Решение
longest = ''
if var_string:
    curString = var_string[0]
    longest = var_string[0]
    for i in range(1, len(var_string)):
        if var_string[i] >= curString[-1]:
            curString += var_string[i]
            if len(curString) > len(longest):
                longest = curString
        else:
            curString = var_string[i]
print(longest)
