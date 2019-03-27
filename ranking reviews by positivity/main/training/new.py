import csv
import sqlite3
import re
import math
from lemmatiz_1 import lem_1

#Запись в новый csv файл
FILENAME = "train_data_classes_with_lemm.csv"
def ins(index,type,title,text):
    with open(FILENAME, "a", newline="") as file:
        descr = [index,type,title,text]
        writer = csv.writer(file)
        writer.writerow(descr)


#Читаем наш csv файл
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    
    for line in reader:
        ins((line[""]),lem_1(line["type"]),lem_1(line["title"]),lem_1(line["text"]))



if __name__ == "__main__":
    with open("classes/train_data.csv") as f_obj:
        csv_dict_reader(f_obj)
