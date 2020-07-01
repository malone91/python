import csv
import json
import time


def getTime(tlong):
    timeObj = time.localtime(tlong / 1000)
    tmStr = time.strftime("%Y-%m-%d %H:%M:%S", timeObj)
    return tmStr

csv_headers = ['name', 'number', 'age', 'height', 'color', 'salary']
rows = []
with open("json.txt", "r", encoding='UTF-8') as json_file:
    data = json.load(json_file)
    for info in data:
        rows.append([
            info.get('name'),
            info.get('number'),
            info.get('age'),
            info.get('height'),
            info.get('color'),
            info.get('salary')
        ])
fileName = 'test.csv'
with open(fileName, 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(csv_headers)
    f_csv.writerows(rows)