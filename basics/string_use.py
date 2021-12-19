# coding:utf-8

info = 'Python is a very charming language'

result = 'charming' in info
print(result)

result = 'language' not in info
print(result)

info2 = '我Python is a good code'  # 中文字符 > 英文字母 > 数字 > 英文字符
print(max(info2))
print('.', min(info2), '.')
