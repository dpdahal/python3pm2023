import sqlite3
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('oop\college.sqlite3')
        self.cr = self.conn.cursor()
        self.table()

    def table(self):
        self.cr.execute("""
                           CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,email TEXT NOT NULL,
                           address INTEGER NOT NULL)""")
        self.conn.commit()


    def insert(self,name,email,address):
        self.cr.execute("""
        INSERT INTO students(name,email,address) VALUES(?,?,?)
        """, (name,email,address))
        self.conn.commit()
        print("Data inserted successfully")

    def show(self):
        self.cr.execute("""SELECT * FROM students""")
        data = self.cr.fetchall()
        for i in data:
            print(i)

    def update(self,id,name,address):
        self.cr.execute(""" UPDATE students SET name = ?,
                        address = ? WHERE id = ?""",(name,address,id))
        self.conn.commit()
        print("Data updated successfully")


    def delete(self,id):
        self.cr.execute(""" DELETE FROM students WHERE id = ?""",(id,))
        self.conn.commit()
        print("Data deleted successfully")
        

obj = Database()
# obj.show()
# obj.insert("sita","sita@gmail.com","Delhi")
obj.update(3,"rama","kathmandu")
# obj.delete(2)
