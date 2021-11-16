import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

sql = """
        DROP TABLE IF EXISTS Student;
        CREATE TABLE Student(
        rollNo integer unique primary key ,
        name text
        );
"""

c.executescript(sql)
conn.commit()
conn.close()
print('Database has been setup successfully...!!!')