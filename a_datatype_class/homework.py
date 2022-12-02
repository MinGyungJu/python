import math
#1
# a = int(input("입력1"))
# b = int(input("입력2"))
# c = int(input("입력3"))
# d = int(input("입력4"))
# e = int(input("입력5"))
# print("평균 : ", (a+b+c+d+e)/5)

#2
# a = input("문자열 입력 : ")
# print(a[::-1])

# 3. 사용자에게서 받은 정수들의 평균과 표준편차를 계산하여 출력한다.
# 평균과 표준편차를 프로그램을 작성하세요

numbers = input('정수리스트입력:')     #입력값 받아오기
nums = numbers.split()              #list로 변환
sum = 0.0                           #총합변수 선언
for i in range(len(nums)):          #총합 계산
    sum = sum + float(nums[i])

avg=sum/len(nums)                   #평균수 계산

#표준편차계산(수학문제)
aa = 0.0
for i in range(len(nums)):
    aa = aa + abs(float(nums[i])-avg)**2  #abs= 절대값
bb = aa/(len(nums)-1)
bb=math.sqrt(bb)  #sqrt = 제곱근
print('평균= {}'.format(avg))
print('표준편차{:.2f}'.format(bb))

# str = input('문자열을입력하시오:')               #입력값 받아오기
# str = str.upper()
# for i in range(len(str)):
#     if str[i] in ('A' , 'B' , 'C'):
#         print(2,end='')
#     elif str[i] in ('D' , 'E' , 'F'):
#         print(3,end='')
#     elif str[i] in ('G' , 'H' , 'I'):
#         print(4,end='')
#     elif str[i] in('J' , 'K' , 'L'):
#         print(5,end='')
#     elif str[i] in('M' , 'N' , 'O'):
#         print(6,end='')
#     elif str[i] in('P' , 'Q' , 'R' , 'S'):
#         print(7,end='')
#     elif str[i] in('T' , 'U' , 'V'):
#         print(8,end='')
#     else:
#          print(9, end='')

