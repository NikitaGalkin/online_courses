import csv
from datetime import datetime, date, time

class primary_type:
    def __init__(self, name):
        self.name = name
        self.counter = 0
    
    def enc(self):
        self.counter += 1

def find_type(name):
    for i in range(len(our_types)):
        if (our_types[i].name == name):
            return our_types[i]
    return -1

our_types = []

with open('Crimes.csv', 'r') as file:
    reader = csv.reader(file)
    first = True
    for row in reader:
        if (not first):
            if ((row[2].split(" ")[0]).split("/")[2] == "2015"):
                current_type = find_type(row[5])
                if (current_type == -1):
                    current_type = primary_type(row[5])
                    our_types.append(current_type)
                current_type.enc()
        first = False

for i in range(len(our_types)):
    print(our_types[i].name, end = " >> ")
    print(our_types[i].counter)
