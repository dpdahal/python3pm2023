import sqlite3

conn = sqlite3.connect('database\college.sqlite3')
cr = conn.cursor()

cr.execute("""
           CREATE TABLE IF NOT EXISTS students(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           address TEXT NOT NULL,
            phone INTEGER NOT NULL
           )
           
           """)
conn.commit()


def insert():
    # conn.execute("""
    # INSERT INTO students(name,address,phone) VALUES('Rahul','Delhi',1234567890)
    # """)
    conn.executemany("""
    INSERT INTO students(name,address,phone) VALUES(?,?,?)
    """, [('hari', 'pokhara', 1234567890),
           ('laxmi', 'kathmandu', 1234567890),
             ('ram', 'kathmandu', 1234567890)])
    conn.commit()
# insert()
def select():
    cr.execute("""
    SELECT * FROM students
    """)
    # data = cr.fetchall()
    # data=cr.fetchone()
    data=cr.fetchmany(2)
    print(data)
# select()
def delete():
    cr.execute("""DELETE FROM students WHERE id=1""")
    conn.commit()
delete()