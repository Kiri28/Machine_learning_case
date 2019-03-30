import csv
import re
import math
from lemmatiz import lem

def inserting(a,b,c):
    data = [[a],[b],[c]]
    csv_file = open('data.csv', 'w')
    with csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
    print("Done!")

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
        inserting(lem(line["title"]),lem(line["text"]),line["score"])
        



if __name__ == "__main__":
    with open("scores/train_data.csv") as f_obj:
        csv_dict_reader(f_obj)

