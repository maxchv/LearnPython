'''
Задание 6.1
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
Создать скрипт, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']


'''
Задание 6.2
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

'''
Задание 6.2b
Сделать копию скрипта задания 6.2a.
Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

'''
Определение адреса сети [10 баллов]  Даны IP-адрес и маска подсети, необходимо вычислить адрес сети — реализуйте программу GetNetAddress, которая должен вычислять и возвращать адрес сети согласно переданным параметрам через stdin (IP-адрес и маска подсети). Используйте операцию поразрядной конъюнкции (логическое И)
Пример:
IP-адрес: 11000000 10101000 00000001 00000010 (192.168.1.2)
Маска подсети: 11111111 11111111 11111110 00000000 (255.255.254.0)
Адрес сети: 11000000 10101000 00000000 00000000 (192.168.0.0)
Программа на вход должна принимать два аргумента IP-адрес и Маску подсети.

Sample Input 1:

192.168.1.2 255.255.254.0

Sample Output 1:

192.168.0.0

Sample Input 2:

192.168.1.2

Sample Output 2:

GetNetAddress <IP address> <Subnet mask>

Sample Input 3:

111.168.1.abc. 255.255.254.0

Sample Output 3:

Wrong ip address

Sample Input 4:

192.168.1.2 127.0.0.0

Sample Output 4:

Wrong mask

Валидация маски: https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D0%BA%D0%B0_%D0%BF%D0%BE%D0%B4%D1%81%D0%B5%D1%82%D0%B8#%D0%9C%D0%B0%D1%81%D0%BA%D0%B8_%D0%BF%D1%80%D0%B8_%D0%B1%D0%B5%D1%81%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BC%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_(CIDR)
'''