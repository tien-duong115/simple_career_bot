import json
import csv
import re
with open ('majors-list.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    Agriculture = [i for i in reader if re.search("^Agriculture", i[2])]


def split_repose(mlist):
    output = []
    for i in mlist:
        for e in i:
            output.append(e)
    return output

print(split_repose(Agriculture))