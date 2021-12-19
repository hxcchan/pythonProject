# coding:utf-8

none_list = [None, None, None]
empty_list = []
max_list = [1, 'dewei', 'xiaomu', 3.14, [1, 2, 3]]
max_int_list = [1, 2, 3, 4]


print(none_list)
print(max_list)
# print(max(max_list)) --> will have error, because can't put different type in a list when using max().
print(max(max_int_list))
print(bool(none_list))
print(len(none_list))
print(bool(empty_list))

id_address = id(max_list)
print(id_address)
