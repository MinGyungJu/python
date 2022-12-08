"""
 data / sample.json 파일을 읽고 총합 구해서 출력
"""
f = open('./data/sample.json','rt',encoding='utf-8')
data = f.read()
f.close()

# print(data)

import json
items = json.loads(data)

priceSum=0
priceCount=0
sum = 0
for k,val in items.items():
    print(k,'and',val)
    print(k, 'andand', val["price"])
    print(val["price"])
    # priceSum += val['price']
    # priceCount += val['count']
    sum += val['price']*val['count']
# print(priceSum)
# print(priceCount)
print(sum)