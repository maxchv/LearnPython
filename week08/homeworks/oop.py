import re # Для 3 задания

class Person:
    """
    Задание 1

    Класс Person имеет атрибуты объекта: __first_name, __last_name,
    __age.
    
    Необходимо:
        добавить конструктор класса, который принимает три аргумента.

        добавить свойства атрибутов (только геттеры)

        добавить метод is_major, который возвращает True, если человек
        совершеннолетний (больше или равно 18 лет) иначе False

    >>> p = Person('First', 'Last', 43)
    >>> print(p.first_name)
    First
    >>> print(p.last_name)
    Last
    >>> print(p.age)
    43
    >>> p.first_name = "Test"
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.last_name = "Test"
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.age = 43
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.is_major()
    True
    >>> p = Person('First', 'Last', 18)
    >>> p.is_major()
    True
    >>> p = Person('First', 'Last', 17)
    >>> p.is_major()
    False
    """
    pass


class Address:
    """
    Задание 2

    Реализуйте класс Address, который должен иметь атрибуты объекта: __street,
    __state, __country, __zipcode.

    Необходимо:
        добавить конструктор с параметрами

        добавить свойства street, state, country и zipcode (только геттеры)

        написать метод is_valid_zipcode, который возвращает True если __zipcode
        содержить 5 цифр

        написать метод get_full_address, который возвращает строку содержащую
        улицу, область, страну и почтовый индекс. Каждое значение выводится с новой
        строки
    
    >>> address = Address('Javornitskogo, 101', 'Dnepropetrovskaja', 'Ukraine', 49000)
    >>> address.street
    'Javornitskogo, 101'
    >>> address.state
    'Dnepropetrovskaja'
    >>> address.country
    'Ukraine'
    >>> address.zipcode
    '49000'
    >>> address.street = 'Lazarana'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.state = 'Hmelnitskaja'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.country = 'USA'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.zipcode = '12345'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.is_valid_zipcode()
    True
    >>> print(address.get_full_address())
    Javornitskogo, 101
    Dnepropetrovskaja
    Ukraine
    49000
    
    """
    pass

class ContactInfo(object):
    """
    Задание 3

    Реализуйте класс ContactInfo, который должен
    содержать два свойства: email и phone (геттеры и сеттеры).

    Добавить конструктор с параметрами, а также деструктор, в
    котором выводиться сообщение Bye.

    Реализовать метод is_valid_email возвращающий True, если
    введенный email правильный, и is_valid_phone возвращающий
    True, если введенный тоже записан в правильном формате, т.е.
         +3 8 (ццц) ццц-цц-цц

    >>> ci = ContactInfo('mail@mail.com', '+38 (050) 123-45-56')
    >>> ci.email
    'mail@mail.com'
    >>> ci.phone
    '+38 (050) 123-45-56'
    >>> ci.is_valid_email()
    True
    >>> ci.is_valid_phone()
    True
    >>> ci.email = "test"
    >>> ci.email
    'test'
    >>> ci.is_valid_email()
    False
    >>> ci.phone = "#12"
    >>> ci.phone
    '#12'
    >>> ci.is_valid_phone()
    False
    """    
    pass


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()


