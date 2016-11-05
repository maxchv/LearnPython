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

north_american_cities = """Guadalajara	Mexico	1500800	20.659699	-103.349609
Toronto	Canada	2795060	43.653226	-79.383184
Houston	United States	2195914	29.760427	-95.369803
New York	United States	8405837	40.712784	-74.005941
Philadelphia	United States	1553165	39.952584	-75.165222
Havana	Cuba	2106146	23.05407	-82.345189
Mexico City	Mexico	8555500	19.432608	-99.133208
Phoenix	United States	1513367	33.448377	-112.074037
Los Angeles	United States	3884307	34.052234	-118.243685
Ecatepec de Morelos	Mexico	1742000	19.601841	-99.050674
Montreal	Canada	1717767	45.501689	-73.567256
Chicago	United States	2718782	41.878114	-87.629798"""


def generate_insert_sql(text, table):
    sql = 'INSERT INTO {} VALUES '.format(table)
    for row in text.split('\n'):
        cols = [c if c.isdigit() else "\""+c+"\"" for c in row.split('\t')]
        sql += '\n\t('+', '.join(cols[1:])+'),'
    return sql[:-1]



print(generate_insert_sql(movies, 'movies (title, director, year, length_minutes)'))
print(generate_insert_sql(north_american_cities, "north_american_cities (city,	country	population,	latitude,	longitude)"))