#Удаление; НЕ ЗАПУСКАТЬ!
import sqlite3
conn = sqlite3.connect('table.db')
cursor = conn.cursor()
#выбираем прошедшие данные чтобы их вывести...
sql = "DELETE FROM comments WHERE title== ?"
cursor.execute(sql,[('*')])
conn.commit()
conn.close()
print("yes!")
