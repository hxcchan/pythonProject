# coding:utf-8

a = 1
b = 2
c = 3

d = a + b + c
print(d)

a /= b
print(a)

a //= b
print(a)

b **= 2
print(b)

print("============================")

k = 300
y = 300
print(k is y)  # True

list_01 = [1, 2, 3]
list_111 = [1, 2, 3]
print(list_01 is list_111)  # False

print(id(list_01))
print(id(list_01 * 2))
list_02 = list_01 * 2
print(list_02)
print(id(list_02))
list_03 = [1, 2, 3, 1, 2, 3]
print(id(list_03))
print(list_03 is not list_01 * 2)

tuple_01 = (1, 2, 3)
print(tuple_01 * 2)

dict_01 = {'name' : 'song'}
# print(dict_01 * 2)

gb = 1
b = gb * 1024 * 1024 * 1024
print(b)
