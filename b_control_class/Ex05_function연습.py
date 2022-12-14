# [ 연습문제 ]
#
# - 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
#     [ 실행 ]
#         print(even_filter([1, 2, 4, 5, 8, 9, 10]))
#
# - 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
#     [ 실행 ]
#         print(is_prime_number(60))
#         print(is_prime_number(61))
#
# - 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
#     [ 실행 ]
#         print(count_vowel("pythonian"))


def even_filter(list):
    return [x for x in list if x%2==0]

print(even_filter([1,2,4,5,8,9,10]))

def is_prime_number(x):
    for i in range(2,int(x/2)):
        if x%i==0:
            return False
    return True

print(is_prime_number(60))
print(is_prime_number(61))

def count_vowel(x):
    cnt=0
    for char in x:
        if char in ['a','e','i','o','u']:
            cnt+=1
    return cnt


