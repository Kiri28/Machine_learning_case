import csv
import sqlite3
import re
import math
from lemmatiz import lem

def inserting(type,title,text):
    # Создаем соединение с нашей базой
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()
    # Делаем INSERT запрос к базе данных
    cursor.execute("insert into comments values (?,?,?)",[(type),(title),(text)])
    conn.commit()
    # Проверяем результат
    #cursor.execute("SELECT stud_kod FROM stud_spisok ORDER BY stud_kod LIMIT 1")
    #results = cursor.fetchall()
    #print(results)
    
    # Не забываем закрыть соединение с базой данных
    conn.close()

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    i=0
    for line in reader:
        if i<100:
            inserting(line["type"].lower(),lem(line["title"]),lem(line["text"]))
            i+=1
        else: break


if __name__ == "__main__":
    with open("db/train_data.csv") as f_obj:
        csv_dict_reader(f_obj)

