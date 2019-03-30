import sqlite3

#Это наши словари куда мы будем добавлять слова из хороших и плохих отзывов!
positive_list_t={}
negative_list_t={}

#Разбиваем предложение на слова и заносим их в список
def pars(lister,sentense):
    for word in sentense.split():
        if word in lister:
            lister[word]+=1
        else: lister[word]=1
    return(lister)


#Парсим инфу из таблицы
def parser():
    
    conn = sqlite3.connect("scores_list.db")
    cursor = conn.cursor()
    
    #выбираем прошедшие данные чтобы их вывести...
    sql = "SELECT score,title FROM table_1"
    cursor.execute(sql)
    #cursor.execute(sql1)
    #print(cursor.fetchall())
    checking=cursor.fetchall()
    conn.commit()
    conn.close()
    return(checking)

for check in parser():
    if(check[0]=="Позитивный"): pars(positive_list_t,check[1])
    else:pars(negative_list_t,check[1])


positive_list_t={i:positive_list_t[i] for i in positive_list_t if positive_list_t[i]>43}
negative_list_t={i:negative_list_t[i] for i in negative_list_t if negative_list_t[i]>43}
    
def showing_text():
    return([positive_list,negative_list])
    
    
    
def showing_title():
    return([positive_list_t,negative_list_t])
    
    
#from pos_neg_plots import showing_text
import sqlite3
#print(showing[0])
    
#Парсим инфу из таблицы
def parser_1():
        
    conn = sqlite3.connect("scores_list.db")
    cursor = conn.cursor()
        
    #выбираем прошедшие данные чтобы их вывести...
    sql = "SELECT score, title FROM table_1"
    cursor.execute(sql)
    #print(cursor.fetchall())
    checking=cursor.fetchall()
    conn.commit()
    conn.close()
    return(checking)
    
#Будем считать рейтинг качества наших ответов
raiting=0
#Отношение положительных отзывов к отрицательным в тестовой выборке
coeff=2575/7425#2575/7425
k1=1138/738
#Будем считать положительные ответы
positive_ansvers=0
    
#for w in negative_list:
#negative_list[w]=negative_list[w]/coeff
    
    
#Читаем предложения
scoring=0
for sent in parser_1():
    chisl=0
    znam=0
    for word in sent[1].split():   #Читаем слова в предложении
        if(word in positive_list_t): chisl+=positive_list_t[word]
        if(word in negative_list_t): znam+=negative_list_t[word]
    #print(word)
    #Подсчитываем вероятность отзыва с учётом коэффициента
    #if(znam!=0):sck=chisl/znam*coeff*k1
    chisl=chisl*coeff
    if(znam+chisl!=0):sck=chisl/(chisl+znam)
        
    #print(chisl/znam*coeff)
    if(sck<0.5 and sent[0]=='Негативный'):raiting+=1
    if(sck>0.5 and sent[0]=='Позитивный'):raiting+=1
    
#  Тестим результат
#print("текущий рейтинг работы системы: ",raiting/len(parser_1()))


