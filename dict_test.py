# coding:utf-8

user_info = {'name': 'xiaomu', 'age': 10, 'height': '180cm'}
result = 'name' in user_info

print(result)

result = 'hope' in user_info
print(result)

result = 'hope' not in user_info
print(result)

count = len(user_info)
print(count)

result = bool(user_info)
print(result)

result = bool({})
print(result)

print(type({}))

print(max(user_info))
print(min(user_info))
