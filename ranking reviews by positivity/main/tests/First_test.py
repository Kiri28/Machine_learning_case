from pos_neg_plots import showing
import sqlite3
import math
from lemmatiz import lem
import csv


#Функция для определения качества предложения
def pos_or_neg(string):
    scoring=0
    chisl=0
    znam=0
    coeff=2575/10000
    #Читаем слова в предложении
    for word in string.split():
        if(word in showing()[0]): chisl+=showing()[0][word]
        if(word in showing()[1]): znam+=showing()[1][word]
    #print(word)
    #Подсчитываем вероятность отзыва с учётом коэффициента
    if(znam!=0):sck=chisl/znam
    #print(chisl/znam*coeff)
    if (sck<1): print("Негативный")
    if (sck>1): print("Позитивный")



#Грузим наши данные
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
            pos_or_neg(lem(line["text"]))
        


if __name__ == "__main__":
    with open("scores/test_data.csv") as f_obj:
        csv_dict_reader(f_obj)
