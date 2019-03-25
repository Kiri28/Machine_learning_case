from title_descrription import showing_title
from pos_neg_plots import showing_text
from lemmatiz import lem

import csv
import re
import math

#Импортируем наборы слов
positive_list_t=showing_title()[0]
negative_list_t=showing_title()[1]

positive_list=showing_text()[0]
negative_list=showing_text()[1]


#Вероятность, что заголовок принадлежит верноиу ответу
def title_probability(positive_list_t,negative_list_t,title_):
	#Будем считать рейтинг качества наших ответов
    raiting=0
        #Отношение положительных отзывов к отрицательным в тестовой выборке
    coeff=2575/7425 # Коэффициент отношения положительных отзывов к отрицательным
    k1=1138/738 # Коэффициент отношения длин
        #Будем считать положительные ответы
    positive_ansvers=0
    scoring=0
    chisl=0
    znam=0
    for word in title_.split():   #Читаем слова в предложении
        if(word in positive_list_t): chisl+=positive_list_t[word]
        if(word in negative_list_t): znam+=negative_list_t[word]
        #Подсчитываем вероятность отзыва с учётом коэффициента
    chisl=chisl*coeff
    if(znam+chisl!=0): sck=chisl/(chisl+znam)
    else: sck=0.5
        #print(chisl/znam*coeff)
    #if (sck>1): sck=0.99
    return(sck)
#Тестим результат
#print("текущий рейтинг работы системы на заголовках: ",raiting/len(parser_1()))


def text_probability(positive_list,negative_list,text_):
    #Будем считать рейтинг качества наших ответов
    raiting=0
    #Отношение положительных отзывов к отрицательным в тестовой выборке
    coeff=2575/7425#2575/7425
    k1=1138/738
    #Будем считать положительные ответы
    positive_ansvers=0

    chisl=0
    znam=0
    sck=0.5
    for word in text_.split():   #Читаем слова в предложении
        if(word in positive_list): chisl+=positive_list[word]
        if(word in negative_list): znam+=negative_list[word]
        #print(word)
        #Подсчитываем вероятность отзыва с учётом коэффициента
        #if(znam!=0):sck=chisl/znam*coeff*k1
    chisl=chisl*coeff*k1
    if(znam+chisl!=0):sck=chisl/(chisl+znam)
    else: sck=0.5
    #if (sck>1):sck=0.99
    return(sck)


#Объединяем наши вероятности
def combine_results(index_,title_,text_):
    UnionP=title_probability(positive_list_t,negative_list_t,title_)*text_probability(positive_list,negative_list,text_)*2
    if(UnionP>1):UnionP=0.99
    ins(index_,UnionP)
    #return([index_,UnionP])




#**************************************************************

#Запись в новый csv файл
FILENAME = "rep_1.csv"
def ins(index,prob):
	with open(FILENAME, "a", newline="") as file:
		descr = [index,prob]
		writer = csv.writer(file)
		writer.writerow(descr)


#Читаем наш csv файл
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
            combine_results((line[""]),lem(line["title"]),lem(line["text"]))



if __name__ == "__main__":
    with open("scores/test_data.csv") as f_obj:
        csv_dict_reader(f_obj)












