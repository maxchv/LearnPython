import sqlite3

conn = sqlite3.connect("db.sqlite3")

c = conn.cursor() # курсор базы данных
# DDL
# c.execute("""
# CREATE TABLE IF NOT EXISTS Department
# (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL,
#   phone TEXT
# )
# """)
# #c.execute("DROP TABLE IF EXISTS Employee")
# c.execute("""CREATE TABLE IF NOT EXISTS Employee
# (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL,
#   department_id INTEGER REFERENCES Department(id)
# )""")

# DML
# c.execute("""INSERT INTO Department(name, phone) VALUES
#                                    ("Гараж", "9324"),
#                                    ("Бухгалтерия", "5374");""")

# c.execute("""INSERT INTO Employee(first_name, last_name, department_id) VALUES
#                                  ("Вася", "Пупкин", 1),
#                                  ("Даша", "Астафьева", 1),
#                                  ("Дима", "Инкогнито", 2)""")

#c.execute("""UPDATE Employee SET last_name="Суходрищева" WHERE id=3""")

#c.execute("""DELETE FROM Employee WHERE id=1""")

conn.commit()

c.execute("SELECT name FROM Department")
# for row in c:
#     print(row)
departments = c.fetchall()
print(departments)

#c.execute("SELECT * FROM Employee WHERE department_id=2")\
#c.execute("SELECT * FROM Employee WHERE first_name LIKE 'Д%'")
c.execute("SELECT * FROM Employee ORDER BY last_name DESC")
for row in c:
    print(row)

c.execute("""SELECT e.first_name, e.last_name, d.name FROM Employee AS e, Department AS d
      WHERE e.department_id = d.id""")
for row in c:
    print(row)


conn.close()