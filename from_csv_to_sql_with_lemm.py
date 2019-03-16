import csv
import sqlite3
import re
import math
from lemmatiz import lem

def inserting(title,text,score):
    # Создаем соединение с нашей базой
    conn = sqlite3.connect('scores_list.db')
    cursor = conn.cursor()
    # Делаем INSERT запрос к базе данных
    cursor.execute("insert into table_1 values (?,?,?)",[(title),(text),(score)])
    conn.commit()
    # Проверяем результат
    #cursor.execute("SELECT stud_kod FROM stud_spisok ORDER BY stud_kod LIMIT 1")
    #results = cursor.fetchall()
    #print(results)
    
    # Не забываем закрыть соединение с базой данных
    conn.close()

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
            inserting(lem(line["title"]),lem(line["text"]),line["score"])
        



if __name__ == "__main__":
    with open("scores/train_data.csv") as f_obj:
        csv_dict_reader(f_obj)

