"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt.keys())
print(dt.values())
print(dt.items())

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}

print(dt2[(3,4)])
dt2[(3,4)] = 'python'
print(dt2[(3,4)])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt2['korea'] = 'seoul'
print(dt2)
dt2['korea'] = '한국'
print(dt2)

# 여러개 추가할 때
dt2.update({5 : 'five', 6 : 'six'})
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2.keys())
print(dt2.values())
print(dt2.items())  # 투플을 여러개로 뽑아내는
print(dt2[1])





# Key와 Value만 따로 검색

list_1 = [[1, 2], [3], [4, 5, 6]]

a,b,c = list_1
print(a)
print(b)
print(c)

list_2 = a + b + c

print(list_2)

list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']

list_b = []

for i in range(len(list_a)):

    if i % 2 != 1:

        list_b.append(list_a[i])

print(list_b)