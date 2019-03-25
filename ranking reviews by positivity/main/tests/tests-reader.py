from pos_neg_plots import showing
import sqlite3


#Парсим инфу из таблицы
def parser_1():
    
    conn = sqlite3.connect("scores_list.db")
    cursor = conn.cursor()
    
    #выбираем прошедшие данные чтобы их вывести...
    sql = "SELECT score, text FROM table_1"
    cursor.execute(sql)
    #print(cursor.fetchall())
    checking=cursor.fetchall()
    conn.commit()
    conn.close()
    return(checking)

#Будем считать рейтинг качества наших ответов
raiting=0
#Отношение положительных отзывов к отрицательным в тестовой выборке
coeff=2575/7425
#Будем считать положительные ответы
positive_ansvers=0

#Читаем предложения
scoring=0
for sent in parser_1():
    chisl=0
    znam=0
    for word in sent[0].split():   #Читаем слова в предложении
        chisl+=showing()[0][word]
        znam+=showing()[1][word]
    
    #Подсчитываем вероятность отзыва с учётом коэффициента
    sck=chisl/znam*coeff
    if (sck<1 and sent[1]=='негативный'):raiting+=1
    if (sck>1 and sent[1]=='позитивный'):raiting+=1

#Тестим результат
print("текущий рейтинг работы системы: ",raiting)#/len(parser_1()))


		
