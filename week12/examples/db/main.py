import sqlite3


def main():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name VARCHAR NOT NULL,
                        last_name VARCHAR NOT NULL,
                        email VARCHAR NOT NULL
                    )""")

    # cursor.execute("""INSERT INTO user(first_name, last_name, email)
    #                          VALUES (?,?,?)
    #                """, ("Maxim", "Shaptala", "shaptala@itstep.org"))
    conn.commit()

    cursor.execute("SELECT * FROM user")
    all_rows = cursor.fetchall()
    print(all_rows)
    cursor.close()
    conn.close()



if __name__ == "__main__":
    main()