import sqlite3

#Это наши словари куда мы будем добавлять слова из хороших и плохих отзывов!
positive_list={}
negative_list={}

#Разбиваем предложение на слова и заносим их в список
def pars(lister,sentense):
    for word in sentense.split():
        if word in lister:
            lister[word]+=1
        else: lister[word]=1
    return(lister)

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

#Парсим инфу из таблицы
def parser():
    
    conn = sqlite3.connect("db_new.db")
    cursor = conn.cursor()
    
    #выбираем прошедшие данные чтобы их вывести...
    sql = "SELECT score,text FROM table_1"
    cursor.execute(sql)
    #cursor.execute(sql1)
    #print(cursor.fetchall())
    checking=cursor.fetchall()
    conn.commit()
    conn.close()
    return(checking)

for check in parser():
    if(check[0]=="Позитивный"): pars(positive_list,check[1])
    else:pars(negative_list,check[1])

#positive_list={i:positive_list[i] for i in positive_list if positive_list[i]>730}
#negative_list={i:negative_list[i] for i in negative_list if negative_list[i]>730}

def shown(j,positive_list,negative_list):
    positive_list={i:positive_list[i] for i in positive_list if positive_list[i]>j}
    negative_list={i:negative_list[i] for i in negative_list if negative_list[i]>j}
    return([positive_list,negative_list])






from pos_neg_plots import showing
import sqlite3
#print(showing[0])

#Парсим инфу из таблицы
def parser_1():
    
    conn = sqlite3.connect("db_new.db")
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
k1=1138/738
#Будем считать положительные ответы
positive_ansvers=0

#for w in negative_list:
    #negative_list[w]=negative_list[w]/coeff


#Читаем предложения
#scoring=0
#for sent in parser_1():
#chisl=0
#znam=0
#for word in sent[1].split():   #Читаем слова в предложении
#if(word in positive_list): chisl+=positive_list[word]
#if(word in negative_list): znam+=negative_list[word]
        #print(word)
    #Подсчитываем вероятность отзыва с учётом коэффициента
    #if(znam!=0):sck=chisl/znam*coeff*k1
    #print(chisl/znam*coeff)
    #if (sck<1 and sent[0]=='Негативный'):raiting+=1
#if(sck>1 and sent[0]=='Позитивный'):raiting+=1

#Тестим результат
#print("текущий рейтинг работы системы: ",raiting/len(parser_1()))
#print(raiting," - ",i)
max=0
for bb in range(1000):
    scoring=0
    for sent in parser_1():
        chisl=0
        znam=0
        for word in sent[1].split():   #Читаем слова в предложении
            if(word in shown(bb,positive_list,negative_list)[0]): chisl+=shown(bb,positive_list,negative_list)[0][word]
            if(word in shown(bb,positive_list,negative_list)[1]): znam+=shown(bb,positive_list,negative_list)[1][word]
        #print(word)
        #Подсчитываем вероятность отзыва с учётом коэффициента
        if(znam!=0):sck=chisl/znam*coeff*k1
        #print(chisl/znam*coeff)
        if (sck<1 and sent[0]=='Негативный'):raiting+=1
        if(sck>1 and sent[0]=='Позитивный'):raiting+=1

    #Тестим результат
    if raiting/len(parser_1())>max: max=raiting/len(parser_1())
    print("текущий рейтинг работы системы: ",raiting/len(parser_1()))
    print(raiting," - ",i)
print(max)
