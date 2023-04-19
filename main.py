from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    #pprint(contacts_list)

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)\3-\4-\5 \6 \7'

list_1 = []

for a in contacts_list:
    names = ' '.join(a[0:3]).split()
    while len(names) != 3:
        names.append("")
    for i in range(3, 7):
        names.append(a[i])
    list_1.append(names)

for a in list_1:
    for i in list_1[:-1]:
        if a[0:2] == i[0:2] and a != i:
            for k in range(7):
                if a[k]:
                    continue
                else:
                    a[k] = i[k]
            list_1.remove(i)

for a in list_1:
    a[5] = re.sub(pattern, phone_sub, a[5])

pprint(list_1)

with open("telephonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_1)





