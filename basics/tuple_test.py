# coding:utf-8

# 元组的长度是不可变的，占用资源更小。

tuple_test = ('dewei',)  # 注意如果只有一个元素一定要加逗号！！！
tuple_single_no_comma_str = ('dewei')
tuple_01 = ()
tuple_int = (4, 2, 8, 12, 24)
print(tuple_test)
print(type(tuple_test))
print(type(tuple_single_no_comma_str))  # 此处注意是strl类型
print(type(tuple_01))
print(bool(tuple_01))
print(bool((1, )))
print(len(tuple_int))
print(max(tuple_int))
print(min(tuple_int))
print(tuple_int * 2)  # 把内容复制两次
