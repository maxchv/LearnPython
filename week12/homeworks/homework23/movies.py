"""
Домашнее задание 23

Работа с базами данных. Язык SQL.

В текущей директории должен находится файл db.sqlite3 - база данных в формате
sqlite которую можно скачать по адресу https://github.com/maxchv/LearnPython/blob/master/week12/homeworks/homework23/db.sqlite3

В базе данных находится таблица movies:

id  title           director            year    length_minutes
--------------------------------------------------------------
1	Toy Story	    John Lasseter	    1995	81
2	A Bug's Life	John Lasseter	    1998	95
3	Toy Story 2	    John Lasseter	    1999	93
4	Monsters, Inc.	Pete Docter	        2001	92
5	Finding Nemo	Andrew Stanton	    2003	107
6	The Incredibles	Brad Bird	        2004	116
7	Cars	        John Lasseter	    2006	117
8	Ratatouille	    Brad Bird	        2007	115
9	WALL-E	        Andrew Stanton	    2008	104
10	Up	            Pete Docter	        2009	101

Все задания относятся к этой таблице
"""
import sqlite3


def task01():
    """
    Найти названия (поле title) всех фильмов.
    Вернуть список строк с названиями фильмов из таблицы movies

    >>> task01()
    ["A Bug's Life", 'Cars', 'Finding Nemo', 'Monsters, Inc.', 'Ratatouille', 'The Incredibles', 'Toy Story', 'Toy Story 2', 'Up', 'WALL-E']
    """

    return []


def task02():
    """
    Найти всех режисеров (поле director) всех фильмов.
    Вернуть список строк продюсеров из таблицы movies

    >>> task02()
    ['Andrew Stanton', 'Andrew Stanton', 'Brad Bird', 'Brad Bird', 'John Lasseter', 'John Lasseter', 'John Lasseter', 'John Lasseter', 'Pete Docter', 'Pete Docter']
    """

    return []


def task10():
    """
    Найти фильм, первичный ключ для которого (поле id) равно  6
    Верунть список полей для заданного фильма. Поля id, year и length_minutes
    необходимо привести к целочисленному значению

    >>> task10()
    [6, 'The Incredibles', 'Brad Bird', 2004, 116]
    """
    return []


def task11():
    """
    Найти все фильмы выпущенные в период между 2000 и 2004 годом (включительно)
    Вернуть список со списом полей всех фильмов соответствующих заданию

    >>> task11()
    [[4, 'Monsters, Inc.', 'Pete Docter', 2001, 92], [5, 'Finding Nemo', 'Andrew Stanton', 2003, 107], [6, 'The Incredibles', 'Brad Bird', 2004, 116]]
    """

    return []


def task20():
    """
    Найти все фильмы в которых режисером был John Lasseter
    Вернуть список со списом полей всех фильмов соответствующих заданию

    >>> task20()
    [[1, 'Toy Story', 'John Lasseter', 1995, 81], [2, "A Bug's Life", 'John Lasseter', 1998, 95], [3, 'Toy Story 2', 'John Lasseter', 1999, 93], [7, 'Cars', 'John Lasseter', 2006, 117]]
    """

    return []


def task21():
    """
    Найти все фильмы длительность которыъ более 100 минут
    Вернуть список со списом полей всех фильмов соответствующих заданию

    >>> task21()
    [[5, 'Finding Nemo', 'Andrew Stanton', 2003, 107], [6, 'The Incredibles', 'Brad Bird', 2004, 116], [7, 'Cars', 'John Lasseter', 2006, 117], [8, 'Ratatouille', 'Brad Bird', 2007, 115], [9, 'WALL-E', 'Andrew Stanton', 2008, 104], [10, 'Up', 'Pete Docter', 2009, 101]]
    """

    return []