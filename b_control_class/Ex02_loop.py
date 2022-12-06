# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들


a = 112  # 숫자형  - 얘만 집합이 아님
b = ['1', '2', '3']  # 리스트
c = '987'  # 문자열
d = tuple(b)  # 튜플
e = dict(k=5, j=6, d=3)  # 딕셔너리

# for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.  // a는 집합이아니라 for못돌림
# print(entry)

# 딕셔너리 인 경우
for entry in e:  # a는 반복이 안되지만 b부터 e까지는 반복된다.  // a는 집합이아니라 for못돌림
    print(e.items())
"""

# 1부터 10까지의 합 구하기
sum = 0
for i in range(1, 11):  # 11보다 작은정수까지 = 10까지
    sum += i
print('sum = ', sum)

# 1부터 10까지의 홀수 합 구하기

sum = 0
for i in range(1, 11, 2):  # 뒤에 2가 2씩 건너뜀
    sum += i
print('sum = ', sum)
"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for x in range(2, 10):
    for y in range(1, 10):
        print(x, "X", y, "=", x * y,end=' ')
    print()
print("--------------------------------------------------------")
li = ['z','y','x']
while li:
    data = li.pop()
    print(data)
else:
    print('end')
print("--------------------------------------------------------")

fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)
print("--------------------------------------------------------")
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])

num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break
    i += 1
    num += i

print(num)

result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)

num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num +=str(i)
print(num)

coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j

print(result)
