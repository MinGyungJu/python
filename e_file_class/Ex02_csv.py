# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value


data = [[1,'김','책임'],
        [2,'박','선임'],
        [3,'맹','연구원']]

import csv

with open('./data/imsi.csv','wt',encoding='utf-8-sig') as f:
    # cout = csv.writer(f)
    # cout.writerow(data)

result = []
with open('./data/imsi.csv','rt',encoding='utf-8') as f:
    cin = csv.reader(f)
    result = [ row for row in cin ]


print(result)