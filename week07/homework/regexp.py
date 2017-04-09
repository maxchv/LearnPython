import re


def is_date(date):
    """
    Задание 1.

    Функция is_date проверяет является ли параметр date датой записанной в
    "правильном" формате. Возвращает True, если формат верный, иначе - возвращает False.

    Напишите регулярное выражение (в методе complile), которое должно соответсовать
    дате следующих форматов (д - день, м - месяц, г - год):
        дд.мм.гггг
        дд-мм-гггг
        дд/мм/гггг

    >>> is_date("24.09.2016")
    True
    >>> is_date("24-09-2016")
    True
    >>> is_date("24/09/2016")
    True
    >>> is_date("24=09=2016")
    False
    >>> is_date("dd/mm/yyyy")
    False
    """
    re_date = re.compile("Здесь должно быть регулярное выражение")
    return re_date.match(date) is not None


def is_phone(phone):
    """
    Задание 2.

    Функция is_phone проверяет является ли параметр phone телефоном записанным в
    "правильном" формате. Возвращает True, если формат верный, иначе - возвращает False.

    Напишите регулярное выражение (в методе complile), которое должно соответсовать
    телефону следующих форматов (ц - цифра в диапазоне от 0 до 9):
        ццц-цц-цц
        (0цц) ццц-цц-цц
        +38 (0цц) ццц-цц-цц

    >>> is_phone("123-45-67")
    True
    >>> is_phone("(045) 123-34-45")
    True
    >>> is_phone("+38 (023) 121-23-12")
    True
    >>> is_phone("24=09=2016")
    False
    >>> is_phone("dd/mm/yyyy")
    False
    >>> is_phone("1234567")
    False
    """
    re_phone = re.compile(r"Здесь должно быть регулярное выражение")
    return re_phone.match(phone) is not None

def is_dummy_match(text):
    """
    Задание 3.

    Функция is_dummy_match проверяет является ли параметр text значением из
    первой колонки. В этом случае возвращается значение True, a значение False -
    если значения из второй колонки:

     pit
     spot		    pt
     spate		    Pot
     slap two	    peat
     respite		part

    Напишите регулярное выражение для

    >>> is_dummy_match("pit")
    True
    >>> is_dummy_match("spot")
    True
    >>> is_dummy_match("slap two")
    True
    >>> is_dummy_match("respite")
    True
    >>> is_dummy_match("")
    False
    >>> is_dummy_match("pt")
    False
    >>> is_dummy_match("Pot")
    False
    >>> is_dummy_match("peat")
    False
     >>> is_dummy_match("part")
    False
    """
    re_phone = re.compile(r"Здесь должно быть регулярное выражение")
    return re_phone.match(text) is not None

def parse_tag(html):
    """
    Задание 4.

    Функция parse_tag принимает параметр html - строку текста и возвращает имя тега
    и содержимое элемента в виде кортежа.
    Открывающий тег в html заключаестя в угловые скобки (< и >), а закрывающий
    - в < и />. Содержимое элемента помещается между открывающим и закрывающим
    тегом. Пример:

            <title>Заголовок</title>

    Тегом является слово title, а содержимое элемента - Заголовок.

    Для извлечения данных необходимо написать регулярное выражение, в котором
    выделить первую группу - имя тега, а во вторую - поместить содержимое.

    Если тег не имеет содержимого, то функция должна возвратить кортеж из
    одного элемента - имени тега

    >>> parse_tag("<title>Заголовок</title>")
    ('title', 'Заголовок')
    >>> parse_tag("<p>Параграф</p>")
    ('p', 'Параграф')
    >>> parse_tag("<h1>Заголовок первого уровня</h1>")
    ('h1', 'Заголовок первого уровня')
    >>> parse_tag("<a href='url' />")
    ('a',)
    >>> parse_tag("only text")
    ()
    """
    re_phone = re.compile(r"Здесь должно быть регулярное выражение")
    return re_phone.match(html) is not None

if __name__ == "__main__":
    import doctest

    doctest.testmod()


