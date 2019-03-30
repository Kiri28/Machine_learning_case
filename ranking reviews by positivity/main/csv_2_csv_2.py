import csv
import re
import math
from lemmatiz import lem
 

list=[]

def ins(type,title,text):
	with open(FILENAME, "a", newline="") as file:
    	descr = [type, title,text]
    	writer = csv.writer(file)
    	writer.writerow(descr)


FILENAME = "from_db_to_scv.csv"
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
        ins(lem(line["type"]),lem(line["title"]),lem(line["text"]))



if __name__ == "__main__":
    with open("scores/train_data.csv") as f_obj:
        csv_dict_reader(f_obj)



 
#with open(FILENAME, "w", newline="") as file:
    #writer = csv.writer(file)
    #writer.writerows(list)
