import re


content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
# group代表被匹配到的内容
print(result.group())
# span是横跨的下标
print(result.span())

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
# group 0 是整个字符串，1是括号内的部分
print(result.group(1))
print(result.span())