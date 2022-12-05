# a = [0, 1, 2, 3, 4]
#
# print(a[:3], a[:-3])
#
# #[0,1,2] [0,1]
#
#
# a = [0, 1, 2, 3, 4]
#
# print(a[::-1])
# #[4,3,2,1,0]

first = ["egg", "salad", "bread", "soup", "canafe"]

second = ["fish", "lamb", "pork", "beef", "chicken"]
print(second[1::3])
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]

john = [order[0][:-2], second[1::3], third[0]]

print(john)

del john[2]
print(john)

john.extend([order[2][0:1]])

print(john)

#-----------------------------------------------

list_a = [3, 2, 1, 4]

list_b = list_a.sort()
list_b = sorted(list_a)

print(list_a, list_b)
#-----------------------------------------------

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']

print(fruits[-3:], fruits[1::3])
#-----------------------------------------------
num = [1, 2, 3, 4]

print(num * 2)
#-----------------------------------------------
a = [1, 2, 3, 5]

b = ['a', 'b', 'c','d','e']

a.append('g')

b.append(6)

print('g' in b, len(b))
#-----------------------------------------------

# list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
#
# list_b = []
#
# for i in range(len(list_a)):
#
#     if i % 2 != 1:
#
#     list_b.append(list_a[i])
#
# print(list_b)

#admission_year = input("입학 연도를 입력하세요: ")

#print(type(admission_year))


a = [5, 4, 3, 2, 1]

b = a

c = [5, 4, 3, 2, 1]

print(a is b)
print(a is c)

country = ["Korea", "Japan", "China"]

capital = ["Seoul", "Tokyo", "Beijing"]

index = [1, 2, 3]

country.append(capital)

country[3][1] = index[1:]

print(country)

a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b)
print(c)
print(b + c)