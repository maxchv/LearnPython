
def squareRoot(num):
    """
    Задание 1
    ---------
    Реализуйте функцию squareRoot, которая возвращает квадратный корень
    параметра num.
    Если аргумент функции - отрацательное число или не число, то
    функция должна вернуть строку 'Invalid number'
    Для вычисления квадратного корня используйте функцию math.sqrt(num)
    модуля math

    >>> squareRoot(4)
    2.0
    >>> squareRoot(9)
    3.0
    >>> squareRoot('a')
    'Invalid number'
    >>> squareRoot(-4)
    'Invalid number'
    """
    import math
    pass

## [Вспомогательный класс для тестирования функции readNumber]
    
class FakeInput:
    '''
    Вспомогательный класс. Не удалять и не изменять!
    Используется для тестирования функции readNumber
    '''
    inputData = [
        '1', '2', '3', '4', '5', # данные 1
        '1', 'a',                # данные 2
        '5', '6', '1',           # данные 3
        '1', '2', '3', '200',    # данные 4
    ]
    i = 0
        
    @staticmethod
    def fakeInput(text = ''):
        _next = FakeInput.inputData[FakeInput.i]
        FakeInput.i += 1
        return _next
    
## [Конец вспомогательного класса]

def readNumber(start, end, input_function = input):
    """
    Задание 2
    ---------
    Реализуйте метод readNumber, который принимает в качестве аргументов два целых числа
    определяющих диапазон чисел [start, end]

    Параметр по умолчанию input_function необходим для тестирования, поэтому не удалять!!!

    Назначение функции readNumber - считывание у пользователя (через input) 5 целых чисел
    в диапазоне указанном [start, end].
    
    Если пользователь ввел нечисловое значение - необходимо сгенерировать исключение
    типа ValueError и передать сообщение 'An invalid number or non-number text is entered' 

    Если пользователь вводит вводит число выходящее за диапазон [start, end] - в функции
    необходимо сгенерировать исключение IndexError и передать сообщение:
    
      - если число больше, чем конец диапазона (end), то сообщение: "The number bigger than end"
      - если число меньше, чем начало диапазона (start), то сообщение: "The number lesser than start"

    В после успешного ввода 5 целых чисел выводится сообщение: 'End of function'

    Пример работы функции:
    
    >>> readNumber(1, 5, FakeInput.fakeInput)  # данные 1
    End of function
    >>> readNumber(1, 10, FakeInput.fakeInput) # данные 2
    Traceback (most recent call last):
    ...
    ValueError: An invalid number or non-number text is entered
    >>> readNumber(5, 10, FakeInput.fakeInput) # данные 3
    Traceback (most recent call last):
    ...
    IndexError: The number lesser than start
    >>> readNumber(0, 100, FakeInput.fakeInput) # данные 4
    Traceback (most recent call last):
    ...
    IndexError: The number bigger than end
    
    """
    pass

def toUpperList(*args):
    """
    Задание 3
    ---------
    
    Реализуйте функцию toUpperList, которая принимает переменное количество
    позиционных агрументов (строкового типа) и возвращает список строк
    в верхнем регистре

    Обязательно использовать генератор списков (List comprehensions)

    Пример:

    >>> toUpperList('python', 'django', 'itstep')
    ['PYTHON', 'DJANGO', 'ITSTEP']
    >>> toUpperList()
    []
    >>> toUpperList('PYTHON', 'DJANGO', 'ITSTEP')
    ['PYTHON', 'DJANGO', 'ITSTEP']
    
    """
    pass

def prodKeyValue(d):
    """
    Задание 4
    ---------
    
    Реализуйте функцию prodKeyValue, которая принимает словарь с
    числовыми ключами и значениями

    Вернуть список, в котором элементы - это произведение ключа на значение
    исходного словаря

    Обязательно использовать геератор списков (List comprehensions)

    Пример:

    >>> prodKeyValue({1: 1, 2: 5, 4: 1})
    [1, 10, 4]
    >>> prodKeyValue({})
    []
    
    """
    pass

def rfact(n):
    """
    Задание 5
    ---------
    Напишите функцию, которая вычисляет факториал числа n.
    
    В этой задаче нельзя использовать циклы - используйте рекурсию.
    
    Факториа́л числа n (лат. factorialis — действующий, производящий, умножающий; обозначается n!, 
    произносится эн факториа́л) — произведение всех натуральных чисел от 1 до n включительно.
    Подробнее: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
    
    >>> rfact(0)
    1
    >>> rfact(1)
    1
    >>> rfact(2)
    2
    >>> rfact(3)
    6
    >>> rfact(4)
    24
    >>> rfact(5)
    120
    """
    pass
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
