import sqlite3


def task01():
    """
    Find the title of each film

    :return: list of title sorted ascending

    >>> task01()
    ["A Bug's Life", 'Cars', 'Finding Nemo', 'Monsters, Inc.', 'Ratatouille', 'The Incredibles', 'Toy Story', 'Toy Story 2', 'Up', 'WALL-E']
    """
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies ORDER BY title ASC")
    titles = cursor.fetchall()
    cursor.close()
    conn.close()

    return [title[0] for title in titles]


def task02():
    """
    Find the director of each film

    :return: list of director sorted ascending

    >>> task02()
    ['Andrew Stanton', 'Andrew Stanton', 'Brad Bird', 'Brad Bird', 'John Lasseter', 'John Lasseter', 'John Lasseter', 'John Lasseter', 'Pete Docter', 'Pete Docter']
    """
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT director FROM movies ORDER BY director ASC")
    directors = cursor.fetchall()
    cursor.close()
    conn.close()

    return [director[0] for director in directors]

def task10():
    """
    Find the movie with a row id of 6

    :return: list of columns for first row

    >>> task10()
    [6, 'The Incredibles', 'Brad Bird', 2004, 116]
    """
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE id=6")
    row = cursor.fetchall()
    cursor.close()
    conn.close()

    return list(row[0])