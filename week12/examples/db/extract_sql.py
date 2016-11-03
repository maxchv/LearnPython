movies = """1	Toy Story	John Lasseter	1995	81
2	A Bug's Life	John Lasseter	1998	95
3	Toy Story 2	John Lasseter	1999	93
4	Monsters, Inc.	Pete Docter	2001	92
5	Finding Nemo	Andrew Stanton	2003	107
6	The Incredibles	Brad Bird	2004	116
7	Cars	John Lasseter	2006	117
8	Ratatouille	Brad Bird	2007	115
9	WALL-E	Andrew Stanton	2008	104
10	Up	Pete Docter	2009	101"""


def generate_insert_sql(text, table):
    sql = 'INSERT INTO {} VALUES '.format(table)
    for row in text.split('\n'):
        cols = [c if c.isdigit() else "\""+c+"\"" for c in row.split('\t')]
        sql += '\n\t('+', '.join(cols[1:])+'),'
    return sql[:-1]



print(generate_insert_sql(movies, 'movies (title, director, year, length_minutes)'))